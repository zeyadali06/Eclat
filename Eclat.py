import pandas as pd
from itertools import combinations
from Rules import Rules


class Eclat:

    @staticmethod
    def generate_frequent_itemsets(df: pd.DataFrame, minsub: float) -> list[list[str]]:
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
    def get_strong_rules(allrules: list[Rules], minconf: float) -> list[Rules]:
        """ 
        NOTE: df should be the main dataframe
        """
        # return list containing strong rules

        all = []
        for i in range(len(allrules)):
            if allrules[i].confidnce >= minconf:
                all.append(allrules[i])

        return all

    @staticmethod
    def generate_rules(df: pd.DataFrame, minsup: int, no_transactions: int) -> list[Rules]:
        """ 
        NOTE: df should be the main dataframe
        """
        # return list containing all rules

        freqitems = Eclat.generate_frequent_itemsets(df, minsup)
        rules = []
        for i in range(len(freqitems)):
            if len(freqitems[i][0]) == 1:
                continue
            for j in range(len(freqitems[i])):
                combination = []
                for k in range(1, len(freqitems[i][j])):
                    combination.extend(combinations([item for item in freqitems[i][j]], k))
                for k in range(len(combination)):
                    for l in range(len(combination)):
                        if set(combination[k]).intersection(set(combination[l])) == set() and combination[k] != combination[l]:
                            ret = Rules(df, combination[k], combination[l], no_transactions)
                            rules.append(ret)

        filter = set()
        unique = []
        for obj in rules:
            current = (obj.first, obj.second)
            if current not in filter:
                filter.add(current)
                unique.append(obj)

        return unique

    @staticmethod
    def print_rules(strongrules: list[Rules]) -> None:
        for i in strongrules:
            if i.lift > 1:
                print(f"{''.join(i.first)} -> {''.join(i.second)}, Confidance:{i.confidnce:.3f}, Lift:{i.lift:.3f}, Dependency:yes, Corelation:+ve")
            elif i.lift < 1:
                print(f"{''.join(i.first)} -> {''.join(i.second)}, Confidance:{i.confidnce:.3f}, Lift:{i.lift:.3f}, Dependency:yes, Corelation:-ve")
            else:
                print(f"{''.join(i.first)} -> {''.join(i.second)}, Confidance:{i.confidnce:.3f}, Lift:{i.lift:.3f}, Dependency:no")
