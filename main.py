import turtle

# Add documentation


# main function (all inputs in main)
def main():
  # Declare Variables
  screen = turtle.Screen()
  # Ask for what background color
  background_color = input(
      "Enter the desired background color (Red, Blue, Green): ")
  # Call function 1
  set_background_color(screen, background_color)
  # Ask for what background pattern
  print("Enter the desired pattern shape")
  pattern_choice = input(
      "(Grid, Stripes, Diagonal, Dot, Diagonal R, Diagrid): ")
  # Call function 2
  draw_grid_pattern(screen, pattern_choice)
  # Ask for what shape
  shape_choice = input(
      "Enter the shape you want to draw (diamond, square, circle): ").lower()
  # Call function 3
  draw_shape(screen, shape_choice)
  # Ask for Text Letter overlay
  text_letter = input("Enter the text letter you want to overlay: ")
  # Call function 4
  # draw_text(screen, text_letter)

# function 1 (background color)
def set_background_color(screen, color):
  screen.bgcolor(color)


# function 2 (logo back design / pattern options?)
def draw_grid_pattern(screen, pattern):
  width, height = screen.window_width(), screen.window_height()
  if pattern == "Grid":
    Verticle(width, height)
    Horizontal(width, height)
  elif pattern == "Stripes":
    stripe_direction = input("Enter stripe direction (horizontal/vertical): ")
    if stripe_direction == "horizontal":
      Horizontal(width, height)
    elif stripe_direction == "vertical":
      Verticle(width, height)
    else:
      print(
          "Invalid stripe direction. Please enter 'horizontal' or 'vertical'.")
  elif pattern == "Diagonal":
    Diagonal(width, height)
  elif pattern == "Dot":
    dot_size = int(input("Size of each Dots: "))
    spacing = int(input("Spacing between each Dots: "))
    DotPattern(dot_size, spacing, width, height)
  elif pattern == "Diagonal R":
    diagonalR(width, height)
  elif pattern == "Diagrid":
    Diagonal(width, height)
    diagonalR(width, height)
  else:
    print("Invalid pattern choice. Please choose from")
    print("'Grid', 'Stripes', 'Diagonal', 'Dot', 'Diagonal R', or 'Diagrid'.")


# function 2.1 (Verticle lines)
def Verticle(width, height):
  turtle.speed(0)
  lines = int()
  lines = width // 50
  for x in range(-lines // 2, lines // 2 + 1):
    turtle.penup()
    turtle.goto(x * 50, -height // 2)
    turtle.pendown()
    turtle.goto(x * 50, height // 2)


# function 2.2 (Horizontal lines)
def Horizontal(width, height):
  turtle.speed(0)
  lines = int()
  lines = height // 50
  for y in range(-lines // 2, lines // 2 + 1):
    turtle.penup()
    turtle.goto(-width // 2, y * 50)
    turtle.pendown()
    turtle.goto(width // 2, y * 50)


# function 2.3 (Diagonal lines)
def Diagonal(width, height):
  turtle.speed(0)
  turtle.penup()
  stripe_width = 20
  diagonal_length = (width**2 + height**2)**0.5
  num_stripes = int(diagonal_length // stripe_width) + 1
  for i in range(-num_stripes, num_stripes):
    start_x = max(-width / 2, -width / 2 + i * stripe_width)
    start_y = min(height / 2, height / 2 + i * stripe_width)
    turtle.goto(start_x, start_y)
    turtle.pendown()
    end_x = start_x + diagonal_length
    end_y = start_y - diagonal_length
    turtle.goto(end_x, end_y)
    turtle.penup()


# function 2.4 (Dots)
def DotPattern(dot_size, spacing, width, height):
  turtle.speed(0)
  turtle.penup()
  start_x = -width / 2 + spacing / 2
  start_y = height / 2 - spacing / 2
  for y in range(int(height / spacing)):
    for x in range(int(width / spacing)):
      turtle.goto(start_x + x * spacing, start_y - y * spacing)
      turtle.dot(dot_size)


# function 2.5 (Reversed diagonal)
def diagonalR(width, height):
  turtle.speed(0)  # Set the drawing speed to the fastest
  turtle.penup()
  stripe_width = 20
  diagonal_length = (width**2 + height**2)**0.5
  num_stripes = int(diagonal_length // stripe_width) + 1
  for i in range(-num_stripes, num_stripes):
    start_x = min(width / 2, width / 2 - i * stripe_width)
    start_y = min(height / 2, height / 2 + i * stripe_width)
    turtle.goto(start_x, start_y)
    turtle.pendown()
    end_x = start_x - diagonal_length
    end_y = start_y - diagonal_length
    turtle.goto(end_x, end_y)
    turtle.penup()


# function 3 (foreground design options?)
def draw_shape(screen, shape):
  width, height = screen.window_width(), screen.window_height()
  turtle.write("Hi", font=("Fantasy", 20, ''))
  if shape == "diamond":
    draw_diamond(width, height)
  elif shape == "square":
    draw_square(width, height)
  elif shape == "circle":
    draw_circle(width, height)
  else:
    print("Invalid shape choice. Please choose from 'diamond', 'square', or 'circle'.")

# function 3.1 (diamond)
def draw_diamond(width, height):
  halfH = height // 2
  halfW = width // 2
  turtle.speed(0)
  turtle.penup()
  turtle.goto(0, halfH // 2)
  turtle.pendown()
  turtle.color("black")
  turtle.begin_fill()
  turtle.goto(halfW // 2, 0)
  turtle.goto(0, -halfH // 2)
  turtle.goto(-halfW // 2, 0)
  turtle.goto(0, halfH // 2)
  turtle.end_fill()
  turtle.hideturtle()

# function 3.2 (square)
def draw_square(width, height):
  halfH = height // 2
  halfW = width // 2
  turtle.speed(0)
  turtle.penup()
  turtle.goto(halfW // 2, halfH // 2)
  turtle.pendown()
  turtle.color("black")
  turtle.begin_fill()
  turtle.goto(halfW // 2, -halfH // 2)
  turtle.goto(-halfW // 2, -halfH // 2)
  turtle.goto(-halfW // 2, halfH // 2)
  turtle.goto(halfW // 2, halfH // 2)
  turtle.end_fill()
  turtle.hideturtle()

# function 3.3 (circle)
def draw_circle(width, height):
  turtle.speed(0)
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()
  turtle.color("black")
  turtle.begin_fill()
  turtle.circle(50)
  turtle.end_fill()
  turtle.hideturtle()


# function 4 (logo design text? limit 1 character)
def get_text_overlay():
  turtle.write("TEXT", align='center', font=('Pacifico', 48, ''))


main()
