import pandas as pd
from Eclat import Eclat
from PreparingData import PrepareData
import warnings
warnings.filterwarnings('ignore', category=Warning)


df = pd.read_excel("Horizontal_Format.xlsx")
df = PrepareData.is_vertical(df)

min_supp = 0
min_conf = 0.0
number_of_transactions = len(df.explode(df.columns[1])[df.columns[1]].drop_duplicates())

while True:
    try:
        print("\n------------------------- Support --------------------------------")
        print("Do you want to enter numbers or percentages?\n1- number\n2- percentage")
        choice = int(input().strip())
        if choice == 1:
            print("Enter Min Support: ", end='')
            min_supp = int(input().strip())
        elif choice == 2:
            print("Enter Min Support: %", end='')
            min_supp = int((float(input().strip()) / 100) * number_of_transactions)
        else:
            raise Exception()
        if min_supp > number_of_transactions or min_supp < 0:
            print("Enter Valid Support")
            continue
        break
    except:
        print("Enter Valid Number")
        continue

while True:
    try:
        print("\n------------------------- Confidence --------------------------------")
        print("Do you want to enter numbers or percentages?\n1- number\n2- percentage")
        choice = int(input().strip())
        if choice == 1:
            print("Enter Min Confidence: ", end='')
            min_conf = float(input().strip())
        elif choice == 2:
            print("Enter Min Confidence: %", end='')
            min_conf = float(input().strip()) / 100
        else:
            raise Exception()
        break
    except:
        print("Enter Valid Number")
        continue

print("\n------------------------- Inputs --------------------------------")
print(f"Min Support: {min_supp}")
print(f"Min Confidence: {min_conf}")
print(f"Number Of Transactions: {number_of_transactions}")

# Print all frequent itemsets
print("\n------------------------- Frequent Itemsets --------------------------------")
for index, item in enumerate(Eclat.generate_frequent_itemsets(df, min_supp)):
    print(f"Frequent {index + 1}-Itemsets: {item}")

# Print all rules
print("\n------------------------- All Rules --------------------------------")
ret = Eclat.generate_rules(df, int(min_supp), number_of_transactions)
Eclat.print_rules(ret)

# Print strong rules
print("\n------------------------- Strong Rules --------------------------------")
Eclat.print_rules(Eclat.get_strong_rules(ret, min_conf))
