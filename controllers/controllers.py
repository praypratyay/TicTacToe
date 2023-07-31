from models.models import GameBuilder

"""INTERMEDIATE ABSTRACTION LAYER
   Why? Tomorrow the implementation details may change. 
   We may have to change classes, create more sublcasses.
   So use a loosely coupled object like controller that talks to client.
"""
class GameController:

    def createGame(self, dimension, players, winningstrategies):   
        return GameBuilder().setDimension(dimension).setPlayers(players).setwinningStrategies(winningstrategies).build()
    
    def displayBoard(self, game):
        game.printBoard()
    
    def UNDO(self, game):
        game.UNDO()
    
    def makeMove(self, game):
        game.makeMove()
    
    def getGameStatus(self, game):
        return game.gameStatus

    def displayResult(self, game):
        return game.printResult()
        
