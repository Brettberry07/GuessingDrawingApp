from torch.cpu.amp import autocast

from graph_globals import *
from grid import Grid

# Initialize the game
pygame.init()

screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Graph Visualization")

points = []

for x in range(0, 20):
    for y in range(0, 20):
        if Grid.check_point(x * 50).real <= float(y * 50):
            points.append((x * 50, y * 50, (255, 0, 0)))
        else:
            points.append((x * 50, y * 50, (0, 255, 0)))


Grid.draw(points)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if Grid.check_point(pos[0]).real <= float(pos[1]):
                points.append((pos[0], pos[1], (255, 0, 0)))
            else:
                points.append((pos[0], pos[1], (0, 255, 0)))
            Grid.draw(points)

    # Flip the display (updating the screen)
    pygame.display.flip()

    # making it move at 120 frames per second
    pygame.time.Clock().tick(FPS)




