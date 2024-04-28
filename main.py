# import liberaries
import turtle
# Add documentation


# main function (all inputs in main)
def main():
  # Declare Variables
  screen = turtle.Screen()
  turtle.speed(0)

  # Call function 1
  set_background_color(screen)

  # Call function 2
  draw_grid_pattern(screen)

  # Call function 3
  draw_shape(screen)

  # Ask for Text Letter overlay
  text_letter = input("Enter the text letter you want to overlay: ")
  # Call function 4
  draw_text(text_letter)
  turtle.done()
  # draw_text(screen, text_letter)

# function 1 (background color)
def set_background_color(screen):
  color = str
  while True:
    color = input("Enter the desired background color (Red, Blue, Green, etc.): ")
    if color.lower() in ["red", "blue", "green", "yellow", "orange", "pink", "brown", "cyan", "black", "white", "purple"]:  # Add more colors if needed
        break
    else:
        print("Invalid color. Please choose from: Red, Blue, Green, Yellow, Orange, Pink, Purple, Brown, Black, White")
  screen.bgcolor(color)

# function 2 (logo back design / pattern options?)
pattern = str
color = str
def draw_grid_pattern(screen):
  pattern = str()
  color = str()
  while True:
      color = input("Enter the desired color for the pattern (Red, Blue, Green, etc.): ")
      if color.lower() in ["red", "blue", "green", "yellow", "orange", "pink", "brown", "cyan", "black", "white", "purple"]:  
          break
      else:
          print("Invalid color. Please choose from: Red, Blue, Green, Yellow, Orange, Pink, Purple, Brown, Black, White")
  # change color
  turtle.pencolor(color)

  while True:
      print("\nSelect desired pattern shape")
      print("1. Grid\n2. Stripes\n3. Diagonal\n4. Dot\n5. Diagrid")
      pattern = input("Enter a pattern: ")
      width, height = screen.window_width(), screen.window_height()
      if pattern == "Grid":
          Verticle(width, height)
          Horizontal(width, height)
          break
      elif pattern == "Stripes":
          stripe_direction = input("Enter stripe direction (horizontal/vertical): ")
          if stripe_direction == "horizontal":
              Horizontal(width, height)
          elif stripe_direction == "vertical":
              Verticle(width, height)
          else:
              print("Invalid stripe direction. Please enter 'horizontal' or 'vertical'.")
          break
      elif pattern == "Diagonal":
          dir = input("Enter direction (left/right): ")
          if dir == "left":
              Diagonal(width, height)
              break
          elif dir == "right":
              DiagonalR(width, height)
              break
          else:
              print("Invalid direction. Please enter 'left' or 'right'.")
      elif pattern == "Dot":
          dot_size = int(input("Size of each Dots: "))
          spacing = int(input("Spacing between each Dots: "))
          DotPattern(dot_size, spacing, width, height)
          break
      elif pattern == "Diagrid":
          Diagonal(width, height)
          DiagonalR(width, height)
          break
      else:
          print("\nInvalid pattern choice.\n")
          Q = input("Try again")


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
def DiagonalR(width, height):
  turtle.speed(0)
  turtle.penup()
  stripe_width = int()
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
def draw_shape(screen):
  shape = input(
    "Enter the shape you want to draw (diamond, square, circle): ").lower()
  color = str()
  color = input("\nEnter the desired color for shape: ")
  width, height = screen.window_width(), screen.window_height()
  while shape not in ["diamond", "square", "circle"]:
    print("Invalid shape choice. Please choose from 'diamond', 'square', or 'circle'.")
    print("\n1. Diamond\n2. Square\n3. Circle")
    shape = input("Enter the shape you want to draw: ").lower()

  if shape == "diamond":
    draw_diamond(width, height)
    turtle.fillcolor(color)
  elif shape == "square":
    draw_square(width, height)
    turtle.fillcolor(color)
  elif shape == "circle":
    draw_circle(width, height)
    turtle.fillcolor(color)
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
  halfH = height // 2
  halfW = width // 2
  if width > height:
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -halfH // 2)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(halfH // 2)
    turtle.end_fill()
    turtle.hideturtle()
  else:
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -halfW // 2)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(halfW // 2)
    turtle.end_fill()
    turtle.hideturtle()


# function 4 (logo design text?)
def draw_text(text_letter):
    font = fontstyle()
    turtle.speed(0)
    turtle.penup()
    # Adjust the position as needed
    turtle.goto(0, -60)
    turtle.pendown()
    turtle.color("white")
    turtle.write(text_letter, align='center', font=(font, 80, 'normal'))
    turtle.hideturtle()

# function 5 (logo design font?
def fontstyle():
  while True:
    font = str()
    print("A, B or C")
    font = input("('Arial', 'High Tower Text', 'Imprint MT Shadow'): ").lower()
    if font == "a":
      return "Arial"
      break
    elif font == "b":
      return "High Tower Text"
      break
    elif font == "c":
      return "Imprint MT Shadow"
      break
    else:
      print("Invalid font style.")




# call main
main()


