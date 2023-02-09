from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
class App(QWidget):
    eda = 10
    energiya = 100
    goda = 0
    dney = 0
    dosyg = 99
    zdarovya = 100
    kihka = 0

    def kiihka(self):
        if self.kihka >= 100:
            print(f'{self.name} ты сново обосрался')
            self.kihka = 0

    def dniiiiii(self):
        self.dney += 1
        if self.dney == 365:
            self.goda += 1
            self.dney = 0
        elif self.eda <= 0:
            self.zdarovya -= 20
        elif self.energiya <= 0:
            print('ты вырубился (ы)')
            self.spiii()
            self.dney += 1
        self.kiihka()

    def gylya(self):
        print('ты гуууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууляешь')
        self.energiya -= 30
        self.dosyg += 30
        self.kihka += 20
        self.dniiiiii()

    def jrat(self):
        if self.eda >= 100:
            print("игрок ты совсем в меня не лезет")
        else:
            self.eda += 50
            self.dosyg -= 10
            self.kihka += 20
            self.dniiiiii()

    def figna(self):
        print('ты занемаешься фигнёй')
        self.energiya -= 30
        self.eda -= 20
        self.dosyg += 30
        self.kihka += 20
        self.dniiiiii()

    def spiii(self):
        print('ты спишь')
        self.energiya += 40
        self.eda -= 50
        self.dosyg += 5
        self.kihka += 20
        self.dniiiiii()

    def sriii(self):
        print('ты cрёёёёёёёёёёооооооооош')
        self.energiya -= 20
        self.eda -= 20
        self.kihka = 0
        self.dniiiiii()

    def __init__(self):
        self.start()
        self.pritt_info()
        self.button()

    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()

    def pritt_info(self):
        self.main_menu.textBrowser.setText("Здоровье - {}\nСытость - {}\nБодрость - {}\nДосуг - {}\nВозраст - {}\n"
                                           "Прожито дней - {}\nЖелудок -{}".format(self.zdarovya,self.eda,self.energiya,self.dosyg,self.goda,self.dney,self.kihka))
    def eat(self):
        self.jrat()
        self.pritt_info()
    def sleep(self):
        self.spiii()
        self.pritt_info()
    def fignya(self):
        self.figna()
        self.pritt_info()
    def puu(self):
        self.sriii()
        self.pritt_info()
    def walk(self):
        self.gylya()
        self.pritt_info()

    def button(self):
        self.main_menu.pushButton_2.clicked.connect(lambda: self.eat())
        self.main_menu.pushButton_3.clicked.connect(lambda: self.sleep())
        self.main_menu.pushButton_4.clicked.connect(lambda: self.fignya())
        self.main_menu.pushButton_5.clicked.connect(lambda: self.puu())
        self.main_menu.pushButton_6.clicked.connect(lambda: self.walk())
if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()