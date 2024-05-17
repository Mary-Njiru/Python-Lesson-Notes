def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)


def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(number)


def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number %2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")


def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 ==0:
            print(f"{number} is divisible by 3")
        elif number % 5==0:
            print(f"{number} is divisible by 5")
        elif number % 7 ==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisible by 3,5 or 7")

        
def count_down(n):
    x=0
    while n>x:
        print(n)
        n-=1


def count_down_to_five(n):
    x=0
    while n>x:
        print(n)
        if n==5:
            break
        n=n-1
        print(n)


def divisible_by_seven(n):
    x=1
    while x<=n:
        x+=1
        if x%7!=0:
            continue
        print(f"{x} is divisible by 7")
        

# Using while, continue and if statements, write a function that prints,
# all the odd numbers between 0 and 100
def my_odd_numbers():
    num=1
    while num<100:
        num+=1
        if num%2==0:
            continue
    print(f"{num} is an odd number")
    


# Create a function named 'fizzbuzz'.
# For numbers divisible by 3, print 'fizz'
# For numbers divisible by 5, print 'buzz'
# For all the other numbers, print 'fizzbuzz'
# Use if, elif, and else

def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 ==0:
            print("fizz")
        elif number % 5==0:
            print("buzz")
        else:
            print("fizzbuzz")













