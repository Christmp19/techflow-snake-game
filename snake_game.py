import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

# Creating the window and setting height and width
wn = turtle.Screen()
wn.title("TechFlow's Snake Game")
wn.bgcolor('green')
wn.setup(width=700, height=700)
wn.tracer(0) # Turns off the screen updates

# Creating a border for the game
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color('white')
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.penup()
border.hideturtle()

# Creating head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Creating space to show score and high score
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape('square')
scoreBoard.color('white')
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 260)
scoreBoard.write("Score : 0  High Score : 0", align='center', font=('Courier', 25, 'bold'))

# Creating food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randint(-290, 290), random.randint(-240, 240))

# Assigning key directions
def move_up():
    if head.direction != 'down':
        head.direction = 'up'

def move_down():
    if head.direction != 'up':
        head.direction = 'down'

def move_left():
    if head.direction != 'right':
        head.direction = 'left'

def move_right():
    if head.direction != 'left':
        head.direction = 'right'
        
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(move_up, 'Up')
wn.onkeypress(move_down, 'Down')
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')

segments = []

def game_over():
    global score, high_score, segments, delay

    # Display game over message in the middle of the white square
    # scoreBoard.clear()
    # scoreBoard.goto(0, 0)
    # scoreBoard.color('red')
    # scoreBoard.write("GAME OVER", align='center', font=('Courier', 40, 'bold'))
    
    # Pause to show the game over message
    time.sleep(2)
    
    # Reset the game
    head.goto(0, 0)
    head.direction = "stop"
    
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    
    # Clear the segments list
    segments.clear()

    # Update the high score if necessary
    if score > high_score:
        high_score = score

    # Reset the score
    score = 0

    # Reset the delay
    delay = 0.1

    # Reset the scoreboard
    scoreBoard.clear()
    scoreBoard.goto(0, 260)
    scoreBoard.color('white')
    scoreBoard.write("Score : {}  High Score : {}".format(score, high_score), align='center', font=('Courier', 25, 'bold'))

# Main Game
while True:  # Running an infinite loop until the collision occurs and then game ends
    wn.update()
    
    # Ending the game on collision with any of the walls
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 240 or head.ycor() < -240:
        game_over()
    
    # If snake collects food
    if head.distance(food) < 20:
        # Increasing score and updating the high score
        score += 10
        if score > high_score:
            high_score = score
        scoreBoard.clear()
        scoreBoard.write("Score : {}  High Score : {}".format(score, high_score), align='center', font=('Courier', 25, 'bold'))
        
        # Creating food at random location
        x_cord = random.randint(-290, 290)
        y_cord = random.randint(-240, 240)
        food_color = 'red'
        food_shape = 'circle'
        food.speed(0)
        food.shape(food_shape)
        food.color(food_color)
        food.goto(x_cord, y_cord)
        
        # Adding a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('blue')  # giving a new color to the tail
        new_segment.penup()
        segments.append(new_segment)  # adding the segment to the list
    
    # Moving the snake and ending the game on collision of head with body segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    
    # Checking for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()
    
    time.sleep(delay)
    
turtle.Terminator()