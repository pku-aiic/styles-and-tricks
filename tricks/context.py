from typing import Any


class graceful_context:
    def __enter__(self) -> None:
        print("Nice to meet you!")

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        print("Hope to see you soon!")


if __name__ == "__main__":
    import time

    with graceful_context():
        time.sleep(1)
