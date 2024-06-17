class BomberMan:
    def __init__(self,x,y,color,health,damage,bombs,image,speed):
        self.x = x
        self.y = y
        self.color = color
        self.damage = damage
        self.bombs = bombs
        self.image = image
        self.health = health
        self.speed = speed

    def set_color(self):
        if(self.color=='red'):
            print('czerwony')
        else:
            print('niebieski')
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
class Bomb:
    def __init__(self,color,range,x,y):
        self.color = color
        self.range = range
        self.x = x
        self.y = y


