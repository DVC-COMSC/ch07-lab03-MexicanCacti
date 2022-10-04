numbers = []

for i in range(5):
    numbers.append(int(input()))
average = sum(numbers)/len(numbers)

for i in range(len(numbers)):
    if(numbers[i] > average):
        print(numbers[i], end= " ")