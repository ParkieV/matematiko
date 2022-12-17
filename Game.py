from random import randint



f = open("log.txt", 'w')


class Game():
    def __init__(self):
        self.acc = 0
        self.arr =[[0, 0, 0, 0, 0] for x in range(5)]

    def add(self, x, y, num):
        self.arr[x][y] = num
        self.count()

    def count_arr(self, arr, fl=False):
        tempacc = 0
        nums = dict()
        for j in arr:
            if j != 0:
                if j not in nums:
                    nums[j] = 1
                else:
                    nums[j] += 1
        l = sorted(arr)[0]
        if sorted(arr) == [1,10,11,12,13]:
            tempacc += 150
        elif sorted(arr) == [l, l + 1, l + 2, l + 3, l + 4] and l != 0:
            tempacc += 50
        else:
            if len(list(nums.keys())) == 1:
                if nums[list(nums.keys())[0]] == 4:
                    if list(nums.keys())[0] == 1:
                        tempacc += 200
                    else:
                        tempacc += 160
                elif nums[list(nums.keys())[0]] == 3:
                    tempacc += 40
                elif nums[list(nums.keys())[0]] == 2:
                    tempacc += 10
            elif len(list(nums.keys())) == 2:
                if sorted(list(nums.keys())) == [1, 13]:
                    if nums[1] == 3 and nums[13] == 2:
                        tempacc += 100
                    else:
                        if nums[1] == 3:
                            tempacc += 100
                        elif nums[1] == 4:
                            tempacc += 200
                        elif nums[1] == 2:
                            tempacc += 10
                        if nums[13] == 4:
                            tempacc += 160
                        elif nums[13] == 3:
                            tempacc += 40
                        elif nums[13] == 2:
                            tempacc += 10
                elif sorted(list(nums.keys()))[0] == 1 and nums[1] == 4:
                    tempacc += 200
                else:
                    flpair = False
                    for j in nums:
                        if nums[j] == 2:
                            tempacc += 10
                            if flpair:
                                tempacc += 30
                                break
                            flpair = True
                        elif nums[j] == 3:
                            tempacc += 40
                            if flpair:
                                tempacc += 30
                                break
                            flpair = True
            elif len(list(nums.keys())) == 3:
                for j in nums:
                    if nums[j] == 2:
                        tempacc += 10
                    elif nums[j] == 3:
                        tempacc += 40
            else:
                for j in nums:
                    if nums[j] == 2:
                        tempacc += 10
                        break
        if fl and tempacc != 0:
            return tempacc + 10
        else:
            return tempacc

    def count(self):
        self.acc = 0
        tempacc = 0
        for i in self.arr:
            self.acc += self.count_arr(i)
        for i in range(len(self.arr)):
            arr_height = []
            for j in range(5):
                arr_height.append(self.arr[j][i])
            self.acc += self.count_arr(arr_height)
        temparr, temparr2 = [], []
        for i in range(5):
            temparr.append(self.arr[i][i])
            temparr2.append(self.arr[4 - i][i])
        self.acc += self.count_arr(temparr, True)
        self.acc += self.count_arr(temparr2, True)
        temparr.clear()

    def print_table(self):
        global f
        for i in range(5):
            for j in range(5):
                f.write(self.arr[i][j], end="/t")
            f.write()
        f.write("acc now is:", self.acc, end="/n/n")


def main():
    Player1 = Game()
    ARR = [0]
    for i in range(1, 26):
        for j in range(4):
            ARR.append(i)
    for i in range(25):
        index = randint(1, len(ARR) - 1)
        card = ARR[index]
        ARR.pop(index)
        print("Card is:", card, end="/n/n")
        Player1.print_table()
        fl = False
        while fl is False:
            print("Input correct coords: ", end="")
            x, y = i // 5, (i + 1) % 5
            # x, y = [int(i) for i in input().split(" ")]
            if Player1.arr[x - 1][y - 1] == 0:
                Player1.add(x - 1, y - 1, card)
                fl = True
            else:
                print("Incorrect coords")

if __name__ == "__main__":
    player = Game()
    player.add(0, 0, 3)
    player.add(1, 1, 3)
    player.add(2, 2, 0)
    player.add(3, 3, 13)
    player.add(4, 4, 13)
    assert player.acc == 30