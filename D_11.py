def main():

    data = []

    with open('data_02.js', 'r') as file:
        for line in file:
            parts = list(map(int, line.strip().split()))
            data.append(parts)
    
    c1 = increasing(data)
    c2 = decreasing(data)
    safe = check_distance(c1, c2)
    print(str(len(safe)) + " reports are safe")

def increasing(data):

    incdata = []

    for i in range(len(data)):
        flag = False
        for k in range(len(data[i]) - 1):
            if data[i][k] < data[i][k + 1]:
                flag = True
            else:
                flag = False
            if flag == False:
                break
        if flag == True:
            incdata.append(data[i])
    
    return incdata

def decreasing(data):

    decdata = []

    for i in range(len(data)):
        flag = False
        for k in range(len(data[i]) - 1):
            if data[i][k] > data[i][k + 1]:
                flag = True
            else:
                flag = False
            if flag == False:
                break
        if flag == True:
            decdata.append(data[i])

    return decdata

def check_distance(increasing, decreasing):
    
    cond_met = []

    for i in range(len(increasing)):
        flag = False
        for k in range(len(increasing[i]) - 1):
            difference = abs(increasing[i][k] - increasing[i][k + 1])
            if difference >= 1 and difference <= 3:
                flag = True
            else:
                flag = False
            if flag == False:
                break
        if flag == True:
            cond_met.append(increasing[i])

    for i in range(len(decreasing)):
        flag = False
        for k in range(len(decreasing[i]) - 1):
            difference = abs(decreasing[i][k] - decreasing[i][k + 1])
            if difference >= 1 and difference <= 3:
                flag = True
            else:
                flag = False
            if flag == False:
                break
        if flag == True:
            cond_met.append(decreasing[i])

    return cond_met

if __name__ == '__main__':
    main()