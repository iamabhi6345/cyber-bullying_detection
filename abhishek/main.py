import black
import numpy
import pytest


def add_two_integers(a: int, b: int) -> int:
    return a + b


def add_two_floats(a: float, b: float) -> float:
    return a + b


def concatenate_two_strings(a: str, b: str) -> str:
    return a + b


def main() -> None:
    print(add_two_integers(1, 2))
    print(add_two_floats(1.0, 2.0))
    print(concatenate_two_strings("Hello", "World"))

    # Now, let's use a wrong type while calling these functions to see some mypy errors:
    # The following lines are intentional errors for mypy checks, so they should be commented out in production code
    # print(add_two_integers(1.0, 2.0))  # Argument of type "float" cannot be assigned to parameter "a" of type "int"
    # print(add_two_floats("1", "2"))    # Argument of type "Literal['1']" cannot be assigned to parameter "a" of type "float"
    # print(concatenate_two_strings(1, 2))  # Argument of type "Literal[1]" cannot be assigned to parameter "a" of type "str"


if __name__ == "__main__":
    main()
    
