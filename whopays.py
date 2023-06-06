import random
names_string = input("Enter everyone's names seperated by a comma. ")
names = names_string.split(", ")
bill_payer = len(names)
#the range of items we want is between 0 and bill_payer minus 1, which is the last index i think
bill_payer = random.randint(0, bill_payer - 1)
unlucky_person = names[bill_payer]
print(f"{unlucky_person} is paying the bill!")