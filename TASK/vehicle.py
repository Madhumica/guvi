ef distance_input():
    valid = False
    while valid == False:
        try:            
            distance = int(input("Enter the distance you want to travel in km"))
            if distance > 0:
                valid = True
        except ValueError:
            valid = False
    return distance
def passengers():
    try:
        n = int(input("How many are coming in the taxi?"))
        if n > 0:
            return n
        else:
            if n < 5:
                passengers()
            else:
                print ("Too many people")
                passengers()
    except ValueError:
        passengers()
def calc(distance, n):
    total = (n * 2) + (distance * 1.5)
    return total
distance = distance_input()
n = passengers()
print ("your fare is: ", calc(distance, n))
