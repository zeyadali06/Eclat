import pandas as pd


class PreparData:

    @staticmethod
    def is_vertical(df: pd.DataFrame) -> pd.DataFrame:
        # Check if the dataframe is vertical
        if str.lower(df.columns[1])=="items"and str.lower(df.columns[0])=="tid":
            return PreparData.to_vertical(df)
        else :
            df.rename(columns={df.columns[0]: "items"}, inplace=True)
            df.rename(columns={df.columns[1]: "TID"}, inplace=True)
            return df

    @staticmethod
    def to_vertical(df: pd.DataFrame) -> pd.DataFrame:
        # Convert the parametarized horizontal dataframe to vertical dataframe
        newDf=pd.DataFrame(columns=["items","TID"])
        for i in range(len(df)):
            df[df.columns[1]][i] = list(str.split(df.values[i][1], ','))
        for index,row in df.iterrows():
            for item in row[df.columns[1]]:
                if item in newDf["items"]:
                    print("k")
                    print(newDf.iloc[newDf["items"]==item]["items"])
                else:
                    newrow=pd.DataFrame({"items":[item],"TID":[row[df.columns[0]]]})
                    newDf=pd.concat([newDf,newrow], ignore_index=True)

        print(newDf)
        return df
