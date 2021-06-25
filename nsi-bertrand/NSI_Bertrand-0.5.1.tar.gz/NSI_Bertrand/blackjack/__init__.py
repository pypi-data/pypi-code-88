"""
Projet jeu de Blackjack
=======================

 But du jeu : Après avoir reçu deux cartes, le joueur tire des cartes pour s’approcher de la valeur 21 sans la dépasser. Le but du joueur est de battre le croupier en obtenant un total de points supérieur à celui-ci ou en voyant ce dernier dépasser 21. Chaque joueur joue contre le croupier, qui représente la banque, ou le casino, et non contre les autres joueurs.

Une carte sera un tuple (valeur, couleur).

Le croupier sera représenter par un deck de carte c'est à dire une Pile de cartes.

Chaque joueur sera représenter par une main de carte c'est à dire une liste (au sens de Python) de carte.

L'ensemble des joueurs sera une file de mains. On ne fera pas de différence entre un jour et le croupier.


Règles du jeu (depuis Wikipédia):

La partie oppose individuellement chaque joueur contre la banque. Le but est de battre le croupier sans dépasser 21. Dès qu'un joueur fait plus que 21, on dit qu'il « Brûle » ou qu'il « crève » et il perd sa mise initiale. La valeur des cartes est établie comme suit :

de 2 à 9 → valeur nominale de la carte
chaque figure + le 10 surnommées "bûche" → 10 points
l'As → 1 ou 11 (au choix)
Un Blackjack est composé d'un As et d'une « buche » (carte ayant pour valeur 10, donc 10, J, Q ou K). Cependant, si le joueur atteint le point 21 en 3 cartes ou plus on compte le point 21 et non pas Blackjack; de même lorsque le joueur sépare deux as et qu'il reçoit une buche pour l'un d'eux.

Au début de la partie, le croupier distribue une carte face visible à chaque joueur et tire une carte face visible également pour lui. Il tire ensuite pour chacun une seconde carte face visible et tire une seconde carte face cachée pour lui au Blackjack américain. Au blackjack européen, le croupier tire sa seconde carte après le tour de jeu des joueurs.

Puis, il demande au premier joueur de la table (joueur situé à sa gauche) l'option qu'il désire choisir. Si le joueur veut une carte, il doit l'annoncer en disant « Carte ! ». Le joueur peut demander autant de cartes qu'il le souhaite pour approcher la valeur sans la dépasser. Si après le tirage d'une carte, il a dépassé 21, il perd sa mise et le croupier passe au joueur suivant. S'il décide de s'arrêter, en disant « Je reste », le croupier passe également au joueur suivant.

Le croupier répète cette opération jusqu'à ce que tous les joueurs soient servis.

Ensuite, il joue pour lui selon une règle simple et codifiée « la banque tire à 16, reste à 17 ». Ainsi, le croupier tire des cartes jusqu'à atteindre un nombre compris entre 17 et 21 que l'on appelle un point. S'il fait plus de 21, tous les joueurs restants gagnent mais s'il fait son point, seuls gagnent ceux ayant un point supérieur au sien (sans avoir sauté). Dans cette situation, le joueur remporte l'équivalent de sa mise. En cas d'égalité le joueur garde sa mise mais n'empoche rien en plus. À noter que le blackjack (une bûche et un as en deux cartes) est plus fort que 21 fait en ayant tiré plus de deux cartes. Si un joueur fait blackjack et que le banquier fait 21 en 3 cartes ou plus, le joueur fait blackjack et remporte une fois et demi de sa mise. Le banquier lui gagne contre tous les joueurs ayant 20 ou moins. Réciproquement si la banque a un as et une bûche, elle gagne contre tout joueur ayant 21 en ayant tiré plus de deux cartes. Dans ce cas, si un joueur fait également blackjack, il peut récupérer sa mise mais n'est pas payé, le jeu étant à égalité. Un joueur ayant fait blackjack (sauf blackjack à la banque auquel cas il y a égalité) remporte une fois et demi sa mise.

"""

import random
import itertools
from pile import Pile
from file import File

values = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "Valet": 10,
    "Dame": 10,
    "Roi": 10,
    "As": 11,  # dans la vrai version du BlackJack, l'As peut valoir 1 ou 11 au choix du joueur.
}
colors = ["Pique", "Coeur", "Trefle", "Carreau"]


class Player:
    def __init__(self, name, hand=None):
        self.name = str(name)
        if hand is None:
            self.hand = []
        else:
            self.hand = hand

    @property
    def score(self):
        """Calcule le score du joueur"""
        if self.hand:
            return sum([values[c[0]] for c in self.hand])
        return 0

    def want_continue(self, croupier_cards):
        """Fait le choix de demander ou non des cartes

        Pour cela, le joueur peut voir les cards du croupier

        :param croupier_cards: cartes du croupier
        :return: booléen en fonction de s'il veut ou non continuer
        """
        if self.score >= 17:
            return False
        return True

    def __repr__(self):
        return f"<Player {self.name}: {self.hand}>"


def build_deck():
    """Construit une pile de 52 cartes mélangés


    Pour mélanger les cartes de façon aléatoire, vous pouvez utiliser la bibliothèque random.

    :return: Une pile de 52 cartes différentes mélangées

    :example:
    >>> deck = build_deck()
    >>> deck.is_empty()
    False
    >>> for i in range(52):
    ...    if deck.is_empty():
    ...        print(f"Pas assez de cartes. Il y en uniquement {i}")
    ...        break
    ...    card = deck.pop()
    >>> deck.is_empty()
    True
    """
    deck = Pile()
    cards = list(itertools.product(values, colors))
    random.shuffle(cards)
    for card in cards:
        deck.append(card)
    return deck


def build_players(nbr):
    """Construit une file de joueurs avec des mains vides

    :param nbr: nombre de joueurs (on se limitera à 4 joueurs)
    :return: file de mains vides

    :example:
    >>> players = build_players(3)
    >>> players.is_empty()
    False
    >>> for _ in range(3):
    ...    print(players.pop())
    <Player 0: []>
    <Player 1: []>
    <Player 2: []>
    >>> players.is_empty()
    True
    """
    players = File()
    for n in range(nbr):
        players.append(Player(n))
    return players


def can_play(player):
    """détermine si un joueur peu encore jouer

    :param player: une joueur
    :return: True if his score is lower than 21

    :example:
    >>> hand = [(2, "Pique"), ("As", "Coeur"), (8, "Carreau")]
    >>> p = Player(1, hand)
    >>> can_play(p)
    True
    >>> hand = [(2, "Pique"), ("As", "Coeur"), (6, "Carreau")]
    >>> p = Player(1, hand)
    >>> can_play(p)
    True
    >>> hand = [(2, "Pique"), ("As", "Coeur"), ("Valet", "Carreau")]
    >>> p = Player(1, hand)
    >>> can_play(p)
    False
    """
    if player.score <= 21:
        return True
    return False


def won(player):
    """Détermine si un jour a gagné c'est à dire qu'il a atteint les 21 points

    :param player: une joueur avec une main
    :return: True si le joueur a exactement 21 points

    :example:
    >>> hand = [(2, "Pique"), ("As", "Coeur"), (8, "Carreau")]
    >>> p = Player(1, hand)
    >>> won(p)
    True
    >>> hand = [(2, "Pique"), ("As", "Coeur"), (6, "Carreau")]
    >>> p = Player(1, hand)
    >>> won(p)
    False
    """
    if player.score == 21:
        return True
    return False


def draw(player, deck):
    """Distribue 1 carte à un joueur

    :param player: Un joueur
    :param deck: pile avec toutes les cartes

    :return: (player, deck) où le joueur a une carte en plus en main

    :example:
    >>> player = build_players(1).pop()
    >>> deck = build_deck()
    >>> player, deck = draw(player, deck)
    >>> len(player.hand)
    1
    >>> player, deck = draw(player, deck)
    >>> len(player.hand)
    2
    """
    player.hand.append(deck.pop())
    return (player, deck)


def first_draw(players, deck):
    """Distribue 2 cartes à chaque joueur

    :param players: file de joueur avec des mains vides
    :param deck: pile avec toutes les cartes

    :return: (players, deck) où les joueurs ont deux cartes et où le deck a été mis à jour.

    :example:
    >>> players = build_players(3)
    >>> deck = build_deck()
    >>> players, deck = first_draw(players, deck)
    >>> for i in range(3):
    ...    print(len(players.pop().hand))
    2
    2
    2
    """
    drawn = File()
    while not players.is_empty():
        p = players.pop()
        p, deck = draw(p, deck)
        p, deck = draw(p, deck)
        drawn.append(p)
    return drawn, deck


def play_backjack(nbr_players):
    """Simule une partie de blackjack entre "nbr_players"

    On ne vous demande pas de reproduire une simulation parfaite du jeu blackjack. Commencez par une version simple où les joueur s obtiennent petit à petit les cartes. Puis complexifiez en ajoutant une par une les règles.

    La version de correction ne prend pas en compte toutes les règles du jeux ni tout le déroulement d'une partie.

    :param nbr_players: nombre de joueurs
    :return: la liste des joueurs gagnants

    """
    winners = []
    deck = build_deck()
    players = build_players(nbr_players)
    dealer = Player("croupier")

    # Première main
    dealer, deck = draw(dealer, deck)
    players, deck = first_draw(players, deck)
    still_in_game_players = File()
    while not players.is_empty():
        p = players.pop()
        if won(p):
            winners.append(p)
        still_in_game_players.append(p)
    if winners:
        return winners

    dealer, deck = draw(dealer, deck)
    if won(dealer):
        return [dealer]

    players = still_in_game_players
    still_in_game_players = File()
    while not players.is_empty():
        p = players.pop()
        while p.want_continue(dealer.hand):
            p, deck = draw(p, deck)
            if won(p):
                winners.append(p)
                break
            elif not can_play(p):
                break
        if not can_play(p):
            break
        still_in_game_players.append(p)

    if still_in_game_players.n == 0:
        return []

    while dealer.want_continue(dealer.hand):
        dealer, deck = draw(dealer, deck)
        if won(p):
            return []
        elif not can_play(p):
            break

    while not still_in_game_players.is_empty():
        p = still_in_game_players.pop()
        if not can_play(dealer):
            winners.append(p)
        elif p.score > dealer.score:
            winners.append(p)

    return winners


if __name__ == "__main__":
    print(play_backjack(3))
