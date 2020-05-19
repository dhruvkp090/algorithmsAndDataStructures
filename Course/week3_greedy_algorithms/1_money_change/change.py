# Uses python3
import sys

def get_change(m):
    numberOfCoins = 0
    while m > 0:
        if m  >= 10:
            numberOfCoins += m // 10 #Number of 10rs coins
            m = m%10 #Remaining m value
        elif m  >= 5:
            numberOfCoins += m // 5  #Number of 5rs coins
            m = m%5 #Remaining m value
        else:
            numberOfCoins += m
            m = 0 #Remaining m value

    return numberOfCoins



if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
