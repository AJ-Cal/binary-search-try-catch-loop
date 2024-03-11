# This will make a program for binary search

# def binarySearch():
#     searchnum = int(input('What number should I look for? '))
#     nums = []
#     items = int(input('How long is the list? '))

#     def makeList():
#         counter = 1
#         while len(nums) != items:
#             nums.append(counter)
#             counter = counter + 1
#     makeList()
#     length = len(nums)
    
#     start = 0
#     midpoint = int(length/2)
#     end = int(len(nums))

#     while True:
#         if searchnum == midpoint:
#             return 
#         elif searchnum > midpoint:
#             start = midpoint
#             midpoint = ((end - start) / 2) + start
#         elif searchnum < midpoint:
#             end = midpoint
#             midpoint = ((end - start) / 2) + start
#         if searchnum > end or searchnum < start:
#             return -1
# print(binarySearch())

def binarySearch():
    searchnum = int(input('What number should i look for? '))
    nums = []
    
    while True:
        firstnum = input('What number would you like to add? Please add numbers in order from smallest to largest. ')
        try:
            num = int(firstnum)
        except ValueError:
            break

        nums.append(num)
    
    length = len(nums)
    start = 0
    midpoint = int((length/2) - 1)
    end = int((len(nums)) - 1)

    while True:
        if searchnum == nums[midpoint]:
            print('yay ♡⸜(˶˃ ᵕ ˂˶)⸝♡ u win <3<3<3 ')
            return midpoint
        elif searchnum > nums[midpoint]:
            start = midpoint
            midpoint = int(((end - start) / 2)) + start
        elif searchnum < nums[midpoint]:
            end = midpoint
            midpoint = int(((end - start) / 2) + start)
        if searchnum > end or searchnum < start:
            return "sorry (╥﹏╥) this number is not in the list <3<3<3 "
print(binarySearch())
    

binarySearch()
