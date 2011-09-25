import sys, pygame
pygame.init() # Init pygame. Should be done, don't know why

size = width, height = 320, 240 # Specify the size of the window we are going to draw

white = 255, 255, 255 # Define the color white for convenience when redrawing the background

screen = pygame.display.set_mode(size) # Create the actual window

#mariorect = mario.get_rect() # Get a Rect-object, describing the size of the mario surface

class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def zero():
        return Vector2(0,0)

    def getTuple(self):
        return self.x, self.y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

class Player(object):
    def __init__(self, surface, position, speed):
        self.surface = surface
        self.position = position
        self.speed = speed
        self.rect = surface.get_rect()
        self._jump_start = None

    def jump(self):
        if self.isGrounded():
            self._jump_start = None
        if self._jump_start is None:
            self._jump_start = pygame.time.get_ticks()

        if self._jump_start and pygame.time.get_ticks() - self._jump_start < 0.4:
            self.speed.y += 5

    def update(self):
        self.rect = self.rect.move(self.speed.x, -self.speed.y)
        self._applyGravity()
        self._movementDecay()

    def _applyGravity(self):
        if not self.isGrounded():
            self.speed.y -= 0.2
        elif self.speed.y < 0:
            self.speed.y = 0

    def _movementDecay(self):
        if self.isGrounded():
            if self.speed.x > 0.08 or self.speed.x < -0.08:
                pass
                self.speed.x *= 0.95
            else:
                self.speed.x = 0

    def isGrounded(self):
        if self.rect.bottom >= 240:
            return True
        return False

    def addSpeed(self, speed):
        self.speed += speed

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

player = Player(pygame.image.load("mario.bmp"), Vector2.zero(), Vector2.zero())

while 1: # Start an infinite loop, the "game loop"
    for event in pygame.event.get(): # Loop through the event queue
        if event.type == pygame.QUIT: sys.exit() # If we're receiving the QUIT event, quit

    if pygame.key.get_pressed()[pygame.K_RIGHT]: # If the right arrow key is pressed, set the x-speed to 1
        player.addSpeed(Vector2(0.2, 0))

    if pygame.key.get_pressed()[pygame.K_LEFT]: # If the left arrow key is pressed, set the x-speed to -1
        player.addSpeed(Vector2(-0.2, 0))

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player.jump()

    screen.fill(white) # Redraw the screen, by filling it with white
    player.update()
    player.draw(screen)
    pygame.display.flip() # Make the newly drawn frame visible to the user
    pygame.time.delay(10) # Put in a delay to make mario walk in a groovy pace