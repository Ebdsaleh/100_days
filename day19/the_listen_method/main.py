# main.py
# Day 19 - The listen() method


from turtle import Turtle, Screen

t: Turtle = Turtle()


def move_forwards():
    t.forward(10)


def main():
    screen: Screen = Screen()
    screen.listen()  # tells the window to listen to events such as keystrokes.
    screen.onkey(key="space", fun=move_forwards)

    screen.exitonclick()


if __name__ == '__main__':
    main()
