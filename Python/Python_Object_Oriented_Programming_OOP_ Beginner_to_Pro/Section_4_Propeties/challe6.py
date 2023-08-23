from enum import Enum

class Models(Enum):
    LITE = "Lite"
    PRO = "Pro"
    MAX = "Max"

class Tablet:
    _base_storage_capacity = {
        "Lite":[32,1],
        "Pro":[64,2],
        "Max":[128,4]
    }
    MAXSTORAGE = 1024
    def __init__(self, model = Models.LITE.value, base_storage = 32, added_storage = 0, memory=0) -> None:
        self._model = model
        self._base_storage = self._base_storage_capacity[self._model][0]
        self._memory = self._base_storage_capacity[self._model][1]
        self._added_storage = added_storage

    def added_storage(self, plus_storage):
        if (self._base_storage + self._added_storage) <= self.MAXSTORAGE:
            self._base_storage += plus_storage
        else:
            raise ValueError(f"Total storage can not be bigger that {self.MAXSTORAGE}")

    def storage(self, new_storage):
        if (new_storage + self._base_storage) <= self.MAXSTORAGE:
            self._added_storage = new_storage - self._base_storage
        else:
            raise ValueError(f"Total storage can not be bigger that {self.MAXSTORAGE}")
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, new_model):
        valid_models = [x.value for x in Models]
        if new_model in valid_models:
             self._model = new_model
             self._base_storage = self._base_storage_capacity[self._model][0]
             self._memory = self._base_storage_capacity[self._model][1]
        else:
            raise TypeError(f"{new_model} Not valid model")

    def __repr__(self) -> str:
        return f"Tablet(model = {self._model}, base_storage = {self._base_storage}, added_storage = {self._added_storage}, memory = {self._memory})"
    
    storage = property(fset=storage)

new_tablet = Tablet()
print(new_tablet.added_storage(32))
print(new_tablet)
new_tablet.storage = 500
print(new_tablet)
new_tablet.model = "Max"
print(new_tablet)

        
        