def проверка_на_число():
    try:
        float(ввод_двоичного.get())
        вывод()
        return True
    except ValueError:
        messagebox.showinfo('Fatal ERROR', 'Введено число?')
        return False


def вывод():
    вывод_ноль = Label(master=window, text="Было введено число: " + ввод_двоичного.get())
    вывод_ноль.pack(expand=True)

    ввод = int(ввод_двоичного.get(), base=2)

    Восьмиричная = ''
    while ввод > 0:
        Восьмиричная = str(ввод % 8) + Восьмиричная
        ввод //= 8
    Восьмиричная = "Восьмиричная: " + Восьмиричная
    вывод_раз = Label(master=window, text=Восьмиричная)
    вывод_раз.pack(expand=True)

    ввод = int(ввод_двоичного.get(), base=2)
    Десятиричная = "Десятиричная: " + str(ввод)
    вывод_два = Label(master=window, text=Десятиричная)
    вывод_два.pack(expand=True)

    ввод = int(ввод_двоичного.get(), base=2)
    Шестнадцатеричная = ''
    алфавит16 = '0123456789ABCDEF'
    while ввод > 0:
        Шестнадцатеричная = алфавит16[ввод % 16] + Шестнадцатеричная
        ввод //= 16
    Шестнадцатеричная = "Шестнадцатеричная: " + Шестнадцатеричная
    вывод_три = Label(master=window, text=Шестнадцатеричная)
    вывод_три.pack(expand=True)


from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Калькулятор перевода из двоичной системы")

группа = Frame(master=window)
группа.pack(expand=True)

ввод_двоичного = Entry(master=группа)
ввод_двоичного.grid(row=0, column=0)
запись_двоичная = Label(master=группа, text="2")
запись_двоичная.grid(row=0, column=1)
кнопка = Button(master=группа, text="\N{RIGHTWARDS BLACK ARROW}", command=проверка_на_число)
кнопка.grid(row=0, column=2)

window.mainloop()

