import pygame

class MovingObject:
    def __init__(self, x, y, width, height, color, speed_x, speed_y, path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.path = path  # The path that restricts movement

    def move(self):
        # Get the direction vector from the path
        direction_x, direction_y = self.path.get_direction_vector()

        # Apply the direction to the movement
        self.x += direction_x * self.speed_x
        self.y += direction_y * self.speed_y

        # Check if the object is still within the path
        if not self.path.is_within(self):
            # If out of bounds, reset the position to the path boundaries
            if self.x < self.path.x:
                self.x = self.path.x
            elif self.x + self.width > self.path.x + self.path.width:
                self.x = self.path.x + self.path.width - self.width

            if self.y < self.path.y:
                self.y = self.path.y
            elif self.y + self.height > self.path.y + self.path.height:
                self.y = self.path.y + self.path.height - self.height

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )
