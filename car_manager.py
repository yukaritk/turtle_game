import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_car.append(new_car)

    def move_cars(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def speed_move(self):
        self.car_speed += MOVE_INCREMENT
