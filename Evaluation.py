import pandas as pd


class Evaluation:

    @staticmethod
    def calc_prob(df: pd.DataFrame, items: list) -> float:
        # items may contain 2 items for P(first U second) or contain 1 item for P(first)
        # calculate the probability of the paramter items
        return Evaluation.calc_support(df, items) / len(df.explode(df.columns[1])[df.columns[1]].drop_duplicates())

    @staticmethod
    def calc_support(df: pd.DataFrame, items: list) -> int:
        """ 
        NOTE: df should be the main dataframe
        """
        # items is a list of items
        # you should calculate the support of items and return it
        # items may contain 1,2,.... items

        if len(items) == 1:
            for i in range(len(df)):
                if (df[df.columns[0]][i] == items[0]):
                    return len(df[df.columns[1]][i])

        checker = []
        for i in range(len(df)):
            for j in items:
                if (df[df.columns[0]][i] == j):
                    checker.append(set(df[df.columns[1]][i]))

        intersecte = set({})
        for i in range(len(checker)):
            if i == 0:
                intersecte.update(
                    set(checker[i]).intersection(set(checker[i + 1])))
                continue
            intersecte = set(intersecte).intersection(checker[i])

        return len(intersecte)
