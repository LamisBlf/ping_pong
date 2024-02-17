import turtle

window = turtle.Screen()
window.title("Ping Pong game")
window.setup(width=800 ,height=600)
window.tracer(0)
window.bgcolor(.1,.1,.1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.goto(x=0,y=0)
ball.penup()
ball_dx, ball_dy = 1,1
ball_speed = 1.5

right_line = turtle.Turtle()
right_line.shape("square")
right_line.speed(0)
right_line.color("blue")
right_line.shapesize(stretch_len=0.25,stretch_wid=30)
right_line.penup()
right_line.goto(x=390,y=0)

left_line = turtle.Turtle()
left_line.shape("square")
left_line.speed(0)
left_line.color("red")
left_line.shapesize(stretch_len=0.25,stretch_wid=30)
left_line.penup()
left_line.goto(x=-398,y=-0)

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.shapesize(stretch_len=1,stretch_wid=5)
player1.penup()
player1.goto(x=350,y=0)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_len=1,stretch_wid=5)
player2.penup()
player2.goto(x=-358,y=0)

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0,y=260)
score.write("Player_2 : 0 _ Player_1 : 0",align="center", font=("courier",14,"normal"))
score.hideturtle()
p1_score , p2_score = 0,0
players_speed= 20

def p1_move_up():
    player1.sety(player1.ycor()+ players_speed)

def p1_move_down():
    player1.sety(player1.ycor()- players_speed)

def p2_move_up():
    player2.sety(player2.ycor()+ players_speed)

def p2_move_down():
    player2.sety(player2.ycor()- players_speed)

window.listen()
window.onkeypress(p1_move_up,"Up")
window.onkeypress(p1_move_down,"Down")
window.onkeypress(p2_move_up,"a")
window.onkeypress(p2_move_down,"q")

while True:
    window.update()

    ball.setx(ball.xcor()+(ball_dx * ball_speed))
    ball.sety(ball.ycor()+(ball_dy * ball_speed))
    if (ball.ycor() > 290):
        ball.sety(290)
        ball_dy *= -1

    if (ball.ycor() < -290):
        ball.sety(-290)
        ball_dy *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor()>(player2.ycor()-60) and ball.ycor()<(player2.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor()>(player1.ycor()-60) and ball.ycor()<(player1.ycor()+60):
        ball.setx(340)
        ball_dx *= -1

    if(ball.xcor() > 390):
        ball.goto(0,0)
        ball_dx *= -1
        score.clear()
        p1_score +=1
        score.write(f"Player_2 : {p1_score} _ Player_1 : {p2_score}",align="center", font=("courier",14,"normal"))

    if(ball.xcor() < -390):
        ball.goto(0,0)
        ball_dx *= -1
        score.clear()
        p2_score +=1
        score.write(f"Player_2 : {p1_score} _ Player_1 : {p2_score}",align="center", font=("courier",14,"normal"))

    if (p1_score == 3):
        window.clear()
        score.clear()
        score.goto(0,0)
        score.write("Player_2 Win",align="center" , font=("courier", 50, "normal" ))
        score.speed(1)
        score.color("red")

    if (p2_score == 3):
       window.clear()
       score.clear()
       score.goto(0,0)
       score.write("Player_1 Win",align="center" , font=("courier", 50, "normal" ))
       score.speed(1)
       score.color("blue")