import pygame

class GunSystem:

    def __init__(self) -> None:

        super.__init__
        
        # Vatiables
        self.shooting:bool = False
    

    def posanddir(self, gun, player):

        # Makes the gun follow you
        gun.x = player.x + 55
        gun.y = player.y + 10
    
    
    def shoot(self):

        # Detects if you click the mouse
        if pygame.mouse.get_pressed()[0] == True:
            self.shooting = True


    def run(self, gun, player):
        
        # Runs the whole function in order
        GunSystem.posanddir(self, gun, player)
        GunSystem.shoot(self)
        print(self.shooting)