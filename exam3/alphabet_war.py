def alphabet_war(fight):
    left_side = [w, p, b, s]
    right_side = [m, q, d, z]
    fighting = fight[::]
    w = 4
    p = 3
    b = 2
    s = 1
    m = 4
    q = 3
    d = 2
    z = 1
    if fighting == left_side[::]:
        return "left side wins"
    if fighting == right_side[::]:
        return "right side wins"
    elif fighting == left_side[::] and right_side[::]:
        n = sum(left_side[::])
        s = sum(right_side[::])
        if n == s:
            return "Let's fight again!"
        elif n > s:
            return "Left side wins!"
        else:
            return "Rignt side wins!"