import pickle

class MapStorage:
    def __init__(self, map_location):
        self._location = map_location

    def Read(self):
        readed_dict = {}
        try:
            with open(self._location, 'rb') as file:
                readed_dict = pickle.load(file)
        except FileNotFoundError:
            readed_dict = {}
        
        return readed_dict
    
    def Write(self, dict):
        with open(self._location, 'wb') as file:
            pickle.dump(dict, file)
            