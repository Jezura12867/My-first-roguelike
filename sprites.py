import pygame


class Player:
    def movement(player_hitbox, SCREEN_WIDTH, SCREEN_HEIGHT, dodge_roll_cooldown, wall_colide) -> bool:
        # Variables
        player_movement_speed: int = 5
        direction:list = [0, 0]
        
        
        # Key input
        key = pygame.key.get_pressed()


        

        # Movement
        if player_hitbox.y >= 0 and wall_colide[0] != True:
            if key[pygame.K_w] == True:
                player_hitbox.y -= player_movement_speed
                direction[1] = -1

        
        if player_hitbox.y + 64 <= SCREEN_HEIGHT - 17.5 and wall_colide[1] != True:
            if key[pygame.K_s] == True:
                player_hitbox.y += player_movement_speed
                direction[1] = 1


        if player_hitbox.x > 0 and wall_colide[2] != True:
            if key[pygame.K_a] == True:
                player_hitbox.x -= player_movement_speed
                direction[0] = -1


        if player_hitbox.x + 75 <= SCREEN_WIDTH and wall_colide[3] != True:
            if key[pygame.K_d] == True:
                player_hitbox.x += player_movement_speed
                direction[0] = 1
    
        


        # Dodge roll
        dodge_roll_cooldown -= 1

        if dodge_roll_cooldown <= 0:
            if key[pygame.K_SPACE] == True:
                player_hitbox.x += direction[0] * player_movement_speed * 50
                player_hitbox.y += direction[1] * player_movement_speed * 50
                return True
            else:
                return False
        else:
            return False
        


        

class Cube(pygame.sprite.Sprite):
    def __init__(self, pozice, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pozice)

    