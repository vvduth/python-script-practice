# arithemic operator
x  = 2 
y = 7 
total = x + y 
print(total)

total = x  - y
print(total)

total = x * y
print(total)

total = x / y
print(total)

total = y % x 
print(total)

total = y ** x
print(total)
 
# comparison
a = 30 
b = 60

out = a < b
print("out is {}" , out)

# assignemnt operator
c = 0
d = 1

c+=d # x = c + d
print("value of c is ", c)


# Logical operators
a= 40
b=60
x=2
y=3

out = (a < b) and (x >y) 
print("out is {}" , out)

out = not (a < b)
print("out is {}" , out)

# membership operatoes
devops =(47, "Linux", "Vagraant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
ans = "Linux" not in devops
print("ans: ", ans)

# Identity operation
a = 15
b = 15

result = a is b
result2 = a is not b 
print("result: ", result)
print("result2: ", result2)
