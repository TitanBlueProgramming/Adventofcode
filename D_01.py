def main():

    column1 = []
    column2 = []
    line_counter = 0

    with open('data_01.js', 'r') as file:
        for line in file:
            line_counter += 1
            parts = line.strip().split()
            number1 = int(parts[0])
            number2 = int(parts[1])
            column1.append(number1)
            column2.append(number2)
   
    sort(column1, column2)
    value = difference(column1, column2)
    print("The total difference is:", value)

def difference(column1, column2):

    difference_list = []

    for k in range(len(column1)):
        differences = abs(column2[k] - column1[k])
        difference_list.append(differences)

    total_difference = sum(difference_list)
    
    return total_difference

def sort(column1, column2):
    column1.sort()
    column2.sort()
    return column1, column2

if __name__ == '__main__':
    main()