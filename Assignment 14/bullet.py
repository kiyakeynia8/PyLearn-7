import arcade

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 5
        self.angle = 90
        self.change_x = 0
        self.change_y = 1

    def sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'), 0.2, 0.0,False)

    def move(self):
        self.center_y += self.speed