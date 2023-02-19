from models import PlayingCard, CardSuit, GameStrategy
from typing import List, Tuple
from random import shuffle, randint


class Game:
    cards: List[PlayingCard] = []

    def __init__(self):
        for suit in range(4):
            for number in range(13):
                self.cards.append(PlayingCard(number + 1, suit + 1))

    def deal_new_deck(self):
        self.cards = []
        for suit in range(4):
            for number in range(13):
                self.cards.append(PlayingCard(number + 1, suit + 1))

    def shuffle_deck(self):
        shuffle(self.cards)

    def draw_card(self):
        drawn_card = self.cards.pop(0)
        return drawn_card

    def play_first_card(self, strategy: GameStrategy) -> Tuple[PlayingCard, str, bool]:
        if strategy in [GameStrategy.RANDOM, GameStrategy.SENSIBLE]:
            guess = ["RED", "BLACK"][randint(0, 1)]
        else:
            # TODO Implement Optimised play
            guess = ["RED", "BLACK"][randint(0, 1)]
        first_card = self.draw_card()
        success = guess == first_card.suit.colour()

        return first_card, guess, success

    def play_second_card(self, first_card: PlayingCard, strategy: GameStrategy) -> Tuple[PlayingCard, bool, bool]:
        if strategy == GameStrategy.RANDOM:
            guess = bool(randint(0, 1))
        elif strategy == GameStrategy.SENSIBLE:
            if first_card.num_int() < 7:
                guess = True
            elif first_card.num_int() > 7:
                guess = False
            else:
                guess = bool(randint(0, 1))
        else:
            # TODO implement optimised play
            guess = bool(randint(0, 1))

        second_card = self.draw_card()

        if second_card.number.value < first_card.number.value:
            is_higher = False
        elif second_card.number.value > first_card.number.value:
            is_higher = True
        else:
            is_higher = None

        success = guess == is_higher

        return second_card, guess, success

    def play_third_card(self, first_card: PlayingCard, second_card: PlayingCard,
                        strategy: GameStrategy) -> Tuple[PlayingCard, bool, bool]:
        if strategy == GameStrategy.RANDOM:
            guess = bool(randint(0, 1))
        elif strategy == GameStrategy.SENSIBLE:
            guess = True if abs(first_card.number.value - second_card.number.value) > 6 else False
        else:
            # TODO Implement Optimised play
            guess = bool(randint(0, 1))

        third_card = self.draw_card()
        if first_card.number.value < second_card.number.value:
            span = list(range(first_card.number.value, second_card.number.value))
        else:
            span = list(range(second_card.number.value, first_card.number.value))
        is_inside = third_card.number.value in span
        success = guess == is_inside

        return third_card, guess, success

    def play_fourth_card(self, strategy: GameStrategy.RANDOM) -> Tuple[PlayingCard, bool, bool]:
        if strategy in [GameStrategy.RANDOM, GameStrategy.SENSIBLE]:
            guess = CardSuit(randint(1, 4))
        else:
            # TODO Implement Optimised play
            guess = CardSuit(randint(1, 4))
        fourth_card = self.draw_card()
        success = guess == fourth_card.suit

        return fourth_card, guess, success

    def play_random(self) -> Tuple[bool, int]:
        self.deal_new_deck()
        self.shuffle_deck()
        escape = False

        while not escape:
            try:
                first_card, guess, success_first = self.play_first_card(GameStrategy.RANDOM)
                if not success_first:
                    continue

                second_card, guess, success_second = self.play_second_card(first_card, GameStrategy.RANDOM)
                if not success_second:
                    continue

                third_card, guess, success_third = self.play_third_card(first_card, second_card, GameStrategy.RANDOM)
                if not success_third:
                    continue

                fourth_card, guess, success_fourth = self.play_fourth_card(GameStrategy.RANDOM)
                if not success_fourth:
                    continue

                escape = True

            except IndexError:
                return False, 0

        return True, len(self.cards)

    def play_sensible(self) -> Tuple[bool, int]:
        self.deal_new_deck()
        self.shuffle_deck()
        escape = False

        while not escape:
            try:
                first_card, guess, success_first = self.play_first_card(GameStrategy.SENSIBLE)
                if not success_first:
                    continue

                second_card, guess, success_second = self.play_second_card(first_card, GameStrategy.SENSIBLE)
                if not success_second:
                    continue

                third_card, guess, success_third = self.play_third_card(first_card, second_card, GameStrategy.SENSIBLE)
                if not success_third:
                    continue

                fourth_card, guess, success_fourth = self.play_fourth_card(GameStrategy.SENSIBLE)
                if not success_fourth:
                    continue

                escape = True

            except IndexError:
                return False, 0

        return True, len(self.cards)


def main():
    new_game = Game()
    outcomes = []
    card_counter = []
    for i in range(100):
        # print(f"Playing game {i + 1}...")
        outcome, n_cards = new_game.play_sensible()
        outcomes.append(outcome)
        card_counter.append(n_cards)
        # print(n_cards)

    print(f"{sum(outcomes)}/{len(outcomes)}")


    # approximations = []
    # for j in range(1000):
    #     print(f"Batch {j+1} out of 100...")
    #     new_game = Game()
    #     outcomes = []
    #     card_counter = []
    #
    #     for i in range(10):
    #         # print(f"Playing game {i + 1}...")
    #         outcome, n_cards = new_game.play_random()
    #         outcomes.append(outcome)
    #         card_counter.append(n_cards)
    #
    #     approximation = sum(outcomes)/len(outcomes)
    #     approximations.append(approximation)
    # from statistics import mean
    # print(mean(approximations))


if __name__ == "__main__":
    main()
