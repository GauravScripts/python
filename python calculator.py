from tkinter import *


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False


    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1, pady = 5)

bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3, pady = 5)

bttn_mult = Button(calc, text = "x")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3, pady = 5)

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, pady = 5)

point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, pady = 5)

add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, pady = 5)

neg= Button(calc, text = "+/-")
neg["command"] = sum1.sign
neg.grid(row = 5, column = 0, pady = 5)

clear = Button(calc, text = "C")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, pady = 5)

all_clear = Button(calc, text = "AC")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 5, column = 2, pady = 5)

equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = 5)

root.mainloop()
