from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = self.get_score()
        self.goto(0, 270)
        self.write(f"Score : {self.score}  High score : {self.high_score}", align=ALIGNMENT, font=("Ariel", 18, "normal"))

    def change_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}  High score : {self.high_score}", align=ALIGNMENT, font=("Ariel", 18, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(f"Score : {self.score}  High score : {self.high_score}", align=ALIGNMENT, font=("Ariel", 18, "normal"))

    def get_score(self):
        with open("highest_score.txt", "r") as file:
            return int(file.read())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=("Ariel", 18, "normal"))
