#Doraemon using Turtle
import turtle
wn=turtle.Screen()
wn.bgcolor("black")



t=turtle.Turtle()
t.color('white')
t.width(2)
t.speed(10)
t.hideturtle()
#draw outer circle face
t.up()
t.goto(65,0)
t.down()
t.fd(15)

t.setheading(40)
t.begin_fill()
t.fillcolor('blue')
t.circle(148,280)
t.end_fill()

#to remove blue color by white
t.goto(67,0)
t.setheading(0)
t.color('black')
t.lt(40)
t.down()
t.begin_fill()
t.fillcolor('white')

#t.circle(130,280)
t.circle(100,140)
t.setheading(180)
#t.color('white')
t.fd(55)
t.lt(40)
t.rt(31)
t.circle(100,132)
t.end_fill()
#t.hideturtle()
#t.begin_fill()
#t.fillcolor('white')
#t.color('black')




#mouth
t.up()
t.setposition(-90,90)
t.setheading(0)
t.rt(70)
t.down()
#t.begin_fill()
#t.fillcolor('white')
t.color('black')
t.circle(80,140)
#t.end_fill()
t.up()
t.home()
t.lt(90)

#t.fd(60)
t.setposition(-15,40)#fixed position at centre of mouth
t.down()
t.fd(90)#to draw connection line of nose and mouth

#to draw the nose with red and white color
t.setheading(0)
t.begin_fill()
t.fillcolor('red')
t.circle(15)
t.end_fill()

#to draw the dotted nose
t.up()
t.setheading(90)
t.fd(23)
t.begin_fill()
t.fillcolor('white')
#t.width(0)
t.circle(2)
t.end_fill()

#to draw the eyes
t.color('black')#change eye color
t.setheading(90)
t.fd(6)
t.setheading(0)
t.fd(15)
t.down()
t.begin_fill()
t.fillcolor('white')
t.circle(20)

#second eye
t.setheading(180)
t.up()
t.fd(30)

t.setheading(0)

t.down()
t.circle(20)
t.end_fill()

#change color from white to black
t.color('black')

#eyes inside eye(4)
t.up()
t.setheading(0)
t.lt(60)
t.fd(20)
t.down()
t.begin_fill()
t.fillcolor('black')
t.circle(4)
t.end_fill()

#another 2 radius eye
t.up()
t.setheading(0)
t.lt(60)
t.fd(0.5)
t.down()
t.begin_fill()
t.fillcolor('white')
t.circle(2)
t.end_fill()

t.up()
t.setheading(0)
t.fd(15)
t.down()
t.begin_fill()
t.fillcolor('black')
t.circle(4)
t.end_fill()
t.fd(0.5)
t.begin_fill()
t.fillcolor('white')
t.circle(2)
t.end_fill()


#move to home for neck
t.up()
t.home()
t.down()
#fill red color in neck
t.begin_fill()
t.fillcolor('red')
t.setheading(180)
t.fd(110)
t.setheading(0)
t.fd(188)
t.rt(90)
t.fd(15)
t.rt(90)
t.fd(188)
t.rt(90)
t.fd(15)
t.end_fill()
t.rt(90)



#draw moustache
#1down left below and up right moustache
t.color('black')
t.up()
t.goto(-145,55)
t.setheading(0)
t.lt(20)
t.down()
t.fd(100)
t.up()
#for hiding
t.fd(80)
t.down()
t.fd(95)

#2down left middle and up middle moustache
t.color('black')
t.up()
t.goto(-150,100)
#t.lt(20)
#t.setheading(0)
t.rt(20)
t.down()
t.fd(100)
t.up()
#for hiding
t.fd(80)
t.down()
t.fd(95)

#3down left below and up right moustache
t.color('black')
t.up()
t.goto(-145,140)
t.setheading(0)
t.rt(17)
t.down()
t.fd(95)
t.up()
#for hiding
t.fd(80)
t.down()
t.fd(100)



#left hand
t.width(2)
t.up()
t.home()
t.setheading(180)
t.fd(110)
t.lt(90)
t.fd(15)
t.rt(60)

t.down()
t.color('white')
t.fd(8)
t.circle(40,145)

#left leg
t.up()
t.goto(-100,-60)
t.rt(45)
t.down()
#t.circle(-300,5)
 #draw half 70unit leg
t.setheading(270)
t.fd(60)

#draw red lollypop
t.setheading(180)
t.fd(15)
t.rt(90)
t.begin_fill()
t.fillcolor('red')
t.circle(10)
t.end_fill()
t.setheading(0)
t.fd(15)
t.setheading(270)
t.fd(80)

#left foot
t.setheading(180)
t.begin_fill()
t.fillcolor('white')
t.fd(18)
t.circle(25,210)
t.rt(15)
t.circle(100,5)
t.fd(80)
t.circle(9,180)

t.rt(150)
t.fd(20)
t.bk(20)
t.setheading(180)
t.fd(80)
t.end_fill()



#rightfoot(i am repeating the same above 4 to 5 lines.
t.bk(80)
t.rt(140)
t.fd(12)
t.rt(40)

#t.circle(200,10)
t.begin_fill()
t.fillcolor('white')
t.fd(30)
t.lt(7)
t.fd(48)
t.circle(-24,210)

t.lt(13)
t.fd(84)
t.end_fill()
#to draw right side stomaach margin

t.width(0)
t.bk(93)
t.rt(167)
t.circle(24,180)
t.end_fill()
t.width(2)
t.rt(100)
t.fd(148)

#right hand from my side

t.bk(15)
t.setheading(40)
t.fd(60)
t.setheading(0)
t.begin_fill()
t.fillcolor('white')
t.circle(18)
t.end_fill()
t.circle(18,260)
t.setheading(180)
t.fd(20)







#to paint middle part(excluding leg and face) using blue color
t.width(2)
t.up()
t.home()
t.setheading(180)
t.fd(110)
t.lt(90)
t.fd(15)
t.rt(60)

t.down()

t.fd(8)
t.begin_fill()#filling color in stomach
t.fillcolor('blue')
t.circle(40,145)

#left leg
t.up()
t.goto(-100,-60)
t.rt(45)
t.down()
#t.circle(-300,5)
#draw half 70unit leg
t.setheading(270)
t.fd(140)
t.setheading(0)
t.fd(80)
t.lt(40)
t.fd(12)
t.rt(40)

#t.circle(200,10)
t.fd(30)
t.lt(7)
t.fd(39)


t.width(2)
t.lt(76)
t.fd(148)

t.bk(15)
t.setheading(40)
t.fd(60)
t.setheading(180)
t.circle(-18,28)

t.setheading(180)
t.up()
t.fd(120)
#t.setheading(0)
t.lt(60)
t.circle(-10,122)

t.setheading(180)
t.fd(83)
t.end_fill()

t.begin_fill()
t.fillcolor('blue')
t.bk(83)
t.setheading(0)
#t.rt(120)
t.end_fill()

#hide some part
t.up()
t.width(2)
t.fd(104)
t.lt(90)
t.begin_fill()
t.fillcolor('blue')
t.fd(15)

t.down()
t.width(1)
t.setheading(28)

t.circle(148,4)
t.setheading(0)
t.fd(14.5)
t.setheading(260)
t.circle(18,80)
t.end_fill()



#make stomach circle and color it white

t.setheading(180)
t.up()
t.width(3)
t.fd(180)
t.lt(45)
t.down()
t.begin_fill()
t.fillcolor('white')
t.circle(75,270)
t.end_fill()

t.up()
t.goto(-70,-60)
t.setheading(180)
t.down()
t.lt(85)
t.color('black')
t.circle(55,190)
t.setheading(180)
t.fd(110)

#draw circle on rectangle
t.up()
t.home()

t.width(0)
t.goto(-16,0)
t.down()
t.begin_fill()
t.fillcolor('yellow')
t.circle(-10)
t.end_fill()
     
t.circle(-10,65)
t.setheading(180)
t.fd(17)

t.up()
t.goto(-16,0)
t.setheading(0)
t.circle(-10,85)
t.setheading(180)
t.down()
t.fd(22)

#To introduce doraemon by saying Hey My name is doraemon
sketch=turtle.Turtle()
sketch.width(3)
sketch.color("red")
sketch.hideturtle()
sketch.up()
sketch.goto(0,270)
sketch.write("Hey, MY Name Is Doraemon.",align='center',font=('Courier',28,'normal'))

#The below line is not necessary to write it's just to solve the problem which is mentioned also.
x=input()#JUST to stop the screen of graphics because i wrote this in vs code and after doing all stufs in screen will disappear or you can say it automatically exits.