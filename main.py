import json
from typing import Any
import pygame
import os


class main():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((640, 360))
        self.clock = pygame.time.Clock()
        self.running = True
        self.deltaTime = 0
        self.run()
    def run(self):
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.player_location = [0,0]
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #self.screen.fill("grey")
            pygame.draw.circle(self.screen, "red", self.player_pos, 10)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * self.deltaTime
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * self.deltaTime
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * self.deltaTime
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * self.deltaTime
            pygame.display.flip()
            self.deltaTime = self.clock.tick(60) / 1000
            if self.player_pos.y < -10:
                
                print("OOB")
                self.player_location[1] += 1
                self.player_pos.y = 370
            elif self.player_pos.y > 370:
                print("OOB")
                self.player_location[1] -= 1
                self.player_pos.y = -10
            if self.player_pos.x < -10:
                print("OOB")
                self.player_location[0] -= 1
                self.player_pos.x = 715
            elif self.player_pos.x > 715:
                print("OOB")
                self.player_location[0] += 1
                self.player_pos.x = -10
            #print(self.player_pos)
            #print(self.player_location)
            self.update()
            pygame.display.update()
    def update(self, pos = None, screen = None) -> None:
        if pos == [0,0]:
            pass
        self.image = self.load_png("grass.jpg")
        #self.image = pygame.image.load(os.path.join('', 'grass.jpg'))
        print(self.image)   
        #pygame.Surface.blit(self.image, (0,0))
        self.screen.blit(self.image[0], (0,0))
    def load_png(self,name):
        """ Load image and return image object"""
        #fullname = os.path.join("data", name)
        try:
            image = pygame.image.load(name)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except FileNotFoundError:
            print(f"Cannot load image: {name}")
            raise SystemExit
        return image, image.get_rect()
    
class background():
    def __init__(self) -> None:
       pass
        
    










if __name__ == "__main__":
    main()