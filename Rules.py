import pandas as pd
from Evaluation import Evaluation


class Rules:
    # # Rules
    # # if first --> second
    # first = []
    # second = []
    # lift = 0.0
    # confidnce = 0.0

    def __init__(self, df: pd.DataFrame, fir: list, sec: list, no_transactions: int) -> None:
        # df: the main dataframe
        self.first = fir
        self.second = sec
        self.lift = self.calc_lift(df, no_transactions)
        self.confidnce = self.calc_conf(df)

    def calc_lift(self, df: pd.DataFrame, no_transactions: int) -> float:
        return Evaluation.calc_prob(df, self.first + self.second, no_transactions) / (Evaluation.calc_prob(df, self.first, no_transactions) * Evaluation.calc_prob(df, self.second, no_transactions))

    def calc_conf(self, df: pd.DataFrame) -> float:
        return Evaluation.calc_support(df, list(set(self.first + self.second))) / Evaluation.calc_support(df, self.first)
