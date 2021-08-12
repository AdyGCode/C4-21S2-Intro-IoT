# ---------------------------------------------------------------------
# Filename:     xxx
# Location:     xxx
# Project:      xxx
# Author:       Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:      2021-07-29
# Description:
#       A simple program to display a "hello world" message.
#
# ---------------------------------------------------------------------

class Greeter:
    """
    Greeter Class that provides methods to say hello.
    """
    @staticmethod
    def greet_user():
        """
        Displays a greeting to the user

        :return: None
        """
        print("Hello, World!")

if __name__ == "__main__":
    # Single line comment
    # Call the greet user static method
    Greeter.greet_user()

