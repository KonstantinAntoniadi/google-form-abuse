import pickle
from settings import MAP_PATH
from data import count

def write():
    with open(MAP_PATH, 'wb') as file:
        pickle.dump(count, file)

def read():
    try:
        with open(MAP_PATH, 'rb') as file:
            count = pickle.load(file)
    except FileNotFoundError:
        count = {}
    
    for key, value in count.items():
        print(f'{key}: {value}')

# write()
read()