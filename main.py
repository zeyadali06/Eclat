import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=Warning)

df = pd.read_excel("Horizontal_Format (1).xlsx", thousands=',')

# min_supp = 0.0
# min_conf = 0.0

min_supp = 2
min_conf = 0.7

print(df.columns[1])

for i in range(len(df)):
    df[df.columns[1]][i] = list(str.split(df.values[i][1], ','))

print(df)

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
