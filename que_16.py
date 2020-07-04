# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

class Mario:
    def __init__(self,character_name,color,size,level,speed):
        self.character_name = character_name
        self.color = color
        self.size = size
        self.level = level
        self.speed = speed
        
    def increase_level(self):
        self.level += 1
    
    def increase_size_speed(self):
        if self.level >= 5 and self.level <=10:
            self.size += 5
            self.speed +=5

        elif self.level > 10 and self.level <= 20:
            self.size += 5
            self.speed += 5
        else:
            pass
    
    def change_color(self,new_color):
        self.color = new_color
    
    def mario_info(self):
        print("Character Name= ", self.character_name)
        print('level= ',self.level)
        print("speed= ",self.speed)
        print('size= ',self.size)



mario=Mario('pujan','green',5,5,10)
mario.mario_info()
mario.increase_size_speed()
mario.mario_info()
mario.increase_level()
mario.mario_info()