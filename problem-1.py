"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""

import itertools
def binarySearch(array, target): #returns the index or the target 
    low = array[0]
    high = array[len(array)-1]
    if array[0+1] == target:
            return 0
    elif array[len(array)-1] == target:
        return len(array)-1
    else:
        while(low <= high):
            mid = int((low+high+1)/2)
            if array[mid]==target:
                return mid
            elif array[mid] > target:
                high = mid -1
            elif array[mid] < target:
                low = mid +1
        return -1  #returns -1 if the target does not exist
    
monthlyExpences={
    'January':2200,
    'February':2350,
    'March':2600,
    'April':2130,
    'May':2190
}

"""1"""
print("In Feb, "+ str(monthlyExpences['February']-monthlyExpences['January'])+ " dollars you spent extra compare to January")

"""2"""
totalExpenceFirstQuarter=monthlyExpences['January']+monthlyExpences['February']+monthlyExpences['March']
print(str(totalExpenceFirstQuarter)+ " dollars your total expense in first quarter (first three months) of the year.")

"""3"""
newArr=new_arr(monthlyExpences)
print(sorted(newArr))
sortedValues=sorted(monthlyExpences.items(),key=lambda x:x[1])
value=list(itertools.chain.from_iterable(sortedValues))
print(value)
n=len(monthlyExpences)
middle=int(n/2)
flag=False

