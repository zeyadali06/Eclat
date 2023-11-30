import pandas as pd
# from main import min_conf
# from main import min_conf


class Eclat:

    @staticmethod
    def genarate_frequent_itemsets(df: pd.DataFrame, minsub: float) -> pd.DataFrame:
        """ 
        NOTE: df should be the main dataframe
        """
        # Genarate all frequent itemsets
        # should return list of dataframes each dataframe contain k-frequent itemsets (k = 1,2,3,.....)
        df = df[df['TID'].apply(lambda tid: len(tid) >= minsub)]
        freq = df
        c = 0
        while True:
            length = len(df)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if c == 0:
                        new = pd.DataFrame({'items': [df.iloc[i]['items']+df.iloc[j]['items']],
                                            'TID': [set(df.iloc[i]['TID']).intersection(set(df.iloc[j]['TID']))]})
                        df = pd.concat([df, new], ignore_index=True)
                    else:
                        if df.iloc[i]['items'][0:c] == df.iloc[j]['items'][0:c]:
                            new = pd.DataFrame({'items': [df.iloc[i]['items'][0:c]+df.iloc[i]['items'][c:]+df.iloc[j]['items'][c:]],
                                                'TID': [set(df.iloc[i]['TID']).intersection(set(df.iloc[j]['TID']))]})
                            df = pd.concat([df, new], ignore_index=True)

            df = df.drop(range(0, length))
            df.reset_index(drop=True, inplace=True)
            df = df[df['TID'].apply(lambda tid: len(tid) >= minsub)]
            if len(df) == 0:
                break
            freq = pd.concat([freq, df], ignore_index=True)
            c += 1

        return freq

    @staticmethod
    def strong_rules(df: pd.DataFrame) -> list:
        # df: frequent itemset dataframe
        # should return list of class Rules
        return []

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

        li = []
        intersecte = set({})

        for i in range(len(checker)):
            if i == 0:
                intersecte.update(
                    set(checker[i]).intersection(set(checker[i + 1])))
                continue
            intersecte = set(intersecte).intersection(checker[i])

        return len(intersecte)

    @staticmethod
    def calc_prob(df: pd.DataFrame, items: list) -> float:
        # items may contain 2 items for P(first U second) or contain 1 item for P(first)
        # calculate the probability of the paramter items
        return Eclat.calc_support(df, items) / len(df)
