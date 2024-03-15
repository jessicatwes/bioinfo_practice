# FizzBuzz
Given the prompt 
> In pseudo-code or whatever language you would like: write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

## Pseudo code
My approach for this problem would be to loop through the number from range 1:100 and for each number, **i**, do a if-else statement to ask if **i** is a multiple of 3 and 5 via **if i % 3 == 0 and i % 5 == 0** is True, then return "FizzBuzz". Else if-else statement for multiple of 3, multiple of 5, else return i.

### Python approach
```
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```





