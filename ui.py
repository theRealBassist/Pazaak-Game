from hand import Row, Section
from player import Player
            
import os               
class Screen:

    def __init__(self, players: list[Player] = None):
        self.players = players if players is not None else []
    
    def addPlayer(self, player: Player):
        self.players.append(player)

    def render(self):
        os.system('clear')
        print("=================================")
        for player in self.players:
            print(player.name)
            print(player.getTotalCards())
            hand = player.hand.getRows()
            for row in hand:
                for line in row.bake():
                    print(line)
        print("=================================")
        


class Ui:
    def __init__(self):
        pass

    def renderScreen(self, state):
        screen = Screen()
        for player in state:
            screen.addPlayer(player)
        screen.render()

        


            


