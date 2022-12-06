"""
make a funtion to count coins required to pay that parsed value to funtion.
Quarter = 25 cents
Dime = 10 cents
Nickel = 5 cents
Penny = 1 cent
"""

"""
This solution works but it's not reasonably distributing coins from cash register.
To give 75 as change, it's not wise to give 3 quarters. It should give 2 q, 2 d, 1 nickel instead.

think about runtime for each approach. (time complexity)
"""
# runtime is number of coins for this algorithm. Which is 4. so it's constant.
def num_coins(cents):
    coins = [25, 10, 5, 1]
    if cents < 1:
        return 0
    num_of_coins = 0
    for coin in coins:
        print("current coin ==> ", coin)
        num_of_coins += cents // coin
        print("updated number of coins ==> ", num_of_coins)
        cents = cents % coin
        print("remaining cents ==> ", cents)
        if cents == 0:
            break
    return num_of_coins

# print(num_coins(75))

# runtime is order of n for this algorithm.
def min_coins_dynamic_programming(cents):
    num_of_coins = [0] * (cents + 1)
    print(num_of_coins)
    num_of_coins[0] = 0
    coins = [25, 10, 1]
    for i in range(1, cents + 1):
        temp = cents + 1
        print(i, temp, "==> i, temp")
        for j in coins:
            coins_j = i // j
            print(j, coins_j, "j and coins_j")
            if coins_j != 0:
                temp = min(temp, coins_j + num_of_coins[cents - coins_j * j])
        num_of_coins[i] = temp
    return num_of_coins[cents]


print(min_coins_dynamic_programming(70))