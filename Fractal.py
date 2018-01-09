import turtle

def fractal():
    window=turtle.Screen() #the class is put into a screen almost like a red carpet
    window.bgcolor("red")
    
    putu=turtle.Turtle() #putu happens to be the name of our turtle
    putu.shape("arrow")
    putu.color("blue")
    putu.speed(5) #the speed is increased five folds
    #the circle turns right by 10 degrees every after every circular motion
    i=0
    while i<36:
        putu.right(10)
        putu.circle(100)
    window.exitonclick()
fractal()
