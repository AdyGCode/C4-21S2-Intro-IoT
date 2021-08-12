class Measurement:
    def __init__(self, temperature, location=None):
        self.temperature = temperature
        self.location = location

    def clear(self):
        self.temperature = 0.0
        self.location = None

    def __str__(self):
        return f'{self.temperature} @{self.location}'


if __name__ == '__main__':
    measurement = Measurement(19.6, 'Sydney')
    print(measurement)
