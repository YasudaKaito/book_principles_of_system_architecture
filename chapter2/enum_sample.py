import enum
from abc import ABC, abstractmethod
from typing import Literal


class Fee(ABC):
    @abstractmethod
    def yen(self) -> int:
        ...

    @abstractmethod
    def label(self) -> str:
        ...


class AdultFee(Fee):
    def yen(self):
        return 100

    def label(self):
        return "大人"


class ChildFee(Fee):
    def yen(self):
        return 50

    def label(self):
        return "子供"


class SeniorFee(Fee):
    def yen(self):
        return 60

    def label(self):
        return "シニア"


class FeeType(enum.Enum):
    ADULT = AdultFee()
    CHILD = ChildFee()
    SENIOR = SeniorFee()

    def yen(self) -> int:
        return self.value.yen()

    def label(self) -> str:
        return self.value.label()


def fee_for(fee_type_name: Literal["ADULT", "CHILD", "SENIOR"]) -> int:
    fee_type = FeeType[fee_type_name]
    return fee_type.value.yen()


if __name__ == "__main__":
    result = fee_for("ADULT")
    print(f"料金: {result} 円")
