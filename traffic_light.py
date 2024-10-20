import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the window
width = 800
height = 600

# Create the window
window = pygame.display.set_mode((width, height))

# Set the background color to green
background_color = (87, 76, 65)  # Green color in RGB

# Set the window title
pygame.display.set_caption("Car Simulation")

# Define the color for the line (gray)
line_color = (13, 12, 13)  # Gray color in RGB

# Define the start and end points for the horizontal line
line_start = (0, height // 2)
line_end = (width, height // 2)

# Define the start and end points for the vertical line
vertical_line_start = (width // 2, 0)
vertical_line_end = (width // 2, height)

# Define the line thickness
line_thickness = 50

# Define the first rectangle's initial position and size
rectangle1_x = 0
rectangle1_y = height // 2 - line_thickness // 2 + 30
rectangle1_width = 20
rectangle1_height = 10

# Define the first rectangle's speed
rectangle1_speed = 1  # Adjust the speed value as desired

# Define the second rectangle's initial position and size
rectangle2_x = width
rectangle2_y = height // 2 - line_thickness // 2 + 10
rectangle2_width = 20
rectangle2_height = 10

# Define the second rectangle's speed
rectangle2_speed = -1  # Adjust the speed value as desired

# Define the third rectangle's initial position and size
rectangle3_x = width // 2 - line_thickness // 2 + 10
rectangle3_y = 0
rectangle3_width = 10
rectangle3_height = 20

# Define the third rectangle's speed
rectangle3_speed = 1  # Adjust the speed value as desired

# Define the fourth rectangle's initial position and size
rectangle4_x = width // 2 - line_thickness // 2 + 30
rectangle4_y = height
rectangle4_width = 10
rectangle4_height = 20

# Define the fourth rectangle's speed
rectangle4_speed = -1  # Adjust the speed value as desired

# Define the circle position and size
circle1_x = width // 2 + 50
circle1_y = height // 2
circle1_radius = 10

# Define the circle position and size
circle2_x = width // 2 - 50
circle2_y = height // 2
circle2_radius = 10

# Define the color gradient for the circles
color_gradient = [(0, 128, 0), (255, 255, 0), (255, 0, 0)]
color_index = 0

# Define the time increments for color change (in milliseconds)
green_time = 5000  # 5 seconds
yellow_time = 2000  # 2 seconds
red_time = 3000  # 3 seconds

# Define the elapsed time variables
elapsed_time = 0

# Define the movement flag for rectangle1
rectangle1_moving = True

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse coordinates
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Print the mouse coordinates
    print("Mouse coordinates:", mouse_x, mouse_y)

    # Fill the window with the background color
    window.fill(background_color)

    # Draw the thick gray horizontal line
    pygame.draw.line(window, line_color, line_start, line_end, line_thickness)

    # Draw the vertical line
    pygame.draw.line(window, line_color, vertical_line_start, vertical_line_end, line_thickness)

    # Draw the first rectangle at its current position
    pygame.draw.rect(window, (224, 169, 109), (rectangle1_x, rectangle1_y, rectangle1_width, rectangle1_height))

    # Draw the second rectangle at its current position
    pygame.draw.rect(window, (224, 169, 109), (rectangle2_x, rectangle2_y, rectangle2_width, rectangle2_height))

    # Draw the third rectangle at its current position
    pygame.draw.rect(window, (224, 169, 109), (rectangle3_x, rectangle3_y, rectangle3_width, rectangle3_height))

    # Draw the fourth rectangle at its current position
    pygame.draw.rect(window, (224, 169, 109), (rectangle4_x, rectangle4_y, rectangle4_width, rectangle4_height))

    # Update the first rectangle's position if it is allowed to move
    if rectangle1_moving:
        rectangle1_x += rectangle1_speed

    # Update the second rectangle's position
    rectangle2_x += rectangle2_speed

    # Update the third rectangle's position
    rectangle3_y += rectangle3_speed

    # Update the fourth rectangle's position
    rectangle4_y += rectangle4_speed

    # Update the elapsed time
    elapsed_time += clock.get_time()

    # Check if the elapsed time exceeds the time increments for each color
    if elapsed_time >= green_time + yellow_time + red_time:
        # Reset the elapsed time
        elapsed_time = 0

    # Get the current color based on the elapsed time
    if elapsed_time < green_time:
        color_index = 0  # Green
        rectangle1_moving = True  # Allow rectangle1 to move
    elif elapsed_time < green_time + yellow_time:
        color_index = 1  # Yellow
        rectangle1_moving = True  # Allow rectangle1 to move
    else:
        color_index = 2  # Red
        # Check if rectangle1 is between x values 325 and 370
        if 325 <= rectangle1_x <= 370:
            rectangle1_moving = False  # Stop rectangle1 from moving
        else:
            rectangle1_moving = True  # Allow rectangle1 to move

    # Get the current color based on the color index
    circle1_color = color_gradient[color_index]
    circle2_color = color_gradient[color_index]

    # Draw the circle1
    pygame.draw.circle(window, circle1_color, (circle1_x, circle1_y), circle1_radius)

    # Draw the circle2
    pygame.draw.circle(window, circle2_color, (circle2_x, circle2_y), circle2_radius)

    # Reset the first rectangle's position if it reaches the end of the line
    if rectangle1_x > width:
        rectangle1_x = 0

    # Reset the second rectangle's position if it reaches the end of the line
    if rectangle2_x + rectangle2_width < 0:
        rectangle2_x = width

    # Reset the third rectangle's position if it reaches the end of the line
    if rectangle3_y > height:
        rectangle3_y = 0

    # Reset the fourth rectangle's position if it reaches the end of the line
    if rectangle4_y + rectangle4_height < 0:
        rectangle4_y = height

    # Update the display
    pygame.display.update()

    # Add a delay to control the speed of the rectangles
    clock.tick(60)  # Set the desired frame rate (e.g., 60 frames per second)

# Quit Pygame
pygame.quit()
