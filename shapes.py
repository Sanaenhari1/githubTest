import random
import json
from dataclasses import dataclass

@dataclass
class Shape:
    """Base class for shapes."""
    x: int
    y: int
    size: int
    color: tuple  # RGB format (R, G, B)

    def to_dict(self):
        """Method to be overridden in subclasses."""
        raise NotImplementedError("This method must be implemented in subclasses.")

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, size={self.size}, color={self.color})"


@dataclass
class Circle(Shape):
    """Circle shape."""
    def to_dict(self):
        return {
            "type": "circle",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
        }


@dataclass
class Square(Shape):
    """Square shape."""
    def to_dict(self):
        return {
            "type": "square",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
        }


@dataclass
class Triangle(Shape):
    """Equilateral triangle."""
    def to_dict(self):
        return {
            "type": "triangle",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
        }


def generate_random_shapes(n=40):
    """Generate N random shapes."""
    shape_classes = [Circle, Square, Triangle]  # Possible shape types
    return [
        random.choice(shape_classes)(
            x=random.randint(50, 350),
            y=random.randint(50, 350),
            size=random.randint(30, 70),
            color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ).to_dict()
        for _ in range(n)
    ]


# Test - Display JSON of generated shapes
if __name__ == "__main__":
    print(json.dumps(generate_random_shapes(), indent=4))
