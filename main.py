from matplotlib import pyplot as plt

lst = list()

def collatz(n):
    while n > 1:
        lst.append(n)
        if (n % 2):
            n = 3*n + 1
        else:
            n = n//2

    print(lst)
 
 
n = int(input('Enter n: '))
print('Sequence: ')
collatz(n)

def plotCollatz(lst):
    plt.plot(lst)
    plt.title('Collatz Conjecture')
    plt.show()

plotCollatz(lst)