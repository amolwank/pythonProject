def printPyramid(n):
    #print(n)
    spaces = n-1
    for i in range(0, n):  # outer loop
        for j in range(0, spaces):
            print(end=" ")
        for k in range(0, i+1):
            print("*", end=" ")

        spaces = spaces - 1
        print('\r')

def printOddPyramid(n):
    #print(n)
    spaces = n-1
    odd = 0
    for i in range(0, n):  # outer loop
        for j in range(0, spaces):
            print(end="  ")
        for k in range(0, (i+1)+odd):
            print("* ", end="")

        spaces = spaces - 1
        odd = odd + 1
        print('\r')



n = int(input("--->"))
printOddPyramid(n)
#printPyramid(n)
