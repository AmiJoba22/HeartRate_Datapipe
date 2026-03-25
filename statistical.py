def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    # find sum of list then divide by count or number of strings in list 
    
    data_sum = 0 # assigning a variable for adding up all numbers in list, starting from first index
    count = 0 # assigning a variable to count numbers in the list, starting from first index

    for item in data:
        data_sum += item # searched this logic up, my understanding of this is that the loop adds every number creating a sum and data sum is finalized once the final number is added. 
        count += 1 # as more numbers continue to be added the amount of numbers go up by one.
    return data_sum / count # returns the calculation of the avg



def median(data: list) -> float:
    """
    sort list in ascending order then find middle number 
    """
    sorted_data = sorted(data) # sorted data from least to greatest value 
    data_length = len(sorted_data) # assigning a length variable to the length of data list. 

    if data_length % 2 == 1: #if length of data is odd amount (with modulo remainder is 1) 
        heart_rate_data_med = sorted_data[data_length // 2] #took me a bit to understand this line. but i see that floor divison (//) allows us to split list in half and find median of an odd list by dividing len by 2 and rounding down to the nearest whole number.

    else: #if length of data is even amount
        mid1 = sorted_data[data_length // 2 - 1] # get first middle number 
        mid2 = sorted_data[data_length // 2] # get second middle number 
        heart_rate_data_med = (mid1 + mid2) / 2 # find avg of both middle numbers to get median 
    print(f"sorted data for median = {sorted_data}") #for me to visually see sorted data 
    
    return heart_rate_data_med #return variable for median

def range(data: list) -> float:
    """
    find max and min then subtract 
    """

    max_value = data[0] #assign max value to first item to start checking for maximum
    min_value = data[0] # then assign min value to first item to start checking for minimum 

    for item in data[1:]: #scans value of each element 
        if item < min_value: # if current item being checked is less than minimum
            min_value = item # considered minimum at the time till loop ends and min is finalized
        if item > max_value: # if current item being checked is greater than max
            max_value = item # considered max at the time till loop ends and max is finalized
    return max_value - min_value # calculate range 

def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass