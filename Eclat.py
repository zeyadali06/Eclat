import pandas as pd
from main import *


class Eclat:

    @staticmethod
    def genarate_frequent_itemsets(df: pd.DataFrame) -> list:
        # df: main dataframe
        # Genarate all frequent itemsets
        # should return list of dataframes each dataframe contain k-frequent itemsets (k = 1,2,3,.....)
        return []

    @staticmethod
    def strong_rules(df: pd.DataFrame) -> list:
        # df: frequent itemset dataframe
        # should return list of class Rules
        return []

    @staticmethod
    def calc_support(df: pd.DataFrame, items: list) -> float:
        # items is a list of items
        # you should calculate the support of items and return it
        # items may contain 1,2,.... items
        return 0

    @staticmethod
    def calc_prob(df: pd.DataFrame, items: list) -> float:
        # items may contain 2 items for P(first U second) or contain 1 item for P(first)
        # calculate the probability of the paramter items
        return Eclat.calc_support(df, items) / len(df)
