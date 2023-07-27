# Design TicTacToe (Low Level Design)

## **OVERVIEW**

TicTacToe is a X/O game that two people play on 3x3 grid and three consecutive Xs or Os in a straight line determines the winner of the game. 

![Image](./tic_tac_toe.jpg "RED")

This seems like a software design system thats takes input. No need to persist data.

## Requirements and Clarifications

**Q) Should I restrict the size of grid to 3x3?**

- _No, lets do it nXn._

**Q) Should this game has only two players?**

- _n-1_

**Q) Do we want to support bots with varying difficulty level?**

- _Yes, at max keep one bot per game._.

**Q) How should we represent players?**

- _Every player has a different symbol. Probably a char/string. Validate this._

**Q) Are we supporting tounaments or keeping a leaderboard?**

- _No_

**Q) Can a player do UNDO?**

- _Yes, its a global undo that any player can do._

**Q) Do we want to keep a time limit on the move?**

- _No_

**Q) How will the game start?**

- _Suppose, we have five players A,B,C,D,E. Then we randombly order these players say D,B,A,C,E and they will follow this order for their turn._

**Q) When will the game end?**

- _We will end the game when someone has won or there is a draw. And not when all but one has won._

**Q) What decides a victory in the game?**

- _We should allow to add new ways in which can someone can win. Like all corners of the grid have same symbol. And when we start the game, we configure ways in which a player can win._

**Q) What to do if someone exits?**

- _End the game, or remove their symbols, replace them by bot. Dont support this._

**Q) Should we allow replay?**

- _Yes_

## Interfaces - Classes - Attributes 

### Board
- Size
- Grid (2D list of Cell)

### Cell
- row
- col
- CellState
- Player

### CellState
- EMPTY/FILLED/BLOCKED

### Player
- Symbol
- Name
- PlayerType

### Symbol
- char

### PlayerType
- HUMAN/BOT/GUEST
 
### Bot (Player)
- DifficultyLevel

### DifficultyLevel
- EASY/MEDIUM/HARD

### Move
- Player
- Cell

### GAME
- Board
- Moves (list of Move)
- Players (list of Player)
- currentPlayerindex (We already have a list of players)
- WinningStrategies (list of WinningStrategy)
- GameStatus 
- Winner

### GameStatus
- INPROGRESS/ENDED/DRAW

### WinningStrategy

- #### RowWinningStrategy (WinningStrategy)
- #### ColumnWinningStrategy (WinningStrategy)
- #### DiagonalWinningStrategy (WinningStrategy)

### BotPlayingStrategy

- #### EASYBotPlayingStrategy (BotPlayingStrategy)
- #### MEDIUMBotPlayingStrategy (BotPlayingStrategy)
- #### HARDBotPlayingStrategy (BotPlayingStrategy)

### GAMEBuilder (for Validation)

## Notes

- When UNDO happens, clear cell, remove current move from list of moves and move turn to the previous player. But UNDO moves in games like Chess is complicated. In that case, store the state of board and not just the moves.

