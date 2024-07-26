import turtle
import random
import time

# Game settings
delay = 0.05
score = 0
highestScore = 0
bodies = []

# Getting a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("#2c3e50")  # Dark blue color
s.setup(width=600, height=600)

# Creating a snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#3498db")  # Blue color
head.fillcolor("#2980b9")  # Darker blue color
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#f39c12")  # Orange color
food.penup()
food.goto(0, 200)
food.st()

# Scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.color("#ecf0f1")  # White color
sb.penup()
sb.ht()
sb.goto(0, 260)
sb.write("Score : 0 | Highest Score : 0", align="center", font=("Courier", 18, "normal"))

# Congratulations message
congrats = turtle.Turtle()
congrats.color("#27ae60")  # Green color
congrats.penup()
congrats.hideturtle()

# Game over message
game_over = turtle.Turtle()
game_over.color("red")
game_over.penup()
game_over.hideturtle()

# Movement functions
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event Handling - key mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(s.bye, "Escape")  # Exit game with Escape key

# Main loop
while True:
    s.update()  # This is to update the screen

    # Check collision with border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        # Move the food to a new random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("#c0392b")  # Red color
        body.fillcolor("#e74c3c")  # Darker red color
        bodies.append(body)  # Append the body of the snake

        # Increase the score
        score += 10

        # Increase speed
        delay -= 0.001

    # Move the snake bodies
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide bodies
            for b in bodies:
                b.ht()
            bodies.clear()

            # Display game over message
            game_over.goto(0, 0)
            game_over.write("Game Over!", align="center", font=("Courier", 24, "bold"))
            game_over.goto(0, -30)
            game_over.write("Your Score: {}".format(score), align="center", font=("Courier", 18, "normal"))

            # Update the highest score
            if score > highestScore:
                highestScore = score
                congrats.clear()
                congrats.goto(0, -50)
                congrats.write("Congratulations! New Highest Score!", align="center", font=("Courier", 20, "bold"))

            time.sleep(2)
            game_over.clear()
            congrats.clear()

            score = 0
            delay = 0.05

            # Update scoreboard
            sb.clear()
            sb.write("Score : {} | Highest Score : {}".format(score, highestScore), align="center", font=("Courier", 18, "normal"))

    time.sleep(delay)

# This is needed to keep the window open
s.mainloop()
