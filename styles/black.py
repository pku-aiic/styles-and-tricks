from typing import Any

# case 1 - line length
x = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
]

# case 2 - trailing comma
y = [1, 2, 3]


# case 3 - function with too many args
def f1(
    my_fancy_arg1: Any,
    my_fancy_arg2: Any,
    my_fancy_arg3: Any,
    my_fancy_arg4: Any,
    my_fancy_arg5: Any,
    my_fancy_arg6: Any,
    my_fancy_arg7: Any,
    my_fancy_arg8: Any,
) -> None:
    pass


def this_is_a_very_long_function_name(
    my_fancy_arg1: Any, my_fancy_arg2: Any, my_fancy_arg3: Any
) -> None:
    pass
