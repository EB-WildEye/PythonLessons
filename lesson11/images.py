# ~~~~~~~~~~~~~~~~ Images in pygame library ~~~~~~~~~~~~~~~~
# program that create a window and display an image for background
import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (300, 170)

# Create the window
screen = pygame.display.set_mode(window_size)


# Load the sound file
sound = pygame.mixer.Sound('C:\\Users\\eb300\\Python\\43030\\lesson11\\Skrillex.wav')

# Play the sound
sound.play()

# Load the image
image = pygame.image.load('C:\\Users\\eb300\\Python\\43030\\lesson11\\images.jpeg').convert() 


# Display the image
screen.blit(image, (3, 3))

# Update the display
pygame.display.flip()

# set title 
pygame.display.set_caption('Rainbow Kitty')


# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
