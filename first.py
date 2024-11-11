# ООП
""""
# ИНКАПСУЛЯЦИЯ
class Cat():

    def __init__(self, breed, color, age):
        self._breed = breed
        self._color = color
        self._age   = age

    @property
    def breed(self):
        return self._breed
    
    @property
    def color(self):
        return self._color

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age > self._age:
            self._age = new_age
        return self._age

    def meow(self):
        print("Мяу!")

    def purr(self):
        print("Мрррр")

#Создаем новый класс --- НАСЛЕДОВАНИЕ

class HomeCat(Cat):
    
    def __init__(self, breed, color, age, owner, name):
        super().__init__(breed, color, age)
        self._owner = owner
        self._name = name

    @property
    def owner(self):
        return self._owner
    
    @property
    def name(self):
        return self._name

    def getTreat(self):
        print("мяу-мяу")

my_cat = HomeCat("Сиамская", "Белая", 3, "Иван", "Роза")

print(my_cat.owner)
print(my_cat.breed)
print(my_cat.color)
my_cat.getTreat()
my_cat.purr()

cat1 = Cat("Абиссинская", "Рыжая", 4)

cat1.meow()
print(cat1.color)
print(cat1.breed)
cat1.age = 12
print(cat1.age)


# --- ПОЛИФОРМИЗМ
class Cat:
    
    def sleep(self):
        print('Свернулся в клубок и сладко спит.')

class Parrot:
    
    def sleep(self):
        print('Сел на жёрдочку и уснул.')

def homeSleep(animal):
    animal.sleep()

cat = Cat()
parrot = Parrot()
homeSleep(cat) # Свернулся в клубок и сладко спит.
homeSleep(parrot) # Сел на жёрдочку и уснул.

"""
# --- АБСТРАКЦИЯ
class Predator:
    
    def hunt(self):
        print('Охотится...')

class Cat(Predator):
    
    def __init__(self, name, color):
        super().__init__()
        self._name = name
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

cat = Cat('Даниэла', 'Чёрный')
cat.hunt() # Охотится…

