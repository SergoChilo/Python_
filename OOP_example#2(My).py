class count():
    number = int(input('Vvedite chislo 1-100 : '))
    def init(self, number):
        self.number = number
    def calc_number(self):
        if self.number % 10 == 0:
            tas()
            if self.number % 4 == 0:
                print('Bajanvuma 4-i')
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

class hand(count):
    def hashvark(self, number):
        super().__init__(number)
        super().calc_number()

h = hand()
h.calc_number()

