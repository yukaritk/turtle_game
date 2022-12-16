import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_car:
        if car.distance(player) < 20 or (player.ycor() - 15 < car.ycor() < player.ycor() + 15 and
                                         car.distance(player) < 30):
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        player.restart()
        car_manager.speed_move()
        score.level_text()
        score.level_increase()

screen.exitonclick()
