from graph_globals import *
class Grid:
    STEP: int = 25

    @staticmethod
    def draw(points: list[tuple[float, float, tuple[int, int, int]]]) -> None:

        # Draw the grid lines
        for x in range(0, SCREEN_WIDTH, Grid.STEP):
            for y in range(0, SCREEN_HEIGHT, Grid.STEP):
                pygame.draw.rect(screen, (200, 200, 200), (x, y, Grid.STEP, Grid.STEP), 1)

        # Draw x and y axes
        pygame.draw.line(screen, (0, 0, 0), (0, 20 * Grid.STEP), (SCREEN_WIDTH, 20 * Grid.STEP))  # x-axis
        pygame.draw.line(screen, (0, 0, 0), (3 * Grid.STEP, 0), (3 * Grid.STEP, SCREEN_HEIGHT))  # y-axis

        # Add ticks every 5 points along the different axis
        for x in range(3 * Grid.STEP, SCREEN_WIDTH, 5 * Grid.STEP):
            pygame.draw.line(screen, (0, 0, 0), (x, 20 * Grid.STEP - 7), (x, 20 * Grid.STEP + 7))

        for y in range(0, SCREEN_HEIGHT, 5 * Grid.STEP):
            pygame.draw.line(screen, (0, 0, 0), (3 * Grid.STEP - 7, y), (3 * Grid.STEP + 7, y))

        # Graph the line of the function
        Grid.graph_func()

        # Drawing our points
        for point in points:
            pygame.draw.circle(screen, point[-1], point[:2],5)

    @staticmethod
    def check_point(x: float) -> float:
        return - ((x ** 2.7 ) * 0.00001) + 489


    @staticmethod
    def graph_func() -> None:
        step: int = 1
        for x in range(0, SCREEN_WIDTH, step):
            pygame.draw.line(screen, (0, 0, 255), (x, Grid.check_point(x)), (x + step, Grid.check_point(x + step)), 2)


