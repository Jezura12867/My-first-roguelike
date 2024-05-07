import pygame
from sprites import Cube

class Walls:
    def show(screen, map_num):
        cubes = pygame.sprite.Group()
        map_tile_size = 64
        map1 = [
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
        ]
        map2 = [
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                 X             ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
        ]
        maps = [map1, map2]
        for cislo_radku, radek in enumerate(maps[map_num]):
            for cislo_sloupce, bunka in enumerate(radek):
                if bunka == "X":
                    x = cislo_sloupce * map_tile_size / 1.3 + 2
                    y = cislo_radku * map_tile_size / 1.325
                    cube = Cube((x, y), map_tile_size)
                    cubes.add(cube)
        

        cubes.draw(screen)
        