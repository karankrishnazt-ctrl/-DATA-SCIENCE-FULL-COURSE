import turtle
import time
import random

# ── Window setup ──────────────────────────────────────────────
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off automatic animation

# ── Snake head ────────────────────────────────────────────────
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ── Food ──────────────────────────────────────────────────────
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(
    random.randint(-14, 14) * 20,
    random.randint(-14, 14) * 20
)

# ── Score display ─────────────────────────────────────────────
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Courier", 16, "bold"))

# ── Game state ────────────────────────────────────────────────
segments = []
score = 0
high_score = 0

# ── Direction controls ────────────────────────────────────────
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

wn.listen()
wn.onkeypress(go_up,    "Up")
wn.onkeypress(go_down,  "Down")
wn.onkeypress(go_left,  "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up,    "w")
wn.onkeypress(go_down,  "s")
wn.onkeypress(go_left,  "a")
wn.onkeypress(go_right, "d")

# ── Move function ─────────────────────────────────────────────
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# ── Reset after collision ─────────────────────────────────────
def reset_game():
    global score
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segments:
        seg.goto(1000, 1000)   # hide off-screen
    segments.clear()
    score = 0

# ── Main game loop ────────────────────────────────────────────
while True:
    wn.update()

    # Wall collision
    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):
        reset_game()

    # Food collision
    if head.distance(food) < 15:
        # Move food to new random position
        food.goto(
            random.randint(-14, 14) * 20,
            random.randint(-14, 14) * 20
        )
        # Add a new body segment
        seg = turtle.Turtle()
        seg.speed(0)
        seg.shape("square")
        seg.color("green")
        seg.penup()
        segments.append(seg)

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Courier", 16, "bold"))

    # Move segments (tail follows head)
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(),
                         segments[i - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for seg in segments:
        if seg.distance(head) < 10:
            reset_game()

    time.sleep(0.1)   # ← lower = faster snake