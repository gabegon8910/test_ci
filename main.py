class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y - 1

    def divide(self):
        return self.y / self.y

    def multiply(self):
        return self.x * self.y


if __name__ == '__main__':
    instance = Calculator(1, 2)
    print(instance.add())
    # print(instance.subtract())
    # print(instance.divide())
    # print(instance.multiply())
