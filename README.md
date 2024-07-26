# Snake Game 🐍

This is a simple Snake Game implemented using the Python `turtle` module. The game involves controlling a snake to eat food and grow in length while avoiding collisions with itself and the screen borders.

## Game Features 🎮

- Control the snake using arrow keys (Up, Down, Left, Right).
- Snake grows in length each time it eats food.
- The game ends if the snake collides with itself.
- Score and highest score are displayed on the screen.
- The game speed increases as the snake eats more food.
- The screen wraps around the edges.

## Installation 💻

1. Ensure you have Python installed on your machine. You can download it from [Python's official website](https://www.python.org/).
2. The game uses the `turtle` module, which comes pre-installed with Python. No additional installations are required.

## Running the Game ▶️

1. Save the game code into a file, for example, `snake_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `snake_game.py` is saved.
4. Run the game by executing the following command:
    ```bash
    python snake_game.py
    ```

## Controls 🎮

- **⬆️ Arrow Up:** Move up
- **⬇️ Arrow Down:** Move down
- **⬅️ Arrow Left:** Move left
- **➡️ Arrow Right:** Move right
- **⎋ Escape:** Exit the game

## Code Overview 📝

### Game Settings ⚙️

- `delay`: Controls the game speed.
- `score` and `highestScore`: Track the current score and highest score.
- `bodies`: List to store the snake body segments.

### Screen Setup 🖥️

The game window is created using the `turtle.Screen()` method. Background color and screen size are set.

### Snake and Food Initialization 🐍🍎

The snake's head is created and customized. Food is created and placed randomly on the screen.

### Scoreboard 📊

The scoreboard displays the current score and the highest score.

### Movement Functions ➡️⬅️⬆️⬇️

Functions to change the snake's direction (`moveup`, `movedown`, `moveleft`, `moveright`). The `move()` function moves the snake in the current direction.

### Event Handling ⌨️

Key mappings to control the snake and exit the game.

### Main Game Loop 🔄

- Updates the screen.
- Checks for collisions with the screen border and food.
- Moves the snake body segments.
- Checks for collisions with the snake body.
- Updates the score and displays messages for game over and new highest score.

## Customization 🎨

Colors, shapes, and other game settings can be customized by modifying the code. 
- To change the background color, update `s.bgcolor("#2c3e50")`.
- To change the snake and food colors, update `head.color("#3498db")`, `head.fillcolor("#2980b9")`, and `food.color("#f39c12")`.
