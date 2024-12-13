

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

def on_clear_press():
    print("Clear")
    screen.fill(BACKGROUND_COLOR)

def on_submit_press():
    print("Submit")                         # Get the canvas surface only
    pygame.image.save(canvas_screen, "canvas.png")                  # Save as a png

    # Converting to neural network input
    canvas_array = pygame.surfarray.array3d(canvas_screen)                   # Convert the surface to a 3D array
    canvas_array = np.transpose(canvas_array, (1, 0, 2))        # Transpose the array to match the neural network input shape

    # Converting the array to grayscale
    # canvas_array = np.dot(canvas_array, [0.2989, 0.5870, 0.1140])  # Convert the array to grayscale DOESN'T WORK BC FLOATING POINT
    canvas_array = np.mean(canvas_array, axis=2).astype(np.uint8)    # Convert the array to grayscale WORKS BECAUSE INT

    # Saving the greyscale image using PIL
    Image.fromarray(canvas_array).save("canvas_gray.png")              # Convert the array to an image

    time.sleep(0.5)

    canvas_screen.fill(BACKGROUND_COLOR)

    print('image saved')


submit_button = Button(63.33, 575, 200, 50, (0, 255, 0), (0, 200, 0), "Submit", on_submit_press)
clear_button = Button(426.6, 575, 200, 50, (255, 0, 0), (200, 0, 0), "Clear", on_clear_press)


screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Guessing Drawing App")

# Variables to track drawing state
drawing = False
last_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 10 < pos[0] < 690 and 10 < pos[1] < 500:
                drawing = True
                last_pos = pos  # Start tracking from the first click
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None  # Stop tracking when the mouse is released

    if drawing:                                                                             # Only draw if the mouse is down
        current_pos = pygame.mouse.get_pos()                                                # Get the mouse position
        if 10 < current_pos[0] < 690 and 10 < current_pos[1] < 500:                         # Ensure the position is within the canvas
            if last_pos:                                                                    # Ensure there's a previous position to draw from
                pygame.draw.line(canvas_screen, (0, 0, 0), last_pos, current_pos, 7)  # Draw a line from the last position to the current position
            last_pos = current_pos                                                          # Update last position

    # Draw a solid blue circle in the center
    submit_button.draw()
    clear_button.draw()
    Frame.draw()


    # Flip the display
    pygame.display.flip()

    # making it move at 60 frames per second
    pygame.time.Clock().tick(FPS)




