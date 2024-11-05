# for loop syntax
PLANET = "Earth"
for i in PLANET:
    print(i)


SKILLS = ("Muay Thai", "Wrestling", "Boxing", "Ju Jitsu")
SKILLS2 = ["Muay Thai", "Wrestling", "Boxing", "Ju Jitsu", "Kickiboxing"]
for martial in SKILLS: 
    print(f"MMA have {martial}")
    
for martial in SKILLS2: 
    print(f"MMA have {martial}")    
    

# While syntax
x = 0 
while x <= 10:
    print("Value of x is ", x)
    x+=1
    

print("Rest of the code")