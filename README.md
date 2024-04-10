# CS3263-project

Xiangqi engine using principal variation search

## Testing instruction

Warning: it is best to run our project on a computer with RAM of at least 16GB, as our programme consumes a lot of memory.

1. Make sure that you have Python with version at least 3.10. In your terminal, key in the following command to verify your Python version:

```
python --version
```

2. In your terminal, clone our repository.

```
git clone https://github.com/nknguyenhc/CS3263-project.git
```

3. Redirect the folder containing our repository.

```
cd CS3263-project
```

4. Run the main programme.

```
python main.py
```

You will be greeted with the following message:

```
Welcome! In this programme, you can test out your algorithm by manually playing against it.
Note that the board will always be displayed with red side at the bottom and black side on top.
Please decide if you want to play as red (go first) or black (go second): (R/B) 
```

You can decide to go first or second. If you decide to go first, key in `R`. Otherwise, key in `B`.

```
Current board:
R1 H1 E1 A1 K1 A1 E1 H1 R1
-- -- -- -- -- -- -- -- --
-- C1 -- -- -- -- -- C1 --
P1 -- P1 -- P1 -- P1 -- P1
-- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- --
P0 -- P0 -- P0 -- P0 -- P0
-- C0 -- -- -- -- -- C0 --
-- -- -- -- -- -- -- -- --
R0 H0 E0 A0 K0 A0 E0 H0 R0
turn: 0

Please key in your move:
```

You and the programme will alternate to make a move. When it is your turn, key in your move. Otherwise, the programme will process the board and prints out its move.

Before each move, for both sides, the programme prints out the board. The board shows the coordinates of the table, where `--` indicates that no piece is occupying that position, or the slot is filled with the piece name's initial, followed by the side it is on.

| Piece | Chinese characters | Initial |
|---|---|---|
| Rook | 俥, 車 | R |
| Horse | 傌, 馬 | H |
| Cannon | 炮, 砲 | C |
| Pawn | 兵, 卒 | P |
| Advisor | 仕, 士 | A |
| Elephant | 相, 象 | E |
| King | 帥, 將 | K |

Number `0` indicates that the piece is a red piece, number `1` indicates that the piece is a black piece. For example, red rook is marked with `R0`. Note that the board is always printed such that red side is at the bottom and black side is on top.

We use the international notation system for the moves. More details about the move notation is found in [this Wikipedia article](https://en.wikipedia.org/wiki/Xiangqi#System_2). You are required to key in a move that follows this notation system.

For example, you may decide to use central cannon opening. You key in:

```
C2.5
```

The programme would print out the following:

```
Current board:
R1 H1 E1 A1 K1 A1 E1 H1 R1
-- -- -- -- -- -- -- -- --
-- C1 -- -- -- -- -- C1 --
P1 -- P1 -- P1 -- P1 -- P1
-- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- --
P0 -- P0 -- P0 -- P0 -- P0
-- C0 -- -- C0 -- -- -- --
-- -- -- -- -- -- -- -- --
R0 H0 E0 A0 K0 A0 E0 H0 R0
turn: 1

Algo choose: H8+7

Current board:
R1 H1 E1 A1 K1 A1 E1 -- R1
-- -- -- -- -- -- -- -- --
-- C1 -- -- -- -- H1 C1 --
P1 -- P1 -- P1 -- P1 -- P1
-- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- --
P0 -- P0 -- P0 -- P0 -- P0
-- C0 -- -- C0 -- -- -- --
-- -- -- -- -- -- -- -- --
R0 H0 E0 A0 K0 A0 E0 H0 R0
turn: 0

Please key in your move:
```

This indicates that the algorithm chooses `H8+7`, moving up the horse.
