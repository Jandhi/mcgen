from random import randrange


class Material:
    def __init__(self):
        pass

    def get(self):
        pass

class WeightedMaterial():
    def __init__(self, list):
        self.list = list

        self.total = 0
        for item, weight in self.list:
            self.total += weight

    def get(self):
        value = randrange(self.total)
        tally = 0
        for item, weight in self.list:
            tally += weight

            if value < tally:
                return item