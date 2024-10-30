#Импортирование модуля turtle 
import turtle


#Модуль музыки
import winsound


#Cоздание поля
sc=turtle.Screen()
sc.title("PONG")
sc.bgcolor("black")
sc.setup(width=800,height=600)


#Верхняя полоса
up_line=turtle.Turtle()
up_line.speed(0)
up_line.shape("square")
up_line.color("white")
up_line.shapesize(stretch_wid=1,stretch_len=40)
up_line.penup()
up_line.goto(0,299)


#Нижняя полоса
down_line=turtle.Turtle()
down_line.speed(0)
down_line.shape("square")
down_line.color("white")
down_line.shapesize(stretch_wid=1,stretch_len=40)
down_line.penup()
down_line.goto(0,-293)


#Центральная линия
mid_line=turtle.Turtle()
mid_line.goto(0,290)
mid_line.right(90)
mid_line.color("white")
for i in range(30):   
    mid_line.forward(10)
    mid_line.penup()
    mid_line.forward(10)
    mid_line.pendown()


#Левая ракетка
left_pad=turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=7,stretch_len=1)
left_pad.penup()
left_pad.goto(-350,0)


#Правая ракетка
right_pad=turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=7,stretch_len=1)
right_pad.penup()
right_pad.goto(350,0)


#Мяч
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=12
ball.dy=-12


#Внутренний счет
left_player=0
right_player=0
winner=None

#Функция конца игры
def game_over():
  ball.hideturtle()
  ball.dx=0
  ball.dy=0
  game_over_display=turtle.Turtle() 
  game_over_display.color("white")
  game_over_display.penup()
  game_over_display.hideturtle()
  game_over_display.goto(0,0)
  while True:
   game_over_display.write("Game Over! {} wins!".format(winner),align="center",font=("Arial", 36, "normal"))
  

#Табло
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player 1: 0         Player 2: 0",align="center",font=("Arial", 24, "normal"))


#Движение ракеток
def paddleaup():
 y=left_pad.ycor()
 y+=20
 left_pad.sety(y)

def paddleadown():
 y=left_pad.ycor()
 y-=20
 left_pad.sety(y)

def paddlebup():
 y=right_pad.ycor()
 y+=20
 right_pad.sety(y)

def paddlebdown():
 y=right_pad.ycor()
 y-=20
 right_pad.sety(y)


#Связь ракеток с кнопками
sc.listen()
sc.onkeypress(paddleaup,"w")
sc.onkeypress(paddleadown,"s")
sc.onkeypress(paddlebup,"Up")
sc.onkeypress(paddlebdown,"Down")



#Физика игры
while True:
     sc.update()
      
    #Движение мяча
     ball.setx(ball.xcor()+ball.dx)
     ball.sety(ball.ycor()+ball.dy)

    #Удар об грани поля

    #Верх и них
     if ball.ycor()>280:
      winsound.Beep(440,40)
      ball.sety(280)
      ball.dy*=-1
      
     elif ball.ycor()<-270:
      winsound.Beep(440,40)
      ball.sety(-270)
      ball.dy*=-1
      
       
    #Стороны  
     elif ball.xcor()>350:
      winsound.Beep(640,200)
      left_player+=1
      pen.clear()
      pen.write("Player 1: {}         Player 2: {}".format(left_player, right_player),align="center",font=("Ariel", 24, "normal"))
      ball.goto(0,0)
      ball.dx*=-1

     elif ball.xcor()<-350:
        winsound.Beep(640,200)
        right_player+=1
        pen.clear()
        pen.write("Player 1: {}         Player 2: {}".format(left_player, right_player),align="center",font=("Ariel", 24, "normal"))
        ball.goto(0,0)
        ball.dx*=-1

    #Удар мяча и ракетки
     if ball.xcor()<-340 and ball.ycor() <left_pad.ycor()+70 and ball.ycor()>left_pad.ycor()-70:
        winsound.Beep(410,40)
        ball.dx*=-1 
      
     elif ball.xcor()>340 and ball.ycor()<right_pad.ycor()+70 and ball.ycor()>right_pad.ycor()-70:
        winsound.Beep(410,40)
        ball.dx*=-1
      
    #Проверка на конец игры
     if left_player==3:
      winner="Player 1"
      game_over()
     elif right_player==3:
      winner="Player 2"
      game_over()