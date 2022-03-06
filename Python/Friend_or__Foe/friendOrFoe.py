def friend(x):
    
    friends = []
    
    for i in x:
        if len(i) == 4:
            friends.append(i)
    
    if len(friends) == 0:
        return friends
    else:
        return friends