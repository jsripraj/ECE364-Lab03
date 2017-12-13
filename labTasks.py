import sys
import math

def getTotal(accounts):
    sums = []
    for account in accounts:
        account = account.split()
        sum = 0.00
        for transaction in account[2:]:
            transaction = float(transaction[1:])
            sum = round(sum + transaction, 2)
        sums.append(sum)
    return sums

def getDoublePalindromes():
    DPs = []
    for num in range(10, 1000000):
        digits = list(str(num))
        fwd = digits[:]
        digits.reverse()
        if fwd == digits:
            biNum = getBinary(num)
            digits = list(str(biNum))
            fwd = digits[:]
            digits.reverse()
            if fwd == digits:
                DPs.append(num)
    return DPs

def getBinary(num):
    digits = []
    while not num == 0:
        digit = num % 2
        num = math.floor(num / 2)
        digits.append(str(digit))
    digits.reverse()
    num = "".join(digits)
    return num

if __name__ == "__main__":
    accounts = ["George Teal:     $1.00     $2.00      $3.00      $4.01     ",
                "Christine Doyle:     $10.51      $22.49     $12.00     $5.33     $100.00"]
    # print(getTotal(accounts))
    # print(getDoublePalindromes())
