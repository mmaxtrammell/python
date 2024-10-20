import math
import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the window
width = 800
height = 600

# Create the window
window = pygame.display.set_mode((width, height))

# Set the background color to green
background_color = (1, 50, 32)  # Green color in RGB

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

# Define circle parameters
center = (800, 600)
radius = 250

# Define the line thickness
line_thickness = 50

# Set up colors
YELLOW = (255, 255, 0)

# Set up line parameters
vertical_start_pos = (width // 2, 0)
vertical_end_pos = (width // 2, height)
vertical_dash_length = 10
vertical_gap_length = 10

horizontal_start_pos = (0, height // 2)
horizontal_end_pos = (width, height // 2)
horizontal_dash_length = 10
horizontal_gap_length = 10

# Define the first car's initial position and size
car1_x = 0
car1_y = height // 2 - line_thickness // 2 + 30
car1_width = 20
car1_height = 10

# Define the first car's speed
car1_speed = 1  # Adjust the speed value as desired

# Define the second car's initial position and size
car2_x = width
car2_y = height // 2 - line_thickness // 2 + 10
car2_width = 20
car2_height = 10

# Define the second car's speed
car2_speed = -1  # Adjust the speed value as desired

# Define the third car's initial position and size
car3_x = width // 2 - line_thickness // 2 + 10
car3_y = 0
car3_width = 10
car3_height = 20

# Define the third car's speed
car3_speed = 1  # Adjust the speed value as desired

# Define the fourth car's initial position and size
car4_x = width // 2 - line_thickness // 2 + 30
car4_y = height
car4_width = 10
car4_height = 20

# Define the fourth car's speed
car4_speed = -1  # Adjust the speed value as desired

# Define the rectangle dimensions for light1
light1_x = width // 2 + 50
light1_y = height // 2 - 10
light1_width = 5
light1_height = 15

# Define the rectangle dimensions for light2
light2_x = width // 2 - 50
light2_y = height // 2 + 10
light2_width = 5
light2_height = 15

# Define the rectangle dimensions for light3
light3_x = width // 2 - 10
light3_y = height // 2 - 50
light3_width = 15
light3_height = 5

# Define the rectangle dimensions for light4
light4_x = width // 2 + 10
light4_y = height // 2 + 50
light4_width = 15
light4_height = 5

# Define the rectangle's properties
rect_width, rect_height = 20, 10
rect_center_x, rect_center_y = 800, 600
radius2 = 220
angular_speed = 0.001  # Angular speed

# Define the color gradient for the lights
color_gradient1 = [(0, 128, 0), (255, 0, 0)]  # Green and red colors only
color_gradient2 = [(255, 0, 0), (0, 128, 0)]  # Red and Green colors only
color_index = 0

# Define the time increments for color change (in milliseconds)
green_time = 5000  # 5 seconds
red_time = 3000  # 3 seconds

# Define the elapsed time variables
elapsed_time = 0

# Define the movement flag for car1
car1_moving = True

# Define the movement flag for car2
car2_moving = True

# Define the movement flag for car3
car3_moving = True

# Define the movement flag for car4
car4_moving = True

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

    # Draw the outline of the circle
    pygame.draw.circle(window, (78,53,36), center, radius, line_thickness)

    # Draw the vertical broken yellow line
    vertical_current_pos = vertical_start_pos
    vertical_direction = pygame.math.Vector2(vertical_end_pos) - pygame.math.Vector2(vertical_start_pos)
    vertical_distance = vertical_direction.length()
    vertical_direction.normalize_ip()

    while vertical_distance > 0:
        vertical_dash_end_pos = vertical_current_pos + vertical_direction * min(vertical_dash_length, vertical_distance)
        pygame.draw.line(window, YELLOW, vertical_current_pos, vertical_dash_end_pos)
        vertical_current_pos = vertical_dash_end_pos + vertical_direction * vertical_gap_length
        vertical_distance -= vertical_dash_length + vertical_gap_length

    # Draw the horizontal broken yellow line
    horizontal_current_pos = horizontal_start_pos
    horizontal_direction = pygame.math.Vector2(horizontal_end_pos) - pygame.math.Vector2(horizontal_start_pos)
    horizontal_distance = horizontal_direction.length()
    horizontal_direction.normalize_ip()

    while horizontal_distance > 0:
        horizontal_dash_end_pos = horizontal_current_pos + horizontal_direction * min(horizontal_dash_length, horizontal_distance)
        pygame.draw.line(window, YELLOW, horizontal_current_pos, horizontal_dash_end_pos)
        horizontal_current_pos = horizontal_dash_end_pos + horizontal_direction * horizontal_gap_length
        horizontal_distance -= horizontal_dash_length + horizontal_gap_length

    # Draw the first car at its current position
    pygame.draw.rect(window, (224, 169, 109), (car1_x, car1_y, car1_width, car1_height))

    # Draw the second car at its current position
    pygame.draw.rect(window, (224, 169, 109), (car2_x, car2_y, car2_width, car2_height))

    # Draw the third car at its current position
    pygame.draw.rect(window, (224, 169, 109), (car3_x, car3_y, car3_width, car3_height))

    # Draw the fourth car at its current position
    pygame.draw.rect(window, (224, 169, 109), (car4_x, car4_y, car4_width, car4_height))

    # Calculate the new position of the rectangle
    rect_angle = pygame.time.get_ticks() * angular_speed
    rect_x = rect_center_x + int(radius2 * math.cos(rect_angle))
    rect_y = rect_center_y + int(radius2 * math.sin(rect_angle))

    # Draw the rectangle
    pygame.draw.rect(window, (224, 169, 109), (rect_x - rect_width // 2, rect_y - rect_height // 2, rect_width, rect_height))

    # Define the rectangle dimensions for light1
    light1_rect = pygame.Rect(light1_x - light1_width // 2, light1_y - light1_height // 2, light1_width, light1_height)

    # Define the rectangle dimensions for light2
    light2_rect = pygame.Rect(light2_x - light2_width // 2, light2_y - light2_height // 2, light2_width, light2_height)

    # Define the rectangle dimensions for light3
    light3_rect = pygame.Rect(light3_x - light3_width // 2, light3_y - light3_height // 2, light3_width, light3_height)

    # Define the rectangle dimensions for light4
    light4_rect = pygame.Rect(light4_x - light4_width // 2, light4_y - light4_height // 2, light4_width, light4_height)

    # Get the current color based on the color index
    light1_color = color_gradient1[color_index]
    light2_color = color_gradient1[color_index]
    light3_color = color_gradient2[color_index]
    light4_color = color_gradient2[color_index]

    # Draw the light1 rectangle
    pygame.draw.rect(window, light1_color, light1_rect)

    # Draw the light2 rectangle
    pygame.draw.rect(window, light2_color, light2_rect)

    # Draw the light3 rectangle
    pygame.draw.rect(window, light3_color, light3_rect)

    # Draw the light4 rectangle
    pygame.draw.rect(window, light4_color, light4_rect)

    # Update the first car's position if it is allowed to move
    if car1_moving:
        car1_x += car1_speed

    # Update the second car's position if it is allowed to move
    if car2_moving:
        car2_x += car2_speed

    # Update the third car's position if it is allowed to move
    if car3_moving:
        car3_y += car3_speed

    # Update the fourth car's position if it is allowed to move
    if car4_moving:
        car4_y += car4_speed

    # Update the elapsed time
    elapsed_time += clock.get_time()

    # Check if the elapsed time exceeds the time increments for each color
    if elapsed_time >= green_time + red_time:
        # Reset the elapsed time
        elapsed_time = 0

    # Get the current color based on the elapsed time
    if elapsed_time < green_time:
        color_index = 0  # Green for color_gradient1 and Red for color_gradient2
        car1_moving = True  # Allow car1 to move
        car2_moving = True  # Allow car2 to move
    else:
        color_index = 1  # Red for color_gradient1 and Red for color_gradient2

        # Check if any car is touching the red light
        if light1_color == (255, 0, 0):
            if light2_rect.colliderect(pygame.Rect(car1_x, car1_y, car1_width, car1_height)):
                car1_moving = False  # Stop car1

        if light2_color == (255, 0, 0):
            if light1_rect.colliderect(pygame.Rect(car2_x, car2_y, car2_width, car2_height)):
                car2_moving = False  # Stop car2

    if light3_color == (255, 0, 0):
        if light3_rect.colliderect(pygame.Rect(car3_x, car3_y, car3_width, car3_height)):
            car3_moving = False  # Stop car3

    if light4_color == (255, 0, 0):
        if light4_rect.colliderect(pygame.Rect(car4_x, car4_y, car4_width, car4_height)):
            car4_moving = False  # Stop car4
    else:
        car3_moving = True
        car4_moving = True

    # Check if the first car has reached the right edge of the screen
    if car1_x > width:
        car1_x = -car1_width  # Reset its position to the left edge

    # Check if the second car has reached the left edge of the screen
    if car2_x < -car2_width:
        car2_x = width  # Reset its position to the right edge

    # Check if the third car has reached the bottom edge of the screen
    if car3_y > height:
        car3_y = -car3_height  # Reset its position to the top edge

    # Check if the fourth car has reached the top edge of the screen
    if car4_y < -car4_height:
        car4_y = height  # Reset its position to the bottom edge

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
