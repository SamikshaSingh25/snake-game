import pygame
import random





WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()


    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = random.choice([UP, DOWN, LEFT, RIGHT])

    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = UP
                elif event.key == pygame.K_DOWN:
                    direction = DOWN
                elif event.key == pygame.K_LEFT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    direction = RIGHT

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)


        if head == food:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()


        if (head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT or
            head in snake[1:]):
            pygame.quit()
            return


        screen.fill(WHITE)


        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


        pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()


        clock.tick(10)

if __name__ == "__main__":
    main()
