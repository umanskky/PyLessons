# ООП

class Critter(object):

    def __init__(self, name):
        print("Появился новый зверь")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critten\n"
        rep += "имя: " + self.name + "\n"
        return rep

    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")

crit1 = Critter("Бобик")
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()

print("Вывод объекта Crit1 на экран:")
print(crit1)
print("Непостредственный доступ к атрибуту crit1.name:")
print(crit1.name)




