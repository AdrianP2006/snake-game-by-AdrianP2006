import turtle
import time
from food import *
from snake import *

win = turtle.Screen()
win.title("Snake game")
width = 500
height = 500
win.setup(width=width, height=height)
win.bgcolor("green")

snake = Snake(0, 0)
win.listen()
win.onkey(snake.keyUp, "Up")
win.onkey(snake.KeyDown, "Down")
win.onkey(snake.KeyLeft, "Left")
win.onkey(snake.KeyRight, "Right")

win.onkey(snake.keyUp, "w")
win.onkey(snake.KeyDown, "s")
win.onkey(snake.KeyLeft, "a")
win.onkey(snake.KeyRight, "d")

food = Food()


while True:
    win.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

    if snake.CheckSelfCollision() or snake.checkWallsCollision(width,height):
        food.refresh()
        snake.refresh()

win.mainloop()