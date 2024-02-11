# Task 02- Print the table of 2 by using the command print()
# 2*1 = 2 to 2*10 = 20

table = int(input("Enter your number for table you want: "))
print ("The table of:", table)
for count in range(1, 11):
    print (table, '*', count, '=', table*count)