def solution(block_count, writes, threshold):
    print("you entered solution")
    if threshold == 1:
        print("congrats your out")
        print(writes)
        return writes
    else:
        print("here we go")
        ranges = []
        count = 0

        for i in range(block_count):

            if block_count - i >= 1:
                for j in range(i+1, block_count):
                    print("inside for loop")
                    print("j is " + str(j))

                    tempOne = writes[i]
                    tempTwo = writes[j]
                    print("temp One is : " + str(tempOne))
                    print("temp two is : " + str(tempTwo))

                    if tempOne[1] >= tempTwo[1]:

                        if(tempOne[0] <= tempTwo[0]):
                            ranges.append(tempTwo)
                            count += 1
                        elif(tempOne[0] <= tempTwo[1]):
                            ranges.append([tempOne[0], tempTwo[1]])
                            count += 1

                    elif tempTwo[1] >= tempOne[1]:
                        if(tempTwo[0] <= tempOne[0]):
                            ranges.append(tempOne)
                            count += 1
                        elif(tempTwo[0] <= tempOne[1]):
                            ranges.append([tempTwo[0], tempOne[1]])
                            count += 1

                    print("ranges is: " + str(ranges))

        return solution(count, ranges, threshold - 1)

test = [[1,3], [3,5], [2,4]]
ans = solution(3, test, 2)
print(str(ans))


        