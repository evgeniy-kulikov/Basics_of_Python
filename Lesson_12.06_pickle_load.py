import pickle

# открываем файл
with open('person.dat', 'rb') as dic_person:
    # сразу читаем объект из файла с помощью pickle
    person = pickle.load(dic_person)
print(person)
