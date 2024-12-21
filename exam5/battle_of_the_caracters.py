def battle(x, y):
    def get_power(group):
        power = 0
        for i in group:
            power += "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i) + 1
        return power
    
    x = get_power(x)
    y = get_power(y)
    
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "tie"