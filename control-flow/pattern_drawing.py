size = int(input("Enter the Size of the pattern: "))
row = 0
while row  <= size: 
    for col in range( size ):
         print("*", end="")
    print()
    row = row + 1

