import pygame
import math
import time
import sys

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
true = True
false = False
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("MFPaint")
clock = pygame.time.Clock()
update = []
tile_map = []
mouse_down = [0, 0, 0]
pressed_keys = []
running = true


class Tile:

    # String name, name of province, "Boston"
    # Tuple cords, cords of center of province, [x_cord, y_cord]
    # ??? Owner, Rightful owner of province,
    # Resource output, Main resource of province,
    # int logistics, development level of province, (1-5)
    # int population, amount of people in a province
    # Terrain terrain, type of land that covers the majority of the province
    # dictionary political_leanings, party makeup of a province, {"Liberal": 23, "Conservative": 77}
    # Tuple buildings, first two are province fort and port respectively (Fort, Port) last is a tuple of factories, ([Factory, Factory])
    def __init__(self, name, cords, owner, output, logistics, population, terrain, political_leanings, buildings=(None, None, [])):
        self.FORTS_PER_STATE = 1
        self.PORTS_PER_STATE = 1
        self.FACTORIES_PER_STATE = 10
        self.MAX_STRENGTH = 100
        self.SMALL_ARMS_BONUS = 0.75
        self.HEAVY_FIRE_BONUS = 1.15
        self.MORAL_BONUS = 1.0

        self.units = []
        self.moral = 100
        self.aggression = 0
        self.activity = 0

        self.owner = owner
        self.controller = owner
        self.name = name
        self.terrain = terrain
        self.max_strength = self.MAX_STRENGTH * terrain.defensiveBuff()
        self.strength = self.max_strength
        self.politics = political_leanings
        self.cords = cords
        self.output = output
        self.logistics = logistics
        self.population = population

        self.fort = buildings[0]
        self.port = buildings[1]
        self.factories = buildings[2]

        self.buildingings = []

    # Returns int province_supply
    def getSupplyInfo(self):
        portBonus = 0
        if self.fort is not None:
            portBonus = 1.25
        return int(5.0 * self.terrain.getLimit() * portBonus * 1)

    # Dictionary attack, { small_arms: 3, heavy_fire: 4, morale: 1 }
    def defend(self, attack):
        if self.fort is not None and self.fort.strength > 0 and self.fort.morale > 0:
            self.defend(self.fort.defend(attack))
            # TODO when making Fort class make defend return dict
        else:
            self.strength -= attack["Small Arms"] * self.SMALL_ARMS_BONUS + attack["Heavy Fire"] * self.HEAVY_FIRE_BONUS
            self.moral -= attack["Moral"] * self.MORAL_BONUS

    def update(self):
        self.updateBuildings()

    def updateBuildings(self):
        if self.fort is not None:
            self.fort.update()
        if self.port is not None:
            self.port.update()
        for building in self.buildingings:
            building.build(self.controller)
