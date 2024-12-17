from Drawing.globals import *
from Drawing.button import Button
from Drawing.border import Frame

# Initialize the game
pygame.init()

def on_clear_press():
    print("Clear")
    screen.fill(BACKGROUND_COLOR)
    canvas_screen.fill(BACKGROUND_COLOR)
    time.sleep(0.11)

def on_submit_press():
    print("Submit")                                                   # Get the canvas surface only
    pygame.image.save(canvas_screen, "./Assets/canvas.png")           # Save as a png

    # Converting to neural network input
    canvas_array = pygame.surfarray.array3d(canvas_screen)            # Convert the surface to a 3D array
    canvas_array = np.transpose(canvas_array, (1, 0, 2))        # Transpose the array to match the neural network input shape

    # Converting the array to grayscale
    # canvas_array = np.dot(canvas_array, [0.2989, 0.5870, 0.1140])  # Convert the array to grayscale DOESN'T WORK BC FLOATING POINT
    canvas_array = np.mean(canvas_array, axis=2).astype(np.uint8)    # Convert the array to grayscale WORKS BECAUSE INT

    # Saving the greyscale image using PIL
    Image.fromarray(canvas_array).save("./Assets/canvas_gray.png")              # Convert the array to an image

    # Resizing the image to 28x28
    Image.fromarray(canvas_array).resize((28, 28)).save("./Assets/small_image.png")  # Convert the array to an image and resize

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
                pygame.draw.circle(canvas_screen, (0, 0, 0), pos, 3.5)  # Draw a circle when the mouse is clicked
                drawing = True
                last_pos = pos  # Start tracking from the first click
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None  # Stop tracking when the mouse is released

    if drawing:                                                                                         # Only draw if the mouse is down
        current_pos = pygame.mouse.get_pos()                                                            # Get the mouse position
        if 10 < current_pos[0] < 690 and 10 < current_pos[1] < 500:                                     # Ensure the position is within the canvas
            if last_pos is not None:                                                                                # Ensure there's a previous position to draw from
                pygame.draw.line(canvas_screen, (0, 0, 0), last_pos, current_pos, 7)        # Draw a line from the last position to the current position
            else:
                pygame.draw.circle(canvas_screen, (0, 0, 0), current_pos, 7)                # Draw a circle if there's no last position
            last_pos = current_pos                                                                       # Update last position
    else:
        last_pos = None                                                                                     # Reset last position if the mouse is up



    submit_button.draw()
    clear_button.draw()
    Frame.draw()


    # Flip the display (updating the screen)
    pygame.display.flip()

    # making it move at 120 frames per second
    pygame.time.Clock().tick(FPS)




