import math

def distance(x1,y1,x2,y2): #euclidean distance
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def detect_collisions_in_square(balls): #Code given to us itially
    """
    Detect any pairs of balls that are colliding.
    Returns a set of ball_pairs.
    """

    set_of_collisions = set()

    for i in range(len(balls)):
        b1 = balls[i]
        for j in range(i):
            b2 = balls[j]
            if gas.colliding(b1, b2):
                set_of_collisions.add(gas.ball_pair(b1, b2))

    return set_of_collisions
number_balls=200 # Asuming number ofballs for gas.py
world_min_x = -200.0*number_balls**.5  # minimum x in world coordinates
world_max_x = +200.0*number_balls**.5  # maximum x in world coordinates
world_min_y = -200.0*number_balls**.5  # minimum y in world coordinates
world_max_y = +200.0*number_balls**.5  # maximum y in world coordinates
def ball_in_square(b,xb,yb,v=False): #v -> variable for testing
    min_x=xb*256
    max_x=(xb+1)*256
    min_y=yb*256
    max_y=(yb+1)*256
    #if v:
        #print("Check",b.x,b.y,b.radius,min_x,min_y,256,256,v) # For testing code for errors

    #print("Minimum_x",min_x,"Max_Y",max_x,"MIN_Y",min_y,"MAX_Y",max_y)
    #print("b.x-b.radius,b.x+b.radius,b.y-b.radius,b.y+b.radius")
    #print(b.x-b.radius,b.x+b.radius,b.y-b.radius,b.y+b.radius)
    #print("b.x,b.y,b.radius")
    #print(b.x,b.y,b.radius)
    if b.x < min_x: # for boxes in left the box of reference
        if b.y < min_y:# for boxes below + left side the box of reference
            #if v: print("HERE: 1",max_x,min_y,b.x,b.y) # For testing code for errors
            dist=distance(min_x,min_y,b.x,b.y)#euclidean distance
            if b.radius >= dist: #Check if the ball overlaps in other box that is center and bottom left
                return True
            else:
                return False
        elif b.y<=max_y: #for boxes in top left side of reference
            #if v: print("HERE: 2",max_x,min_y,b.x,b.y) # For testing code for errors
            if b.x+b.radius >= min_x: # if the ball overlaps in other box that is center and top right side of box of reference

                return True
            else:
                return False

        else:
            dist=distance(min_x,max_y,b.x,b.y)#euclidean distance
            #if v: print("HERE: 3",max_x,min_y,b.x,b.y) # For testing code for errors
            if b.radius >= dist: #for ball in left side of box of reference
                return True
            else:
                return False
    elif b.x<=max_x:#for box in right side of box of reference
        if b.y < min_y:# for box in right + below side of box of reference
            #if v: print("HERE: 4",max_x,min_y,b.x,b.y) # For testing code for errors
            if b.y+b.radius >= min_y:# checking if ball overlaps
                return True
            else:
                return False

        elif b.y<=max_y:# checking if ball overlaps
            #if v: print("HERE: 5",max_x,min_y,b.x,b.y) # For testing code for errors
            return True
        else:# checking if ball overlaps
            #if v: print("HERE: 6",max_x,min_y,b.x,b.y) # For testing code for errors
            if b.y-b.radius <= max_y:
                return True
            else:
                return False
    else:#for boxes above and below the box of reference
        if b.y < min_y:#for center below
            #if v: print("HERE: 7",max_x,min_y,b.x,b.y) # For testing code for errors
            dist=distance(max_x,min_y,b.x,b.y)#euclidean distance
            if b.radius >= dist:#checking if ball overlaps
                return True
            else:
                return False
        elif b.y<=max_y:#for center up
            #if v: print("HERE: 8",max_x,min_y,b.x,b.y) # For testing code for errors
            if b.x-b.radius <= max_x:#checking if ball overlaps
                return True
            else:
                return False

        else:
            dist=distance(max_x,max_y,b.x,b.y)#euclidean distance
            #if v: print("HERE: 9",max_x,min_y,b.x,b.y) # For testing code for errors
            if b.radius >= dist:
                return True
            else:
                return False
    return False # this is for worse case when ball doesnt exist


def detect_collisions(balls,v=False): #variables for testing purposes
    test=False #for testing code for errors
    set_of_collisions=set()
    dict_of_balls={}
    for b in balls:

        xb = int(b.x/256)# divde world based on address
        if b.x < 0:
            xb=xb-1
        yb = int(b.y/256)# divde world based on address
        if b.y < 0:
            yb=yb-1



        for x in range(xb-1,xb+2):
            for y in range(yb-1,yb+2):
                key=(x,y)
                #flag=False
                if ball_in_square(b,x,y,v):
                    #flag=True
                    if key not in dict_of_balls.keys():
                        dict_of_balls[key] =[]
                    dict_of_balls[key].append(b)
    for key in dict_of_balls.keys():
        set_of_collisions.update(detect_collisions_in_square(dict_of_balls[key]))
    ace=[] #temp list for making list in a [set(list)]
    final=set()#final set with all collisions
    for element in set_of_collisions:
        b1=element.b1
        b2=element.b2
        if (b1,b2)not in ace: #to make a list of elements and removing copies of elements
            ace.append((b1,b2))
            final.add(element)
    set_of_collisions=final
    #print(set_of_collisions)
    return set_of_collisions

import gas
