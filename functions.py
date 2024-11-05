# defining function
def add(arg1, arg2): 
    total = arg1 + arg2
    return total


def adder(arg1, arg2): 
    total = arg1 + arg2
    print(total)
out = add(1,2)
print(add(12,12))
adder(12,25)

def summ(arg):
    x = 0; 
    for i in arg:
        x = x + i
    return x

out = sum([1,2,3,4])
print(out)

# defuatl argument
def greeting(MSG = "default"):
    print(f"Good {MSG}")
    print("Welcome to this funtion")
    
greeting()
greeting("afternoon")