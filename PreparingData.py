import pandas as pd


class PrepareData:

    @staticmethod
    def is_vertical(df: pd.DataFrame) -> pd.DataFrame:
        for i in range(len(df)):
            df[df.columns[1]][i] = list(str.split(df.values[i][1], ','))
        # Check if the dataframe is vertical
        if str.lower(df.columns[1]) == "items" and str.lower(df.columns[0]) == "tid":
            return PrepareData.to_vertical(df)
        else:
            df.rename(columns={df.columns[0]: "items"}, inplace=True)
            df.rename(columns={df.columns[1]: "TID"}, inplace=True)
            return df

    @staticmethod
    def to_vertical(df: pd.DataFrame) -> pd.DataFrame:
        # Convert the parametarized horizontal dataframe to vertical dataframe
        newDf = pd.DataFrame(columns=["items", "TID"])
        filter = set()
        for index, row in df.iterrows():
            for item in row[df.columns[1]]:
                if item in filter:
                    currTid = newDf.loc[newDf['items'] == item, 'TID'].tolist()[0]
                    if row[df.columns[0]] not in currTid:
                        newDf.loc[newDf['items'] == item, 'TID'] = [currTid + [row[df.columns[0]]]]
                else:
                    newrow = pd.DataFrame({"items": [item], "TID": [[row[df.columns[0]]]]})
                    newDf = pd.concat([newDf, newrow], ignore_index=True)
                    filter.add(item)
        return newDf
