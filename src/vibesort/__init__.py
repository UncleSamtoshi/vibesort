from . import ai
from typing import Any


def vibesort(arr: list[int]) -> list[int]:
    return ai.vibesort(arr)


def vibeequals(value1: Any, value2: Any) -> bool:
    """
    Uses AI to determine if two values are semantically/vibrationally equal.
    
    Args:
        value1: First value to compare
        value2: Second value to compare
        
    Returns:
        bool: True if the values are considered equal by AI, False otherwise
    """
    return ai.vibeequals(value1, value2)
