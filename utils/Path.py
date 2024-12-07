import pygame

class Path:
    def __init__(self, x, y, width, height, direction):
        """
        Initialize a Path object.

        :param x: The x-coordinate of the road
        :param y: The y-coordinate of the road
        :param width: The width of the road
        :param height: The height of the road
        :param direction: The direction of movement ('left', 'right', 'up', 'down')
        """
        self.x = x  # The x-coordinate of the road
        self.y = y  # The y-coordinate of the road
        self.width = width  # The width of the road
        self.height = height  # The height of the road
        self.direction = direction  # The direction of movement ('left', 'right', 'up', 'down')

    def is_within(self, obj):
        """Check if the object is within the road (path) boundaries."""
        return (
            self.x <= obj.x <= self.x + self.width - obj.width and
            self.y <= obj.y <= self.y + self.height - obj.height
        )

    def get_direction_vector(self):
        """Returns the movement direction as a vector."""
        if self.direction == 'right':
            return (1, 0)
        elif self.direction == 'left':
            return (-1, 0)
        elif self.direction == 'down':
            return (0, 1)
        elif self.direction == 'up':
            return (0, -1)
        else:
            return (0, 0)

    def draw(self, surface):
        """Draw the path (road) on the screen."""
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, self.width, self.height))
