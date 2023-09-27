def solution(block_count, writes, threshold):
    #Base case: when threshold is 1 then all values in writes meet the threshold and should be returned
    if threshold == 1: 
        
        writes.sort() #sort the array to make it easier to manipulate and to meet the requirement that the output must be sorted

        inc1 = 0 #we will use these values to keep track of our indexs within the array writes
        inc2 = 1

        #now that we have all possible intersections we must get rid of duplicates and pairs or intersections that can merge
        while inc1 != len(writes): 
            while inc2 != len(writes):
                tempOne = writes[inc1]
                tempTwo = writes[inc2]

                #intersections that consume another: example (1, 5) and (2, 3) should just be (1,5)
                if(tempOne[1] > tempTwo[1]):
                    writes.pop(inc2)
                    inc2 -= 1 #we must decriment inc2 everytime we removew an element to avoid index out of bound errors

                #intersections that can be merged togeter into a new intersection: example (2,3) and (3,4) should be (2,4)
                elif(tempOne[1] <= tempTwo[1] and tempOne[1] >= tempTwo[0]):
                    writes.pop(inc2)
                    writes.insert(inc1, [tempOne[0], tempTwo[1]])
                    writes.pop(inc2)
                    inc2 -= 1

                inc2 += 1
            inc1 += 1
        
        return writes
    
    #Recursive case: When threshold isn't 1 we find all possible intersections in writes
    else:
        output = []#this is where we will store all our possible intersections within writes

        for i in range(block_count):
            if block_count - i >= 1: #check to make sure we don't go out of bonds
                #we will compare every element in the array to every element that comes after it to find all possible intersections
                for j in range(i+1, block_count):

                    tempOne = writes[i]
                    tempTwo = writes[j]

                    #assume an intersection between tempOne and tempTwo exists
                    #if the line below is true then the intersection must end in tempTwo[1]
                    if tempOne[1] >= tempTwo[1]:
                        #case where tempTwo is consumed by tempOne thus making tempTwo the entire intersection
                        if(tempOne[0] <= tempTwo[0]): #example: (1, 7) and (2, 6) intersects at (2,6)
                            output.append(tempTwo) #we append every intersection to output
                        #case where tempOne has a larger index 0 and thus creates the lower boundary for the intersection
                        elif(tempOne[0] <= tempTwo[1]): #example (4, 8) and (3, 7) intersects at (4,7)
                            output.append([tempOne[0], tempTwo[1]])

                    #otherwise if the line beloew is true the intersection must end in tempOne[1]
                    elif tempTwo[1] >= tempOne[1]:
                        #case where tempOne in consumed by tempTwo making tempOne the entire intersection
                        if(tempTwo[0] <= tempOne[0]): #example: (3,5) and (1,6) intersects at (3,5)
                            output.append(tempOne)
                            #case where tempTwo e has a larger index 0 and thus creates the lower boundary for the intersection
                        elif(tempTwo[0] <= tempOne[1]): #exmaple: (7, 9) and (8, 10) intersects at (8, 9)
                            output.append([tempTwo[0], tempOne[1]])

        #subtract 1 from threshold that way we keep finding intersections until we are only left with the ones that meet the threshold
        return solution(len(output), output, threshold - 1)


#testing
print("test1---------------------------------------------------------")
test = [[1,3], [3,5], [2,4]]
ans = solution(3, test, 2)
print(str(ans))

print("test2---------------------------------------------------------")
test2 = [[1,5], [3,4], [8,10]]
ans2 = solution(3, test2, 2)
print(str(ans2))

print("test3---------------------------------------------------------")
test3 = [[2,4], [1,2], [6,7], [6,9]]
ans3 = solution(4, test3, 2)
print(str(ans3))

print("test4---------------------------------------------------------")
test4 = [[1,3], [2,5], [3,8]]
ans4 = solution(3, test4, 3)
print(str(ans4))

print("test5---------------------------------------------------------")
test5 = [[5,7], [2,8], [9,10]]
ans5 = solution(3, test5, 2)
print(str(ans5))

print("test6---------------------------------------------------------")
test6 = [[10,10], [6,10], [4,7], [5,8], [6,7]]
ans6 = solution(5, test6, 4)
print(str(ans6))