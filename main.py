from turtle import  Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_over = True
while game_is_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #delecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detech collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        game_is_over = False
        scoreboard.game_over()

    #delect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_over = False
            scoreboard.game_over()

    #if head collides with any segment in tail



screen.exitonclick()
