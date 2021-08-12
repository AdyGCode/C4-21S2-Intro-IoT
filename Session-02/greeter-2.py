from sense_hat import SenseHat


class Greeter:
    def __init__(self):
        self.sense_hat = SenseHat()

    def greet_user(self):
        self.sense_hat.show_message('Hello, world!',
                                    scroll_speed=0.2,
                                    text_colour=[128, 128, 0],
                                    back_colour=[0, 0, 128])


if __name__ == '__main__':
    # Instantiate a Greeter object
    greeter = Greeter()
    # Call the instance method {greet_user}
    greeter.greet_user()
