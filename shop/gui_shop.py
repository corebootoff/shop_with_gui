from tkinter import *
dic = {'Название': '', 'Производитель': '', 'Страна': '', 'Категория': '', 'Размер': '', 'Обьем': '', 'Цена': ''}

class MainWindow(Tk):
    def __init__(self):
        self.dic = {'Название': None, 'Производитель': None, 'Страна': None, 'Категория': None, 'Размер': None, 'Обьем': None, 'Цена': None}
        super(MainWindow, self).__init__()

        self.btn_add_product = Button(self, text = 'Добавить товар')
        self.btn_add_product.grid(row = 0, column = 0)
        self.sell = Button(self, text = 'Продать')
        self.sell.grid(row = 0, column = 1)
        self.info = Button(self, text = 'Информация')
        self.info.grid(row = 0, column = 2)

        self.btn_add_product.bind('<Button-1>', self.add_product)

    def add_product(self, event):
        ad = AddFrame(self, **dic)
        ad.mainloop()


class FieldFrame(Frame):
    def __init__(self, parent, name, value = str()):
        super(FieldFrame, self).__init__(parent)
        Label(self, text = name, width = 15).grid(row = 0, column = 0)

        self.text = StringVar()
        self.text.set(value if value else str())

        self.input = Entry(self, textvariable = self.text)
        self.input.insert(END, value)
        self.input.grid(row = 0, column = 1)


class AddFrame(Tk):
    def __init__(self, parent, **fields):
        super(AddFrame, self).__init__()

        self.main_frame = Frame(self)
        self.main_frame.grid(row = 0, column = 0)

        self.btn_frame = Frame(self)
        self.btn_frame.grid(row = 1, column =0)

        for idx, (name, value) in enumerate(fields. items()):
            field_frame = FieldFrame(self.main_frame, name, value)
            field_frame.grid(row = idx, column = 0)
        self.accept_btn = Button(self.btn_frame, text='Accept')
        self.accept_btn.grid(row=0, column=0)
        self.decline_btn = Button(self.btn_frame, text='Decline')
        self.decline_btn.grid(row=0, column=1)
    pass

if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
