import random

class dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Собачка вчиться командам')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('Собачка захотiла спати')
        self.gladness += 3

    def to_chill(self):
        print('Собачка захотiла погратись мячиком')
        self.gladness += 5
        self.progress -= 0.15

    def is_alive(self):
        if self.progress < -0.5:
            print('Собачку відрахували з секції про вчення команд')
            self.alive = False
        elif self.gladness <= 0:
            print('Собачка вирішила вивчити команди самостійно')
            self.alive = False
        elif self.progress > 5:
            print('Собачка перевтомилась')
            self.alive = False

    def end_of_day(self):
        print(f'Щастя = {self.gladness}')
        print(f'Прогрес = {round(self.progress, 2)}')

    def live(self, day):
        day = 'Day' + str(day) + ' of ' + self.name + ' life '
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

backs = dog(name='Baks')

for day in range(365):
    if backs.alive == False:
        break
    backs.live(day)