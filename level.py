import pygame
from sprites import Cube

class Walls:
    def show(screen, map_num, player):
        cubes = pygame.sprite.Group()
        map_tile_size = 64
        cube_global = None

        # Maps -----------------------------------------------------------------------------------------------------------------------------------------------------------------
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
            "                 X             ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
            "                               ",
        ]
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        maps = [map1, map2]


        for cislo_radku, radek in enumerate(maps[map_num]):
            for cislo_sloupce, bunka in enumerate(radek):
                if bunka == "X":
                    # Defining cubes
                    x = cislo_sloupce * map_tile_size / 1.3 + 2
                    y = cislo_radku * map_tile_size / 1.325
                    cube = Cube((x, y), map_tile_size)
                    cubes.add(cube)
                    

                    # Rendering cubes
                    cubes.draw(screen)


                    # Player collision
                    player_collisions = []
                    cube_global = cube
                    nextpos_up = (player.x, player.y - 5)
                    nextpos_up_player = pygame.rect.Rect((nextpos_up[0], nextpos_up[1], 64, 64))
                    if pygame.Rect.colliderect(nextpos_up_player, cube_global) == True:
                        player_collisions.append(True)
                    else:
                        player_collisions.append(False)
                    nextpos_down = (player.x, player.y + 5)
                    nextpos_down_player = pygame.rect.Rect((nextpos_down[0], nextpos_down[1], 64, 64))
                    if pygame.Rect.colliderect(nextpos_down_player, cube_global) == True:
                        player_collisions.append(True)
                    else:
                        player_collisions.append(False)
                    nextpos_left = (player.x - 5, player.y)
                    nextpos_left_player = pygame.rect.Rect((nextpos_left[0], nextpos_left[1], 64, 64))
                    if pygame.Rect.colliderect(nextpos_left_player, cube_global) == True:
                        player_collisions.append(True)
                    else:
                        player_collisions.append(False)
                    nextpos_right = (player.x + 5, player.y)
                    nextpos_right_player = pygame.rect.Rect((nextpos_right[0], nextpos_right[1], 64, 64))
                    if pygame.Rect.colliderect(nextpos_right_player, cube_global) == True:
                        player_collisions.append(True)
                    else:
                        player_collisions.append(False)

                    return player_collisions

        