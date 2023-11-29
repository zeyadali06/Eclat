import pandas as pd
# from main import min_conf
# from main import min_conf


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
    def calc_support(df: pd.DataFrame, items: list) -> int:
        # items is a list of items
        # you should calculate the support of items and return it
        # items may contain 1,2,.... items
        supp = 0
        for i in range(len(df)):
            counter = 0
            for j in items:
                if df[df.columns[1]][i].count(j) > 0:
                    counter += 1

            if counter >= len(items):
                supp += 1

        return supp

    @staticmethod
    def calc_prob(df: pd.DataFrame, items: list) -> float:
        # items may contain 2 items for P(first U second) or contain 1 item for P(first)
        # calculate the probability of the paramter items
        return Eclat.calc_support(df, items) / len(df)
