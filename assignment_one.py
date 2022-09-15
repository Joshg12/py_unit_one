# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import turtle


def drawoctagon():
    for x in range(8):
        turtle.forward(100)
        turtle.left(45)


for x in range(1):
    turtle.begin_fill()
    turtle.fillcolor('red')
    drawoctagon()
    turtle.left(20)
    turtle.end_fill()

for x in range(1):
    turtle.begin_fill()
    turtle.fillcolor('green')
    drawoctagon()
    turtle.left(20)
    turtle.end_fill()
for x in range(1):
    turtle.begin_fill()
    turtle.fillcolor('purple')
    drawoctagon()
    turtle.left(20)
    turtle.end_fill()
for x in range(1):
    turtle.begin_fill()
    turtle.fillcolor('black')
    drawoctagon()
    turtle.left(20)
    turtle.end_fill()

turtle.exitonclick()
# remember to use comments!
