class Accumulator:
    def __init__(self, initial_value):
        self.initial_value = initial_value
        self.sum = initial_value

    def getSum(self):
        while True:
            number = (yield)
            self.sum = self.sum + number
            print self.sum
