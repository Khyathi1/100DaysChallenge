print("Hello, Welcome to Love Pizza Delivery Section")
size = input("Select the size of your pizza [S, M, L] : ").upper()
p = input("Do you want pepperoni on your pizza? Y / N : ").upper()
ec = input("Do you want extra cheese? Y / N : ").upper()
s = {'S':15,'M':20,'L':25}
pe = {'Y':{'S':2,'M':3,'L':3},'N':{'S':0,'M':0,'L':0}}
ch=1
total = int(s[size]+pe[p][size]+(ch if ec == 'Y' else 0))
print('Alright! Here is your total :$ '+str(total))
