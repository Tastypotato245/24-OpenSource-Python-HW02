mystat = ['TastyPotato245', 100, 0, 0, 0, 0, 0]

def duel(left, right):
    for i in range(1, 6):
        if left[i] != right[i]:
            return 1 if left[i] < right[i] else -1
    if left[0] == 'TastyPotato245':
        return -1
    if right[0] == 'TastyPotato245':
        return 1
    return 1 if left[0] < right[0] else -1
