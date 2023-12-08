import random
import time
import json
class world():
        def __init__(self) -> None:
                print("controls: w a s d")
                self.coordinates = [0,0]
                self.Environmentarea = {'[-2, 2]': 'Mountains','[-1, 2]': 'Village','[0, 2]': 'Desert', '[1, 2]': 'Desert and Ocean','[2, 2]': 'Ocean',
                                        '[-2, 1]': 'Plains',   '[-1, 1]': 'Plains', '[0, 1]': 'Plains', '[1, 1]': 'Forest',          '[2, 1]': 'Plains',
                                        '[-2, 0]': 'Cave',     '[-1, 0]': 'Forest', '[0, 0]': 'Plains', '[1, 0]': 'Forest',          '[2, 0]': 'Forest',
                                        '[-2, -1]': 'Deepcave','[-1, -1]': 'Swamp', '[0, -1]': 'Swamp', '[1, -1]': 'Cave',           '[2, -1]': 'Deepcave',}
                self.productlist = ['Wooden Sword For $50','Pickaxe For $70', 'Axe For $70', 'Leather Armour For $100','Torch For $20','Iron Sword For $80','Iron Armour For $150','Diamond Sword For $120','Diamond Armour For $200']
                #self.inventory = {'Wooden Sword': 0,'Pickaxe': 0, 'Axe': 0, 'Leather Armour': 0,'Torch': 0,'Iron Sword': 0,'Iron Armour': 0,'Diamond Sword': 0,'Diamond Armour': 0}
                self.inventory = {}
                self.prices = {'wooden sword': 50,'pickaxe': 70, 'axe': 70, 'leather armour': 100,'torch': 20,'iron sword': 80,'iron armour': 150,'diamond sword': 120,'diamond armour': 200}
                self.minerals = ["stone","coal","iron"]
                self.money = 1000
                self.atk = 0
                self.defence = 0
                self.health = 100
                self.tempatk = 0
                self.dead = False
                self.moveit()
                
                
        
        def moveit(self):
                
                print(f"Start\nyou are in {self.Environmentarea[str(self.coordinates)]}")
                
                while True:
                                
                                

                                with open("json.txt","r+") as file:
                                        x = file.read()
                                        if x == "" or x == [0,0]:
                                                pass
                                        else:
                                               
                                                print(x)
                                                prev = json.loads(x)
                                                self.coordinates = prev
                                        file.close()
                               
                                encounter = True
                                self.choice = input("where would you like to go, enter inv to access inventory: ").lower()
                                #print(self.coordinates)
                                self.oldCoord = self.coordinates.copy()
                                
                                if self.choice == "w":
                                        self.coordinates[1]+=1
                                        
                                elif self.choice == "a":
                                        self.coordinates[0]-=1
                                        
                                        
                                elif self.choice == "s":
                                        self.coordinates[1]-=1
                                        
                                elif self.choice == "d":
                                        self.coordinates[0]+=1
                                
                                elif self.choice == 'inv':
                                 
                                        self.viewInv()
                                with open("json.txt","r+") as file:
                                                prev = self.coordinates
                                                file.write(json.dumps(prev))
                                                file.close()
                                if self.coordinates[0] < -2 or self.coordinates[0] > 1:
                                        self.resetOldcoordinate()
                                        encounter = False
                                if self.coordinates[1] < -1 or self.coordinates[1] > 2:
                                        self.resetOldcoordinate()
                                        encounter = False
                                if encounter:
                                        self.rollEncounter()
                                print(f"you are in the {self.Environmentarea[str(self.coordinates)]}, coordinates are: {self.coordinates}")
                                if self.coordinates == [-1,2]:
                                        self.store()
                                if self.coordinates ==[-2,0] or self.coordinates == [1,-1]: 
                                        self.cave()
        def viewInv(self):
                '''
                inv = {}
                for i in self.inventory:
                        if self.inventory[i] != 0:
                                inv[i] = self.inventory[i]
                                print(inv)
                                #FINISH THE INVENTORY OR I WILL be sad :(
                print(f"You have {self.inventory
                }")
                '''
                for i in self.inventory:
                        print(f"You have {self.inventory[i]} {i}'s")
        def rollEncounter(self):
                if random.randint(0,5) == 5:
                        self.fight()
        def fight(self):
                ran = False
                monsterhealth = random.randint(75,125)
                while monsterhealth > 0:
                        
                        tempdefence = 0
                        choice = input("Oh no, an enemy has stepped out from the bushes and is attacking! You can defend (1), attack (2) run away (3), or drink (4): ")
                        if choice == str(1):
                                tempdefence = 10
                        elif choice  == str(2):
                                isHit = random.randint(1,20)
                                self.atkRan = random.randint(1,20)
                                if isHit > 5:
                                        if isHit == 20:
                                                print(f"CRIT!  DEALING {(self.atk + self.tempatk + self.atkRan) * 10} DAMAGE")
                                                monsterhealth -= (self.atk + self.tempatk) * 10
                                        else:
                                                print(f"You attack the monster dealing {self.atk + self.tempatk + self.atkRan} damage!")
                                                monsterhealth -= self.atk + self.tempatk
                                else:
                                        print("You missed!!!")
                                
                        elif choice == str(3):
                                print("You attempt to run away\n")
                                for i in range(3):
                                        time.sleep(1)
                                        print(".\n")
                                if random.randint(1,3) == 3:
                                        print("Luckly you got away safely")
                                        ran = True
                                        break
                                else:
                                        print("You failed to run away!")
                        elif choice == str(4):
                                self.tempatk += random.randint(5,15)
                                print(f"You drink an unknown liquid gaining {self.tempatk} attack")
                        
                        
                        if monsterhealth > 0:
                                mondmg = random.randint(0,15)
                                isHit = random.randint(1,20)
                                if isHit < 3:
                                        print(f"The monster hurt itself somehow doing {mondmg} to itself")
                                        monsterhealth -= mondmg
                                elif isHit > 10:
                                        if isHit == 20:
                                                mondmg *= 10
                                                print(f"The Monster Crit you doing {mondmg} damage to you!!!! You have {self.health} health")
                                                self.health -= mondmg
                                        else:
                                                self.health -= mondmg
                                                print(f"The monster attacks, doing {mondmg} damage to you! You have {self.health} health")
                                else:
                                        print("The monster missed!")
                        if self.health < 0:
                                self.dead = True
                                break
                if self.dead == True:
                        #print("You have perished")
                        raise SystemExit("You have died")
                
                if ran == False:
                        goldadded = random.randint(0,100)
                        print(f"You defeated the monster winning {goldadded} gold")
                        self.money += goldadded
                
                                
        
        
        def resetOldcoordinate(self):
               self.coordinates = self.oldCoord
               print("You have hit a wall, out of bounds :( ")
        
        def store(self):
                while True:
                        
                        self.storechoice = str(input("would you like to go inside the store Yes or No: ").lower())
                        if self.storechoice == "yes":
                                
                                print(f"you have {self.money}")
                                for i in self.prices:
                                        print(self.prices[i], {i})
                                self.purchase = str(input("What item would you like to buy: ")).lower()
                                self.amount = int(input("How many do you want?: "))
                                self.oldmoney = self.money
                                if self.money > 0:
                                        for i in self.prices:
                                        
                                                if self.purchase == i:
                                                        self.money -= self.prices[i] * self.amount
                                                        try:
                                                                if self.inventory[i]:
                                                                        self.inventory[i] += self.amount
                                                        except:
                                                                self.inventory[i] = self.amount
                                        if self.money < 0:
                                                for i in self.prices:
                                        
                                                        if self.purchase == i:
                                                                self.money += self.prices[i] * self.amount
                                                        
                                                                if self.inventory[i]:
                                                                                self.inventory[i] -= self.amount
                                                               
                                                                       
                                else:
                                        break

                        
                        else:           
                                break
                
     
world()
