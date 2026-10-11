"""Small example module used by the GitHub Actions build/test experiment."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divide a by b, raising ValueError for a zero divisor."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b
