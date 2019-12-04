from abc import abstractmethod
from game.cards.card import Card


class KeepCard(Card):
    def __init__(self, name, cost, effect):
        super().__init__(name, cost, effect)

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.add_card(Card)

    @abstractmethod
    def special_effect(self, player_that_bought_the_card, other_players):
        raise NotImplementedError