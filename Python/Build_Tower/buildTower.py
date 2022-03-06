def tower_builder(n_floors):
    floors = []
    
    for i in range(n_floors):
        # initialize sequence with odd numbers
        n = 2*(i+1)-1
        
        floors.append(" " * (n_floors-(i+1)) + "*" * n + " " * (n_floors-(i+1)))
        
    return floors