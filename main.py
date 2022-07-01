# здесь подключаются модули
import sys
import pygame

from random import randint, seed
# здесь определяются константы,
# классы и функции
FPS = 10


W = 1200
H = 585
WC = 15
HC = 15
WW = 80
HH = 40
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GRAY = (127, 127, 127)
FILE = "saveRuler.sav"
colors = 4
nc = 1


def draw_table():

    for i in range(1, WW - 1):
        pygame.draw.line(sc, GREEN, (i * WC, 0), (i * WC, H))
    for i in range(1, HH - 1):
        pygame.draw.line(sc, GREEN, (0, i * HC), (W, i * HC))


def oo():

    for i in range(1, WW):
        for j in range(1, HH):
            if (pos[0] in range(WC * i - WC, WC * i)
                ) and (pos[1] in range(HC * j - HC, HC * j)):
                return (i - 1, j - 1)


def str_int(x):
    if x == '0':
        return 0
    elif x == '1':
        return 1
    elif x == '2':
        return 2
    elif x == '3':
        return 3
    elif x == '4':
        return 4
    else:
        return -1


def draw_world():
    for x in range(WW):
        for y in range(HH):
            for i in range(1, colors + 1):
                if world[x][y] == i:
                    pygame.draw.rect(sc,
                                     (colours[i - 1][0],
                                      colours[i - 1][1],
                                         colours[i - 1][2]),
                                     (WC * x,
                                         HC * y,
                                         WC,
                                         HC))
            if world[x][y] == 0:
                pygame.draw.rect(sc, (0, 0, 0), (WC * x, HC * y, WC, HC))


def read_save():
    f = open(FILE, 'r')
    x = 0
    b = f.read()
    for d in range(4):
        for y in range(2):

            s = b[x:x + 1]

            a = str_int(s)

            s = 0
            rules[d][y] = a
            x += 1

        y = 0

    draw_world()


def write_save():
    f = open(FILE, 'w')
    for x in range(4):
        for y in range(2):
            n = rules[x][y]
            n = str(n)
            f.write(n)


def new_rules():

    for i in range(colors + is_black):
        for j in range(nc):
            rules2[i][j] = randint(0, colors)
            rules3[i][j] = randint(0, colors)
            rules4[i][j] = randint(0, 24)


def new_world():
    for x in range(1, WW - 1):
        for y in range(1, HH - 1):
            world[x][y] = randint(0, colors)


def rules_start():
    world_new = []
    c = 0
    for i in range(WW):
        world_new.append([0] * HH)
    for x in range(WW):
        for y in range(HH):
            world_new[x][y] = world[x][y]
            if(is_black == 0):
                is_black2 = 1
            if(is_black == 1):
                is_black2 = 0
            for i in range(is_black2, colors + is_black):
                for j in range(nc):
                    if world[x][y] == i:
                        c = 0
                        if(not(x == 0 or y == 0 or x == 79 or y == 39)):
                            if(is_col == 1):
                                if(world[x - 1][y] == rules2[i][j]):
                                    c += 1
                                if(world[x + 1][y] == rules2[i][j]):
                                    c += 1

                                if(world[x - 1][y - 1] == rules2[i][j]):
                                    c += 1
                                if(world[x][y - 1] == rules2[i][j]):
                                    c += 1
                                if(world[x + 1][y - 1] == rules2[i][j]):
                                    c += 1

                                if(world[x - 1][y + 1] == rules2[i][j]):
                                    c += 1
                                if(world[x][y + 1] == rules2[i][j]):
                                    c += 1
                                if(world[x + 1][y + 1] == rules2[i][j]):
                                    c += 1

                                if(rules4[i][j] // 8 == 0):
                                    if(c < rules4[i][j] % 8):
                                        world_new[x][y] = rules3[i][j]
                                if(rules4[i][j] // 8 == 1):
                                    if(c == rules4[i][j] % 8):
                                        world_new[x][y] = rules3[i][j]
                                if(rules4[i][j] // 8 == 2):
                                    if(c > rules4[i][j] % 8):
                                        world_new[x][y] = rules3[i][j]
                            else:
                                if(world[x - 1][y] == rules2[i][j]):
                                    c += 1
                                if(world[x + 1][y] == rules2[i][j]):
                                    c += 1

                                if(world[x - 1][y - 1] == rules2[i][j]):
                                    c += 1
                                if(world[x][y - 1] == rules2[i][j]):
                                    c += 1
                                if(world[x + 1][y - 1] == rules2[i][j]):
                                    c += 1

                                if(world[x - 1][y + 1] == rules2[i][j]):
                                    c += 1
                                if(world[x][y + 1] == rules2[i][j]):
                                    c += 1
                                if(world[x + 1][y + 1] == rules2[i][j]):
                                    c += 1
                                if(c > 0):
                                    world_new[x][y] = rules3[i][j]

    for x in range(WW):
        for y in range(HH):
            world[x][y] = world_new[x][y]


#
# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

world = []

rules2 = []
rules3 = []
rules4 = []
world_new = []
rulerNum = 0
colors = int(input("Cells: "))
nc = int(input("How many cells will a cell watch: "))
is_col = int(input("Will the cell look at the number: "))
is_black = int(input("Will the black cell influence: "))
colours = []
for i in range(colors + is_black):

    rules2.append([0] * nc)
    rules3.append([0] * nc)
    rules4.append([0] * nc)

for i in range(WW):
    world.append([0] * HH)
for i in range(colors):
    colours.append([0] * 3)
for x in range(colors):
    for y in range(3):
        colours[x][y] = randint(0, 255)


new_rules()
new_world()

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    # --------
    # изменение объектов
    # --------
    if pressed[0]:
        a, b = oo()
        world[a][b] = 0

    if pressed[2]:
        a, b = oo()
        if key[pygame.K_1]:
            world[a][b] = 1
        if key[pygame.K_2]:
            world[a][b] = 2
        if key[pygame.K_3]:
            world[a][b] = 3
        if key[pygame.K_4]:
            world[a][b] = 4
        if key[pygame.K_5]:
            world[a][b] = 5
        if key[pygame.K_6]:
            world[a][b] = 6
        if key[pygame.K_7]:
            world[a][b] = 7
        if key[pygame.K_8]:
            world[a][b] = 8
        if key[pygame.K_9]:
            world[a][b] = 9
        if key[pygame.K_0]:
            world[a][b] = 10

    if key[pygame.K_g]:
        x = 0
        y = 0
        for x in range(WW):
            for y in range(HH):
                world[x][y] = 0
    if key[pygame.K_r]:
        new_rules()
        print(rules2)
        print(rules3)
    if key[pygame.K_h]:
        new_world()
    if key[pygame.K_s]:
        write_save()
    if key[pygame.K_l]:
        read_save()

    rules_start()
    draw_world()
    draw_table()

    # обновление экрана
    pygame.display.update()
