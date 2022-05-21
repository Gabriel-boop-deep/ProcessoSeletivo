for c in range(1,101):
    if c%2==0:
        print('{} Fizz'.format(c))
    if c%3==0:
        print('{} Buzz'.format(c))
    if c%2==0  and c%3==0:
        print('{} FizzBuzz'. format(c))        
        