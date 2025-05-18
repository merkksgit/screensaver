# Bouncing Image Screensaver

A simple Python screensaver that displays an image bouncing around the screen in fullscreen mode.

## Description

This screensaver loads an image of your choice and displays it bouncing around the screen with realistic physics.

## Features

- Fullscreen display
- Realistic bouncing physics
- Random initial position and direction
- Smooth animation with controlled frame rate
- Simple keyboard controls to exit

## Requirements

- Python 3.x
- Pygame 2.5.2
- Numpy 1.26.0
- Pillow 10.1.0

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the screensaver, you need to specify the path to the image you want to display:

1. Open `screensaver.py` in a text editor
2. Locate the following line in the `__init__` method:
   ```python
   self.image_path = "/home/user/path/to/imagefile"
   ```
3. Replace the path with the path to your image file

## Usage

Run the screensaver with the following command:

```bash
python screensaver.py
```

To exit the screensaver, press the `ESC` key or `Q` key.

## Customization

You can modify the following parameters in the `screensaver.py` file:

- `self.speed`: Change the base movement speed of the image
- `self.fps`: Adjust the frame rate
- `self.background_color`: Change the background color (RGB tuple)
  - Located in the `__init__` method: `self.background_color = (36, 40, 59)`
  - Modify these values to create your desired color (values range from 0-255)

## License

MIT
