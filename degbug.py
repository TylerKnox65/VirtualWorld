
class main:
    def __init__(self) -> None:
                self.coordinates = [0,0]
                self.Environmentarea = {'[-2, 2]': 'Mountains','[-1, 2]': 'Village','[0, 2]': 'Desert', '[1, 2]': 'Desert and Ocean','[2, 2]': 'Ocean',
                                        '[-2, 1]': 'Plains',   '[-1, 1]': 'Plains', '[0, 1]': 'Plains', '[1, 1]': 'Forest',          '[2, 1]': 'Plains',
                                        '[-2, 0]': 'Cave',     '[-1, 0]': 'Forest', '[0, 0]': 'Plains', '[1, 0]': 'Forest',          '[2, 0]': 'Forest',
                                        '[-2, -1]': 'Deepcave','[-1, -1]': 'Swamp', '[0, -1]': 'Swamp', '[1, -1]': 'Cave',           '[2, -1]': 'Deepcave',}
                self.productlist = ['Wooden Sword','Pickaxe', 'Axe', 'Leather Armour','Torch','Iron Sword','Iron Armour','Diamond Sword','Diamond Armour']
                self.products = {'Wooden Sword': 0,'Pickaxe': 0, 'Axe': 0, 'Leather Armour': 0,'Torch': 0,'Iron Sword': 0,'Iron Armour': 0,'Diamond Sword': 0,'Diamond Armour': 0}
                self.moveit()
    def moveit(self):
                
                print(f"Start\nyou are in {self.Environmentarea[str(self.coordinates)]}")
                
                while True:
                        
                                self.choice = input("where would you like to go: ").capitalize()
                                print(self.coordinates)
                                self.oldCoord = self.coordinates
                                
                                if self.choice == "W":
                                        self.coordinates[1]+=1
                                        
                                elif self.choice == "A":
                                        self.coordinates[0]-=1
                                        
                                        
                                elif self.choice == "S":
                                        self.coordinates[1]-=1
                                        
                                elif self.choice == "D":
                                        self.coordinates[0]+=1
                                        
                                print(self.coordinates, self.oldCoord)
                                if self.coordinates[0] < -2 or self.coordinates[0] > 1:
                                        self.resetOldcoordinate()
                                if self.coordinates[1] < -1 or self.coordinates[1] > 2:
                                        self.resetOldcoordinate()
                                
                                print(f"you are in the {self.Environmentarea[str(self.coordinates)]}")

main()