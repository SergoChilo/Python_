class Enemy:
    name = ""
    lives = int(input('Enter your lives : '))  # Kolichestvo jizni

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives > 0:
            print(self.name + ' killed !!!', ' has ' + str(self.lives) + ' lives')
        elif self.lives == 0:
            print(self.name + ' has ' + str(self.lives) + ' lives')
            exit()


class Monster(Enemy):
    def init(self, name, lives):
        super().__init__(self)


class Alien(Enemy):
    def init(self, name, lives):
        super().__init__(self)


m = Monster('Monster', 3)
a = Alien('Alien', 5)

while True:
    x = input('Enter your weapon : laser / gun     ')
    if x == 'exit':
        break
    elif x == 'gun':
        m.hit()
    elif x == 'laser':
        a.hit()
    else:
        print('Please enter only laser or gun !!!!!')
