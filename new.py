import turtle as t
playerAscore=0
playerBscore=0

window=t.Screen()
window.title("pong game made by @aditya136")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("red")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("red")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#creting pen for scorecard update

pen=t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=("Arial",24,"normal"))



#moving the leftpaddle

def leftpaddleup():
  y=leftpaddle.ycor()
  y=y-90
  leftpaddle.sety(y)


def leftpaddledown():
  y=leftpaddle.ycor()
  y=y-90
  leftpaddle.sety(y)

  #moving the right paddle
  
def rightpaddleup():
  y=rightpaddle.ycor()
  y=y+90
  rightpaddle.sety(y)


def rightpaddledown():
  y=rightpaddle.ycor()
  y=y-90
  rightpaddle.sety(y)

  #assign keys to play

  window.listen()
  window.onkeypress(leftpaddleup,"w")
  window.onkeypress(leftpaddledown,"s")
  window.onkeypress(rightpaddleup,"Up")
  window.onekeypress(rightpaddledown,"down")

while True:
  window.update()

   #moving the ball
  ball.setx(ball.xcor()+ballxdirection)
  ball.setx(ball.ycor()+ballydirection)

   #settingup border
  if ball.ycor()>290:
      ball.sety(290)
      ballydirection=ballydirection*-1
  if ball.ycor()>-290:
      ball.sety(-290)
      ballydirection=ballydirection*-1

  if (ball.xcor())<-390:
        ball .goto(0,0)
        ballxdirection=ballxdirection*-1
        playerBscore+1
        pen.clear()
        pen.write("player A:{}    player B:{}".format(playerAscore,playerBscore),align="canter",font=("Arial",24,"normal"))



   