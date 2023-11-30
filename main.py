import pandas as pd
import warnings
from Eclat import Eclat
warnings.filterwarnings('ignore', category=Warning)

df = pd.read_excel("Horizontal_Format (1).xlsx")

# min_supp = 0.0
# min_conf = 0.0

min_supp = 2
min_conf = 0.7

for i in range(len(df)):
    df[df.columns[1]][i] = list(str.split(df.values[i][1], ','))
# Eclat.genarate_frequent_itemsets(df,min_supp)

print(Eclat.genarate_frequent_itemsets(df,min_supp))

# print(df[df.columns[1]][0][0])

# for i in range(len(df)):
#     print(df[df.columns[1]][i].count('T1'))

# li = [1, 2, 3, 4, 1]
# print(li.count(1))

# df['items'] = df['items'].astype(str)


# print(Eclat.calc_support(df, ['T2','T4']))

# li=["T1", "T2", "T3"]
# print(li[0:1])

# while True:
#     try:
#         print("\n------------------------- Support --------------------------------")
#         print("Do you want to enter numbers or percentages?\n1- number\n2- percentage")
#         choice = int(input().strip())
#         if choice == 1:
#             print("Enter Min Support: ", end='')
#             min_supp = int(input().strip())
#         elif choice == 2:
#             print("Enter Min Support: %", end='')
#             min_supp = (float(input().strip()) / 100) * len(df)
#         else:
#             raise Exception()
#         break
#     except:
#         print("Enter Valid Number")
#         continue

# while True:
#     try:
#         print("\n------------------------- Support --------------------------------")
#         print("Do you want to enter numbers or percentages?\n1- number\n2- percentage")
#         choice = int(input().strip())
#         if choice == 1:
#             print("Enter Min Support: ", end='')
#             min_supp = int(input().strip())
#         elif choice == 2:
#             print("Enter Min Support: %", end='')
#             min_supp = (float(input().strip()) / 100) * len(df)
#         else:
#             raise Exception()
#         break
#     except:
#         print("Enter Valid Number")
#         continue

# while True:
#     try:
#         print("\n------------------------- Confidence --------------------------------")
#         print("Do you want to enter numbers or percentages?\n1- number\n2- percentage")
#         choice = int(input().strip())
#         if choice == 1:
#             print("Enter Min Confidence: ", end='')
#             min_conf = int(input().strip())
#         elif choice == 2:
#             print("Enter Min Confidence: %", end='')
#             min_conf = (float(input().strip()) / 100)
#         else:
#             raise Exception()
#         break
#     except:
#         print("Enter Valid Number")
#         continue
