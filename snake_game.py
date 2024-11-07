import turtle
import time
import random

delay = 0.1

#score
score=0
high_score = 0

#setup screen
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  #turns off the screen updates


#snake head

head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction ="stop"

#snake food

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments =[]

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write("Score::0 High Score", align="center", font=("Courier",24,"normal"))

#functions

def go_up():
    if head.direction !="down":
        head.direction="up"


def go_down():
    if head.direction !="up":
        head.direction="down"
        

def go_left():
    if head.direction !="right":
        head.direction="left"


def go_right():
    if head.direction !="left":
        head.direction="right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.set(y+20)

    if head.direction == "up":
        y = head.ycor()
        head.set(y-20)

    if head.direction == "up":
        x = head.xcor()
        head.set(x-20)

    if head.direction == "up":
        x = head.xcor()
        head.set(x+20)


#keyboard button set/ binding

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d") 

#main game loop

while True:
    wn.update()


    #check collision with border

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"


        #hide segments

        for segment in segments:
            segment.goto(1000,1000)

        #clear the segment list

        segments.clear()

        #reset the score

        score = 0

        #reset the delay

        delay = -0.1

        pen.clear()

        pen.write("Score: High Score:{}".format(score, high_score), align="center", font=("Courier",24,"normal"))


        #check for collision with food
        if head.distance(food)<20:
            #movement of food in random spot
            x= random.radiant(-290,290)
            y= random.radiant(-290,290)
            food.goto(x,y)


            #add segment
            new_segment=turtle.Turtle()
            new_segment.speed(0)
            new_segment.color("square")
            new_segment.penup()
            segments.append(new_segment)

            #shorts delay

            delay -= 0.001

            #increase score

            score += 10

            if score >  high_score:
                high_score = score

            pen.clear()

            pen.write("Score: High Score:{}".format(score, high_score), align="center", font=("Courier",24,"normal"))


            #move end segment in reverse order

            for index in range(len(segments)-1,0,-1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                
                segments[index].goto(x,y)

            #move segment 0 at where head is 

            if len(segment)>0:
                x = head.xcor()
                y = head.ycor()
                segment[0].goto(x,y)

            move()

            #check for head collision with the body segments

            for segments in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"


                    #hide the premade segments/tail

                    for segments in segments:
                        segment.goto(1000,1000)

                    #clear segment list

                    segments.clear()
                    

                    #reset score

                    score = 0


                    #reset the delay

                    delay = 0.1


                    #update the score display

                    pen.clear()
                    pen.write("Score: High Score:{}".format(score, high_score), align="center", font=("Courier",24,"normal"))

        time.sleep(delay)

wn.mainloop()

