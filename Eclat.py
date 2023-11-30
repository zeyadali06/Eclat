import pandas as pd
from itertools import combinations
from Rules import Rules


class Eclat:

    @staticmethod
    def genarate_frequent_itemsets(df: pd.DataFrame, minsub: float) -> list[list[str]]:
        """ 
        NOTE: df should be the main dataframe
        """
        # Genarate all frequent itemsets
        # should return list of dataframes each dataframe contain k-frequent itemsets (k = 1,2,3,.....)
        df = df[df['TID'].apply(lambda tid: len(tid) >= minsub)]
        df.reset_index(drop=True, inplace=True)
        freq = [df["items"].tolist()]

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
            freq.append(df["items"].tolist())
            c += 1

        return freq

    @staticmethod
    def get_strong_rules(df: pd.DataFrame, minsup: int, minconf: float) -> list[Rules]:
        """ 
        NOTE: df should be the main dataframe
        """
        # return list containing strong rules

        allrules = Eclat.generate_rules(df, minsup, minconf)
        for i in allrules:
            if i.confidnce < minconf:
                allrules.remove(i)
        return allrules

    @staticmethod
    def generate_rules(df: pd.DataFrame, minsup: int, minconf: float) -> list[Rules]:
        """ 
        NOTE: df should be the main dataframe
        """
        # return list containing all rules

        freqitems = Eclat.genarate_frequent_itemsets(df, minsup)
        strongrules = []
        for i in range(len(freqitems)):
            if len(freqitems[i][0]) == 1:
                continue
            for j in range(len(freqitems[i])):
                combination = []
                for k in range(1, len(freqitems[i][j])):
                    combination.extend(combinations(
                        [item for item in freqitems[i][j]], k))

                for k in range(len(combination)):
                    for l in range(len(combination)):
                        if set(combination[k]).intersection(set(combination[l])) == set() and combination[k] != combination[l]:
                            ret = Rules(df, combination[k], combination[l])
                            strongrules.append(ret)

        return strongrules

    @staticmethod
    def print_rules(strongrules: list[Rules]) -> None:
        for i in strongrules:
            print(f"{''.join(i.first)} -> {''.join(i.second)}, confidance:{i.confidnce:.3f}, lift:{i.lift:.3f}")
