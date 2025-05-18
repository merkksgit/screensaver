#!/usr/bin/env python3
"""
Bouncing Image Screensaver - Displays a bouncing image in fullscreen mode.
"""
import os
import random
import sys

import pygame

# Import specific pygame constants instead of using wildcard imports
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_q


class BouncingScreensaver:
    """
    A screensaver that displays an image bouncing around the screen.
    """

    def __init__(self):
        # Path to your image file
        self.image_path = "/home/merkks/projects/screensaver/images/logo-text-link.png"
        # Check if image exists before initializing pygame
        if not os.path.exists(self.image_path):
            print("Error: Image file not found!")
            print(
                "Please specify a valid image path by editing this line in the script:"
            )
            print(f'    self.image_path = "{self.image_path}"')
            sys.exit(1)
        # Initialize pygame
        pygame.init()
        # Set up the display (fullscreen)
        self.screen_info = pygame.display.Info()
        self.width, self.height = self.screen_info.current_w, self.screen_info.current_h
        self.screen = pygame.display.set_mode(
            (self.width, self.height), pygame.FULLSCREEN
        )
        pygame.display.set_caption("Bouncing Image Screensaver")
        # Set up image
        self.load_image()
        # Initial position and velocity
        self.x = random.randint(0, self.width - self.image_width)
        self.y = random.randint(0, self.height - self.image_height)
        self.speed = 3  # Base speed (pixels per frame)
        self.x_vel = self.speed if random.random() > 0.5 else -self.speed
        self.y_vel = self.speed if random.random() > 0.5 else -self.speed
        # Set up clock for controlling FPS
        self.clock = pygame.time.Clock()
        self.fps = 60
        # Set up background
        self.background_color = (36, 40, 59)

    def load_image(self):
        """
        Load and optionally scale the image to be displayed.
        """
        # Load the image
        self.image = pygame.image.load(self.image_path).convert_alpha()
        # Get image dimensions
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        # Scale the image if it's too large
        # max_size = min(self.width, self.height) // 4
        # if self.image_width > max_size or self.image_height > max_size:
        #     scale = max_size / max(self.image_width, self.image_height)
        #     new_width = int(self.image_width * scale)
        #     new_height = int(self.image_height * scale)
        #     self.image = pygame.transform.scale(self.image, (new_width, new_height))
        #     self.image_width, self.image_height = new_width, new_height

    def update_position(self):
        """
        Update the position of the image and handle bouncing off screen edges.
        """
        # Update the position
        self.x += self.x_vel
        self.y += self.y_vel
        # Check for collision with screen edges
        if self.x <= 0 or self.x + self.image_width >= self.width:
            # Bounce off the left/right edge with slight random variation
            self.x_vel = -self.x_vel * random.uniform(0.9, 1.1)
            if self.x <= 0:
                self.x = 0
            else:
                self.x = self.width - self.image_width
        if self.y <= 0 or self.y + self.image_height >= self.height:
            # Bounce off the top/bottom edge with slight random variation
            self.y_vel = -self.y_vel * random.uniform(0.9, 1.1)
            # Make sure we're not stuck in the edge
            if self.y <= 0:
                self.y = 0
            else:
                self.y = self.height - self.image_height
        # Limit the maximum velocity
        max_vel = 8
        self.x_vel = max(min(self.x_vel, max_vel), -max_vel)
        self.y_vel = max(min(self.y_vel, max_vel), -max_vel)

    def run(self):
        """
        Main loop for the screensaver.
        """
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == QUIT or (
                    event.type == KEYDOWN and event.key in (K_ESCAPE, K_q)
                ):
                    running = False
            # Update position
            self.update_position()
            # Clear the screen
            self.screen.fill(self.background_color)
            # Draw the image at the new position
            self.screen.blit(self.image, (int(self.x), int(self.y)))
            # Update the display
            pygame.display.flip()
            # Cap the frame rate
            self.clock.tick(self.fps)
        # Clean up
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    screensaver = BouncingScreensaver()
    screensaver.run()
