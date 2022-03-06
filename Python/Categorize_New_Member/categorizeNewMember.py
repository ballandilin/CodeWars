def openOrSenior(data):
    output = []
    c = len(data)
    
    for i in range(c):
        if data[i][0] >= 55 and data[i][1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
            
    return output