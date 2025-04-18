from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Open the file
        with open("high_scores.txt", "r") as data:
            self.high_score= int(data.read())
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 18, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="center", font=("Arial", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()