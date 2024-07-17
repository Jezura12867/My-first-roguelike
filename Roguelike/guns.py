import pygame

class GunSystem:

    def __init__(self) -> None:

        super.__init__
        self.bullet_spawned:bool = False
        
        
    

    def posanddir(self, gun, player):

        # Makes the gun follow you
        gun.x = player.x + 55
        gun.y = player.y + 10

    
    
    def shoot(self, bullet, SCREEN_WIDTH, SCREEN_HEIGHT, gun):

        # Detects if you click the mouse
        if pygame.mouse.get_pressed()[0] == True:
            self.bullet_spawned = True
        

        if self.bullet_spawned == True:
            bullet.x += 10
        else:
            bullet.x = gun.x
            bullet.y = gun.y
        
        if bullet.x < 0 or bullet.y < 0 or bullet.x > SCREEN_WIDTH or bullet.y > SCREEN_HEIGHT == True:
            self.bullet_spawned = False
        
        



    def run(self, gun, player, bullet, SCREEN_WIDTH, SCREEN_HEIGHT, bullet_spawned):

        # Vatiables
        self.bullet_spawned = bullet_spawned
        
        # Runs the whole function in order
        GunSystem.posanddir(self, gun, player)
        GunSystem.shoot(self, bullet, SCREEN_WIDTH, SCREEN_HEIGHT, gun)
        return self.bullet_spawned