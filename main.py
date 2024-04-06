import turtle
# Add documentation

# main function (all inputs in main)
def main():
  # Declare Variables
  screen = turtle.Screen()
  # Ask for what background color
  background_color = input("Enter the desired background color (Red, Blue, Green): ")
  # Call function 1 
  set_background_color(screen, background_color)
  # Ask for what background pattern
  pattern_choice = input("Enter the desired pattern shape (grid, stripes, diagonal): ")
  # Call function 2
  draw_grid_pattern(screen, pattern_choice)
  # Ask for what shape
  shape_choice = input("Enter the shape you want to draw (diamon, square, circle): ")
  # Call function 3
  draw_shape(screen, shape_choice)
  # Ask for Text Letter overlay

# function 1 (background color)
def set_background_color(screen, color):
  screen.bgcolor(color)

# function 2 (logo back design / pattern options?)
def draw_grid_pattern(screen, pattern):
  width, height = screen.window_width(), screen.window_height()
  if pattern == "grid":
    Verticle(width, height)
    Horizontal(width, height)
  elif pattern == "stripes":
    stripe_direction = input("Enter stripe direction (horizontal/vertical): ")
    if stripe_direction == "horizontal":
      Horizontal(width, height)
    elif stripe_direction == "vertical":
      Verticle(width, height)
    else:
      print("Invalid stripe direction. Please enter 'horizontal' or 'vertical'.")
  elif pattern == "diagonal":

# function 2.1 (Verticle lines)
def Verticle(width, height):
  num_cells_x = width // 50
  for x in range(-num_cells_x // 2, num_cells_x // 2 + 1):
    turtle.penup()
    turtle.goto(x * 50, -height // 2)
    turtle.pendown()
    turtle.goto(x * 50, height // 2)

# function 2.2 (Horizontal lines)
def Horizontal(width, height):
  num_cells_y = height // 50
  for y in range(-num_cells_y // 2, num_cells_y // 2 + 1):
    turtle.penup()
    turtle.goto(-width // 2, y * 50)
    turtle.pendown()
    turtle.goto(width // 2, y * 50)

# function 3 (foreground design options?)
def draw_shape(screen, shape):
  print(shape)

# function 4 (logo design text? limit 1 character)
def get_text_overlay():
  print("hi")

main()
