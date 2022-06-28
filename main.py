# Pong game object-oriented

# libraries
import turtle
import time


# functions
def create_turtle_object(t_turtle: turtle.Turtle(), t_speed, t_shape, t_color, t_stretch_wid, t_stretch_len, t_x,
                         t_y):
    """settings for turtle"""
    t_turtle.speed(t_speed)
    t_turtle.shape(t_shape)
    t_turtle.color(t_color)
    t_turtle.shapesize(stretch_wid=t_stretch_wid, stretch_len=t_stretch_len)
    t_turtle.penup()
    t_turtle.goto(t_x, t_y)


def refresh_headline(t_turtle: turtle.Turtle(), t_message):
    t_turtle.clear()
    t_turtle.write(t_message, align="center", font=("Courier", 12, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()  # get current y coordinate
    y += 20  # increase y coordinate
    paddle_a.sety(y)  # refresh y coordinate


def paddle_a_down():
    y = paddle_a.ycor()  # get current y coordinate
    y -= 20  # increase y coordinate
    paddle_a.sety(y)  # refresh y coordinate


def paddle_b_up():
    y = paddle_b.ycor()  # get current y coordinate
    y += 20  # increase y coordinate
    paddle_b.sety(y)  # refresh y coordinate


def paddle_b_down():
    y = paddle_b.ycor()  # get current y coordinate
    y -= 20  # increase y coordinate
    paddle_b.sety(y)  # refresh y coordinate


def start_sequence():
    refresh_headline(headline, "Welcome to the first pong world champion ship! \n"
                               "Get ready as it will start in just a few seconds!")
    time.sleep(5)
    window.update()

    for t in range(5, 0, -1):
        refresh_headline(headline, str(t))
        time.sleep(1)

    refresh_headline(headline, "Player A: {} points and Player B: {} points".format(score_a, score_b))


def won_point(t_turtle: turtle.Turtle(), t_score):
    pass


def stop_game():
    pass


def continue_game():
    pass


def check_y_border():
    if ball.ycor() > (window.window_height() / 2 - 10):  # ball itself has height of 20 -> divide height
        ball.sety((window.window_height() / 2 - 10))  # reset position at border
        ball.dy *= -1  # reverse sign of speed

    if ball.ycor() < -(window.window_height() / 2 - 10):
        ball.sety(-(window.window_height() / 2 - 10))
        ball.dy *= -1


def check_x_border():
    global score_a, score_b
    if ball.xcor() > (window.window_width() / 2 - 10):
        ball.goto(0, 0)
        # ball.dx *= -1
        score_a += 1
        refresh_headline(headline, "Player A received a point! His score is {}!".format(score_a))
        time.sleep(2)
        for t in range(3, 0, -1):
            refresh_headline(headline, str(t))
            time.sleep(1)
        refresh_headline(headline, "Player A: {} points and Player B: {} points".format(score_a, score_b))

    if ball.xcor() < -(window.window_width() / 2 - 10):
        ball.goto(0, 0)
        # ball.dx *= -1
        score_b += 1
        refresh_headline(headline, "Player B received a point! His score is {}!".format(score_b))
        time.sleep(2)
        for t in range(3, 0, -1):
            refresh_headline(headline, str(t))
            time.sleep(1)
        refresh_headline(headline, "Player A: {} points and Player B: {} points".format(score_a, score_b))


def check_collision():
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


# variables

score_a = 0
score_b = 0

# window

window = turtle.Screen()  # create window
window.title("Pong by Alex")  # title
window.bgcolor("black")  # color of background
window.setup(width=800, height=600)  # size of window -> top y cor =  300 & bottom y cor = - 300
window.tracer(0)  # stop window from updating -> speed up game

# turtle objects

paddle_a = turtle.Turtle()  # player A
create_turtle_object(paddle_a, 0, "square", "white", 5, 1, -350, 0)

paddle_b = turtle.Turtle()  # player B
create_turtle_object(paddle_b, 0, "square", "white", 5, 1, 350, 0)

ball = turtle.Turtle()  # ball
create_turtle_object(ball, 0, "square", "white", 1, 1, 0, 0)
ball.dx = 2
ball.dy = 2

headline = turtle.Turtle()
create_turtle_object(headline, 0, None, "white", 1, 1, 0, 250)
headline.hideturtle()  # headline of game
refresh_headline(headline, "Player A: {} points and Player B: {} points".format(score_a, score_b))

# keyboard binding
window.listen()  # listen for keyboard input
window.onkeypress(paddle_a_up, "w")  # when 'w' is pressed, call function paddle_a_up
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# main
def main():
    global score_a
    global score_b

    # start game
    start_sequence()

    start_time = 0.005

    while True:
        # constantly update screen

        window.update()

        # move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        time.sleep(start_time)

        # border checking
        check_y_border()

        check_x_border()

        # collisions of paddles and ball
        check_collision()


if __name__ == "__main__":
    main()
