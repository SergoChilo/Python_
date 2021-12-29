
class count():
    lives = 10
    def init(self, number, lives):
        self.number = number
        self.lives = lives
    def calc_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print('The program finished !!!!')
            exit()
        else:
            print('You have ' + str(self.lives) + ' lives')
    def calc_number(self):
        if self.number % 10 == 0:
            tas()
        elif self.number % 9 == 0:
            inn()
        elif self.number % 8 == 0:
            ut()
        elif self.number % 7 == 0:
            yot()
        elif self.number % 6 == 0:
            vec()
        elif self.number % 5 == 0:
            hing()
        elif self.number % 4 == 0:
            chors()
        elif self.number % 3 == 0:
            ereq()
        elif self.number % 2 == 0:
            erku()
        else:
            print('Parz tiv')
def tas():
    print('Bajanvuma 10-i')
    hing()
    erku()
def inn():
    print('Bajanvuma 9-i')
    ereq()
def ut():
    print('Bajanvuma 8-i')
    chors()
    erku()
def yot():
    print('Bajanvuma 7-i')
def vec():
    print('Bajanvuma 6-i')
    ereq()
    erku()
def hing():
    print('Bajanvuma 5-i')
def chors():
    print('Bajanvuma 4-i')
    erku()
def ereq():
    print('Bajanvuma 3-i')
def erku():
    print('Bajanvuma 2-i')


number = int(input('Vvedite chislo 1-100 : '))
class hand(count):
    super().__init__(number)
h = hand()
h.calc_lives()


