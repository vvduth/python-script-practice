

DevOps = ["Jenkins", "Ansible", "Bash", " Python", "Puppet", "Docker", "Kubernetes", "Terraform"]
Development = ("NodeJS", "angularJS", "java", ".net", "python")
person1= {"Name": "Santa", "Skill": "Blockchain", "code": 1024}
person2 = {"Name": "Rocky", "Skill": "AI", "code": 1218}

user_skills = input("enter ur desired skills: ")

if user_skills in DevOps:
    print(f"weh have {user_skills} in devops team")
elif user_skills in Development:
    print(f"we have {user_skills} in development team")
elif (user_skills in person1.values() or user_skills in person2.values() ):
    print(f"we have employee with {user_skills} skill")
else: 
    print(f"Sorry we do not have {user_skills} in our stack")