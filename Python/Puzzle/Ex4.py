### We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

def test(n):
    return [n + 2 * i for i in range(n)]

n = int(input("Enter a number: "))
print("Number of piles: ",n)
print("Number of stones in each pile: ")
print(test(n))