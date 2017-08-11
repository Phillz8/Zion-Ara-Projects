from tkinter import *
import random

class Canvascontrol():
    def __init__(self):
        self.width = 5
        self.height = 5
        self.minenum = 1
        self.boxval = [10,0,0,0,0,10,0,0,0,0,10,0,0,0,0,10,0,0,0,0,0,0,0,0,0]
        self.minelist = []
        self.clicklist = []

        listA = [[1, 2, 3],[1, 2, 3],[]]

        listA[x][y]

        #loop for choseing where to place mines
        """num = 0
        while num != self.minenum:
            mineval = random.randint(0, self.width * self.height - 1)
            minepick = False
            for i in self.minelist:
                if i == mineval:
                    minepick = True
            if minepick:
                num -= 1
            else:
                self.minelist.append(mineval)
            num += 1
        
        # loop for placing mines in random places
        num = 0
        while num != self.width * self.height:
            ismine = False
            for i in self.minelist:
                if i == num:
                    ismine = True
                    break
            if ismine:
                self.boxval.append(10)
            else:
                self.boxval.append(0)
            num += 1"""

        #loop for adding numbers
        num = 0
        for i in self.boxval:
            if i >= 10:
                # add one to box to the right
                if not (num + 1) % self.width == 0:
                    self.boxval[num + 1] += 1

                # add one to box to the left
                if not num % self.width == 0:
                    self.boxval[num - 1] += 1

                # add one to box below
                if not num >= self.width * self.height - self.width:
                    self.boxval[num + self.width] += 1

                # add one to box below and to the right
                if not num >= self.width * self.height - self.width and not (num + 1) % self.width == 0:
                    self.boxval[num + self.width + 1] += 1

                # add one to box below and to the left
                if not num >= self.width * self.height - self.width and not num % self.width == 0:
                    self.boxval[num + self.width - 1] += 1

                # add one to box above
                if num >= self.width:
                    self.boxval[num - self.width] += 1

                # add one to box above an to the right
                if num - self.width + 1 > 0 and not (num + 1) % self.width == 0:
                    self.boxval[num - self.width + 1] += 1

                # add one to box above and to the left
                if num - self.width - 1 >= 0 and not num % self.width == 0:
                    self.boxval[num - self.width - 1] += 1
            num += 1

        window = Tk()
        self.canvas = Canvas(window, width=self.width * 32 + 20, height=self.height * 32 + 60)
        self.box = PhotoImage(file='Images/box.gif')
        self.empty = PhotoImage(file='Images/Empty.gif')
        self.mine = PhotoImage(file='Images/Mine.gif')
        num = 0
        while num != self.width * self.height:
            """self.canvas.create_rectangle((num % self.width) * 32 + 10,
                                         ((num - num % self.width) / self.width) * 32 + 50,
                                         ((num % self.width) + 1) * 32 + 10,
                                         ((num - num % self.width) / self.width + 1) * 32 + 50,
                                         outline="black")"""
            self.canvas.create_image((num % self.width) * 32 + 26,((num - num % self.width) / self.width) * 32 + 66, image=self.box)
            num += 1
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.mousedown)
        window.mainloop()

    def mousedown(self, event):
        Canvascontrol.boxclick(self, event.x, event.y)

    def boxclick(self, x, y):
        self.x = x
        self.y = y
        self.loopnum = 0

        num = 0
        for val in self.boxval:
            if self.x > (num % self.width) * 32 + 10 and self.x < ((num % self.width) + 1) * 32 + 10 and self.y > ((num - num % self.width) / self.width) * 32 + 50 and self.y < ((num - num % self.width) / self.width + 1) * 32 + 50:
                if val >= 10:
                    self.canvas.create_image((num % self.width) * 32 + 26,
                                             ((num - num % self.width) / self.width) * 32 + 66, image=self.mine)
                    print("mine hit")
                elif val == 0:
                    self.boxval[num] = 9


                    # click box to the right
                    if not (num + 1) % self.width == 0:
                        self.boxclick(self.x + 32, self.y)

                    # add one to box to the left
                    if not (num - 1) % self.width == 0:
                        self.boxclick(self.x - 32, self.y)

                    # add one to box below
                    if not num >= self.width * self.height - self.width:
                        self.boxclick(self.x, self.y + 32)

                    # add one to box below and to the right
                    if not num >= self.width * self.height - self.width and not (num + 1) % self.width == 0:
                        self.boxclick(self.x + 32, self.y + 32)

                    # add one to box below and to the left
                    if not num >= self.width * self.height - self.width and not num % self.width == 0:
                        self.boxclick(self.x - 32, self.y + 32)

                    # add one to box above
                    if num >= self.width:
                        self.boxclick(self.x, self.y - 32)

                    # add one to box above an to the right
                    if num - self.width + 1 > 0 and not (num + 1) % self.width == 0:
                        self.boxclick(self.x + 32, self.y - 32)

                    # add one to box above and to the left
                    if num - self.width - 1 >= 0 and not num % self.width == 0:
                        self.boxclick(self.x - 32, self.y - 32)


                if val <= 8:
                    self.canvas.create_image((num % self.width) * 32 + 26,
                                             ((num - num % self.width) / self.width) * 32 + 66, image=self.empty)
                    self.canvas.create_text((num % self.width) * 32 + 26,
                                            ((num - num % self.width) / self.width) * 32 + 66, text=val)
                    self.boxval[num] = 9
            num += 1
            print(self.loopnum)

Canvascontrol()