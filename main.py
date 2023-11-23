import json
from typing import Any
import pygame
import os
import random
import time



class main():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((640, 360))
        self.clock = pygame.time.Clock()
        self.running = True
        self.deltaTime = 0
        self.lock2d = False
        self.vel = 1
        self.inshop = False
        self.loaded = False
        self.inventory = {"Gold":1000}
        self.run()
    def run(self):
        timestart = time.time()
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.player_location = [0,0]
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #self.screen.fill("grey")
            if not self.inshop:
                pygame.draw.circle(self.screen, "red", self.player_pos, 10)
                '''
            else:
                #pygame.draw.polygon(self.screen, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
                #pygame.draw.polygon(self.screen, (0, 0, 0), ((self.player_pos.x, self.player_pos.x + 10), (self.player_pos.x, self.player_pos.x + 20), (self.player_pos.x+20, self.player_pos.x+20), (self.player_pos.x+20, self.player_pos.x+30), (self.player_pos.x+30, self.player_pos.x+15), (self.player_pos.x+20, self.player_pos.x), (self.player_pos.x+20, self.player_pos.x+10)), self.player_pos)
                pygame.draw.line(self.screen, color="Black", start_pos=self.player_pos, end_pos=((self.player_pos.x + 50,self.player_pos.y)),width=5)
                '''
               
            
            keys = pygame.key.get_pressed()
            if self.player_location == [0,1]:
                    self.vel = 1
            else:
                if keys[pygame.K_LSHIFT]:
                    self.vel = 5
                else:
                    self.vel = 1
            
            if self.lock2d == False:
                if keys[pygame.K_w]:
                    if not self.inshop:
                        self.player_pos.y -= 300 * self.deltaTime  * self.vel

                    '''
                    else:
                        self.player_pos.y -= 300 * self.deltaTime
                    '''
                if keys[pygame.K_s]:
                    if not self.inshop:
                        self.player_pos.y += 300 * self.deltaTime * self.vel
                    '''
                    else:
                            self.player_pos.y += 300 * self.deltaTime
                    '''
            if keys[pygame.K_a]:
                if not self.inshop:
                    self.player_pos.x -= 300 * self.deltaTime * self.vel
            if keys[pygame.K_d]:
                if not self.inshop:
                    self.player_pos.x += 300 * self.deltaTime * self.vel
            pygame.display.flip()
            self.deltaTime = self.clock.tick(60) / 1000
            font = pygame.font.SysFont('Comic Sans MS', 30)
            
            if self.inshop:
                text_surface = font.render('EXIT SHOP', False, (0, 0, 0))
                self.lock2d = True
                self.loaded = False
                clickLoc = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if clickLoc[0] > 300 and clickLoc[0] < 400 and clickLoc[1] > 200 and clickLoc[1] < 300:
                    if click[0]:
                        if self.inventory["Gold"] < 50:
                            pass
                        else:
                            self.inventory["Gold"] -= 50
                            try:
                                self.inventory["Milk"] += 1
                            except:
                                self.inventory["Milk"] = 1
                        print(self.inventory)
                elif clickLoc[0] > -10 and clickLoc[0] < 100 and clickLoc[1] > -10 and clickLoc[1] < 100:
                    if click[0]:
                        self.inshop = False
                        self.player_location = [6,0]
                        self.player_pos.y = 300
                        self.player_pos.x = 400
                elif clickLoc[0] > 500 and clickLoc[0] < 650 and clickLoc[1] > 200 and clickLoc[1] < 350:
                    if click[0]:
                        try:
                            if self.inventory["Milk"] <= 0:
                                pass
                            else:
                                self.inventory["Gold"] += 50
                                try:
                                    self.inventory["Milk"] -= 1
                                except:
                                    self.inventory["Milk"] = 1
                        except:
                            pass
                        print(self.inventory)
                        
            if self.player_pos.y < -10:
                
                #print("OOB")
                self.player_location[1] += 1
                self.player_pos.y = 370
            elif self.player_pos.y > 370:
                #print("OOB")
                self.player_location[1] -= 1
                self.player_pos.y = -10
            if self.player_pos.x < -10:
                #print("OOB")
                self.player_location[0] -= 1
                self.player_pos.x = 650
            elif self.player_pos.x > 660:
                #print("OOB")
                self.player_location[0] += 1
                self.player_pos.x = -10
            #print(self.player_pos)
            if self.player_location == [1,0] and self.player_pos.x > 400:
                self.lock2d = False
                text_surface = font.render('Press E to enter the cave', False, (0, 0, 0))
                print(text_surface)
                if keys[pygame.K_e]:
                    print("ENTERED")
                    self.player_location = [3,0]
                    self.player_pos.y = 300
                    self.lock2d = True
            else:
                text_surface = font.render('', False, (0, 0, 0))
            
            
            

            #print(self.player_location)
            self.checkOOB()
            self.update()
            
            if self.player_location == [6,0]:
                self.char = self.load_png("buying.jpg")
                self.char = pygame.transform.scale(self.char, (100, 100))
                self.screen.blit(self.char, (400,200))
                if self.player_pos.x > 380 and self.player_pos.x < 490:
                    text_surface = font.render('Press E to buy from the shop', False, (0, 0, 0))
                    if keys[pygame.K_e]:
                        self.player_location = [10,10]
                        self.player_pos.x = 100
                        self.player_pos.y = 0
                        self.lock2d = False
                        self.inshop = True
                       
            if self.inshop:
                text_surface = font.render(f'CLICK HERE EXIT SHOP    Money: {self.inventory["Gold"]}', False, (255, 255, 255))
                if self.loaded:
                    self.char = self.load_png("milk.jpg")
                    self.char = pygame.transform.scale(self.char, (100, 100))
                    self.screen.blit(self.char, (300,200))
                    self.char = self.load_png("milkSell.jpg")
                    self.char = pygame.transform.scale(self.char, (150, 150))
                    self.screen.blit(self.char, (500,200))
            try:
                    for i in range(self.inventory["Milk"]):
                            self.char = self.load_png("milk.jpg")
                            self.char = pygame.transform.scale(self.char, (100, 100))
                            self.screen.blit(self.char, (self.player_pos.x + random.randint(-100,100),self.player_pos.y + random.randint(-100,100)))
            except:
                pass
            self.screen.blit(text_surface, (0,0))
            print(self.player_location)
            pygame.display.update()
    
    def checkOOB(self):
        resetxright = None
        resetxleft = None
        resetyup = None
        resetydown = None


        if self.player_location == [0,-1]:
            self.player_location = [0,0]
            resetydown = True
        elif self.player_location == [2,0]:
            self.player_location = [1,0]
            resetxright = True
        elif self.player_location == [3,0] and self.player_pos.x < -5:
            
            resetxleft = True
        elif self.player_location == [-2,0]:
            self.player_location = [-1,0]
            resetxleft = True
        elif self.player_location == [-1,1]:
            self.player_location = [-1,0]
            resetyup = True
        elif self.player_location == [-1,-1]:
            self.player_location = [-1,0]
            resetydown = True
        elif self.player_location == [-2,-1]:
            self.player_location = [-1,0]
            resetydown = True
            resetxleft = True
        elif self.player_location == [-2,1]:
            self.player_location = [-1,0]
            resetyup = True
            resetxleft = True
        elif self.player_location == [0,1] and self.player_pos.x < 5 and self.player_pos.y < 5:
            resetxleft = True
            resetyup = True
        elif self.player_location == [0,1] and self.player_pos.x < 5:
            resetxleft = True
        elif self.player_location == [0,1] and self.player_pos.x > 640:
            resetxright = True
        elif self.player_location == [0,1] and self.player_pos.y < 0:
            resetyup = True
        elif self.player_location == [-1,2]:
            self.player_location = [0,1]
            resetxleft = True
            resetyup = True
        elif self.player_location == [0,2]:
            self.player_location = [0,1]
            resetyup = True
        elif self.player_location == [7,0]:
            self.player_location = [6,0]
            resetxright = True
        elif self.player_location == [1,1]:
            resetyup = True
            self.player_location = [1,0]
        elif self.player_location == [1,-1]:
            self.player_location = [1,0]
            resetydown = True



        if resetxright:
            self.player_pos.x = 640
        if resetydown:
            self.player_pos.y = 350
        if resetxleft:
            self.player_pos.x = 0
        if resetyup:
            self.player_pos.y = 5
    def update(self, pos = None, screen = None) -> None:
        self.image = self.load_png("grass.jpg")
        if self.player_location == [0,0]:
            self.image = self.load_png("grass.jpg")
        elif self.player_location == [0,1]:
            self.image = self.load_png("house.png")
        elif self.player_location == [1,0]:
            self.image = self.load_png("cave.png")
        elif self.player_location == [3,0] or self.player_location == [4,0] or self.player_location == [5,0]:
            self.image = self.load_png("insidecave.jpg")
        elif self.player_location == [6,0]:
            self.image = self.load_png("cavemeet.jpg")
        elif self.player_location == [10,10]:#SHOP
            self.image = self.load_png("store.jpg")
            self.loaded=True
        elif self.player_location == [-1,0]:
            self.image = self.load_png("lake.jpg")
        self.image = pygame.transform.scale(self.image, (640, 360))
        #self.image = pygame.image.load(os.path.join('', 'grass.jpg'))
        #print(self.image)   
        #pygame.Surface.blit(self.image, (0,0))
        
        self.screen.blit(self.image, (0,0))
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
        return image
    
class background():
    def __init__(self) -> None:
       pass
        
    










if __name__ == "__main__":
    main()