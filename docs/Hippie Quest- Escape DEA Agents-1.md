# Hippie Quest: Journey to the Dispensary

---

### 🎮 Game Overview

Hippie Quest: Journey to the Dispensary is a Mario Bros-style platformer game developed in Python using Pygame. The game features a colorful hippie character navigating through various platforms while avoiding DEA agents to reach the local weed dispensary. The game supports both keyboard controls for PC and touch controls for mobile devices, making it accessible across different platforms.

### Story
You play as a peace-loving hippie trying to find your way to the local dispensary. However, DEA agents are patrolling the area, trying to stop you. Use your jumping skills and quick reflexes to avoid them and reach your destination!

---

## ✨ Features
Cross-Platform Support

PC: Full keyboard controls with arrow keys and spacebar

Mobile: Touch screen controls with on-screen buttons

Responsive Design: Adapts to different screen sizes

---

## Visual Elements

Multi-colored hippie character with detailed sprite

DEA agents with distinct appearance (red suits, sunglasses)

Animated cloud background that scrolls continuously

Themed platforms and dispensary building

Colorful UI with score tracking and lives display

Touch control buttons with visual feedback

---

## Gameplay Features

Smooth platforming mechanics with realistic gravity

Lives system (3 lives per game)

Score system with +1000 point bonus for reaching the dispensary

Precise collision detection with platforms and enemies

Level completion system

Game over and restart functionality

Randomized enemy movement patterns

---

## 🛠 Installation

#### Prerequisites

 - Python 3.7 or higher

 - Pip (Python package installer)

---

## Step-by-Step Installation

 - Clone the Repository

```bash
git clone https://github.com/yourusername/hippie-quest.git
cd hippie-quest
```

---

## Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### Install Dependencies

```bash
pip install pygame
```

---

## Run the Game

```bash
python hippie_quest.py
```

---

## Project Structure

```text
hippie-quest/
├── hippie_quest.py      # Main game file
├── requirements.txt     # Python dependencies (pygame==2.5.1)
├── README.md           # This documentation file
├── screenshot.png      # Game screenshot (to be added)
├── .gitignore          # Git ignore file
├── CONTRIBUTING.md     # Contribution guidelines (optional)
└── CHANGELOG.md        # Version history (optional)
```
---

## 🎯 Controls

#### Keyboard Controls (PC)

← Left Arrow: Move left

→ Right Arrow: Move right

Space / ↑ Up Arrow: Jump

R: Restart game (when game over)

ESC: Exit game

#### Touch Controls (Mobile)

Left Button (←): Move left (bottom-left corner)

Right Button (→): Move right (bottom-left corner)

Jump Button (↑): Jump (bottom-right corner)

The touch controls appear as semi-transparent rounded buttons at the bottom of the screen. They provide visual feedback by changing color when pressed.

---

## 🎮 Game Mechanics

#### Player Movement Physics

Walking Speed: 5 pixels per frame

Jump Strength: -12 pixels (initial upward velocity)

Gravity: 0.5 pixels per frame² (acceleration)

Max Fall Speed: Limited by screen boundaries

---

## Collision System

Platform Collision: Precise detection from all sides

Top Collision: Lands on platform, stops falling

Bottom Collision: Hits head, stops jumping

Side Collision: Pushed away from platform edges

Enemy Collision: Loses a life and respawns

---

## Lives and Scoring System

Starting Lives: 3

Life Loss: Contact with any DEA agent

Respawn Point: (100, 400) coordinates

Score Bonus: +1000 points for reaching dispensary

Game Over: When lives reach 0

---

## Enemy AI Behavior

Patrol Pattern: Moves left and right on platforms

Edge Detection: Reverses direction at platform edges

Random Speeds: 2-4 pixels per frame variation

Screen Boundaries: Reverses at screen edges

---

## 👤 Character Design

#### The Hippie Player

Hoodie: Randomly colored each game (red, green, blue, or yellow)

Jeans: Blue jeans with 3 visible holes showing sky/skin

Accessories: White peace symbol necklace

Hair: Long brown hair flowing from hood

Face: Peach-colored with simple black eyes

Size: 40×60 pixels

Direction: Sprite flips based on movement direction

---

## Visual Details

Hoodie: Covers upper body (40×40 pixels)

Jeans: Lower body with procedurally drawn holes

Necklace: Circular peace symbol with cross design

Head: Simple circle with centered features

Hair: Rectangular brown shape above head

---

## 👮 DEA Agents (Enemies)

#### Appearance

Suit: Bright red (DEA_RED: 220, 20, 60)

Head: Peach-colored circle

Sunglasses: Black rectangles with gray bridge

Badge: Gold circular badge on chest

Tie: Black vertical rectangle

Size: 35×50 pixels

---

## Behavior Patterns

Movement: Continuous left-right patrolling

Intelligence: Platform-aware edge detection

Speed Variation: Each agent has unique speed (2-4)

Starting Direction: Random (left or right)

Patrol Range: Limited to platform surfaces

---

## 🗺️ Level Design

#### Platform Layout

Ground Platform: Full width at bottom (800×100)

Platform 1: Medium height, left side (200×20)

Platform 2: Medium height, center-right (150×20)

Platform 3: High platform, left-center (150×20)

Platform 4: Medium-low, far right (150×20)

Platform 5: High, far left (100×20)

Platform 6: High, center (100×20)

Platform 7: Medium, top-right (100×20)

---

## Strategic Placement

Dispensary: Top-right corner (750, 420)

Player Start: Bottom-left (100, 400)

DEA Agents: Strategically placed to guard paths

Platform Gaps: Require precise jumping

Safe Zones: Areas without enemy patrols

---

## Visual Environment

Sky: Light blue gradient background

Clouds: 3 animated white ellipses scrolling left

Platform Texture: Brown with dark brown borders

Depth Cues: Higher platforms are visually identical

---

## 🏬 The Dispensary (Goal)

#### Building Design

Main Structure: Green rectangle (60×80)

Door: Brown wooden door (20×40)

Windows: 2 sky blue rectangles (15×15 each)

Sign: Yellow rectangle with cannabis leaf

Leaf Symbol: Green circle with leaf lines

---

## Symbolism

Color Scheme: Green for natural/herbal theme

Leaf Design: Stylized cannabis leaf with 4 points

Architecture: Simple building with clear entrance

Visibility: Placed prominently in level

---

## 💻 Technical Architecture

#### Class Structure

Game: Main controller class

Manages game loop and state

Handles input events

Coordinates all game objects

---

## Player: Playable character

Manages movement and physics

Handles sprite drawing and flipping

Tracks score and lives

---

## DEA Agent: Enemy class

Implements patrol AI

Handles platform edge detection

Manages visual appearance

---

## Platform: Level geometry

Simple collision rectangles

Consistent visual style

WeedDispensary: Goal object

End point detection

Themed visual design

---

## Game Loop Structure

```text
Initialize Game
↓
Main Loop:
├─ Handle Events (keyboard/touch)
├─ Update Game State
│  ├─ Player movement
│  ├─ Enemy AI
│  ├─ Collision detection
│  └─ Game state checks
├─ Render Frame
│  ├─ Background
│  ├─ Game objects
│  ├─ UI elements
│  └─ Touch controls
└─ Display Update (60 FPS)
Cross-Platform Implementation
Keyboard Input Handling
```

```python
# Continuous key state checking
keys = pygame.key.get_pressed()
if keys[K_LEFT]: move_left()
if keys[K_RIGHT]: move_right()
if keys[K_SPACE]: jump()
```

---

## Touch Input Handling

```python
# Touch area detection
if touch_controls['left'].collidepoint(mouse_pos):
    move_left()
# Visual button feedback
draw_rounded_button(rect, pressed_color if pressed else default_color)
```

---

## Responsive Design

Screen Size: Fixed 800×600 (scalable)

Button Placement: Bottom corners for thumb access

UI Positioning: Adaptive to screen dimensions

Font Sizes: Relative to screen height

---

## 🚀 Running the Game

On Windows

```bash
# Install Python from python.org
# Open Command Prompt
cd path\to\hippie-quest
python hippie_quest.py
```
On macOS

```bash
# Python usually pre-installed
# Open Terminal
cd ~/Downloads/hippie-quest
python3 hippie_quest.py
```
On Linux

```bash
# Install pygame via package manager if needed
sudo apt-get install python3-pygame
cd ~/hippie-quest
python3 hippie_quest.py
```

---

## On Mobile Devices

#### Android:

Use Pydroid 3 app from Play Store

Install pygame via pip in app

Load and run hippie_quest.py

#### iOS:

Use Pythonista or similar IDE

Pygame support may be limited

Consider web port for better compatibility

---

## 🔧 Customization Options

Easy Modifications

Change Player Colors
```python
# In Player class __init__:
HOODIE_COLORS = [
    (255, 100, 100),  # Light red
    (100, 255, 100),  # Light green
    (100, 100, 255),  # Light blue
]

---

## Adjust Game Difficulty
python
# At top of file:
PLAYER_SPEED = 6      # Faster movement
GRAVITY = 0.3         # Lower gravity
DEA_AGENT_SPEEDS = (1, 3)  # Slower enemies
PLAYER_LIVES = 5      # More lives
Add New Platforms
python
# In reset_game() method:
platforms_data.append((x, y, width, height))
Advanced Customization
Add Sound Effects
python
# Load sounds
jump_sound = pygame.mixer.Sound('jump.wav')
hit_sound = pygame.mixer.Sound('hit.wav')

# Play in appropriate methods
def jump(self):
    if self.on_ground:
        self.velocity_y = JUMP_STRENGTH
        jump_sound.play()
Add Multiple Levels
python
def load_level(self, level_number):
    if level_number == 1:
        platforms = level1_platforms
        agents = level1_agents
    elif level_number == 2:
        platforms = level2_platforms
        agents = level2_agents
🐛 Troubleshooting
Common Issues
"ModuleNotFoundError: No module named 'pygame'"

bash
pip install --upgrade pip
pip install pygame
Game runs too fast/slow

Adjust FPS constant at top of file

Check monitor refresh rate

Ensure no background processes interfering

Touch controls not working

Verify mouse emulation on touch devices

Check button collision areas

Ensure touch events are being registered

Performance issues

Reduce number of agents

Simplify sprite drawing

Lower FPS to 30

Debug Mode
Add debug visualization by uncommenting:

python
# Draw collision rectangles
pygame.draw.rect(screen, (255,0,0), player.rect, 1)
for agent in dea_agents:
    pygame.draw.rect(screen, (0,255,0), agent.rect, 1)
📈 Future Development Roadmap
Phase 1: Core Enhancements
Multiple Levels (3-5 progressive levels)

Sound System (SFX and background music)

Main Menu with options screen

Pause Functionality

Phase 2: Gameplay Expansion
Collectibles (joints, peace signs, bonus items)

Power-ups (temporary speed, invisibility, double jump)

Different Enemy Types (flying agents, snipers)

Boss Battles (DEA captain at level ends)

Phase 3: Polish & Release
Animated Sprites (walking, jumping animations)

Particle Effects (jump dust, collision sparks)

High Score System with local storage

Settings Menu (volume, controls customization)

Phase 4: Advanced Features
Level Editor for community content

Online Leaderboards

Achievement System

Mobile App Packaging (APK, iOS app)

🤝 Contributing Guidelines
Code Standards
PEP 8 Compliance: Use Black or autopep8 formatter

Docstrings: All functions and classes documented

Type Hints: Python 3.7+ type annotations

Commit Messages: Conventional commits format

Pull Request Process
Fork the repository

Create feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open Pull Request

Testing Requirements
Test on both PC (keyboard) and mobile (touch)

Verify no regression in existing features

Update documentation as needed

Add comments for complex logic

📊 Performance Considerations
Optimization Tips
Sprite Groups: Use pygame.sprite.Group for efficient rendering

Surface Caching: Pre-render static elements

Dirty Rectangles: Only update changed screen areas

Image Formats: Use convert() for faster blitting

Memory Management
Reuse surfaces where possible

Clear unused references

Monitor Python garbage collection

Consider texture atlases for mobile

🌐 Cross-Platform Considerations
Screen Sizes
Design for 16:9 aspect ratio

Consider dynamic scaling for different resolutions

Test on common mobile resolutions (1080x1920, etc.)

Input Methods
Support keyboard, mouse, touch, and gamepad

Provide input method detection

Allow control customization

Performance Variance
Account for different CPU/GPU capabilities

Provide graphics quality settings

Implement frame skipping for slow devices

📚 Learning Resources
PyGame Tutorials
Pygame Official Documentation

KidsCanCode Pygame Tutorials

TechWithTim PyGame Platformer

Game Design Principles
Mario level design philosophy

Platformer physics and controls

Difficulty curve design

Player feedback systems

Python Best Practices
Object-oriented design patterns

Game loop architecture

Event-driven programming

Performance optimization

📄 License Information
This project is licensed under the MIT License - see the LICENSE file for details.

Permissions:

Commercial use

Modification

Distribution

Private use

Conditions:

License and copyright notice preservation

Limitations:

No liability

No warranty

🙏 Acknowledgments
Pygame Community: For the incredible open-source game library

Pixel Art Inspiration: Various indie game artists

Testers: All who provided feedback on controls and gameplay

Open Source Contributors: Whose code snippets and ideas helped shape this project

📧 Support and Contact
Issue Reporting
Check existing issues on GitHub

Use issue templates for bugs/features

Include system information and steps to reproduce

Community
GitHub Discussions: For questions and ideas

Discord Server: Real-time chat (if created)

Twitter Updates: Development progress

Developer Contact
GitHub: @yourusername

Email: your.email@example.com

Portfolio: yourportfolio.com

Final Note: This game is a work of fiction created for entertainment and educational purposes. It demonstrates game development concepts using Python and Pygame. Always respect local laws and regulations regarding substance use in your area.

Enjoy the game, and happy coding! ✌️🌿🎮
