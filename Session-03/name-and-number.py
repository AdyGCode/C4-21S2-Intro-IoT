
if __name__ == '__main__':
    the_name = input("Enter your name: ")
    the_num = int(input("What is your favourite number? "))
    print(f"Hello there, {the_name}.")
    print(f"Your favourite number is {the_num}")
    print(f"Type is: {type(the_num)}")
    for count in range(1, the_num+1, 3):
        print(count)
    del(count)

