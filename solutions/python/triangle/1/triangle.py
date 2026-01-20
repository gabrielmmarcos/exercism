def equilateral(sides):
    count = 0
    for i in sides:
        if i == 0:
            count+=1
    
    if count == 3:
        return False
    else: 
        if sides[0] == sides[1] and sides[1] == sides[2]:
            return True
        else:
            return False


def isosceles(sides):
      if sides[0] + sides[1] < sides[2]:
        return False
      elif sides[1] + sides[2] < sides[0]:
          return False
      elif sides[0] + sides[2] < sides[1]:
          return False
      else:
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
        else:
            return False


def scalene(sides):
    if sides[0] + sides[1] < sides[2]:
        return False
    elif sides[1] + sides[2] < sides[0]:
        return False
    elif sides[0] + sides[2] < sides[1]:
        return False
    else:
        if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
            return True
        else:
            return False
        
