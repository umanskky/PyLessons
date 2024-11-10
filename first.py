import pickle, shelve

"""
print("Консервация списков")

variety = ["огурцы", "помидоры", "капуста"]
shape   = ["целые", "кубиком", "соломкой"]
brand   = ["Главпродукт", "Чумак", "Бондюэль"]

f = open("pickles.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)

f.close()


print("Расконсервация списков")

f = open("pickles.dat", "rb")

variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)

f.close()

"""

print("Помещение списков на полку")

s = shelve.open("picles2.dat")

s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"]   = ["целые", "кубиком", "соломкой"]
s["brand"]   = ["Главпродукт", "Чумак", "Бондюэль"]

s.sync()

print("Извлечение списков из файла полки:")

print("торговые  марки - ", s["brand"])
print("формы - ", s["shape"])
print("виды овощей - ", s["variety"])

s.close()

