# Given the variables x,y, and z print the following:

# if x and y are greater than 10, print step 1 is True
# if z or y is greater than x, print step 2 is True
# if step 2 is False, print step 2 is False
x=10
y=15
z=20
# step1
if x>10 and y>10:
    print("step1 is true")
    # step2
if z>x or y>x:
    print("step2 is true")
else:
    print("step2 is false")