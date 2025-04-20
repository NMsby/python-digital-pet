# 🐶 Python Digital Pet

A virtual pet simulation built with Python Object-Oriented Programming principles.

## Project Overview
This project implements a digital pet that has various needs (hunger, energy, happiness) and can perform different actions (eat, sleep, play). The implementation uses OOP concepts including classes, attributes, methods, and constructors.

## Features
- Create a digital pet with a custom name
- Track pet's hunger, energy, and happiness levels
- Feed your pet to reduce hunger and increase happiness
- Let your pet sleep to restore energy
- Play with your pet to increase happiness
- Train your pet to learn new tricks
- Interactive command-line interface

## How to Run
1. Ensure you have Python installed on your system: `https://www.python.org/downloads/`
2. Clone this repository
```bash 
  git clone https://github.com/NMsby/python-digital-pet.git
  cd python-digital-pet
```
3. Run the program using:
```bash
  python main.py
```
4. Follow the on-screen prompts to interact with your pet

## Implementation Details

The `Pet` class includes:

### Attributes:
- `name`: The name of your pet
- `hunger`: Integer (0–10) representing hunger level (0 = full, 10 = very hungry)
- `energy`: Integer (0-10) representing energy level (0 = tired, 10 = fully rested)
- `happiness`: Integer (0–10) representing how happy your pet is
- `tricks`: List of tricks your pet has learned

### Methods:
- `eat()`: Reduces hunger by 3 points and increases happiness by 1
- `sleep()`: Increases energy by 5 points
- `play()`: Decreases energy by 2, increases happiness by 2, and increases hunger by 1
- `get_status()`: Displays the current state of the pet
- `train(trick)`: Teaches your pet a new trick
- `show_tricks()`: Displays all the tricks your pet has learned

## Potential Future Enhancements
Here are some ideas for expanding this project in the future:

1. **Multiple Pet Types** - Create different pet classes (Dog, Cat, Rabbit, etc.) that inherit from a base Pet class but have unique behaviors and needs

2. **Time-Based Simulation** - Implement a real-time element where pet needs change over time even when not interacting with them

3. **Graphical User Interface** - Add a visual interface using Pygame, Tkinter, or another Python GUI library to display your pet and its environment

4. **Pet Lifecycle** - Add growth stages (baby, adolescent, adult, senior) that affect behavior and needs

5. **Health System** - Implement a health attribute with potential illnesses that require special care

6. **Save/Load Functionality** - Allow users to save their pet's state to a file and load it later to continue playing

7. **Multiple Pets** - Enable users to have multiple pets that can interact with each other

8. **Weather/Environment** - Add environmental factors that affect your pet's mood and behavior

9. **Toys and Items** - Implement an inventory system with toys and items that have different effects on your pet

10. **Achievement System** - Create milestones and rewards for successful pet care

## Assignment Completion
This project was created as part of the Python OOP Challenge to demonstrate the implementation of Object-Oriented Programming concepts.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.