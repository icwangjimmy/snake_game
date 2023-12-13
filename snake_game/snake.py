import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 10

# Define food properties
FOOD_SIZE = 20

class Game:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.snake = Snake()
        self.food = Food()

    def start_game(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        clock = pygame.time.Clock()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction("up")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction("down")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction("left")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction("right")

            self.snake.move()

            if self.snake.check_collision():
                self.end_game()

            if self.snake.eat_food(self.food.position):
                self.score += 1
                if self.score > self.high_score:
                    self.high_score = self.score
                self.food.generate()

            screen.fill(BLACK)
            self.snake.draw(screen)
            self.food.draw(screen)
            self.draw_score(screen)

            pygame.display.flip()
            clock.tick(SNAKE_SPEED)

        pygame.quit()

    def end_game(self):
        self.score = 0
        self.snake.reset()
        self.food.generate()

    def draw_score(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}  High Score: {self.high_score}", True, WHITE)
        screen.blit(text, (10, 10))

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, 0)

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_x = x + dx * SNAKE_SIZE
        new_y = y + dy * SNAKE_SIZE
        self.body.insert(0, (new_x, new_y))
        self.body.pop()

    def change_direction(self, direction):
        if direction == "up" and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == "down" and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == "left" and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == "right" and self.direction != (-1, 0):
            self.direction = (1, 0)

    def eat_food(self, food_position):
        head = self.body[0]
        if head == food_position:
            self.body.append((0, 0))
            return True
        return False

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return True
        for segment in self.body[1:]:
            if segment == head:
                return True
        return False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    def reset(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, 0)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.generate()

    def generate(self):
        x = random.randint(0, SCREEN_WIDTH // FOOD_SIZE - 1) * FOOD_SIZE
        y = random.randint(0, SCREEN_HEIGHT // FOOD_SIZE - 1) * FOOD_SIZE
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], FOOD_SIZE, FOOD_SIZE))

if __name__ == "__main__":
    game = Game()
    game.start_game()
