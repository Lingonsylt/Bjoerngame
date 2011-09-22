import sys, pygame
pygame.init() # Init pygame. Should be done, don't know why

size = width, height = 320, 240 # Specify the size of the window we are going to draw

white = 255, 255, 255 # Define the color white for convenience when redrawing the background

screen = pygame.display.set_mode(size) # Create the actual window

mario = pygame.image.load("mario.bmp") # Create a Surface-object by loading an image. Seems like it needs to be a BMP, why?
mariorect = mario.get_rect() # Get a Rect-object, describing the size of the mario surface

while 1: # Start an infinite loop, the "game loop"
    for event in pygame.event.get(): # Loop through the event queue
        if event.type == pygame.QUIT: sys.exit() # If we're receiving the QUIT event, quit

    speed = [0,0] # Define the movement speed this frame in [x, y]-format

    if pygame.key.get_pressed()[pygame.K_RIGHT]: # If the right arrow key is pressed, set the x-speed to 1
        speed[0] = 1
    if pygame.key.get_pressed()[pygame.K_LEFT]: # If the left arrow key is pressed, set the x-speed to -1
        speed[0] = -1
    if pygame.key.get_pressed()[pygame.K_UP]: # If the up arrow key is pressed, set the y-speed to -1
        speed[1] = -1
    if pygame.key.get_pressed()[pygame.K_DOWN]: # If the down arrow key is pressed, set the y-speed to 1
        speed[1] = 1

    screen.fill(white) # Redraw the screen, by filling it with white
    mariorect = mariorect.move(speed) # Set mariorect to a new Rect which is the old mariorect, moved by <speed>
    screen.blit(mario, mariorect) # Draw the <mario> surface on the <screen>, inside the Rect <mariorect>
    pygame.display.flip() # Make the newly drawn frame visible to the user
    pygame.time.delay(10) # Put in a delay to make mario walk in a groovy pace