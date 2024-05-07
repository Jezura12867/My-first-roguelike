import pygame
from sprites import Cube

class Walls:
    def show(screen, player):
        cubes = pygame.sprite.Group()
        map_tile_size = 64
        map = [
            "X                             X",
            "                              X",
            "                              X",
            "                              X",
            "             XXXX             X",
            "             XXXX             X",
            "             XXXX             X",
            "                              X",
            "                              X",
            "                              X",
            "                              X",
            "                              X",
            "                              X",
            "                              X",
            "                              X",
            "                              X",
            "                              X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        ]
        for cislo_radku, radek in enumerate(map):
            for cislo_sloupce, bunka in enumerate(radek):
                if bunka == "X":
                    x = cislo_sloupce * map_tile_size / 1.3 + 2
                    y = cislo_radku * map_tile_size / 1.325
                    cube = Cube((x, y), map_tile_size)
                    cubes.add(cube)
        
        if cube.rect.colliderect(player):
            return True

        cubes.draw(screen)
        