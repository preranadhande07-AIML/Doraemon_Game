
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# --- Screen settings ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doraemon Game")

# --- Colors ---
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# --- Clock ---
clock = pygame.time.Clock()

# --- Player class ---
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.power = 0

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# --- Obstacle class ---
class Obstacle:
    def __init__(self):
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.speed = random.randint(5, 8)

    def move(self):
        self.rect.x -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# --- Background ---
def draw_background():
    screen.fill(WHITE)

# --- Main game loop ---
def main():
    player = Player()
    obstacles = []
    score = 0
    distance = 0
    game_over = False

    font = pygame.font.SysFont(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                main()

        keys = pygame.key.get_pressed()
        if not game_over:
            player.move(keys)
            distance += 1

            # Add new obstacles
            if random.randint(1, 25) == 1:
                obstacles.append(Obstacle())

            # Move obstacles
            for obs in obstacles:
                obs.move()

            # Collision detection
            for obs in obstacles:
                if player.rect.colliderect(obs.rect):
                    game_over = True

            # Remove old obstacles
            obstacles = [obs for obs in obstacles if obs.rect.x > -50]

            score += 1

        # Draw everything
        draw_background()
        player.draw(screen)

        for obs in obstacles:
            obs.draw(screen)

        score_text = font.render(f"Score: {score}  Distance: {distance}  Power: {player.power}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if game_over:
            over_text = font.render("GAME OVER! Click to Restart", True, RED)
            screen.blit(over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

        pygame.display.update()
        clock.tick(30)

# --- Run the game ---
if __name__ == "__main__":
    main()
