def ONSquareTIme(n):
    iterations = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
            iterations += 1
            print(" ")
    print("\nWhen n is",n," Iterations: ", iterations)

    ONSquareTIme(5)
    ONSquareTIme(4)
    ONSquareTIme(3)

    print("\nWith every 'n' the time taken equals n ^ 2")
    print("O(n^2)")