# Lesson_12
# Модуль json в Python. Пример на задаче
#
import json

favourite_tracks = [{'name': 'Московская осень', 'artist': 'Александр Иванов'},
                    {'name': 'Yellow Submarine', 'artist': 'Beatles'},
                    {'name': 'Lady Day', 'artist': 'Frank Sinatra'}]

with open('my_tracks.json', 'w', encoding='utf-8') as my_favour:
    json.dump(favourite_tracks, my_favour)

print('Выполнено')
