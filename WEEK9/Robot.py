class Robot:
    # Class attribute
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __str__(self):
        return f"Robot is called {self.name}, age={self.age}, energy={self.energy}"

if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(robot)  # Calls __str__ method