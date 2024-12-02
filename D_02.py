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
   
    value = calculate_similarity(column1, column2)
    print("The similarity score is:", value)

def calculate_similarity(column1, column2):

    similarity_score = 0

    for k in column1:
        count_in_column2 = column2.count(k)
        product = k * count_in_column2
        similarity_score += product
    return similarity_score

if __name__ == '__main__':
    main()