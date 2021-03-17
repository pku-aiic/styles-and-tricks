from typing import Dict
from typing import Type
from typing import Callable

model_dict: Dict[str, Type["MyFancyModelBase"]] = {}


class MyFancyModelBase:
    def __init__(self) -> None:
        print(f"my fancy model : {type(self).__name__}")

    @classmethod
    def register(cls, name: str) -> Callable[[Type], Type]:
        def _core(cls_: Type) -> Type:
            global model_dict
            model_dict[name] = cls_
            return cls_

        return _core


@MyFancyModelBase.register("yeah")
class YeahModel(MyFancyModelBase):
    pass


if __name__ == "__main__":
    model_dict["yeah"]()
-
