import time
SKILLS = ("Muay Thai", "Wrestling", "Boxing", "Ju Jitsu")
SKILLS2 = ["Muay Thai", "Wrestling", "Boxing", "Ju Jitsu", "Kickboxing"]

    
for martial in SKILLS2: 
    print(f"") 
    print("I would like to learn ")
    for i in martial:
        print(i)   
    
# While syntax

x = 2 
while True:
    print("Value of x is ", x)
    x*=2
    time.sleep(2)