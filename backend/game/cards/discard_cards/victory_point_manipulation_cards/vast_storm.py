from game.cards.discard_card import DiscardCard
from game.cards.card import Card


class VastStorm(DiscardCard):
    def __init__(self):
        Card.__init__(self, "Vast Storm", 6, "+ 2[Star] - 1[Health]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_victory_points_by(2)
        player_that_bought_the_card.update_health_by(-1)
