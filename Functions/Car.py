
class Carro:
    def __init__(self, marca=str, color=str):
        self.marca = marca
        self.color = color

    def marca(self):
        return (self.marca)

    def color(self):
        return self.color()
