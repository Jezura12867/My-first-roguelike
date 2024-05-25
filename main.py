# Importing
import pygame
from random import randint
from sprites import Player, Cube
from level import Walls


# Global variables
SCREEN_WIDTH: int = 1550
SCREEN_HEIGHT: int = 900


# Pygame variables
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon_sprite = pygame.image.load("Assets/Icon.png")
icon_sprite.set_colorkey("White")
icon = pygame.display.set_icon(icon_sprite)
title = pygame.display.set_caption("Rougeu liek")

# Sprites
player_hitbox = pygame.rect.Rect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 64, 64))




# The game
class Game:

    def main() -> None:
        dodge_roll_cooldown: int = 500
        
        # NOTE_ TO SELF: CHANGE THESE NUMBERS
        map_num = randint(1, 1)

        while True:

            # Makes the screen gray
            screen.fill((130, 130, 130))          


            # Functions
            colliding_walls_player = Walls.show(screen, map_num, player_hitbox)
            in_a_dodge_roll = Player.movement(player_hitbox, SCREEN_WIDTH, SCREEN_HEIGHT, dodge_roll_cooldown, colliding_walls_player)

            dodge_roll_cooldown -= 1
            if in_a_dodge_roll == True:
                dodge_roll_cooldown = 120


            # Rendering
            pygame.draw.rect(screen, (0, 255, 175), player_hitbox)



            # Quit function
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit
            


            # 60 fps; updating the screen
            clock.tick(60)
            pygame.display.flip()

            


# Checks if running from this file
if __name__ == "__main__":
    Game.main()