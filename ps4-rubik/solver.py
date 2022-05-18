import rubik

from collections import deque

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.
    Assumes the rubik.quarter_twists move set.
    """
    if start == end: return []

    f_parents = {start: None} #forward parents
    b_parents = {end: None} #back parents
    f_moves = {} #front moves
    b_moves = {} #back moves
    for move in rubik.quarter_twists: #for all face turns
        f_moves[move] = move
        b_moves[rubik.perm_inverse(move)] = move #if there is a face moving cloockwise there should be a move that moves anti clockwise
    forward = (f_moves, f_parents, b_parents)
    backward = (b_moves, b_parents, f_parents)
    queue = deque([(start, forward), (end, backward), None])# uisng deque fuction to make a complex queue
    for i in range(7):
        while True:
            v = queue.popleft()#pop out first element of queue
            if v is None:
                queue.append(None)#append none if v is none
                break
            position = v[0]
            moves, parents, o_parents = v[1]
            for move in moves:
                next_position = rubik.perm_apply(move, position) #using fuction in rubiks.py
                if next_position in parents:
                    continue
                parents[next_position] = (moves[move], position)
                queue.append((next_position, v[1]))
                if next_position in o_parents:
                    f_path = path(next_position, f_parents)#for finding front the path
                    b_path = path(next_position, b_parents)#for finding back the path
                    b_path.reverse()
                    return f_path + b_path

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
