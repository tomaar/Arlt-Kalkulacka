from tkinter import *
from os import path
from calc_functions import *

# global tab
# tab = 1

root = Tk()
# root.attributes('-fullscreen', True)
root.state('zoomed')
root.title("Kalkulačka")

# base1 = Label(root)
# base2 = Label(root)

global FormatLog
global FormatAngle
global settings_list1
global scroll

his1_var = StringVar()
his2_var = StringVar()
his3_var = StringVar()
his4_var = StringVar()
his5_var = StringVar()
his6_var = StringVar()

try:
    settings_list1
except NameError:
    settings_list1 = [0, 0]

try:
    FormatLog
except NameError:
    FormatLog = 1

try:
    FormatAngle
except NameError:
    FormatAngle = 1

try:
    scroll
except NameError:
    scroll = 0


def format_log_10():
    global FormatLog
    FormatLog = 1


def format_log_e():
    global FormatLog
    FormatLog = 2


def format_log_2():
    global FormatLog
    FormatLog = 3


def format_angle_deg():
    global FormatAngle
    FormatAngle = 1


def format_angle_rad():
    global FormatAngle
    FormatAngle = 2


def format_angle_pirad():
    global FormatAngle
    FormatAngle = 3


def format_angle_grad():
    global FormatAngle
    FormatAngle = 4


MenuMain = Menu(root)
root.config(menu=MenuMain)

MenuFormat = Menu(MenuMain)

MenuFormatLog = Menu(MenuFormat)
MenuFormatLog.add_radiobutton(label="10", command=format_log_10)
MenuFormatLog.add_radiobutton(label="e", command=format_log_e)
MenuFormatLog.add_radiobutton(label="2", command=format_log_2)

MenuFormatAngle = Menu(MenuFormat)
MenuFormatAngle.add_radiobutton(label="°", command=format_angle_deg)
MenuFormatAngle.add_radiobutton(label="rad", command=format_angle_rad)
MenuFormatAngle.add_radiobutton(label="πrad", command=format_angle_pirad)
MenuFormatAngle.add_radiobutton(label="grad", command=format_angle_grad)

MenuMain.add_cascade(label="Formát", menu=MenuFormat)

MenuFormat.add_cascade(label="log", menu=MenuFormatLog)
MenuFormat.add_cascade(label="Úhel", menu=MenuFormatAngle)

e = Entry(width=180)


if not path.exists("calc_history.txt"):
    clc_his = open("calc_history.txt", "a", encoding="utf-8")
    for i in range(6):
        clc_his.write("Zde se zobrazí historie výpočtů\n")
    clc_his.close()

# def button_tab():
#     global tab
#     if tab == 1:
#         tab = 2
#         base1.forget()
#     elif tab == 2:
#         tab = 1
#         base2.forget()

# root.grid_remove()

# button1.delete()
# button2.delete()
# button3.delete()
# button4.delete()
# button5.delete()
# button6.delete()
# button7.delete()
# button8.delete()
# button9.delete()
# button0.delete()
#
# buttonPlus.delete()
# buttonMinus.delete()
# buttonTimes.delete()
# buttonDivide.delete()
#
# buttonLog.delete()
# buttonFact.delete()
# buttonPow.delete()
# buttonRoot.delete()
#
# buttonPoint.delete()
#
# buttonC.delete()
# buttonE.delete()

# render()


def key_his_up(event):
    global scroll
    if scroll > 0:
        scroll -= 1
        clc_his = open("calc_history.txt", "r", encoding="utf-8")
        clc_his_lines = clc_his.read().splitlines()
        his1_var.set(clc_his_lines[-scroll-1])
        his2_var.set(clc_his_lines[-scroll-2])
        his3_var.set(clc_his_lines[-scroll-3])
        his4_var.set(clc_his_lines[-scroll-4])
        his5_var.set(clc_his_lines[-scroll-5])
        his6_var.set(clc_his_lines[-scroll-6])
        num_ins = []
        for i in clc_his_lines[-scroll - 1]:
            if i != "=":
                num_ins.append(i)
            else:
                del num_ins[-1]
                break
        num_ins_str = "".join(num_ins)
        e.delete(0, END)
        e.insert(0, num_ins_str)
        clc_his.close()


def key_his_down(event):
    global scroll
    clc_his = open("calc_history.txt", "r", encoding="utf-8")
    clc_his_lines = clc_his.read().splitlines()

    num_ins = []
    for i in clc_his_lines[-scroll - 1]:
        if i != "=":
            num_ins.append(i)
        else:
            del num_ins[-1]
            break
    num_ins_str = "".join(num_ins)

    if e.get() != num_ins_str:
        e.delete(0, END)
        e.insert(0, num_ins_str)

    elif scroll < len(clc_his_lines) - 6:
        scroll += 1
        his1_var.set(clc_his_lines[-scroll - 1])
        his2_var.set(clc_his_lines[-scroll - 2])
        his3_var.set(clc_his_lines[-scroll - 3])
        his4_var.set(clc_his_lines[-scroll - 4])
        his5_var.set(clc_his_lines[-scroll - 5])
        his6_var.set(clc_his_lines[-scroll - 6])
        num_ins = []
        for i in clc_his_lines[-scroll - 1]:
            if i != "=":
                num_ins.append(i)
            else:
                del num_ins[-1]
                break
        num_ins_str = "".join(num_ins)
        e.delete(0, END)
        e.insert(0, num_ins_str)
    clc_his.close()


def key_fullsc(event):
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)


def key_calculate(event):
    button_calculate()


def key_quit(event):
    root.destroy()


root.bind("<KeyPress-Return>", key_calculate)
root.bind("<KeyPress-Escape>", key_quit)
root.bind("<Control-Key-f>", key_fullsc)
root.bind("<F11>", key_fullsc)
root.bind("<Up>", key_his_up)
root.bind("<Down>", key_his_down)


def button_click(char):
    e.insert(END, str(char))


def button_delete_one():
    e.delete(len(e.get())-1)


def button_delete():
    e.delete(0, END)


def button_calculate():
    global scroll
    scroll = 0

    tk_list1 = list(e.get())

    settings_list1[0] = FormatLog
    settings_list1[1] = FormatAngle

    calc_main(tk_list1, settings_list1)
    result_print = tk_list1[0]

    clc_his = open("calc_history.txt", "a", encoding="utf-8")
    clc_his.write(e.get())
    clc_his.write(" = ")
    clc_his.write(str(result_print))
    clc_his.write("\n")
    clc_his.close()

    e.delete(0, END)
    e.insert(0, str(result_print))

    clc_his = open("calc_history.txt", "r", encoding="utf-8")
    clc_his_lines = clc_his.read().splitlines()
    his1_var.set(clc_his_lines[-1])
    his2_var.set(clc_his_lines[-2])
    his3_var.set(clc_his_lines[-3])
    his4_var.set(clc_his_lines[-4])
    his5_var.set(clc_his_lines[-5])
    his6_var.set(clc_his_lines[-6])
    clc_his.close()


clc_his = open("calc_history.txt", "r", encoding="utf-8")
clc_his_lines = clc_his.read().splitlines()

his1_var.set(clc_his_lines[-1])
his2_var.set(clc_his_lines[-2])
his3_var.set(clc_his_lines[-3])
his4_var.set(clc_his_lines[-4])
his5_var.set(clc_his_lines[-5])
his6_var.set(clc_his_lines[-6])

clc_his.close()

his1 = Label(textvariable=his1_var, width=200)
his2 = Label(textvariable=his2_var, width=200)
his3 = Label(textvariable=his3_var, width=200)
his4 = Label(textvariable=his4_var, width=200)
his5 = Label(textvariable=his5_var, width=200)
his6 = Label(textvariable=his6_var, width=200)

button1 = Button(text="1", height=5, width=10, command=lambda: button_click(1))
button2 = Button(text="2", height=5, width=10, command=lambda: button_click(2))
button3 = Button(text="3", height=5, width=10, command=lambda: button_click(3))
button4 = Button(text="4", height=5, width=10, command=lambda: button_click(4))
button5 = Button(text="5", height=5, width=10, command=lambda: button_click(5))
button6 = Button(text="6", height=5, width=10, command=lambda: button_click(6))
button7 = Button(text="7", height=5, width=10, command=lambda: button_click(7))
button8 = Button(text="8", height=5, width=10, command=lambda: button_click(8))
button9 = Button(text="9", height=5, width=10, command=lambda: button_click(9))
button0 = Button(text="0", height=5, width=10, command=lambda: button_click(0))

buttonCE = Button(text="CE", height=5, width=10, command=button_delete)
buttonE = Button(text="=", height=5, width=10, command=button_calculate)

buttonPlus = Button(text="+", height=5, width=10, command=lambda: button_click("+"))
buttonMinus = Button(text="-", height=5, width=10, command=lambda: button_click("-"))
buttonTimes = Button(text="*", height=5, width=10, command=lambda: button_click("*"))
buttonDivide = Button(text="/", height=5, width=10, command=lambda: button_click("/"))

buttonPrime = Button(text="prv", height=5, width=10, command=lambda: button_click("prv"))
buttonNsd = Button(text="nsd", height=5, width=10, command=lambda: button_click("nsd"))
buttonNsn = Button(text="nsn", height=5, width=10, command=lambda: button_click("nsn"))
buttonPoint = Button(text=",", height=5, width=10, command=lambda: button_click(","))

buttonFact = Button(text="!", height=5, width=10, command=lambda: button_click("!"))
buttonLog = Button(text="log", height=5, width=10, command=lambda: button_click("log"))
buttonLd = Button(text="ld", height=5, width=10, command=lambda: button_click("ld"))
buttonLn = Button(text="ln", height=5, width=10, command=lambda: button_click("ln"))

buttonPi = Button(text="π", height=5, width=10, command=lambda: button_click("π"))
buttonEu = Button(text="e", height=5, width=10, command=lambda: button_click("e"))
buttonFi = Button(text="φ", height=5, width=10, command=lambda: button_click("φ"))
buttonC = Button(text="C", height=5, width=10, command=button_delete_one)

buttonLBra = Button(text="(", height=5, width=10, command=lambda: button_click("("))
buttonRBra = Button(text=")", height=5, width=10, command=lambda: button_click(")"))
buttonPow = Button(text="^", height=5, width=10, command=lambda: button_click("^"))
buttonRoot = Button(text="√", height=5, width=10, command=lambda: button_click("√"))

buttonSin = Button(text="sin", height=5, width=10, command=lambda: button_click("sin"))
buttonCos = Button(text="cos", height=5, width=10, command=lambda: button_click("cos"))
buttonTan = Button(text="tan", height=5, width=10, command=lambda: button_click("tan"))
buttonCtan = Button(text="ctan", height=5, width=10, command=lambda: button_click("ctan"))
buttonSec = Button(text="sec", height=5, width=10, command=lambda: button_click("sec"))
buttonCsec = Button(text="csec", height=5, width=10, command=lambda: button_click("csec"))

buttonAsin = Button(text="asin", height=5, width=10, command=lambda: button_click("asin"))
buttonacos = Button(text="acos", height=5, width=10, command=lambda: button_click("acos"))
buttonAtan = Button(text="atan", height=5, width=10, command=lambda: button_click("atan"))
buttonActan = Button(text="actan", height=5, width=10, command=lambda: button_click("actan"))
buttonAsec = Button(text="asec", height=5, width=10, command=lambda: button_click("asec"))
buttonAcsec = Button(text="acsec", height=5, width=10, command=lambda: button_click("acsec"))

buttonSinh = Button(text="sinh", height=5, width=10, command=lambda: button_click("sinh"))
buttonCosh = Button(text="cosh", height=5, width=10, command=lambda: button_click("cosh"))
buttonTanh = Button(text="tanh", height=5, width=10, command=lambda: button_click("tanh"))
buttonCtanh = Button(text="ctanh", height=5, width=10, command=lambda: button_click("ctanh"))
buttonSech = Button(text="sech", height=5, width=10, command=lambda: button_click("sech"))
buttonCsech = Button(text="csech", height=5, width=10, command=lambda: button_click("csech"))

buttonAsinh = Button(text="asinh", height=5, width=10, command=lambda: button_click("asinh"))
buttonacosh = Button(text="acosh", height=5, width=10, command=lambda: button_click("acosh"))
buttonAtanh = Button(text="atanh", height=5, width=10, command=lambda: button_click("atanh"))
buttonActanh = Button(text="actanh", height=5, width=10, command=lambda: button_click("actanh"))
buttonAsech = Button(text="asech", height=5, width=10, command=lambda: button_click("asech"))
buttonAcsech = Button(text="acsech", height=5, width=10, command=lambda: button_click("acsech"))


button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=0, column=0)
button8.grid(row=0, column=1)
button9.grid(row=0, column=2)
button0.grid(row=3, column=1)

buttonPlus.grid(row=0, column=3)
buttonMinus.grid(row=1, column=3)
buttonTimes.grid(row=2, column=3)
buttonDivide.grid(row=3, column=3)

buttonPi.grid(row=0, column=4, padx=(20, 0))
buttonEu.grid(row=1, column=4, padx=(20, 0))
buttonFi.grid(row=2, column=4, padx=(20, 0))
buttonC.grid(row=3, column=4, padx=(20, 0))

buttonLBra.grid(row=0, column=5)
buttonRBra.grid(row=1, column=5)
buttonPow.grid(row=2, column=5)
buttonRoot.grid(row=3, column=5)

buttonPrime.grid(row=0, column=6)
buttonPoint.grid(row=1, column=6)
buttonNsd.grid(row=2, column=6)
buttonNsn.grid(row=3, column=6)

buttonFact.grid(row=0, column=7)
buttonLog.grid(row=1, column=7)
buttonLd.grid(row=2, column=7)
buttonLn.grid(row=3, column=7)

buttonCE.grid(row=3, column=0)
buttonE.grid(row=3, column=2)

buttonSin.grid(row=4, column=0, pady=(20, 0))
buttonCos.grid(row=5, column=0)
buttonTan.grid(row=6, column=0)
buttonCtan.grid(row=7, column=0)
buttonSec.grid(row=8, column=0)
buttonCsec.grid(row=9, column=0)

buttonAsin.grid(row=4, column=1, pady=(20, 0))
buttonacos.grid(row=5, column=1)
buttonAtan.grid(row=6, column=1)
buttonActan.grid(row=7, column=1)
buttonAsec.grid(row=8, column=1)
buttonAcsec.grid(row=9, column=1)

buttonSinh.grid(row=4, column=2, pady=(20, 0))
buttonCosh.grid(row=5, column=2)
buttonTanh.grid(row=6, column=2)
buttonCtanh.grid(row=7, column=2)
buttonSech.grid(row=8, column=2)
buttonCsech.grid(row=9, column=2)

buttonAsinh.grid(row=4, column=3, pady=(20, 0))
buttonacosh.grid(row=5, column=3)
buttonAtanh.grid(row=6, column=3)
buttonActanh.grid(row=7, column=3)
buttonAsech.grid(row=8, column=3)
buttonAcsech.grid(row=9, column=3)

his1.grid(row=4, column=10)
his2.grid(row=5, column=10)
his3.grid(row=6, column=10)
his4.grid(row=7, column=10)
his5.grid(row=8, column=10)
his6.grid(row=9, column=10)

e.grid(row=0, column=10)

root.mainloop()
