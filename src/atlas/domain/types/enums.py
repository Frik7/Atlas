from enum import Enum, unique


@unique
class Currency(str, Enum):
    """Currency codes."""

    USD = "USD"
    ZAR = "ZAR"


@unique
class Side(str, Enum):
    """Transaction side (BUY or SELL)."""

    BUY = "BUY"
    SELL = "SELL"


@unique
class OptionType(str, Enum):
    """Standard Option types."""

    CALL = "CALL"
    PUT = "PUT"


@unique
class LongShort(str, Enum):
    """Direction of the trade exposure."""

    LONG = "LONG"
    SHORT = "SHORT"
