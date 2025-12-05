# Given a number x, use continue to print out even numbers from 0 to x. Use break Stop if you reach a number greater than 20.
x = 20

i = 0
while i <= x:
    if i > 20:
        break       

    if i % 2 != 0:
        i += 1
        continue     

    print(i)         
    i += 1
