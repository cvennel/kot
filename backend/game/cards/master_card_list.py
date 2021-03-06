# Attack Manipulation Cards
from game.cards.keep_cards.attack_manipulation_cards.nova_breath import NovaBreath
from game.cards.keep_cards.attack_manipulation_cards.spiked_tail import SpikedTail

# Energy Manipulation Cards
from game.cards.discard_cards.energy_manipulation_cards.energize import Energize
# Health Manipulation cards
from game.cards.discard_cards.health_manipulation_cards.fire_blast import FireBlast
from game.cards.discard_cards.health_manipulation_cards.high_altitude_bombing import HighAltitudeBombing
from game.cards.keep_cards.health_manipulation_cards.it_has_a_child import ItHasAChild
from game.cards.keep_cards.health_manipulation_cards.even_bigger import EvenBigger
from game.cards.keep_cards.health_manipulation_cards.regeneration import Regeneration
from game.cards.keep_cards.health_manipulation_cards.armor_plating import ArmorPlating

# Multi-Manipulation Cards
from game.cards.discard_cards.multi_manipulation_cards.gas_refinery import GasRefinery
from game.cards.discard_cards.multi_manipulation_cards.jet_fighters import JetFighters
from game.cards.discard_cards.multi_manipulation_cards.national_guard import NationalGuard
from game.cards.discard_cards.multi_manipulation_cards.nuclear_power_plant import NuclearPowerPlant
from game.cards.discard_cards.multi_manipulation_cards.tanks import Tanks
from game.cards.discard_cards.multi_manipulation_cards.vast_storm import VastStorm

# Turn manipulations cards
from game.cards.discard_cards.turn_manipulation_cards.frenzy import Frenzy

# Discard Victory Point Manipulation Cards
from game.cards.discard_cards.victory_point_manipulation_cards.apartment_building import ApartmentBuilding
from game.cards.discard_cards.victory_point_manipulation_cards.commuter_train import CommuterTrain
from game.cards.discard_cards.victory_point_manipulation_cards.corner_store import CornerStore
from game.cards.discard_cards.victory_point_manipulation_cards.drop_from_high_altitude import DropFromHighAltitude
from game.cards.discard_cards.victory_point_manipulation_cards.evacuation_orders import EvacuationOrders
from game.cards.discard_cards.victory_point_manipulation_cards.skyscraper import Skyscraper

# Keep Energy Point Manipulation Cards
from game.cards.keep_cards.energy_manipulation_cards.energy_hoarder import EnergyHoarder
from game.cards.keep_cards.energy_manipulation_cards.friend_of_children import FriendOfChildren
from game.cards.keep_cards.energy_manipulation_cards.solar_powered import SolarPowered
from game.cards.keep_cards.energy_manipulation_cards.were_only_making_it_stronger import WereOnlyMakingItStronger
from game.cards.keep_cards.energy_manipulation_cards.alien_metabolism import AlienMetabolism

# Keep Turn Manipulation Cards
from game.cards.keep_cards.turn_manipulation_cards.GiantBrain import GiantBrain

# Keep Victory Point Manipulation Cards
from game.cards.keep_cards.victory_point_manipulation_cards.alpha_monster import AlphaMonster
from game.cards.keep_cards.victory_point_manipulation_cards.complete_destruction import CompleteDestruction
from game.cards.keep_cards.victory_point_manipulation_cards.dedicated_news_team import DedicatedNewsTeam
from game.cards.keep_cards.victory_point_manipulation_cards.eater_of_the_dead import EaterOfTheDead
from game.cards.keep_cards.victory_point_manipulation_cards.gourmet import Gourmet
from game.cards.keep_cards.victory_point_manipulation_cards.omnivore import Omnivore
from game.cards.keep_cards.victory_point_manipulation_cards.rooting_for_the_underdog import RootingForTheUnderdog


def get_all_cards():
    """
    Serves as the master list of all cards to add to the deck.

    Create lists to reflect package structure and add individual cards to each list.
    If a new list is created extend it onto the full_list_of_cards
    """
    energy_manipulation_cards = [Energize()]

    health_manipulation_cards = [FireBlast(), HighAltitudeBombing()]

    multi_manipulation_cards = [GasRefinery(), JetFighters(), NationalGuard(), NuclearPowerPlant(), Tanks(),
                                VastStorm()]

    victory_point_manipulation_cards = [ApartmentBuilding(), CommuterTrain(), CornerStore(), DropFromHighAltitude(),
                                        EvacuationOrders(), Skyscraper()]

    turn_manipulation_cards = [Frenzy()]

    discard_cards = []
    discard_cards.extend(health_manipulation_cards)
    discard_cards.extend(energy_manipulation_cards)
    discard_cards.extend(multi_manipulation_cards)
    discard_cards.extend(victory_point_manipulation_cards)
    discard_cards.extend(turn_manipulation_cards)

    keep_cards = []

    keep_attack_manipulation_cards = [NovaBreath(), SpikedTail()]

    keep_energy_manipulation_cards = [
        EnergyHoarder(), FriendOfChildren(), SolarPowered(), WereOnlyMakingItStronger(), AlienMetabolism()]

    keep_health_manipulation_cards = [
        ItHasAChild(), EvenBigger(), Regeneration(), ArmorPlating()]


    keep_victory_point_manipulation_cards = [AlphaMonster(),
                                             CompleteDestruction(), DedicatedNewsTeam(), Gourmet(), Omnivore(), EaterOfTheDead()]

    keep_turn_manipulation_cards = [GiantBrain()]

    keep_cards = []
    keep_cards.extend(keep_attack_manipulation_cards)
    keep_cards.extend(keep_energy_manipulation_cards)
    keep_cards.extend(keep_health_manipulation_cards)
    keep_cards.extend(keep_victory_point_manipulation_cards)
    keep_cards.extend(keep_turn_manipulation_cards)

    full_list_of_cards = []
    full_list_of_cards.extend(discard_cards)
    full_list_of_cards.extend(keep_cards)

    return full_list_of_cards
