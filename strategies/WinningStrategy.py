from abc import abstractmethod

class WinningStrategy:

    @abstractmethod
    def checkWinner(self, board, last_move):
        pass

    @abstractmethod
    def handleUNDO(self, board, last_move):
        pass

class RowWinningStrategy(WinningStrategy):
    rowmaps = []

    def __init__(self, size, players):
        for i in range(size):
            self.rowmaps.append({})
            for player in players:
                self.rowmaps[i][player.symbol] = 0


    def checkWinner(self, board, last_move):

        self.rowmaps[last_move.cell.row][last_move.player.symbol] += 1
        if self.rowmaps[last_move.cell.row][last_move.player.symbol] == board.size :
            return True

        return False
    
    def handleUNDO(self, board, last_move):
        self.rowmaps[last_move.cell.row][last_move.player.symbol] -= 1

class ColumnWinningStrategy(WinningStrategy):
    colmaps = []

    def __init__(self, size, players):
        for i in range(size):
            self.colmaps.append({})
            for player in players:
                self.colmaps[i][player.symbol] = 0

    def checkWinner(self, board, last_move):
        self.colmaps[last_move.cell.col][last_move.player.symbol] += 1
        if self.colmaps[last_move.cell.col][last_move.player.symbol] == board.size :
            return True
        
        return False

    def handleUNDO(self, board, last_move):
        self.colmaps[last_move.cell.row][last_move.player.symbol] -= 1

class DiagonalWinningStrategy(WinningStrategy):
    leftD = {}
    rightD = {}

    def __init__(self, players):
            for player in players:
                self.leftD[player.symbol] = 0
                self.rightD[player.symbol] = 0

    def checkWinner(self, board, last_move):

        if (last_move.cell.col == last_move.cell.row):
             self.leftD[last_move.player.symbol] += 1
        
        if (last_move.cell.col + last_move.cell.row == board.size-1):
            self.rightD[last_move.player.symbol] += 1

        if (last_move.cell.col == last_move.cell.row):
            if (self.leftD[last_move.player.symbol] == board.size):
                return True
            
        if (last_move.cell.col + last_move.cell.row == board.size-1):
            if (self.rightD[last_move.player.symbol] == board.size):
                return True

        return False
    
    def handleUNDO(self, board, last_move):
        if (last_move.cell.col == last_move.cell.row):
             self.leftD[last_move.player.symbol] -= 1
        
        if (last_move.cell.col + last_move.cell.row == board.size-1):
            self.rightD[last_move.player.symbol] -= 1