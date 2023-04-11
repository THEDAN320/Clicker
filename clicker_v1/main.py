import sys
import random
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget
from PySide6.QtCore import QTimer, QSize, Qt,QUrl, Slot, Signal, QThread
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from ui.gui import Ui_MainWindow
from ui.UI_Upgrade import Ui_upgradeWidget
from ui.UI_Achievement import Ui_AchievementWidget

from random import randint 


#создаем класс для всех зданий
class Build:
    
    def __init__(self,image: str,cps: int,base_cost: int):
        self.image = image
        self.count = 0
        self.cps = [cps]
        self.base_cost = base_cost
        

#создаем апгрейд виджет
class Upgrade(QWidget):
    buy = Signal()
    
    def __init__(self, price: int, name: str, upgrade_stat: list, number: int, parent=None):
        super(Upgrade, self).__init__(parent)
        self.ui = Ui_upgradeWidget()
        self.ui.setupUi(self)
        self.price = price
        self.name = name
        self.upgrade_stat = upgrade_stat
        self.number = number
        self.ui.info_upgrade_lbl.setText(f"price: {str(price)} \n+{number} to {name} profit")
        self.ui.buy_upgrade_btn.clicked.connect(self.buy_f)
        
    #создаем слот для обработки покупки
    def buy_f(self):
        self.buy.emit()


# создаем обработчик для прогресс бара
class ProgressHandler(QThread):
    mysignal = Signal()
        
    #создаем слот для обработки обновления прогресс бара
    def run(self):
        self.mysignal.emit()


#создаем виджет достижения
class Achievement(QWidget):
    
    def __init__(self, text: list[str], needle_progress_list: list[int], current_progress: int, awards: list, parent=None):
        super(Achievement, self).__init__(parent)
        self.ui = Ui_AchievementWidget()
        self.ui.setupUi(self)
        
        self.level = 0
        self.text = text
        self.ui.achievement_label.setText(text[self.level])
        self.needle_progress_list = needle_progress_list
        self.needle_progress = needle_progress_list[self.level]
        self.awards = awards
        self.current_progress = current_progress
        
        self.ui.progressBar.setValue(0)
        
    #создаем функцию с обновлением прогресс бара
    def signal_handler(self):
            count: int = ((self.current_progress / self.needle_progress) * 100) // 1
            if count < 100:
                self.ui.progressBar.setValue(count)
            else:
                self.ui.progressBar.setValue(100)
    
    #создаем функцию для обновления текущего прогресса
    def update(self, current_progress: int, upgrade_layout):
        #обновляем уровень достижения
        self.needle_progress = self.needle_progress_list[self.level]
        
        #обновляем прогресс достижения
        self.current_progress = current_progress
        
        #создаем экземпляр класса с потоком и его обработчик
        self.handler = ProgressHandler()
        self.handler.mysignal.connect(self.signal_handler)
        self.handler.start()
        if self.needle_progress <= current_progress and self.level < len(self.text):
            self.ui.progressBar.setValue(0)
            upgrade_layout.addWidget(self.awards[self.level])
            self.level += 1
            self.ui.achievement_label.setText(self.text[self.level])
    

#создаем наше главное окно
class apps(QMainWindow):

    def __init__(self):
        super(apps, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.price = 0
        
        #добавляем автоклики
        cps_timer = QTimer(self)
        cps_timer.timeout.connect(self.cps_add)
        cps_timer.start(1000)
        
        #включаем музыку
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("music/Murlock.mp3"))
        self.audioOutput.setVolume(50)
        self.player.play()
        
        timer_music = QTimer(self)
        timer_music.timeout.connect(self.music)
        timer_music.start(145000)
        
        #создаем объекты классов наших зданий
        self.house = Build("sprites_town/house.png",1,50)
        self.hotel = Build(".jpg",5,300)
        self.tavern = Build("sprites_town/tavern.png",30,1_500)
        self.restaurant = Build("sprites_town/restaurant.png",75,9_000)
        self.blacksmith = Build("sprites_town/blacksmith.png",150,30_000)
        self.tailor = Build("sprites_town/tailor.png",400,100_000)
        self.alchemy = Build("sprites_town/alchemy.png",1_000,500_000)
        self.market = Build(".jpg",5_000,3_000_000)
        self.brothel = Build(".jpg",20_000,20_000_000)
        self.arena = Build("sprites_town/arena.png",75_000,1_000_000_000)
        self.barracks = Build(".jpg",200_000,5_000_000_000)
        self.colosseum = Build("sprites_town/colosseum.png",500_000,25_000_000_000)
        self.libraly = Build("sprites_town/libraly.png",5_000_000,500_000_000_000)
        self.church = Build("sprites_town/church.png",25_000_000,5_000_000_000_000)
        self.cathedral = Build("sprites_town/cathedral.png",200_000_000,50_000_000_000_000)
        self.castle = Build(".jpg",1_000_000_000,1_000_000_000_000_000)
        
        #создаем параметры и статистику игрока
        self.cash = 0 
        self.click_cash = [1]
        self.X_Buy = 1
        self.selected_building = self.house
        self.info(self.house)
        self.counter_click = 0
        self.count_click_persecond = 0
        
        #подключаем кнопку для клика
        self.ui.click_button.clicked.connect(self.click)
        
        #подключаем функцию вывода информации для каждого здания
        self.ui.House_button.clicked.connect(lambda: self.info(self.house))
        self.ui.Hotel_button.clicked.connect(lambda: self.info(self.hotel))
        self.ui.Tavern_button.clicked.connect(lambda: self.info(self.tavern))
        self.ui.Restaurant_button.clicked.connect(lambda: self.info(self.restaurant))
        self.ui.Blacksmith_button.clicked.connect(lambda: self.info(self.blacksmith))
        self.ui.Tailor_button.clicked.connect(lambda: self.info(self.tailor))
        self.ui.Alchemy_button.clicked.connect(lambda: self.info(self.alchemy))
        self.ui.Market_button.clicked.connect(lambda: self.info(self.market))
        self.ui.Brothel_button.clicked.connect(lambda: self.info(self.brothel))
        self.ui.Arena_button.clicked.connect(lambda: self.info(self.arena))
        self.ui.Barracks_button.clicked.connect(lambda: self.info(self.barracks))
        self.ui.Colosseum_button.clicked.connect(lambda: self.info(self.colosseum))
        self.ui.Libraly_button.clicked.connect(lambda: self.info(self.libraly))
        self.ui.Church_button.clicked.connect(lambda: self.info(self.church))
        self.ui.Cathedral_button.clicked.connect(lambda: self.info(self.cathedral))
        self.ui.Castle_button.clicked.connect(lambda: self.info(self.castle))
        
        #подключаем кнопку покупки здания
        self.ui.Buy_Button.clicked.connect(self.buy_build)
        
        #подключаем радио кнопки
        self.ui.X1_Radio.toggled.connect(lambda:self.click_radio(1))
        self.ui.X10_Radio.toggled.connect(lambda:self.click_radio(2))
        self.ui.X100_Radio.toggled.connect(lambda:self.click_radio(3))
        
        
        
        #создаем все достижения
        #достижений для кликов
        awards_for_click = [
        self.add_upgrade(200,"click",self.click_cash,1),
        self.add_upgrade(3_000,"click",self.click_cash,98),
        self.add_upgrade(50_000,"click",self.click_cash,900),
        self.add_upgrade(1_000_000,"click",self.click_cash,99_000),
        self.add_upgrade(500_000_000,"click",self.click_cash,9_900_000),
        ]  
        
        text_for_click = ["make a 100 clicks", "make a 1000 clicks", "make a 10_000 clicks", "make a 50__000 clicks", "make a 150_000 clicks"]
        
        needle_progress_for_click = [100, 1000, 10_000,50_000,150_000]
        
        self.achievement_click = Achievement(text_for_click, needle_progress_for_click, self.counter_click, awards_for_click)
        self.ui.achievement_layout.addWidget(self.achievement_click)
        
        #достижений для дома
        awards_for_house = [
        self.add_upgrade(2_000,"house",self.house.cps,1),
        self.add_upgrade(20_000,"house",self.house.cps,1),
        self.add_upgrade(500_000,"house",self.house.cps,1),
        self.add_upgrade(18_000_000,"house",self.house.cps,1),
        self.add_upgrade(650_000_000,"house",self.house.cps,1),
        ]  
        
        text_for_house = ["buy a 10 Houses", "buy a 25 Houses", "buy a 50 Houses", "buy a 75 Houses", "buy a 100 Houses"]
        
        needle_progress_for_house = [10, 25, 50,75,100]
        
        self.achievement_house = Achievement(text_for_house, needle_progress_for_house, self.house.count, awards_for_house)
        self.ui.achievement_layout.addWidget(self.achievement_house)
        
        #достижений для отеля
        awards_for_hotel = [
        self.add_upgrade(10_000,"hotel",self.hotel.cps,1),
        self.add_upgrade(100_000,"hotel",self.hotel.cps,1),
        self.add_upgrade(3_000_000,"hotel",self.hotel.cps,1),
        self.add_upgrade(130_000_000,"hotel",self.hotel.cps,1),
        self.add_upgrade(3_000_000_000,"hotel",self.hotel.cps,1),
        ]  
        
        text_for_hotel = ["buy a 10 hotels", "buy a 25 hotels", "buy a 50 hotels", "buy a 75 hotels", "buy a 100 hotels"]
        
        needle_progress_for_hotel = [10, 25, 50,75,100]
        
        self.achievement_hotel = Achievement(text_for_hotel, needle_progress_for_hotel, self.hotel.count, awards_for_hotel)
        self.ui.achievement_layout.addWidget(self.achievement_hotel)
        
        #достижений для таверны
        awards_for_tavern = [
        self.add_upgrade(50_000,"tavern",self.tavern.cps,1),
        self.add_upgrade(500_000,"tavern",self.tavern.cps,1),
        self.add_upgrade(15_000_000,"tavern",self.tavern.cps,1),
        self.add_upgrade(500_000_000,"tavern",self.tavern.cps,1),
        self.add_upgrade(15_000_000_000,"tavern",self.tavern.cps,1),
        ]  
        
        text_for_tavern = ["buy a 10 taverns", "buy a 25 taverns", "buy a 50 taverns", "buy a 75 taverns", "buy a 100 taverns"]
        
        needle_progress_for_tavern = [10, 25, 50,75,100]
        
        self.achievement_tavern = Achievement(text_for_tavern, needle_progress_for_tavern, self.tavern.count, awards_for_tavern)
        self.ui.achievement_layout.addWidget(self.achievement_tavern)
        
        #достижений для ресторана
        awards_for_restaurant = [
        self.add_upgrade(150_000,"restaurant",self.restaurant.cps,1),
        self.add_upgrade(1_500_000,"restaurant",self.restaurant.cps,1),
        self.add_upgrade(100_000_000,"restaurant",self.restaurant.cps,1),
        self.add_upgrade(3_000_000_000,"restaurant",self.restaurant.cps,1),
        self.add_upgrade(120_000_000_000,"restaurant",self.restaurant.cps,1),
        ]  
        
        text_for_restaurant = ["buy a 10 restaurants", "buy a 25 restaurants", "buy a 50 restaurants", "buy a 75 restaurants", "buy a 100 restaurants"]
        
        needle_progress_for_restaurant = [10, 25, 50,75,100]
        
        self.achievement_restaurant = Achievement(text_for_restaurant, needle_progress_for_restaurant, self.restaurant.count, awards_for_restaurant)
        self.ui.achievement_layout.addWidget(self.achievement_restaurant)
        
        #достижений для кузницы
        awards_for_blacksmith = [
        self.add_upgrade(1_000_000,"blacksmith",self.blacksmith.cps,1),
        self.add_upgrade(10_000_000,"blacksmith",self.blacksmith.cps,1),
        self.add_upgrade(300_000_000,"blacksmith",self.blacksmith.cps,1),
        self.add_upgrade(12_000_000_000,"blacksmith",self.blacksmith.cps,1),
        self.add_upgrade(300_000_000_000,"blacksmith",self.blacksmith.cps,1),
        ]  
        
        text_for_blacksmith = ["buy a 10 blacksmiths", "buy a 25 blacksmiths", "buy a 50 blacksmiths", "buy a 75 blacksmiths", "buy a 100 blacksmiths"]
        
        needle_progress_for_blacksmith = [10, 25, 50,75,100]
        
        self.achievement_blacksmith = Achievement(text_for_blacksmith, needle_progress_for_blacksmith, self.blacksmith.count, awards_for_blacksmith)
        self.ui.achievement_layout.addWidget(self.achievement_blacksmith)
        
        #достижений для швейной
        awards_for_tailor = [
        self.add_upgrade(3_000_000,"tailor",self.tailor.cps,1),
        self.add_upgrade(30_000_000,"tailor",self.tailor.cps,1),
        self.add_upgrade(1_200_000_000,"tailor",self.tailor.cps,1),
        self.add_upgrade(30_000_000_000,"tailor",self.tailor.cps,1),
        self.add_upgrade(1_200_000_000_000,"tailor",self.tailor.cps,1),
        ]  
        
        text_for_tailor = ["buy a 10 tailors", "buy a 25 tailors", "buy a 50 tailors", "buy a 75 tailors", "buy a 100 tailors"]
        
        needle_progress_for_tailor = [10, 25, 50,75,100]
        
        self.achievement_tailor = Achievement(text_for_tailor, needle_progress_for_tailor, self.tailor.count, awards_for_tailor)
        self.ui.achievement_layout.addWidget(self.achievement_tailor)
        
        #достижений для алхимии
        awards_for_alchemy = [
        self.add_upgrade(15_000_000,"alchemy",self.alchemy.cps,1),
        self.add_upgrade(150_000_000,"alchemy",self.alchemy.cps,1),
        self.add_upgrade(5_000_000_000,"alchemy",self.alchemy.cps,1),
        self.add_upgrade(150_000_000_000,"alchemy",self.alchemy.cps,1),
        self.add_upgrade(5_000_000_000_000,"alchemy",self.alchemy.cps,1),
        ]  
        
        text_for_alchemy = ["buy a 10 alchemys", "buy a 25 alchemys", "buy a 50 alchemys", "buy a 75 alchemys", "buy a 100 alchemys"]
        
        needle_progress_for_alchemy = [10, 25, 50,75,100]
        
        self.achievement_alchemy = Achievement(text_for_alchemy, needle_progress_for_alchemy, self.alchemy.count, awards_for_alchemy)
        self.ui.achievement_layout.addWidget(self.achievement_alchemy)
        
        #достижений для рынка
        awards_for_market = [
        self.add_upgrade(100_000_000,"market",self.market.cps,1),
        self.add_upgrade(1_000_000_000,"market",self.market.cps,1),
        self.add_upgrade(30_000_000_000,"market",self.market.cps,1),
        self.add_upgrade(1_200_000_000_000,"market",self.market.cps,1),
        self.add_upgrade(30_000_000_000_000,"market",self.market.cps,1),
        ]  
        
        text_for_market = ["buy a 10 markets", "buy a 25 markets", "buy a 50 markets", "buy a 75 markets", "buy a 100 markets"]
        
        needle_progress_for_market = [10, 25, 50,75,100]
        
        self.achievement_market = Achievement(text_for_market, needle_progress_for_market, self.market.count, awards_for_market)
        self.ui.achievement_layout.addWidget(self.achievement_market)
        
        #достижений для борделя
        awards_for_brothel = [
        self.add_upgrade(600_000_000,"brothel",self.brothel.cps,1),
        self.add_upgrade(6_000_000_000,"brothel",self.brothel.cps,1),
        self.add_upgrade(150_000_000_000,"brothel",self.brothel.cps,1),
        self.add_upgrade(6_000_000_000_000,"brothel",self.brothel.cps,1),
        self.add_upgrade(150_000_000_000_000,"brothel",self.brothel.cps,1),
        ]  
        
        text_for_brothel = ["buy a 10 brothels", "buy a 25 brothels", "buy a 50 brothels", "buy a 75 brothels", "buy a 100 brothels"]
        
        needle_progress_for_brothel = [10, 25, 50,75,100]
        
        self.achievement_brothel = Achievement(text_for_brothel, needle_progress_for_brothel, self.brothel.count, awards_for_brothel)
        self.ui.achievement_layout.addWidget(self.achievement_brothel)
        
        #достижений для арены
        awards_for_arena = [
        self.add_upgrade(30_000_000_000,"arena",self.arena.cps,1),
        self.add_upgrade(300_000_000_000,"arena",self.arena.cps,1),
        self.add_upgrade(12_000_000_000_000,"arena",self.arena.cps,1),
        self.add_upgrade(300_000_000_000_000,"arena",self.arena.cps,1),
        self.add_upgrade(12_000_000_000_000_000,"arena",self.arena.cps,1),
        ]  
        
        text_for_arena = ["buy a 10 arenas", "buy a 25 arenas", "buy a 50 arenas", "buy a 75 arenas", "buy a 100 arenas"]
        
        needle_progress_for_arena = [10, 25, 50,75,100]
        
        self.achievement_arena = Achievement(text_for_arena, needle_progress_for_arena, self.arena.count, awards_for_arena)
        self.ui.achievement_layout.addWidget(self.achievement_arena)
        
        #достижений для барраков
        awards_for_barracks = [
        self.add_upgrade(150_000_000_000,"barracks",self.barracks.cps,1),
        self.add_upgrade(1_500_000_000_000,"barracks",self.barracks.cps,1),
        self.add_upgrade(50_000_000_000_000,"barracks",self.barracks.cps,1),
        self.add_upgrade(1_500_000_000_000_000,"barracks",self.barracks.cps,1),
        self.add_upgrade(50_000_000_000_000_000,"barracks",self.barracks.cps,1),
        ]  
        
        text_for_barracks = ["buy a 10 barrackss", "buy a 25 barrackss", "buy a 50 barrackss", "buy a 75 barrackss", "buy a 100 barrackss"]
        
        needle_progress_for_barracks = [10, 25, 50,75,100]
        
        self.achievement_barracks = Achievement(text_for_barracks, needle_progress_for_barracks, self.barracks.count, awards_for_barracks)
        self.ui.achievement_layout.addWidget(self.achievement_barracks)
        
        #достижений для колизея
        awards_for_colosseum = [
        self.add_upgrade(750_000_000_000,"colosseum",self.colosseum.cps,1),
        self.add_upgrade(8_000_000_000_000,"colosseum",self.colosseum.cps,1),
        self.add_upgrade(150_000_000_000_000,"colosseum",self.colosseum.cps,1),
        self.add_upgrade(8_000_000_000_000_000,"colosseum",self.colosseum.cps,1),
        self.add_upgrade(150_000_000_000_000_000,"colosseum",self.colosseum.cps,1),
        ]  
        
        text_for_colosseum = ["buy a 10 colosseums", "buy a 25 colosseums", "buy a 50 colosseums", "buy a 75 colosseums", "buy a 100 colosseums"]
        
        needle_progress_for_colosseum = [10, 25, 50,75,100]
        
        self.achievement_colosseum = Achievement(text_for_colosseum, needle_progress_for_colosseum, self.colosseum.count, awards_for_colosseum)
        self.ui.achievement_layout.addWidget(self.achievement_colosseum)
        
        #достижений для библиотеки
        awards_for_libraly = [
        self.add_upgrade(15_000_000_000_000,"libraly",self.libraly.cps,1),
        self.add_upgrade(150_000_000_000_000,"libraly",self.libraly.cps,1),
        self.add_upgrade(5_000_000_000_000_000,"libraly",self.libraly.cps,1),
        self.add_upgrade(150_000_000_000_000_000,"libraly",self.libraly.cps,1),
        self.add_upgrade(5_000_000_000_000_000_000,"libraly",self.libraly.cps,1),
        ]  
        
        text_for_libraly = ["buy a 10 libralys", "buy a 25 libralys", "buy a 50 libralys", "buy a 75 libralys", "buy a 100 libralys"]
        
        needle_progress_for_libraly = [10, 25, 50,75,100]
        
        self.achievement_libraly = Achievement(text_for_libraly, needle_progress_for_libraly, self.libraly.count, awards_for_libraly)
        self.ui.achievement_layout.addWidget(self.achievement_libraly)
        
        #достижений для церкви
        awards_for_church = [
        self.add_upgrade(150_000_000_000_000,"church",self.church.cps,1),
        self.add_upgrade(1_500_000_000_000_000,"church",self.church.cps,1),
        self.add_upgrade(50_000_000_000_000_000,"church",self.church.cps,1),
        self.add_upgrade(1_500_000_000_000_000_000,"church",self.church.cps,1),
        self.add_upgrade(50_000_000_000_000_000_000,"church",self.church.cps,1),
        ]  
        
        text_for_church = ["buy a 10 churchs", "buy a 25 churchs", "buy a 50 churchs", "buy a 75 churchs", "buy a 100 churchs"]
        
        needle_progress_for_church = [10, 25, 50,75,100]
        
        self.achievement_church = Achievement(text_for_church, needle_progress_for_church, self.church.count, awards_for_church)
        self.ui.achievement_layout.addWidget(self.achievement_church)
        
        #достижений для собора
        awards_for_cathedral = [
        self.add_upgrade(2_000,"cathedral",self.cathedral.cps,1),
        self.add_upgrade(7_500,"cathedral",self.cathedral.cps,1),
        self.add_upgrade(200_000,"cathedral",self.cathedral.cps,1),
        self.add_upgrade(6_000_000,"cathedral",self.cathedral.cps,1),
        self.add_upgrade(100_000_000,"cathedral",self.cathedral.cps,1),
        ]  
        
        text_for_cathedral = ["buy a 10 cathedrals", "buy a 25 cathedrals", "buy a 50 cathedrals", "buy a 75 cathedrals", "buy a 100 cathedrals"]
        
        needle_progress_for_cathedral = [10, 25, 50,75,100]
        
        self.achievement_cathedral = Achievement(text_for_cathedral, needle_progress_for_cathedral, self.cathedral.count, awards_for_cathedral)
        self.ui.achievement_layout.addWidget(self.achievement_cathedral)
        
        #достижений для замка
        awards_for_castle = [
        self.add_upgrade(2_000,"castle",self.castle.cps,1),
        self.add_upgrade(7_500,"castle",self.castle.cps,1),
        self.add_upgrade(200_000,"castle",self.castle.cps,1),
        self.add_upgrade(6_000_000,"castle",self.castle.cps,1),
        self.add_upgrade(100_000_000,"castle",self.castle.cps,1),
        ]  
        
        text_for_castle = ["buy a 10 castles", "buy a 25 castles", "buy a 50 castles", "buy a 75 castles", "buy a 100 castles"]
        
        needle_progress_for_castle = [10, 25, 50,75,100]
        
        self.achievement_castle = Achievement(text_for_castle, needle_progress_for_castle, self.castle.count, awards_for_castle)
        self.ui.achievement_layout.addWidget(self.achievement_castle)
        
        #запускаем обновление достижений
        timer = QTimer(self)
        timer.timeout.connect(self.achievements_update)
        timer.start(1000)
        
    #функция обновления всех достижений
    def achievements_update(self):
        self.achievement_click.update(self.counter_click, self.ui.upgrade_layout)
        self.achievement_house.update(self.house.count, self.ui.upgrade_layout)
        self.achievement_hotel.update(self.hotel.count, self.ui.upgrade_layout)
        self.achievement_tavern.update(self.tavern.count, self.ui.upgrade_layout)
        self.achievement_restaurant.update(self.restaurant.count, self.ui.upgrade_layout)
        self.achievement_blacksmith.update(self.blacksmith.count, self.ui.upgrade_layout)
        self.achievement_tailor.update(self.tailor.count, self.ui.upgrade_layout)
        self.achievement_alchemy.update(self.alchemy.count, self.ui.upgrade_layout)
        self.achievement_market.update(self.market.count, self.ui.upgrade_layout)
        self.achievement_brothel.update(self.brothel.count, self.ui.upgrade_layout)
        self.achievement_arena.update(self.arena.count, self.ui.upgrade_layout)
        self.achievement_barracks.update(self.barracks.count, self.ui.upgrade_layout)
        self.achievement_colosseum.update(self.colosseum.count, self.ui.upgrade_layout)
        self.achievement_libraly.update(self.libraly.count, self.ui.upgrade_layout)
        self.achievement_church.update(self.church.count, self.ui.upgrade_layout)
        self.achievement_cathedral.update(self.cathedral.count, self.ui.upgrade_layout)
        self.achievement_castle.update(self.castle.count, self.ui.upgrade_layout)
    
    #конвретируем вывод числа в научную нотацию если число больше 99_999
    def convert(self, number: int) -> str:
        if number > 99_999: #1.33+e5
            num = str(number)
            resault = num[0] + "." + num[1] + num[2] + "+e"
            count = 0
            for _ in num:
                count += 1
            resault += str(count-3)
            
            return resault
            
        else:
            return str(number)
            
    #функция клика
    def click(self):
        self.cash += self.click_cash[0]
        self.counter_click += 1
        self.count_click_persecond += 1
        self.ui.cash_label.setText(self.convert(self.cash) + '$')  
        
    #функция для добавления автокликов
    def cps_add(self):
        build_cps = [
            self.house.count * self.house.cps[0],
            self.hotel.count * self.hotel.cps[0],
            self.tavern.count * self.tavern.cps[0],
            self.restaurant.count * self.restaurant.cps[0],
            self.blacksmith.count * self.blacksmith.cps[0],
            self.tailor.count * self.tailor.cps[0],
            self.alchemy.count * self.alchemy.cps[0],
            self.market.count * self.market.cps[0],
            self.brothel.count * self.brothel.cps[0],
            self.arena.count * self.arena.cps[0],
            self.barracks.count * self.barracks.cps[0],
            self.colosseum.count * self.colosseum.cps[0],
            self.libraly.count * self.libraly.cps[0],
            self.church.count * self.church.cps[0],
            self.cathedral.count * self.cathedral.cps[0],
            self.castle.count * self.castle.cps[0]
        ]
        cps = sum(build_cps)
        self.cash += cps
        self.ui.cash_label.setText(self.convert(self.cash) + '$')
        self.ui.cps_label.setText(self.convert(cps + self.count_click_persecond) + '$ cps')
        self.count_click_persecond = 0

    #функция создания апгрейд виджета
    def add_upgrade(self,price: int,name: str, upgrade_stat: list, number: int):
        upgrade_widget = Upgrade(price, name, upgrade_stat, number)
        upgrade_widget.buy.connect(lambda: self.buy_upgrade(upgrade_widget))
        return upgrade_widget
       
    #функция покупки улучшения
    def buy_upgrade(self, btn):
        if self.cash >= btn.price:
            btn.upgrade_stat[0] += btn.number
            btn.deleteLater()

    #вывод стоимости здания с покупкой за раз
    def cost_buy(self):
        self.price = 0
       
        x = self.selected_building.count
        for _ in range(self.X_Buy):
            self.price += (self.selected_building.base_cost * ( 1.15 ** x)) // 1
            x += 1
        self.ui.price_label.setText(f"Price - " + self.convert(self.price // 1))
        
    #функция покупки здания
    def buy_build(self):
        if self.cash < self.price:
            return
            
        elif self.cash >= self.price:
            self.cash -= self.price
            self.selected_building.count += self.X_Buy
            self.info(self.selected_building)
        
    #функция вывода информации о здании
    def info(self,build):
        self.selected_building = build
        self.ui.image_build_label.setPixmap(QPixmap.fromImage(QImage(self.selected_building.image)))
        self.ui.count_have_label.setText(f"You have {self.selected_building.count} builds| +{self.selected_building.cps} cps")
        self.cost_buy()
        
    #функция повтора музыки
    def music(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("music/Murlock.mp3"))
        self.audioOutput.setVolume(50)
        self.player.play()
        
    #функция обработки нажати по радио кнопкам
    def click_radio(self,num):
        
        if num == 1:
            self.ui.X1_Radio.setProperty("check",1)
            self.ui.X1_Radio.style().unpolish(self.ui.X1_Radio);
            self.ui.X1_Radio.style().polish(self.ui.X1_Radio);
            self.ui.X1_Radio.update();
            self.X_Buy = 1
            self.cost_buy()
            
            
            self.ui.X10_Radio.setProperty("check",0)
            self.ui.X10_Radio.style().unpolish(self.ui.X10_Radio);
            self.ui.X10_Radio.style().polish(self.ui.X10_Radio);
            self.ui.X10_Radio.update();
            
            self.ui.X100_Radio.setProperty("check",0)
            self.ui.X100_Radio.style().unpolish(self.ui.X100_Radio);
            self.ui.X100_Radio.style().polish(self.ui.X100_Radio);
            self.ui.X100_Radio.update();
            
        if num == 2:
            self.ui.X1_Radio.setProperty("check",0)
            self.ui.X1_Radio.style().unpolish(self.ui.X1_Radio);
            self.ui.X1_Radio.style().polish(self.ui.X1_Radio);
            self.ui.X1_Radio.update();
            
            self.ui.X10_Radio.setProperty("check",1)
            self.ui.X10_Radio.style().unpolish(self.ui.X10_Radio);
            self.ui.X10_Radio.style().polish(self.ui.X10_Radio);
            self.ui.X10_Radio.update();
            self.X_Buy = 10
            self.cost_buy()
            
            self.ui.X100_Radio.setProperty("check",0)
            self.ui.X100_Radio.style().unpolish(self.ui.X100_Radio);
            self.ui.X100_Radio.style().polish(self.ui.X100_Radio);
            self.ui.X100_Radio.update();
            
        if num == 3:
            self.ui.X1_Radio.setProperty("check",0)
            self.ui.X1_Radio.style().unpolish(self.ui.X1_Radio);
            self.ui.X1_Radio.style().polish(self.ui.X1_Radio);
            self.ui.X1_Radio.update();
            
            self.ui.X10_Radio.setProperty("check",0)
            self.ui.X10_Radio.style().unpolish(self.ui.X10_Radio);
            self.ui.X10_Radio.style().polish(self.ui.X10_Radio);
            self.ui.X10_Radio.update();
            
            self.ui.X100_Radio.setProperty("check",1)
            self.ui.X100_Radio.style().unpolish(self.ui.X100_Radio);
            self.ui.X100_Radio.style().polish(self.ui.X100_Radio);
            self.ui.X100_Radio.update();
            self.X_Buy = 100
            self.cost_buy()
            

#точка входа в программу
if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    window = apps()
    window.show()
    
    sys.exit(app.exec())
    