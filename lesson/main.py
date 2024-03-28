class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} - лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} - сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} - наносит удар")
        self.endurance -= 1

    def walk(self):
        print(f"{self.name} - гуляет")

    def info(self):
        print(f"Имя - {self.name}\n"
              f"Сила - {self.power}\n"
              f"Выносливость - {self.endurance}\n"
              f"Цвет волос  - {self.hair_color}\n")
