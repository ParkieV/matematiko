import pygame
import sys

screen = ''
SIZE = WIDTH, HEIGHT = 800, 640
WHITE = 255, 255, 255


class Table(pygame.Surface):
    global screen

    def __init__(self, x=0, y=0, tablewidth=5, tableheight=5, casewidth=30, caseheight=30, color=(0,0,0)):
        pygame.Surface.__init__(self, (800, 640))
        self.tablewidth = tablewidth
        self.tableheight = tableheight
        self.casewidth = casewidth
        self.caseheight = caseheight
        self.pos = [x, y]
        self.color = color

    def initialization(self):
        x, y = self.pos
        for i in range(self.tableheight):
            for j in range(self.tablewidth):
                pygame.draw.rect(screen, self.color,
                                 (x, y, self.casewidth, self.caseheight),
                                 1)
                x += self.casewidth - 1
            x = self.pos[0]
            y += self.caseheight - 1


class MainMenu(pygame.Surface):
    global screen, WIDTH, HEIGHT, WHITE

    def __init__(self):
        pygame.Surface.__init__(self, size=(WIDTH, HEIGHT))
        self.postext = 213, 90
        self.posbutton1 = 275, 215
        self.posbutton2 = 275, 335
        self.posbutton3 = 275, 455
        self.f1 = pygame.font.Font('C:/projects/matematiko/src/fonts/Roboto-Black.ttf', 60)

    def initialization_objects(self):
        screen.fill(WHITE)
        text1 = self.f1.render('Математико', True, (172, 33, 22))
        button1 = pygame.image.load("C:/projects/matematiko/src/img/button1.gif")
        button2 = pygame.image.load("C:/projects/matematiko/src/img/button2.gif")
        button3 = pygame.image.load("C:/projects/matematiko/src/img/button3.gif")
        screen.blit(text1, self.postext)
        screen.blit(button1, self.posbutton1)
        screen.blit(button2, self.posbutton2)
        screen.blit(button3, self.posbutton3)


class Rules(pygame.Surface):
    global screen, WIDTH, HEIGHT

    def __init__(self):
        pygame.Surface.__init__(self, size=(WIDTH, HEIGHT))
        self.postext1 = 273, 50
        self.postext2 = 45, 150
        self.postext3 = 30, 175
        self.postext4 = 30, 200
        self.postext5 = 30, 225
        self.postext6 = 30, 250
        self.postext7 = 30, 275
        self.postext8 = 30, 300
        self.postext9 = 30, 325
        self.postext10 = 30, 350
        self.postext11 = 45, 390
        self.postext12 = 30, 415
        self.postext13 = 30, 440
        self.posbutton1 = 50, 500
        self.posbutton2 = 500, 500
        self.f1 = pygame.font.Font('C:/projects/matematiko/src/fonts/Roboto-Black.ttf', 60)
        self.f2 = pygame.font.Font('C:/projects/matematiko/src/fonts/Roboto-Black.ttf', 18)

    def initialization_objects(self):
        screen.fill(WHITE)
        text1 = self.f1.render('Правила', True, (0, 0, 0))
        text2 = self.f2.render('Имеется набор из 52 карточек, на которых записаны числа от 1 до 13,', True, (0, 0, 0))
        text3 = self.f2.render('причем карточки с каждым из этих чисел встречаются четырежды.', True, (0, 0, 0))
        text4 = self.f2.render('У каждого игрока имеется квадратное поле с 25 клетками. Программа', True, (0, 0, 0))
        text5 = self.f2.render('случайным образом извлекает какую-либо из имеющихся карточек и', True, (0, 0, 0))
        text6 = self.f2.render('выдает записанное на ней число. Каждый игрок заносит это число в одну из', True, (0, 0, 0))
        text7 = self.f2.render('клеток квадрата на своем поле. После того, как число записано,', True, (0, 0, 0))
        text8 = self.f2.render('перемещать его в другую клетку запрещается. Затем программа', True, (0, 0, 0))
        text9 = self.f2.render('случайным образом извлекает следующую карточку и.т.д.', True, (0, 0, 0))
        text10 = self.f2.render('Так продолжается до тех пор, пока не будут заполнены все клетки квадрата.', True, (0, 0, 0))
        text11 = self.f2.render('Результат игрока оценивается числом набранных им очков, зависящим от способа', True, (0, 0, 0))
        text12 = self.f2.render('чисел в клетках квадрата. Победителем считается тот, кто набирает наибольшее', True, (0, 0, 0))
        text13 = self.f2.render('количество очков. Подсчет очков производится по таблице.', True, (0, 0, 0))
        button1 = pygame.image.load("C:/projects/matematiko/src/img/button4.gif")
        button2 = pygame.image.load("C:/projects/matematiko/src/img/button5.gif")
        screen.blit(text1, self.postext1)
        screen.blit(text2, self.postext2)
        screen.blit(text3, self.postext3)
        screen.blit(text4, self.postext4)
        screen.blit(text5, self.postext5)
        screen.blit(text6, self.postext6)
        screen.blit(text7, self.postext7)
        screen.blit(text8, self.postext8)
        screen.blit(text9, self.postext9)
        screen.blit(text10, self.postext10)
        screen.blit(text11, self.postext11)
        screen.blit(text12, self.postext12)
        screen.blit(text13, self.postext13)
        screen.blit(button1, self.posbutton1)
        screen.blit(button2, self.posbutton2)


class TableWidget(pygame.Surface):
    global screen, SIZE

    def __init__(self):
        pygame.Surface.__init__(self, SIZE)
        self.f1 = pygame.font.Font('C:/projects/matematiko/src/fonts/Roboto-Black.ttf', 60)
        self.postext1 = 180, 20

        self.f2 = pygame.font.Font('C:/projects/matematiko/src/fonts/Roboto-Black.ttf', 16)
        self.postext2 = 162, 109
        self.postext3 = 412, 109
        self.postext4 = 592, 109

        self.f3 = pygame.font.Font('C:/projects/matematiko/src/fonts/Roboto-Black.ttf', 14)
        self.postext11 = 66, 143
        self.postext12 = 66, 177
        self.postext13 = 66, 211
        self.postext14 = 66, 245
        self.postext15 = 66, 279
        self.postext16 = 66, 313
        self.postext17f = 66, 343
        self.postext17s = 66, 360
        self.postext18f = 66, 387
        self.postext18s = 66, 404
        self.postext19f = 66, 431
        self.postext19s = 66, 448

        self.postext21 = 460, 143
        self.postext22 = 460, 177
        self.postext23 = 460, 211
        self.postext24 = 457, 245
        self.postext25 = 457, 279
        self.postext26 = 457, 313
        self.postext27 = 460, 352
        self.postext28 = 460, 396
        self.postext29 = 457, 440

        self.postext31 = 620, 143
        self.postext32 = 620, 177
        self.postext33 = 620, 211
        self.postext34 = 617, 245
        self.postext35 = 617, 279
        self.postext36 = 617, 313
        self.postext37 = 620, 352
        self.postext38 = 620, 396
        self.postext39 = 617, 440

        self.table1 = Table(57, 100, 1, 7, 350, 35)
        self.table2 = Table(406, 100, 2, 7, 160, 35)
        self.table3 = Table(57, 338, 1, 3, 350, 45)
        self.table4 = Table(406, 338, 2, 3, 160, 45)

        self.posbutton = 280, 510

    def initialization(self):

        text1 = self.f1.render('Таблица очков', True, (0, 0, 0))
        text2 = self.f2.render('Комбинации чисел', True, (0, 0, 0))
        text3 = self.f2.render('В ряду или столбце', True, (0, 0, 0))
        text4 = self.f2.render('По диагонали', True, (0, 0, 0))
        text11 = self.f3.render('За 2 одинаковых числа', True, (0, 0, 0))
        text12 = self.f3.render('За 2 пары одинаковых чисел', True, (0, 0, 0))
        text13 = self.f3.render('За 3 одинаковых числа', True, (0, 0, 0))
        text14 = self.f3.render('За 4 единицы', True, (0, 0, 0))
        text15 = self.f3.render('За 4 одинаковых числа', True, (0, 0, 0))
        text16 = self.f3.render('За три раза по 1 и два раза по 13', True, (0, 0, 0))
        text17f = self.f3.render('За 3 одинаковых числа и два других', True, (0, 0, 0))
        text17s = self.f3.render('одинаковых числа', True, (0, 0, 0))
        text18f = self.f3.render('За 5 последовательных чисел, но не обязательно', True, (0, 0, 0))
        text18s = self.f3.render('расположенных по порядку', True, (0, 0, 0))
        text19f = self.f3.render('За числа 1, 13, 12, 11 и 10, но не обязательно', True, (0, 0, 0))
        text19s = self.f3.render('расположенных по порядку', True, (0, 0, 0))
        text21 = self.f3.render('10 очков', True, (0, 0, 0))
        text22 = self.f3.render('20 очков', True, (0, 0, 0))
        text23 = self.f3.render('40 очков', True, (0, 0, 0))
        text24 = self.f3.render('200 очков', True, (0, 0, 0))
        text25 = self.f3.render('160 очков', True, (0, 0, 0))
        text26 = self.f3.render('100 очков', True, (0, 0, 0))
        text27 = self.f3.render('80 очков', True, (0, 0, 0))
        text28 = self.f3.render('50 очков', True, (0, 0, 0))
        text29 = self.f3.render('150 очков', True, (0, 0, 0))
        text31 = self.f3.render('20 очков', True, (0, 0, 0))
        text32 = self.f3.render('30 очков', True, (0, 0, 0))
        text33 = self.f3.render('50 очков', True, (0, 0, 0))
        text34 = self.f3.render('210 очков', True, (0, 0, 0))
        text35 = self.f3.render('170 очков', True, (0, 0, 0))
        text36 = self.f3.render('110 очков', True, (0, 0, 0))
        text37 = self.f3.render('90 очков', True, (0, 0, 0))
        text38 = self.f3.render('60 очков', True, (0, 0, 0))
        text39 = self.f3.render('160 очков', True, (0, 0, 0))
        button = pygame.image.load("C:/projects/matematiko/src/img/button5.gif")

        screen.fill(WHITE)
        self.table1.initialization()
        self.table2.initialization()
        self.table3.initialization()
        self.table4.initialization()
        screen.blit(text1, self.postext1)
        screen.blit(text2, self.postext2)
        screen.blit(text3, self.postext3)
        screen.blit(text4, self.postext4)
        screen.blit(text11, self.postext11)
        screen.blit(text12, self.postext12)
        screen.blit(text13, self.postext13)
        screen.blit(text14, self.postext14)
        screen.blit(text15, self.postext15)
        screen.blit(text16, self.postext16)
        screen.blit(text17f, self.postext17f)
        screen.blit(text17s, self.postext17s)
        screen.blit(text18f, self.postext18f)
        screen.blit(text18s, self.postext18s)
        screen.blit(text19f, self.postext19f)
        screen.blit(text19s, self.postext19s)
        screen.blit(text21, self.postext21)
        screen.blit(text22, self.postext22)
        screen.blit(text23, self.postext23)
        screen.blit(text24, self.postext24)
        screen.blit(text25, self.postext25)
        screen.blit(text26, self.postext26)
        screen.blit(text27, self.postext27)
        screen.blit(text28, self.postext28)
        screen.blit(text29, self.postext29)
        screen.blit(text31, self.postext31)
        screen.blit(text32, self.postext32)
        screen.blit(text33, self.postext33)
        screen.blit(text34, self.postext34)
        screen.blit(text35, self.postext35)
        screen.blit(text36, self.postext36)
        screen.blit(text37, self.postext37)
        screen.blit(text38, self.postext38)
        screen.blit(text39, self.postext39)
        screen.blit(button, self.posbutton)


class Logic():
    def __init__(self):
        self.acc = 0
        self.arr = [[0, 0, 0, 0, 0] for x in range(5)]

    def add(self, x, y, num):
        self.arr[x][y] = num
        self.count()

    def count_arr(self, arr):
        tempacc = 0
        nums = dict()
        for j in arr:
            if j != 0:
                if j not in nums:
                    nums[j] = 1
                else:
                    nums[j] += 1
        l = sorted(arr)[0]
        if sorted(arr) == [1, 10, 11, 12, 13]:
            tempacc += 150
        elif sorted(arr) == [l, l + 1, l + 2, l + 3, l + 4]:
            tempacc += 50
        else:
            for j in nums:
                if nums[j] == 4:
                    if j == 1:
                        tempacc += 200
                    else:
                        tempacc += 160
                elif nums[j] == 3:
                    if len(nums.keys()) >= 2:
                        if nums[j + 1] == 2:
                            if sorted(arr) == [1, 1, 1, 13, 13]:
                                tempacc += 100
                            else:
                                tempacc += 80
                        else:
                            tempacc += 40
                    else:
                        tempacc += 40
                elif nums[j] == 2:
                    if len(nums.keys()) >= 2:
                        if nums[j + 1] == 3:
                            if sorted(arr) == [1, 1, 1, 13, 13]:
                                tempacc += 100
                                tempacc -= 40
                            else:
                                tempacc += 80
                                tempacc -= 40
                            tempacc += 40
                        elif nums[j + 1] == 2 or nums[j + 2] == 2:
                            tempacc += 20
                        else:
                            tempacc += 10
                    else:
                        tempacc += 10
            return tempacc

    def count(self):
        self.acc = 0
        tempacc = 0
        for i in self.arr:
            self.acc += self.count_arr(i)
        temparr, temparr2 = [], []
        for i in range(5):
            temparr.append(self.arr[i][i])
            temparr2.append(self.arr[4 - i][4 - i])
        self.acc += self.count_arr(temparr)
        self.acc += self.count_arr(temparr2)
        temparr.clear()


class Field(pygame.Surface):
    def __init__(self):
        self.logic = Logic()
        self.table = Table(100, 100, 5, 5, 70, 70)

    def initialization(self):
        self.table.initialization()

class Game():
    def __init__(self, numplayers=2):
        self.numplayers = numplayers
        self.index = 1
        self.players = [0]

    def initialization_players(self):
        for i in range(self.numplayers):
            self.players.append(Field())
            

    def initialization(self):
        global screen, WHITE
        screen.fill(WHITE)
        self.initialization_players()
        self.players[self.index].initialization()


def main():
    pygame.init()

    global screen, SIZE
    screen = pygame.display.set_mode(SIZE)
    screen.fill(WHITE)
    numsurf = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if numsurf == 0:
                    if 275 <= x <= 525 and 455 <= y <= 535:
                        sys.exit()
                    elif 275 <= x <= 525 and 335 <= y <= 415:
                        numsurf = 2
                    elif 275 <= x <= 525 and 215 <= y <= 295:
                        for alp in range(150, 0, -8):
                            screen.set_alpha(alp)
                        numsurf = 4
                elif numsurf == 2:
                    if 500 <= x <= 750 and 500 <= y <= 580:
                        numsurf = 0
                    elif 50 <= x <= 300 and 500 <= y <= 580:
                        numsurf = 3
                elif numsurf == 3:
                    if 280 <= x <= 530 and 510 <= y <= 590:
                        numsurf = 2
            else:
                if numsurf == 0:
                    MainMenu().initialization_objects()
                elif numsurf == 2:
                    Rules().initialization_objects()
                elif numsurf == 3:
                    TableWidget().initialization()
                elif numsurf == 4:
                    GameWidget = Game()
                    GameWidget.initialization()
        pygame.display.flip()


if __name__ == "__main__":
    main()