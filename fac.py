import sys

def fac_it(n):
    number=int(n)
    if number == 0 :
        return 1
    elif number == 1:
        return 1
    else:
        return number*fac_it(number-1)

def factorial(n):
    print('Factorial '+n+'! = '+str(fac_it(n)))

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
