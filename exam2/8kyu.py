#student's final grade

def final_grade(exam, projects):
    if exam >= 90 or projects > 10:
        return 100
    if exam >= 75 or projects > 5:
        return 90
    if exam >= 50 or projects > 2:
        return 75
    if exam < 50 or projects <= 2:
        return 0
    
print(final_grade(75, 0))

#fake_binary

def fake_bin(x):
    if x < 5:
        return 0
    elif x > 5:
        return 1
        
