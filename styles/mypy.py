from typing import Any

# case 1 - missing typing
def case_1(**kwargs: Any) -> None:
    print(kwargs)


# case 2 - re-assignment
def case_2() -> None:
    a = 0
    aa = "Hello!"
    print(aa)


# case 3 - wrong typing
def case_3(x: float) -> None:
    print(x)


case_3(1.0)
