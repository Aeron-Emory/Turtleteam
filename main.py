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
  pattern_choice = input("Enter the desired pattern shape (Dots, Stars, Circles): ")
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
  
# function 3 (foreground design options?)
def draw_shape(screen, shape):

# function 4 (logo design text? limit 1 character)
def get_text_overlay():


