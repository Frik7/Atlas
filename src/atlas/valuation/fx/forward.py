import numpy as np


class FxForwardPricer:
    def __init__(
        self, ccy_base: str, ccy_quote: str, spot: float, strike: float, maturity: float
    ):
        self.ccy_base = ccy_base
        self.ccy_quote = ccy_quote
        self.spot = spot
        self.strike = strike
        self.maturity = maturity

    def price(self) -> float:
        return self.spot * (1 - np.exp(-self.rate * self.time))
