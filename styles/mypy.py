# case 1 - missing typing
def case_1(**kwargs: str) -> None:
    print(kwargs)


# case 2 - re-assignment
def case_2() -> None:
    a = "Hello!"
    print(a)


# case 3 - wrong typing
def case_3(x: int) -> None:
    print(x)


case_3(1)
