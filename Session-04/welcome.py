class Welcome:
    def __init__(self, name=None):  # Constructor (optional)
        self.name = "World"  # This is my default
        if name is not None:
            self.name = name  # self.name is an instance variable

    def greeting(self, time_of_day):
        print(f"Good {time_of_day}, {self.name}, welcome to Python!")


if __name__ == "__main__":
    my_greeter = Welcome("Angela")  # Create an instance of Welcome
    my_greeter.greeting("morning")

    another_greeter = Welcome()
    another_greeter.greeting("afternoon")
