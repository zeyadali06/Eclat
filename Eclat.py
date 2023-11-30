import pandas as pd
# from main import min_conf
# from main import min_conf


class Eclat:

    @staticmethod
    def genarate_frequent_itemsets(df: pd.DataFrame,minsub: float) -> list:
        # df: main dataframe
        # Genarate all frequent itemsets
        # should return list of dataframes each dataframe contain k-frequent itemsets (k = 1,2,3,.....)
        df=df[df['TID'].apply(lambda tid: len(tid) >= minsub)]
        df.reset_index(drop=True, inplace=True)
        freq=[df["items"].tolist()]
        
        c=0
        while True :
            length=len(df)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if c==0:
                        new = pd.DataFrame({'items': [df.iloc[i] ['items']+df.iloc[j] ['items']], 'TID': [set(df.iloc[i] ['TID']).intersection(set(df.iloc[j] ['TID']))]})
                        df = pd.concat([df, new], ignore_index=True)
                    else :
                        if df.iloc[i] ['items'][0:c]==df.iloc[j]['items'][0:c] :
                            new = pd.DataFrame({'items': [df.iloc[i]['items'][0:c]+df.iloc[i]['items'][c:]+df.iloc[j] ['items'][c:]], 'TID':[set(df.iloc[i] ['TID']).intersection(set(df.iloc[j] ['TID']))]})
                            df = pd.concat([df, new], ignore_index=True)

                    
            df=df.drop(range(0,length))
            df.reset_index(drop=True, inplace=True)
            df=df[df['TID'].apply(lambda tid: len(tid) >= minsub)]
            if len(df)==0 :
                break
            freq.append(df["items"].tolist())
            c+=1
            
       
        return freq
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
