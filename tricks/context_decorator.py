import torch

from typing import Any
from contextlib import ContextDecorator
from torch.nn import Linear


in_dim = 10
out_dim = 12
batch_size = 128
linear = Linear(in_dim, out_dim, bias=False)


class NotRequiresGrad(ContextDecorator):
    def __init__(self, module: Linear):
        self.linear = module

    def __enter__(self) -> None:
        self.linear.weight.requires_grad_(False)

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.linear.weight.requires_grad_(True)


def echo_requires_grad() -> None:
    print("requires_grad", any(param.requires_grad for param in linear.parameters()))


@NotRequiresGrad(linear)
def inference(net: torch.Tensor) -> torch.Tensor:
    echo_requires_grad()
    return linear(net)


if __name__ == "__main__":
    echo_requires_grad()
    inference(torch.randn(batch_size, in_dim))
    echo_requires_grad()
    with NotRequiresGrad(linear):
        echo_requires_grad()
    echo_requires_grad()
