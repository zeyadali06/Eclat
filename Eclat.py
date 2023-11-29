import pandas as pd


class Eclat:

    @staticmethod
    def genarate_frequent_itemsets(df: pd.DataFrame,minsub: float) -> list:
        # df: main dataframe
        # Genarate all frequent itemsets
        # should return list of dataframes each dataframe contain k-frequent itemsets (k = 1,2,3,.....)
        df=df[df['TID'].apply(lambda tid: len(tid) >= minsub)]
        freq=df
        c=0
        while True :
            length=len(df)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if c==0:
                        print(df.loc[i, 'items'])
                        new = pd.DataFrame({'items': [df.loc[i, 'items']+df.loc[j, 'items']], 'TID': [set(df.loc[i, 'TID']).intersection(set(df.loc[j, 'TID']))]})
                        df = pd.concat([df, new], ignore_index=True)
                    else :
                        if df.loc[i, 'items'][0:c]==df.loc[j, 'items'][0:c] :
                            new = pd.DataFrame({'items': [df.loc[i, 'items'][0:c]+df.loc[i, 'items'][c:]+df.loc[j, 'items'][c:]], 'TID': [set(df.loc[i, 'TID']).intersection(set(df.loc[j, 'TID']))]})
                            df = pd.concat([df, new], ignore_index=True)

                    
            df=df.drop(range(0,length))
            df.reset_index(drop=True, inplace=True)
            df=df[df['TID'].apply(lambda tid: len(tid) >= minsub)]
            if len(df)==0 :
                break
            freq=pd.concat([freq,df], ignore_index=True)
            c+=1
            
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
