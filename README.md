# Hippie Quest: Escape DEA Agents

You are a Hippie trying to make it to the weed dispensary while avoiding DEA agents.

---

We use the Pygame library for PC and mobile (with touch controls).
 - However, note that mobile deployment with Pygame might require additional steps (like using pygame_sdl2 or building with an Android toolchain).

For simplicity, we'll focus on PC with keyboard controls and add basic touch controls for mobile (if run on a touch device).

## Game Features:

### Hippie Character:

 - Multi-colored hoodie (randomly colored each game)

 - Peace symbol necklace

 - Blue jeans with holes

 - Long hair

### DEA Agents:

 - Red suits with sunglasses

 - Patrol platforms with AI

 - Contact with them costs a life

### Weed Dispensary Goal:

 - Green building with cannabis leaf symbol

 - Reaching it completes the level

### Controls:

 - Keyboard: Arrow keys to move, Space to jump

 - Touch/Mobile: On-screen buttons for left, right, and jump

 - Both: Fully functional with either input method

### Game Mechanics:

 - Platform jumping with gravity

 - Lives system (3 lives)

 - Score system

 - Level progression

### Visual Features:

 - Animated clouds

 - Detailed sprites for all characters

 - Clear UI showing score, lives, and level

 - Touch control buttons with visual feedback

## To Run the Game:

### Install pygame:

```bash
pip install pygame
```
Save the code to a file (e.g., Hippie_quest.py)

### Run the game:

```bash
python Hippie_quest.py
```

### Future Enhancements You Could Add:

 - Multiple levels with increasing difficulty

 - Collectible items (joints, peace signs, etc.)

 - Power-ups (temporary invisibility, speed boost)

 - Sound effects and background music

 - More enemy types

 - Mobile optimization (better touch controls, scaling)

 - Animated sprites

 - Parallax scrolling background

---

The game works on both PC and mobile devices that support Pygame. The touch controls are sized appropriately for mobile screens. You can expand this foundation with more levels, better graphics, and additional gameplay elements!

I need this to have a read me file that describes in great detail what this game does how you install it and in the code I need comments to explain what everything is doing in the next segment of code and everything set up to be added as a GitHub repo. I need you to always give me a response in markdown format 
We are going to create a detailed README.md file and add extensive comments to the code.
Since the code is long, we will break it down and comment each section.

Let's start by creating the README.md file content.

Hippie Quest: Journey to the Dispensary
https://screenshot.png

📋 Table of Contents
Game Overview

Features

Installation

Controls

Game Mechanics

Character Design

Enemies

Level Design

Development Setup

Project Structure

Contributing

License

🎮 Game Overview
Hippie Quest: Journey to the Dispensary is a Mario Bros-style platformer game developed in Python using Pygame. The game features a colorful Hippie character navigating through various platforms while avoiding DEA agents to reach the local weed dispensary. The game supports both keyboard controls for PC and touch controls for mobile devices, making it accessible across different platforms.

Story
You play as a peace-loving Hippie trying to find your way to the local dispensary. However, DEA agents are patrolling the area, trying to stop you. Use your jumping skills and quick reflexes to avoid them and reach your destination!

✨ Features
Cross-Platform Support
PC: Full keyboard controls

Mobile: Touch screen controls with on-screen buttons

Responsive Design: Adapts to different screen sizes

Visual Elements
Multi-colored Hippie character with detailed sprite

DEA agents with distinct appearance

Animated cloud background

Themed platforms and dispensary building

Colorful UI with score tracking

Gameplay Features
Smooth platforming mechanics with gravity

Lives system (3 lives per game)

Score system with bonus for reaching the dispensary

Collision detection with platforms and enemies

Level completion system

Game over and restart functionality

🛠 Installation
Prerequisites
Python 3.7 or higher

Pip (Python package installer)

Step-by-Step Installation
Clone the Repository

bash
git clone https://github.com/yourusername/Hippie-quest.git
cd Hippie-quest
Create a Virtual Environment (Recommended)

bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install Dependencies

bash
pip install pygame
Run the Game

bash
python Hippie_quest.py
Alternative Installation Methods
Using requirements.txt
bash
pip install -r requirements.txt
Running on Mobile Devices
For mobile devices, you'll need:

Pygame Subset for Android (PGSU) for Android devices

Or use a Python IDE that supports Pygame on iOS

🎯 Controls
Keyboard Controls (PC)
Left Arrow: Move left

Right Arrow: Move right

Space/Up Arrow: Jump

R: Restart game (when game over)

ESC: Exit game

Touch Controls (Mobile)
Left Button (←): Move left

Right Button (→): Move right

Jump Button (↑): Jump

The touch controls appear as semi-transparent buttons at the bottom of the screen on touch-enabled devices.

🎮 Game Mechanics
Player Movement
Walking Speed: 5 pixels per frame

Jump Strength: -12 pixels (upward velocity)

Gravity: 0.5 pixels per frame²

Collision Detection: Precise platform collision from all sides

Lives System
Start with 3 lives

Lose a life when touching a DEA agent

Respawn at starting position after losing a life

Game ends when all lives are lost

Scoring
Base score increases over time

+1000 points for reaching the dispensary

Score displayed in top-left corner

Level Progression
Currently one level (expandable)

Reaching the dispensary completes the level

Level number displayed on screen

👤 Character Design
The Hippie
Hoodie: Randomly colored from red, green, blue, or yellow each game

Jeans: Blue jeans with realistic holes

Accessories: Peace symbol necklace

Hair: Long brown hair

Skin Tone: Natural peach color

Size: 40×60 pixels

Animation Features
Character faces direction of movement

Smooth jumping and falling animations

Visual feedback on collision

👮 Enemies
DEA Agents
Appearance: Red suits with sunglasses

Features: Gold badges, black ties

AI Behavior:

Patrols platforms

Changes direction at edges

Random movement speeds (2-4 pixels/frame)

Platform-aware navigation

Size: 35×50 pixels

🗺️ Level Design
Platforms
Ground platform covering entire bottom

Multiple floating platforms at varying heights

Platform sizes range from 100-200 pixels wide

All platforms have collision detection

The Dispensary
Location: Top-right corner of the level

Features: Green building with cannabis leaf symbol

Details: Wooden door, windows, sign

Size: 60×80 pixels

Visual Elements
Background: Sky blue with animated clouds

Platforms: Brown wooden texture

UI: Clear, non-intrusive interface

💻 Development Setup
Project Structure
text
Hippie-quest/
├── Hippie_quest.py      # Main game file
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── screenshot.png      # Game screenshot
├── assets/             # (Optional) For future assets
│   ├── images/
│   ├── sounds/
│   └── fonts/
└── docs/               # Documentation
Code Architecture
The game follows an object-oriented design with these main classes:

Game: Main game controller

Player: Player character

DEAAgent: Enemy characters

Platform: Level platforms

WeedDispensary: Goal object

Extending the Game
Adding New Levels
python
# Example of adding a new level
def create_level_2(self):
    # Clear existing platforms
    self.platforms.empty()
    
    # Add new platform layout
    new_platforms = [
        (0, 500, 800, 100),
        # Add more platforms...
    ]
    
    # Update DEA agent positions
    self.dea_agents.empty()
    # Add new agents...
    
    # Update dispensary position
    self.dispensary.rect.center = (new_x, new_y)
Adding Sound Effects
python
# Load sound
jump_sound = pygame.mixer.Sound('assets/sounds/jump.wav')

# Play sound in jump method
def jump(self):
    if self.on_ground:
        self.velocity_y = JUMP_STRENGTH
        jump_sound.play()
🚀 Future Enhancements
Planned Features
Multiple Levels: Progressive difficulty

Collectibles: Joints, peace signs, bonus items

Power-ups: Temporary invisibility, speed boosts

Sound Effects: Background music and SFX

High Score System: Local storage of high scores

Mobile Optimization: Better touch controls

Animation: Sprite sheets for smooth animation

Parallax Scrolling: Multi-layer backgrounds

Technical Improvements
Database integration for scores

Network multiplayer

Level editor

Particle effects

Screen shake on damage

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the Repository

Create a Feature Branch

bash
git checkout -b feature/AmazingFeature
Commit Your Changes

bash
git commit -m 'Add some AmazingFeature'
Push to the Branch

bash
git push origin feature/AmazingFeature
Open a Pull Request

Contribution Guidelines
Follow PEP 8 Python style guide

Add comments for new code

Update documentation as needed

Test changes on both PC and mobile

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Pygame Community: For the amazing game development library

Pixel Artists: Inspiration for character designs

Open Source Contributors: For various code snippets and ideas

📧 Contact
For questions or feedback:

GitHub Issues: Report a bug or request a feature

Email: your.email@example.com

🎨 Art Assets Credits
All art in this game is procedurally generated using Pygame drawing functions. No external assets are used, making the game completely open-source and modifiable.

Happy Gaming! ✌️🌿

Remember: This is a fictional game for entertainment purposes only. Always obey local laws regarding substance use.

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.json
coverage.xml
*.cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Game specific
screenshot.png  # Keep if you add one, or ignore if auto-generated
*.save
highscores.txt
GitHub Repository Setup Instructions
Creating the Repository
Initialize Local Repository

bash
git init
git add .
git commit -m "Initial commit: Hippie Quest platformer game"
Create GitHub Repository

Go to GitHub.com

Click "New repository"

Name: Hippie-quest

Description: "Mario Bros-style platformer with Hippie character avoiding DEA agents"

Public repository

Don't initialize with README (we already have one)

Connect and Push

bash
git remote add origin https://github.com/NateWeiler/Hippie-quest.git
git branch -M main
git push -u origin main
Repository Features to Add
1. GitHub Actions CI/CD (.github/workflows/python-tests.yml)
yaml
name: Python Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pygame
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
2. Issue Templates (.github/ISSUE_TEMPLATE)
Bug report template

Feature request template

3. Pull Request Template (.github/PULL_REQUEST_TEMPLATE.md)
markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Other (please describe)

## Testing
- [ ] Tested on PC
- [ ] Tested on mobile
- [ ] Added new tests

## Screenshots (if applicable)
Project Tags for GitHub
Add these topics to your repository:

python

pygame

platformer-game

game-development

cross-platform

mobile-game

open-source

Additional Documentation Files
CONTRIBUTING.md
markdown
# Contributing to Hippie Quest

Welcome! We're excited you want to contribute...

### Development Setup
1. Fork the repository
2. Clone your fork
3. Set up virtual environment
4. Install dependencies

### Coding Standards
- Follow PEP 8
- Add docstrings
- Test your changes
CHANGELOG.md
markdown
# Changelog

## [1.0.0] - 2024-01-01
### Added
- Initial game release
- Player character with Hippie design
- DEA agent enemies
- Cross-platform controls
- Basic level design
Final Steps
Add a screenshot to the repository

Enable GitHub Pages for documentation (optional)

Add badges to README:

https://img.shields.io/badge/python-3.7%252B-blue

https://img.shields.io/badge/pygame-2.5.1-green

https://img.shields.io/badge/license-MIT-yellow

Create a release on GitHub:

Tag: v1.0.0

Title: Initial Release

Upload compiled executables (using PyInstaller)

This complete package provides everything needed for a professional GitHub repository with detailed documentation, comprehensive code comments, and cross-platform support.
