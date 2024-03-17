# Observations
## Pikafish

[Pikafish](https://github.com/official-pikafish/Pikafish?tab=readme-ov-file#overview) is the strongest engine derived from Stockfish. Its underlying algorithms are mostly similar to Stockfish.
* Its main search algorithm is principal variation search with aspiration windows, which are improved search algorithms from negamax with alpha-beta pruning.
* It uses iterative deepening, to return an answer faster for simpler boards and take more time for more complicated boards.
* The search algorithm is dependent on a good move ordering to explore the best moves first, so that the trees of the next moves to be explored can mostly be pruned.
* Evaluation of a board is dependent on the side to move, material value, and a neural network evaluation.
* Quiescence search is used to evaluate a board at a quiet position (where there are no winning tactical move to be made)

### Board representation

Pikafish uses [bitboards](https://www.chessprogramming.org/Bitboards) for efficiency representation of a game state. The states represented include squares attacked by pieces, piece position, where each state is represented by one bitboard.

In Xiangqi, each bitboard is a `__uint128_t`, a 128-bit integer, where each bit indicates the state of the corresponding cell on the board. Note that Xiangqi only has 90 squares, so only the first 90 bits are used.

### Move generation

Move generation is simply the generation of all possible moves within the game, and hence is imperative in emulating the game rules.

In Pikafish, moves are divided into types. In `movegen.h`, lines 31-38:

```cpp
enum GenType {
    CAPTURES,
    QUIETS,
    QUIET_CHECKS,
    EVASIONS,
    PSEUDO_LEGAL,
    LEGAL
};
```

For each type of move, Pikafish has its own move generator function. In `movegen.cpp`, lines 124-125:

```cpp
template<GenType Type>
ExtMove* generate(const Position& pos, ExtMove* moveList)
```

The function for each type of move is called dependent on the state that the game is in, for move-ordering. Here, the `GenType Type` is the type of move to generate, `pos` is the game state, `moveList` is the current list of moves generated.

### Piece value

In Xiangqi, each piece is assigned a value, irrespective of where it stands. These values are used as part of evaluation of a position or a move. Conventionally, these are the values assigned to the pieces. Note that these values are only relative, and need to be scaled in calculation of heuristics.

| Piece | Value |
|---|---|
| Rook | 9 |
| Cannon | 4.5 |
| Horse | 4 |
| Pawn (river not crossed) | 1 |
| Pawn (river crossed) | 2 |
| Advisor | 2 |
| Elephant | 2 |

In Pikafish, the values are more fine-tuned to fit its evaluations. In `types.h`, lines 148 - 153:

```cpp
constexpr Value RookValue    = 1213;
constexpr Value AdvisorValue = 216;
constexpr Value CannonValue  = 746;
constexpr Value PawnValue    = 140;
constexpr Value KnightValue  = 964;
constexpr Value BishopValue  = 191;
```

### Move selection

Move selection is to sort the moves in the order of priority to consider and select the next best move for the current state of the game. Each move is assigned a score representing its priority to be explored. Some heuristics that Pikafish uses for a move evaluation:
* Checks and putting piece en prise (under threat): A move has higher priority if it results in a check on the opponent, and lower priority if it puts a piece on the same side under threat.
* [History Heuristic](https://www.chessprogramming.org/History_Heuristic): representing how often the move causes a cutoff in the main search routine. If the move causes more cutoff in the search history, it is likely to be a good move and hence has higher priority.
* [Most Valuable Victom/Least Valuable Aggressor](https://www.chessprogramming.org/MVV-LVA): select a capture move based on the most valuable victim and the least valuable aggressor. Here the "victim" is the captured piece, and the "aggressor" is the piece doing the capture.
* [Static Exchange Evaluation](https://www.chessprogramming.org/Static_Exchange_Evaluation): a simulation of a series of exchange to calculate the material gain/loss at the end. A move has higher priority if there is more material gain at the end.
* [ProbCut](https://www.chessprogramming.org/ProbCut): cut deep tree search on irrelevant search tree, based on the assumption that a shallow search on the move is a rough estimate of the result of a deep search on the same move.

In lines `movepick.cpp`, lines 145 - 223 (a few lines have been cut short):

```cpp
template<GenType Type>
void MovePicker::score() {
    static_assert(Type == CAPTURES || Type == QUIETS || Type == EVASIONS, "Wrong type");
    // ...
    for (auto& m : *this)
    {
        if constexpr (Type == CAPTURES)
            m.value = // Calculation with most valuable victim and capture history

        else if constexpr (Type == QUIETS)
        {
            m.value = // Calculation with main history, pawn history and continuation history, bonus for check and malus for putting piece under threat
        }

        else  // Type == EVASIONS
        {
            if (pos.capture(m))
                m.value = // Calculation with most valuable victim and least valuable aggressor
            else
                m.value = // Calculation with main history, pawn history and continuation history
        }
    }
}
```

We observe that for different types of moves, different heuristics are used. If the move is a capture, most valuable victim, least valuable aggressor and capture history are used. If the move is a quiet move, history heuristics is used alongside bonus for check and malus for putting piece en prise.

Finally, the main move pick routine, it selects the next move based on the scores assigned and the state of the game. Based on the score assigned to moves, partial insertion sort on the move list is done to reorder the move list. Some of the states are labelled with `INIT` because the routine does the scoring before moving onto the actual move picking. In `movepick.cpp`, lines 246 - 388 (only some lines are shown):

```cpp
Move MovePicker::next_move(bool skipQuiets) {
    auto quiet_threshold = [](Depth d) { return -3330 * d; };
top:
    switch (stage)
    {
    // some cases
    case CAPTURE_INIT :
    case PROBCUT_INIT :
    case QCAPTURE_INIT :
        // Generate capture moves, score the capture moves and do partial insertion sort on the capture moves
        ++stage;
        goto top;
    case GOOD_CAPTURE :
        // Using static exchange evaluation to evaluate the first capture move, if it is a bad capture, try it later
        // Otherwise, prepare logic to loop through refutation array
    // some cases
    case QUIET_INIT :
        if (!skipQuiets)
        {
            // Generate quiet moves, score the quiet moves, and do partial insertion sort on the quiet moves
        }
        ++stage;
        [[fallthrough]];
    // some cases
    case EVASION_INIT :
        // Generate evasion moves, score the evasion moves, and do partial insertion sort on the evasion moves
        [[fallthrough]];
    case EVASION :
        return // the first move in the re-ordered move array
    case PROBCUT :
        return // the first move with value passing the threshold from the static exchange evaluation
    // some cases
    }
}
```

Notice that in a capture and in a ProbCut, static exchange evaluation is done to select the next move. Otherwise, the first move in the move list is picked.

### Board evaluation

The board evaluation is used in the main search routine, for move pruning and at the end of quiescence search. The following are the components of a board evaluation:
* Side to move. Given the same board, the score must be higher for red if it is red to move than if it is black to move.
* Count to 60-move stalemate. In Xiangqi, if there are 60 consecutive moves without any piece capture, the match is considered a draw.
* Material count. This is a simple count of pieces and sum of their values on each side.
* Neural network evaluation. Efficiently Updatable Neural Network (NNUE) is used to enhance the evaluation of a board.

In `evaluate.cpp`, lines 130 - 156:

```cpp
Value Eval::evaluate(const Position& pos, int optimism) {
    // Some variable declarations.
    // stm: side to move; shuffling: count to 60 moves; simpleEval: material calculation; nnueComplexity: complexity of the NNUE
    Value nnue = NNUE::evaluate(pos, true, &nnueComplexity);

    // Blend optimism and eval with nnue complexity and material imbalance
    optimism += optimism * (nnueComplexity + std::abs(simpleEval - nnue)) / 781;
    nnue -= nnue * (nnueComplexity + std::abs(simpleEval - nnue)) / 30087;

    int mm = pos.major_material() / 41;
    v      = (nnue * (568 + mm) + optimism * (138 + mm)) / 1434;

    // Damp down the evaluation linearly when shuffling
    v = v * (293 - shuffling) / 194;

    // Guarantee evaluation does not hit the mate range
    v = std::clamp(v, VALUE_MATED_IN_MAX_PLY + 1, VALUE_MATE_IN_MAX_PLY - 1);

    return v;
}
```

Board evaluation is also fine-tuned during each game, using correction history to adjust the value of a board evaluation. In `search.cpp`, lines 66-70:

```cpp
Value to_corrected_static_eval(Value v, const Worker& w, const Position& pos) {
    auto cv = w.correctionHistory[pos.side_to_move()][pawn_structure_index<Correction>(pos)];
    v += cv * std::abs(cv) / 16384;
    return std::clamp(v, VALUE_MATED_IN_MAX_PLY + 1, VALUE_MATE_IN_MAX_PLY - 1);
}
```

Here, the parameter `Value v` is the value obtained from the evaluation function in `evaluation.cpp` above.
