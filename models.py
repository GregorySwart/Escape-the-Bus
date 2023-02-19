from enum import Enum
from typing import Union


class CardNumber(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class CardSuit(Enum):
    HEARTS = 1
    SPADES = 2
    DIAMONDS = 3
    CLUBS = 4

    def colour(self):
        if self.value in [1, 3]:
            return "RED"
        else:
            return "BLACK"


class SuitSymbols(Enum):
    HEARTS = "♥"
    SPADES = "♠"
    DIAMONDS = "♦"
    CLUBS = "♣"


class PlayingCard:
    number: CardNumber
    suit: CardSuit

    def __init__(self, number: Union[CardNumber, int], suit: Union[CardSuit, int]):
        if type(number) == int:
            number = CardNumber(number)

        if type(suit) == int:
            suit = CardSuit(suit)

        self.number = number
        self.suit = suit

    def display_text(self):
        return f"{self.number.name} of {self.suit.name}"

    def colour(self):
        if self.suit.value in [1, 3]:
            return "RED"
        else:
            return "BLACK"

    def num_int(self):
        return self.number.value

    # TODO Add method that displays cards in short format e.g. "K of ♥" instead of "KING of HEARTS"


class GameStrategy(Enum):
    RANDOM = "random"
    SENSIBLE = "sensible"
    OPTIMISED = "optimised"


def main():
    my_card = PlayingCard(CardNumber(1), CardSuit(1))
    print(my_card.number.value)


if __name__ == "__main__":
    main()
