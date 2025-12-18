"""
Hippie Quest: Journey to the Dispensary
A platformer game with cross-platform support.
Main game file: Hippie_quest.py
"""

import pygame
import random
import sys
from pygame.locals import *

# ============================================================================
# INITIALIZATION AND CONSTANTS
# ============================================================================

# Initialize all pygame modules
pygame.init()

# Game Constants
SCREEN_WIDTH = 800          # Game window width in pixels
SCREEN_HEIGHT = 600         # Game window height in pixels
FPS = 60                    # Frames per second (controls game speed)
GRAVITY = 0.5               # Acceleration due to gravity (pixels/frame^2)
JUMP_STRENGTH = -12         # Initial upward velocity when jumping
PLAYER_SPEED = 5            # Horizontal movement speed

# Color Definitions (RGB tuples)
SKY_BLUE = (135, 206, 235)      # Background sky color
GREEN = (76, 175, 80)           # General green color
BROWN = (139, 69, 19)           # Platform/wood color
BLUE_JEANS = (25, 25, 112)      # Player's jeans color
PEACE_SYMBOL = (255, 255, 255)  # White for peace symbol
DEA_RED = (220, 20, 60)         # DEA agent suit color
DISPENSARY_GREEN = (0, 150, 0)  # Dispensary building color

# Hippie hoodie colors (randomly selected at game start)
HOODIE_COLORS = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0)     # Yellow
]


# ============================================================================
# PLAYER CHARACTER CLASS
# ============================================================================

class Player(pygame.sprite.Sprite):
    """
    Represents the main player character - a Hippie trying to reach the dispensary.
    Handles movement, drawing, and collision detection for the player.
    """
    
    def __init__(self):
        """Initialize player with default attributes and position."""
        super().__init__()
        
        # Create player surface (transparent background)
        self.image = pygame.Surface((40, 60), pygame.SRCALPHA)
        
        # Randomly select hoodie color from available options
        self.hoodie_color = random.choice(HOODIE_COLORS)
        
        # Draw the initial sprite
        self.update_sprite()
        
        # Set up collision rectangle and starting position
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)  # Starting position
        
        # Movement attributes
        self.velocity_y = 0    # Vertical velocity (for jumping/falling)
        self.velocity_x = 0    # Horizontal velocity
        self.on_ground = False # Whether player is touching a platform
        self.direction = 1     # 1 = facing right, -1 = facing left
        
        # Game state attributes
        self.score = 0         # Player's current score
        self.lives = 3         # Number of lives remaining
    
    def update_sprite(self):
        """
        Draws the player character sprite with all visual details.
        Called whenever the player's appearance needs to be updated.
        """
        # Clear the surface with transparency
        self.image.fill((0, 0, 0, 0))
        
        # Draw hoodie (upper body)
        pygame.draw.rect(self.image, self.hoodie_color, (0, 0, 40, 40))
        
        # Draw jeans (lower body) with holes
        pygame.draw.rect(self.image, BLUE_JEANS, (0, 40, 40, 20))
        
        # Add holes in jeans (circles showing skin/sky through)
        for hole in [(5, 45), (30, 50), (20, 55)]:
            pygame.draw.circle(self.image, SKY_BLUE, hole, 3)
        
        # Draw head (circle)
        pygame.draw.circle(self.image, (255, 218, 185), (20, 15), 10)
        
        # Draw peace symbol necklace
        pygame.draw.circle(self.image, PEACE_SYMBOL, (20, 35), 4)
        # Draw peace symbol lines (vertical and horizontal)
        pygame.draw.line(self.image, PEACE_SYMBOL, (20, 33), (20, 37), 2)
        pygame.draw.line(self.image, PEACE_SYMBOL, (17, 35), (23, 35), 2)
        
        # Draw eyes
        pygame.draw.circle(self.image, (0, 0, 0), (16, 13), 2)
        pygame.draw.circle(self.image, (0, 0, 0), (24, 13), 2)
        
        # Draw long hair
        pygame.draw.rect(self.image, (139, 69, 19), (5, 5, 30, 10))
    
    def update(self, platforms):
        """
        Update player position and handle collisions.
        
        Args:
            platforms: Sprite group containing all platform objects
        """
        # Apply gravity to vertical velocity
        self.velocity_y += GRAVITY
        
        # Update position based on velocity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Prevent player from moving outside screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y = 0  # Stop upward movement at top
        
        # Reset ground state and check for platform collisions
        self.on_ground = False
        
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Collision from above (landing on platform)
                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                # Collision from below (hitting head)
                elif self.velocity_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
    
    def jump(self):
        """Make the player jump if currently on the ground."""
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH
    
    def draw(self, screen):
        """
        Draw the player sprite to the screen, flipped based on direction.
        
        Args:
            screen: Pygame surface to draw onto
        """
        if self.direction == -1:  # Facing left
            # Flip sprite horizontally
            flipped_sprite = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped_sprite, self.rect)
        else:  # Facing right
            screen.blit(self.image, self.rect)


# ============================================================================
# DEA AGENT CLASS (ENEMY)
# ============================================================================

class DEAAgent(pygame.sprite.Sprite):
    """
    Represents DEA agents that patrol the platforms.
    These are enemies the player must avoid.
    """
    
    def __init__(self, x, y):
        """
        Initialize a DEA agent at specified position.
        
        Args:
            x: Starting x-coordinate
            y: Starting y-coordinate
        """
        super().__init__()
        
        # Create agent surface
        self.image = pygame.Surface((35, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # Movement attributes
        self.direction = random.choice([-1, 1])  # Start moving left or right
        self.speed = random.randint(2, 4)        # Random speed between 2-4
        
        # Draw the initial sprite
        self.update_sprite()
    
    def update_sprite(self):
        """Draw the DEA agent sprite with all details."""
        # Fill with DEA red color
        self.image.fill(DEA_RED)
        
        # Draw tie
        pygame.draw.rect(self.image, (0, 0, 0), (16, 25, 3, 15))
        
        # Draw badge
        pygame.draw.circle(self.image, (255, 215, 0), (18, 20), 6)
        pygame.draw.rect(self.image, (255, 215, 0), (15, 18, 6, 4))
        
        # Draw head
        pygame.draw.circle(self.image, (255, 218, 185), (18, 10), 8)
        
        # Draw sunglasses
        pygame.draw.rect(self.image, (0, 0, 0), (11, 8, 6, 3))
        pygame.draw.rect(self.image, (0, 0, 0), (19, 8, 6, 3))
        pygame.draw.rect(self.image, (100, 100, 100), (17, 8, 2, 3))
    
    def update(self, platforms):
        """
        Update agent position and handle platform edge detection.
        
        Args:
            platforms: Sprite group containing all platform objects
        """
        # Move in current direction
        self.rect.x += self.direction * self.speed
        
        # Check if agent is about to walk off a platform
        future_rect = self.rect.copy()
        future_rect.y += 2  # Check slightly below current position
        future_rect.x += self.direction * self.speed  # Check in movement direction
        
        # Determine if agent is still on a platform
        on_platform = False
        for platform in platforms:
            if future_rect.colliderect(platform.rect):
                on_platform = True
                break
        
        # Reverse direction if at edge or screen boundary
        if not on_platform or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
            self.rect.x += self.direction * self.speed  # Move back


# ============================================================================
# PLATFORM CLASS
# ============================================================================

class Platform(pygame.sprite.Sprite):
    """
    Represents platforms that players can walk and jump on.
    """
    
    def __init__(self, x, y, width, height, color=None):
        """
        Initialize a platform.
        
        Args:
            x: X-coordinate of top-left corner
            y: Y-coordinate of top-left corner
            width: Platform width in pixels
            height: Platform height in pixels
            color: Optional custom color (defaults to BROWN)
        """
        super().__init__()
        
        # Create platform surface
        self.image = pygame.Surface((width, height))
        self.color = color or BROWN  # Use custom color or default brown
        self.image.fill(self.color)
        
        # Set position
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


# ============================================================================
# WEED DISPENSARY CLASS (GOAL)
# ============================================================================

class WeedDispensary(pygame.sprite.Sprite):
    """
    Represents the goal object - the weed dispensary the player must reach.
    """
    
    def __init__(self, x, y):
        """
        Initialize dispensary at specified position.
        
        Args:
            x: X-coordinate for center
            y: Y-coordinate for center
        """
        super().__init__()
        
        # Create dispensary surface
        self.image = pygame.Surface((60, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # Draw the initial sprite
        self.update_sprite()
    
    def update_sprite(self):
        """Draw the dispensary sprite with all details."""
        # Fill with dispensary green
        self.image.fill(DISPENSARY_GREEN)
        
        # Draw wooden door
        pygame.draw.rect(self.image, (139, 69, 19), (20, 40, 20, 40))
        
        # Draw windows
        pygame.draw.rect(self.image, (135, 206, 235), (10, 20, 15, 15))
        pygame.draw.rect(self.image, (135, 206, 235), (35, 20, 15, 15))
        
        # Draw sign
        pygame.draw.rect(self.image, (255, 255, 0), (15, 0, 30, 15))
        
        # Draw cannabis leaf symbol
        pygame.draw.circle(self.image, (0, 100, 0), (30, 7), 4)
        
        # Define leaf shape points
        points = [
            (30, 3), (34, 10), (30, 15), (26, 10),
            (30, 3), (26, 4), (34, 4), (30, 15)
        ]
        
        # Draw leaf lines
        for i in range(0, len(points)-1, 2):
            pygame.draw.line(self.image, (0, 100, 0), points[i], points[i+1], 2)


# ============================================================================
# MAIN GAME CLASS
# ============================================================================

class Game:
    """
    Main game controller class.
    Manages game state, events, and rendering.
    """
    
    def __init__(self):
        """Initialize game window, fonts, and game objects."""
        # Create game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hippie Quest: Journey to the Dispensary")
        
        # Initialize game clock for FPS control
        self.clock = pygame.time.Clock()
        
        # Load fonts for UI text
        self.font = pygame.font.Font(None, 36)      # Main font
        self.small_font = pygame.font.Font(None, 24)  # Smaller font
        
        # Set up touch control areas for mobile devices
        self.touch_controls = {
            'left': pygame.Rect(50, SCREEN_HEIGHT - 100, 60, 60),
            'right': pygame.Rect(130, SCREEN_HEIGHT - 100, 60, 60),
            'jump': pygame.Rect(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 100, 60, 60)
        }
        
        # Track pressed keys/touch buttons
        self.keys_pressed = {'left': False, 'right': False, 'jump': False}
        
        # Initialize game state
        self.reset_game()
    
    def reset_game(self):
        """
        Reset all game objects to their initial state.
        Called at game start and after game over.
        """
        # Create player character
        self.player = Player()
        
        # Create sprite groups
        self.platforms = pygame.sprite.Group()
        self.dea_agents = pygame.sprite.Group()
        self.dispensary = None
        
        # Define platform positions and sizes (x, y, width, height)
        platforms_data = [
            (0, 500, 800, 100),   # Ground platform
            (100, 400, 200, 20),  # Platform 1
            (400, 300, 150, 20),  # Platform 2
            (200, 200, 150, 20),  # Platform 3
            (600, 350, 150, 20),  # Platform 4
            (50, 150, 100, 20),   # Platform 5
            (500, 150, 100, 20),  # Platform 6
            (700, 250, 100, 20),  # Platform 7
        ]
        
        # Create platform objects from data
        for x, y, w, h in platforms_data:
            platform = Platform(x, y, w, h)
            self.platforms.add(platform)
        
        # Define DEA agent starting positions
        agent_positions = [(300, 450), (550, 250), (150, 150), (450, 450)]
        
        # Create DEA agent objects
        for x, y in agent_positions:
            agent = DEAAgent(x, y)
            self.dea_agents.add(agent)
        
        # Create the dispensary (goal object)
        self.dispensary = WeedDispensary(750, 420)
        
        # Reset game state variables
        self.game_over = False
        self.level_complete = False
        self.current_level = 1
    
    def handle_events(self):
        """
        Process all game events (keyboard, mouse, touch, window).
        Updates player controls based on input.
        """
        # Reset pressed keys for this frame
        self.keys_pressed = {'left': False, 'right': False, 'jump': False}
        
        # Process all events in the queue
        for event in pygame.event.get():
            # Window close event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Keyboard key press events
            elif event.type == KEYDOWN:
                # Restart game when R is pressed (if game over)
                if event.key == K_r and self.game_over:
                    self.reset_game()
                # Jump when space is pressed
                elif event.key == K_SPACE:
                    self.player.jump()
                # Quit game when escape is pressed
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            # Mouse/touch press events (for mobile controls)
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Check which touch button was pressed
                if self.touch_controls['left'].collidepoint(mouse_pos):
                    self.keys_pressed['left'] = True
                elif self.touch_controls['right'].collidepoint(mouse_pos):
                    self.keys_pressed['right'] = True
                elif self.touch_controls['jump'].collidepoint(mouse_pos):
                    self.keys_pressed['jump'] = True
        
        # Check for continuous key presses (for smooth movement)
        keys = pygame.key.get_pressed()
        
        # Handle left movement
        if keys[K_LEFT] or self.keys_pressed['left']:
            self.player.velocity_x = -PLAYER_SPEED
            self.player.direction = -1
        
        # Handle right movement
        elif keys[K_RIGHT] or self.keys_pressed['right']:
            self.player.velocity_x = PLAYER_SPEED
            self.player.direction = 1
        
        # Stop horizontal movement if no keys pressed
        else:
            self.player.velocity_x = 0
        
        # Handle jump input
        if keys[K_UP] or keys[K_SPACE] or self.keys_pressed['jump']:
            self.player.jump()
    
    def update(self):
        """
        Update game state for current frame.
        Handles player movement, collisions, and game logic.
        """
        # Only update if game is still active
        if not self.game_over and not self.level_complete:
            # Update player position and check platform collisions
            self.player.update(self.platforms)
            
            # Update DEA agent positions
            self.dea_agents.update(self.platforms)
            
            # Check for collisions with DEA agents
            for agent in self.dea_agents:
                if self.player.rect.colliderect(agent.rect):
                    # Player hit by DEA agent
                    self.player.lives -= 1
                    # Reset player position
                    self.player.rect.center = (100, 400)
                    
                    # Check if game is over
                    if self.player.lives <= 0:
                        self.game_over = True
                    break
            
            # Check if player reached the dispensary
            if self.player.rect.colliderect(self.dispensary.rect):
                self.level_complete = True
                self.player.score += 1000  # Bonus points
    
    def draw_touch_controls(self):
        """Draw touch control buttons for mobile devices."""
        for key, rect in self.touch_controls.items():
            # Determine button color based on pressed state
            color = (100, 100, 100, 180)  # Default gray with transparency
            
            # Highlight button if currently pressed
            if (key == 'left' and self.keys_pressed['left']) or \
               (key == 'right' and self.keys_pressed['right']) or \
               (key == 'jump' and self.keys_pressed['jump']):
                color = (150, 150, 150, 200)  # Lighter when pressed
            
            # Create semi-transparent surface for button
            button_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            
            # Draw rounded rectangle for button
            pygame.draw.rect(button_surface, color, (0, 0, rect.width, rect.height), 0, 10)
            pygame.draw.rect(button_surface, (50, 50, 50), (0, 0, rect.width, rect.height), 3, 10)
            
            # Draw button onto screen
            self.screen.blit(button_surface, rect)
            
            # Draw button label/icon
            if key == 'left':
                text = self.small_font.render("←", True, (255, 255, 255))
            elif key == 'right':
                text = self.small_font.render("→", True, (255, 255, 255))
            else:  # jump button
                text = self.small_font.render("↑", True, (255, 255, 255))
            
            # Center text on button
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)
    
    def draw(self):
        """
        Draw all game objects to the screen.
        Called once per frame.
        """
        # Draw sky background
        self.screen.fill(SKY_BLUE)
        
        # Draw animated clouds
        for i in range(3):
            # Calculate cloud position with slow scrolling
            x = (pygame.time.get_ticks() // 30 + i * 300) % (SCREEN_WIDTH + 200) - 100
            pygame.draw.ellipse(self.screen, (255, 255, 255), (x, 50 + i * 40, 100, 40))
        
        # Draw all platforms
        for platform in self.platforms:
            self.screen.blit(platform.image, platform.rect)
            # Add border to platforms for visual detail
            pygame.draw.rect(self.screen, (101, 67, 33), platform.rect, 2)
        
        # Draw all DEA agents
        for agent in self.dea_agents:
            self.screen.blit(agent.image, agent.rect)
        
        # Draw dispensary (goal)
        if self.dispensary:
            self.screen.blit(self.dispensary.image, self.dispensary.rect)
        
        # Draw player character
        self.player.draw(self.screen)
        
        # Draw touch controls (visible on all platforms)
        self.draw_touch_controls()
        
        # Draw UI elements (score, lives, level)
        score_text = self.font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        level_text = self.font.render(f"Level: {self.current_level}", True, (255, 255, 255))
        
        # Position UI elements in top-left corner
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.screen.blit(level_text, (10, 90))
        
        # Draw game state messages
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press R to restart", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(game_over_text, text_rect)
        elif self.level_complete:
            complete_text = self.font.render("LEVEL COMPLETE! You found the dispensary!", True, (0, 255, 0))
            text_rect = complete_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(complete_text, text_rect)
        
        # Draw control instructions
        hint_text = self.small_font.render(
            "Arrow Keys to move, Space to jump (Touch controls on mobile)",
            True, (255, 255, 255)
        )
        self.screen.blit(hint_text, (SCREEN_WIDTH//2 - 250, SCREEN_HEIGHT - 30))
    
    def run(self):
        """
        Main game loop.
        Runs continuously until the game is closed.
        """
        while True:
            # Process input events
            self.handle_events()
            
            # Update game state
            self.update()
            
            # Draw everything
            self.draw()
            
            # Update display
            pygame.display.flip()
            
            # Control game speed
            self.clock.tick(FPS)


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    Game entry point.
    Creates a Game instance and starts the game loop.
    """
    # Create and run the game
    game = Game()
    game.run()