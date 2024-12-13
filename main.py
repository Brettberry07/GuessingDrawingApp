from globals import *
from button import Button
from border import Frame

# Initialize the game
pygame.init()
'''
making a basic loop that open up a window displaying hello world
'''

def print_helloworld():
    print("Hello World")
    time.sleep(0.11)


submit_button = Button(63.33, 575, 200, 50, (0, 255, 0), (0, 200, 0), "Submit", print_helloworld)
clear_button = Button(426.6, 575, 200, 50, (255, 0, 0), (200, 0, 0), "Clear", print_helloworld)

while True:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

    # Fill the background with white
    screen.fill(BACKGROUND_COLOR)

    # Draw a solid blue circle in the center
    submit_button.draw()
    clear_button.draw()
    Frame.draw()


    # Flip the display
    pygame.display.flip()

    # making it move at 60 frames per second
    pygame.time.Clock().tick(FPS)




