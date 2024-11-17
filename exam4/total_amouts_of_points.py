def points(games, x, y):
    points = 0
    while games == 10:
        if x > y:               
            return points + 3
        elif x == y:
            return points + 1
        else:
            return points + 0
        games = games + 1