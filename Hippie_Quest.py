# Hippie Quest: Escape DEA Agents

import pygame
import random
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLAYER_SPEED = 5

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (76, 175, 80)
BROWN = (139, 69, 19)
BLUE_JEANS = (25, 25, 112)
PEACE_SYMBOL = (255, 255, 255)
DEA_RED = (220, 20, 60)
DISPENSARY_GREEN = (0, 150, 0)
HOODIE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Multi-colored

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.hoodie_color = random.choice(HOODIE_COLORS)
        self.update_sprite()
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)
        
        self.velocity_y = 0
        self.velocity_x = 0
        self.on_ground = False
        self.direction = 1  # 1 for right, -1 for left
        self.score = 0
        self.lives = 3

    def update_sprite(self):
        # Draw hippie character
        self.image.fill((0, 0, 0, 0))  # Transparent
        
        # Body (hoodie)
        pygame.draw.rect(self.image, self.hoodie_color, (0, 0, 40, 40))
        
        # Jeans with holes
        pygame.draw.rect(self.image, BLUE_JEANS, (0, 40, 40, 20))
        # Draw holes in jeans
        for hole in [(5, 45), (30, 50), (20, 55)]:
            pygame.draw.circle(self.image, SKY_BLUE, hole, 3)
        
        # Head
        pygame.draw.circle(self.image, (255, 218, 185), (20, 15), 10)
        
        # Peace symbol necklace
        pygame.draw.circle(self.image, PEACE_SYMBOL, (20, 35), 4)
        # Draw peace symbol lines
        pygame.draw.line(self.image, PEACE_SYMBOL, (20, 33), (20, 37), 2)
        pygame.draw.line(self.image, PEACE_SYMBOL, (17, 35), (23, 35), 2)
        
        # Eyes
        pygame.draw.circle(self.image, (0, 0, 0), (16, 13), 2)
        pygame.draw.circle(self.image, (0, 0, 0), (24, 13), 2)
        
        # Long hair
        pygame.draw.rect(self.image, (139, 69, 19), (5, 5, 30, 10))

    def update(self, platforms):
        # Apply gravity
        self.velocity_y += GRAVITY
        
        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Keep on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y = 0
        
        # Platform collision
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # Jumping
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH

    def draw(self, screen):
        # Flip sprite based on direction
        if self.direction == -1:
            screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        else:
            screen.blit(self.image, self.rect)

class DEAAgent(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((35, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(2, 4)
        self.update_sprite()
        
    def update_sprite(self):
        # Draw DEA agent
        self.image.fill(DEA_RED)
        
        # Tie
        pygame.draw.rect(self.image, (0, 0, 0), (16, 25, 3, 15))
        
        # Badge
        pygame.draw.circle(self.image, (255, 215, 0), (18, 20), 6)
        pygame.draw.rect(self.image, (255, 215, 0), (15, 18, 6, 4))
        
        # Head
        pygame.draw.circle(self.image, (255, 218, 185), (18, 10), 8)
        
        # Sunglasses
        pygame.draw.rect(self.image, (0, 0, 0), (11, 8, 6, 3))
        pygame.draw.rect(self.image, (0, 0, 0), (19, 8, 6, 3))
        pygame.draw.rect(self.image, (100, 100, 100), (17, 8, 2, 3))

    def update(self, platforms):
        self.rect.x += self.direction * self.speed
        
        # Platform edge detection
        future_rect = self.rect.copy()
        future_rect.y += 2  # Check just below
        future_rect.x += self.direction * self.speed
        
        on_platform = False
        for platform in platforms:
            if future_rect.colliderect(platform.rect):
                on_platform = True
                break
        
        if not on_platform or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
            self.rect.x += self.direction * self.speed

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=None):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color or BROWN
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class WeedDispensary(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.update_sprite()
        
    def update_sprite(self):
        # Draw dispensary
        self.image.fill(DISPENSARY_GREEN)
        
        # Door
        pygame.draw.rect(self.image, (139, 69, 19), (20, 40, 20, 40))
        
        # Windows
        pygame.draw.rect(self.image, (135, 206, 235), (10, 20, 15, 15))
        pygame.draw.rect(self.image, (135, 206, 235), (35, 20, 15, 15))
        
        # Sign
        pygame.draw.rect(self.image, (255, 255, 0), (15, 0, 30, 15))
        
        # Cannabis leaf symbol
        pygame.draw.circle(self.image, (0, 100, 0), (30, 7), 4)
        points = [
            (30, 3), (34, 10), (30, 15), (26, 10),
            (30, 3), (26, 4), (34, 4), (30, 15)
        ]
        for i in range(0, len(points)-1, 2):
            pygame.draw.line(self.image, (0, 100, 0), points[i], points[i+1], 2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hippie Quest: Journey to the Dispensary")
        self.clock = pygame.time.Clock()
        
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.reset_game()
        
        # Touch controls
        self.touch_controls = {
            'left': pygame.Rect(50, SCREEN_HEIGHT - 100, 60, 60),
            'right': pygame.Rect(130, SCREEN_HEIGHT - 100, 60, 60),
            'jump': pygame.Rect(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 100, 60, 60)
        }
        
        self.touch_buttons = {}
        self.keys_pressed = {'left': False, 'right': False, 'jump': False}
        
    def reset_game(self):
        self.player = Player()
        self.platforms = pygame.sprite.Group()
        self.dea_agents = pygame.sprite.Group()
        self.dispensary = None
        
        # Create platforms
        platforms_data = [
            (0, 500, 800, 100),  # Ground
            (100, 400, 200, 20),
            (400, 300, 150, 20),
            (200, 200, 150, 20),
            (600, 350, 150, 20),
            (50, 150, 100, 20),
            (500, 150, 100, 20),
            (700, 250, 100, 20),
        ]
        
        for x, y, w, h in platforms_data:
            platform = Platform(x, y, w, h)
            self.platforms.add(platform)
        
        # Create DEA agents
        agent_positions = [(300, 450), (550, 250), (150, 150), (450, 450)]
        for x, y in agent_positions:
            agent = DEAAgent(x, y)
            self.dea_agents.add(agent)
        
        # Create dispensary at the end
        self.dispensary = WeedDispensary(750, 420)
        
        self.game_over = False
        self.level_complete = False
        self.current_level = 1
        
    def handle_events(self):
        self.keys_pressed = {'left': False, 'right': False, 'jump': False}
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Keyboard events
            elif event.type == KEYDOWN:
                if event.key == K_r and self.game_over:
                    self.reset_game()
                elif event.key == K_SPACE:
                    self.player.jump()
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            # Touch events for mobile
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.touch_controls['left'].collidepoint(mouse_pos):
                    self.keys_pressed['left'] = True
                elif self.touch_controls['right'].collidepoint(mouse_pos):
                    self.keys_pressed['right'] = True
                elif self.touch_controls['jump'].collidepoint(mouse_pos):
                    self.keys_pressed['jump'] = True
            
            elif event.type == MOUSEBUTTONUP:
                # Reset touch buttons
                pass
        
        # Check keyboard state for continuous movement
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or self.keys_pressed['left']:
            self.player.velocity_x = -PLAYER_SPEED
            self.player.direction = -1
        elif keys[K_RIGHT] or self.keys_pressed['right']:
            self.player.velocity_x = PLAYER_SPEED
            self.player.direction = 1
        else:
            self.player.velocity_x = 0
            
        if keys[K_UP] or keys[K_SPACE] or self.keys_pressed['jump']:
            self.player.jump()

    def update(self):
        if not self.game_over and not self.level_complete:
            # Update player
            self.player.update(self.platforms)
            
            # Update DEA agents
            self.dea_agents.update(self.platforms)
            
            # Check collision with DEA agents
            for agent in self.dea_agents:
                if self.player.rect.colliderect(agent.rect):
                    self.player.lives -= 1
                    self.player.rect.center = (100, 400)
                    if self.player.lives <= 0:
                        self.game_over = True
                    break
            
            # Check if reached dispensary
            if self.player.rect.colliderect(self.dispensary.rect):
                self.level_complete = True
                self.player.score += 1000

    def draw_touch_controls(self):
        # Draw touch control buttons
        for key, rect in self.touch_controls.items():
            color = (100, 100, 100, 180)
            if (key == 'left' and self.keys_pressed['left']) or \
               (key == 'right' and self.keys_pressed['right']) or \
               (key == 'jump' and self.keys_pressed['jump']):
                color = (150, 150, 150, 200)
            
            # Semi-transparent surface
            s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(s, color, (0, 0, rect.width, rect.height), 0, 10)
            pygame.draw.rect(s, (50, 50, 50), (0, 0, rect.width, rect.height), 3, 10)
            self.screen.blit(s, rect)
            
            # Draw button labels
            if key == 'left':
                text = self.small_font.render("←", True, (255, 255, 255))
            elif key == 'right':
                text = self.small_font.render("→", True, (255, 255, 255))
            else:
                text = self.small_font.render("↑", True, (255, 255, 255))
            
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    def draw(self):
        # Draw sky background
        self.screen.fill(SKY_BLUE)
        
        # Draw clouds
        for i in range(3):
            x = (pygame.time.get_ticks() // 30 + i * 300) % (SCREEN_WIDTH + 200) - 100
            pygame.draw.ellipse(self.screen, (255, 255, 255), (x, 50 + i * 40, 100, 40))
        
        # Draw platforms
        for platform in self.platforms:
            self.screen.blit(platform.image, platform.rect)
            # Platform edge details
            pygame.draw.rect(self.screen, (101, 67, 33), platform.rect, 2)
        
        # Draw DEA agents
        for agent in self.dea_agents:
            self.screen.blit(agent.image, agent.rect)
        
        # Draw dispensary
        if self.dispensary:
            self.screen.blit(self.dispensary.image, self.dispensary.rect)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw touch controls (for mobile/touch screens)
        self.draw_touch_controls()
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        level_text = self.font.render(f"Level: {self.current_level}", True, (255, 255, 255))
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.screen.blit(level_text, (10, 90))
        
        # Draw instructions
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press R to restart", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(game_over_text, text_rect)
        elif self.level_complete:
            complete_text = self.font.render("LEVEL COMPLETE! You found the dispensary!", True, (0, 255, 0))
            text_rect = complete_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(complete_text, text_rect)
        
        # Draw control hints
        hint_text = self.small_font.render("Arrow Keys to move, Space to jump (Touch controls on mobile)", True, (255, 255, 255))
        self.screen.blit(hint_text, (SCREEN_WIDTH//2 - 250, SCREEN_HEIGHT - 30))

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()