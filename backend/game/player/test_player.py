import pytest

from game.cards.discard_cards.energy_manipulation_cards.energize import Energize
from game.cards.discard_cards.health_manipulation_cards.fire_blast import FireBlast
from game.player.player import Player
from game.values import constants
from game.values.locations import Locations


@pytest.fixture(autouse=True)
def player():
    player = Player()
    return player


def test_set_monster_name(player):
    player.set_monster_name('Godzilla')
    assert player.monster_name == 'Godzilla'


def test_set_username(player):
    player.set_username('Tester')
    assert player.username == 'Tester'


def test_player_default_health(player):
    assert player.maximum_health == constants.DEFAULT_HEALTH


def test_player_username():
    sweet_username = "Sam the man, destroyer of worlds"
    player = Player(sweet_username)
    assert player.username == sweet_username


def test_player_default_location(player):
    assert player.location == Locations.OUTSIDE


def test_player_can_move_to_tokyo(player):
    player.move_to_tokyo()
    assert player.location == Locations.TOKYO


def test_player_can_leave_tokyo(player):
    player.leave_tokyo()
    assert player.location == Locations.OUTSIDE


def test_player_current_health_is_maximum_health_when_created(player):
    assert player.current_health == player.maximum_health


def test_player_got_hurt_by_one(player):
    player.update_health_by(-1)
    assert player.current_health == player.maximum_health - 1


def test_player_got_hurt_by_three_and_healed_by_1(player):
    player.update_health_by(-3)
    player.update_health_by(1)
    assert player.current_health == player.maximum_health - 2


def test_player_health_can_not_exceed_max_health(player):
    player.update_health_by(1)
    assert player.current_health == player.maximum_health


def test_player_dies_when_current_health_hits_zero(player):
    player.update_health_by(-10)
    assert not player.is_alive


def test_player_starts_with_zero_victory_points(player):
    assert player.victory_points == constants.DEATH_HIT_POINT


def test_player_can_gain_victory_points(player):
    player.update_victory_points_by(10)
    assert player.victory_points == 10


def test_player_can_lose_victory_points(player):
    player.update_victory_points_by(10)
    player.update_victory_points_by(-5)
    assert player.victory_points == 5


def test_player_starts_with_zero_energy(player):
    assert player.energy == constants.DEFAULT_ENERGY_CUBE


def test_player_can_gain_energy(player):
    player.update_energy_by(3)
    assert player.energy == 3


def test_player_can_lose_energy(player):
    player.update_energy_by(7)
    player.update_energy_by(-3)
    assert player.energy == 4


def test_player_energy_cannot_go_below_zero(player):
    player.update_energy_by(2)
    player.update_energy_by(-5)
    assert player.energy == 0


def test_player_can_not_have_less_than_zero_victory_points(player):
    player.update_victory_points_by(-1)
    assert player.victory_points == 0


def test_player_health_cannot_exceed_decreased_max_health(player):
    player.update_max_health_by(-1)
    assert player.current_health == player.maximum_health


def test_player_health_less_than_increased_max_health(player):
    player.update_max_health_by(1)
    assert player.current_health < player.maximum_health


def test_player_has_instance_of_card_sees_basic_card(player):
    player.add_card(Energize())
    # check player has Energize but not FireBlast to prove method isn't matching to Card or DiscardCard
    assert player.has_instance_of_card(
        Energize()) and not player.has_instance_of_card(FireBlast())


def test_discard_all_cards_removes_all_cards(player):
    player.add_card(Energize())
    player.add_card(FireBlast())
    player.discard_all_cards()
    assert not player.has_instance_of_card(
        Energize()) and not player.has_instance_of_card(FireBlast())


def test_lose_all_stars_zeros_out_stars(player):
    player.add_card(Energize())
    player.add_card(FireBlast())
    player.discard_all_cards()
    assert not player.has_instance_of_card(
        Energize()) and not player.has_instance_of_card(FireBlast())


def test_remove_card(player):
    player.add_card(Energize())
    player.remove_card(Energize())
    assert not player.has_instance_of_card(Energize())


def test_lose_all_stars(player):
    player.update_victory_points_by(10)
    player.lose_all_stars()
    assert player.victory_points == constants.DEATH_HIT_POINT


def test_generate_player_status_summary(player):
    summary: {} = player.generate_player_status_as_dictionary()
    assert summary["username"] is not ""
    assert summary["current_health"] == constants.DEFAULT_HEALTH
    assert summary["location"] is "Out"
    assert summary["is_alive"]
    assert summary["victory_points"] == constants.DEATH_HIT_POINT
    assert summary["energy"] == constants.DEFAULT_ENERGY_CUBE
    print(summary)


def test_newly_dead():
    player = Player("test")
    assert not player.is_newly_dead
    player.update_health_by(-player.current_health)
    assert player.is_newly_dead
    assert not player.is_newly_dead
