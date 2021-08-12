from sense_hat import SenseHat


class Greeter:
    @staticmethod
    def greet_user():
        # sense_hat is LOCAL to this method
        sense_hat = SenseHat()
        sense_hat.show_message('Hello, world!',
                               scroll_speed=0.2,
                               text_colour=[128, 128, 0],
                               back_colour=[0, 0, 128])


if __name__ == '__main__':
    # Call the greet_user static method
    Greeter.greet_user()