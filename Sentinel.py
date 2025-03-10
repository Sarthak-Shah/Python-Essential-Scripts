# Sentinel value example

# our special value to terminate user input
SENTINEL = -99

# asking for a number.
n = int(input("Enter Number to find out its double !, -99 to quit ==>> "))

# test for the sentinel
while(n!=SENTINEL):
    # process the input
    print(n**2)
    # get the next input
    n = int(input("Enter Number to find out its double ! ==>> "))

# continue once they have entered the sentinel
print("Good bye!")
    
