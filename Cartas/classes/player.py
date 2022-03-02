from termcolor import colored, cprint

class player:

    playerList=[]

    def __init__(self, name):
        self.cards = []
        self.currentValue = 0
        self.name = name
        self.state = "In-game"
        player.playerList.append(self)
    
    @staticmethod
    def compareValue(cards):
        sigma=0
        for x in cards:
            sigma+=x.point_val

        if(sigma > 21):
            cprint("Overflow","red")
            return "Loser"
        return "In-game"

    def pedirCarta(self,card):
        if(self.state == "In-game"):
            entrada=input("ingrese Y para pedir otra carta o enter para plantar\t").upper()
            if(entrada=="Y"):
                self.cards.append(card)
                self.currentValue += card.point_val
                self.state = player.compareValue(self.cards)
            else:
                self.state = "Stand"
    def showCards(self):
            for card in self.cards:
                card.card_info()
            print(self.currentValue)