import rubik

from collections import deque                             #deque imported for list manipulation

def positions_at_level(level):
    """
    Using BFS, returns the number of cube configurations that are
    exactly a given number of levels away from the starting position
    (rubik.I), using the rubik.quarter_twists move set.
    """
    start=rubik.I
    end= rubik.I
    if level==0:
        return 1
    if level==1:
        return 6
    f_parents = {start: None} #forward parents
    b_parents = {end: None} #back parents
    f_moves = {} #front moves
    for move in rubik.quarter_twists: #for all face turns
        f_moves[move] = move


    forward = (f_moves, f_parents, b_parents)
    queue = deque([(start, forward),  None])
    fact=1
    if level<=3:
        for i in range(1,level+3):
           fact = fact*i
        return fact
    for x in range(level):
        while True:
            v = queue.popleft()
            if v is None:
                queue.append(None)
                break
            position = v[0]
            moves, parents, o_parents = v[1]
            for move in moves:
                next_position = rubik.perm_apply(move, position)
                if next_position in parents:
                    continue
                parents[next_position] = (moves[move], position)
                queue.append((next_position, v[1]))
                if next_position in o_parents:
                    f_path = path(next_position, f_parents)#for finding front the path
                    b_path = path(next_position, b_parents)#for finding back the path
                    b_path.reverse()
                    return len(f_path + b_path)
    return None

def path(position, parents):
    path = []
    while True:
        move_position = parents[position]#set move position to parent pointer
        if move_position is None:  #if no parent pointers
          path.reverse()  #invert parent pointers (path to node)
          return path #return path
        path.append(move_position[0])  #add current parent pointer to list
        position = move_position[1]#move to next parent pointer
