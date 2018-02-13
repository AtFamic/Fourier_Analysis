import numpy as np

def main():
    a = np.arange(1,5,1)
    print(plus(a))
    print(a)

def plus(data):
    for i in range(7):
        print(data+1)

main()