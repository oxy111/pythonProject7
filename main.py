class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы доски"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass


    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots
        self.count = 0

class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid


        for i, row in enumerate(self.field):
            self.field = [["0"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
         res = ""
         res += " | 1 | 2 | 3 | 4 | 5 | 6 |"
             res += f"\n{i + 1} | " + " | ".join(row) + " | "

         if self.hid:
             res = res.replace("■", "0")
             return res
    def out(selfself, d):
         return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

b = Board()

def contour(self, ship, verb = False):
    near =[
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for d in ship.dots:
        for dx, dy in near:
            cur = Dot(d.x + dx, d.y + dy)
            if not(self.out(cur)) and cur not in self.busy:
                if verb:
                    self.field[cur.x][cur.y] = "."
                self.busy.append(cur)




