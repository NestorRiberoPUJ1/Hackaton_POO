from classes.deck import Deck
from classes.player import player

Maso = Deck()

# bicycle.show_cards()
Game = "Ok"
input("Presione Enter para iniciar el juego\t")

while(Game.upper() != "EXIT"):

    Nestor = player("Nestor")

    while(Nestor.state == "In-game"):
        Nestor.pedirCarta(Maso.randomCard())
        Nestor.showCards()

    Game = input("Presione Enter para reiniciar el juego o escriba exit para salir\t")
    print(Game)
