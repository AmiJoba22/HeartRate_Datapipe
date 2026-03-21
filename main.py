def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    1. loop for data 
    2. if checking valid data, if not valid, create a new list 
    """
    # 1. takes in a list of strings and filters out all strings that include non-digit characters.
       
    cleaned_list = []
    removed_values = []
    
    for item in data:
        if item.isdigit(): # checks if item in data is a digit only string
            cleaned_list.append(item)
        else:
            removed_values.append(item)
    print(f"clean list = {cleaned_list}, removed_values = {removed_values}")
     # there were too many numbers in my face, so I wanted to visually see which was labeled clean and what was removed. 
    return (cleaned_list, removed_values) # return tuple 

    

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


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    file_object = open(file) 
    for line in file_object: #iterated through every line in file 
        print(line.strip()) # stripped new line characters 
        data.append(line.strip()) # put data of each line into a list 
    print(data)
    

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list,removed_values= clean_heartrate_data(data) #tuple unpacking 
    cleaned_list= tuple(map(int, cleaned_list)) #converted cleaned list to tuple
    print(f"FINAL CLEANED LIST ={cleaned_list}") # just wanted to organize data to make sure output was correct

    # calculate the average, median, and range of this file using the functions you've wrote
    heart_rate_data_avg = average(cleaned_list) 
    heart_rate_data_med = median(cleaned_list) 
    heart_rate_date_range = range(cleaned_list)
    # pretty much calculated them in functions themselves
    
    
    # print out your data quality measure to the console
    print(f"avg = {float(heart_rate_data_avg)}")
    print(f" median = {float(heart_rate_data_med)}") # just making sure they print as float 
    print(f" range = {float(heart_rate_date_range)}")

    # print out your descriptive statistics to the console
    
    print(float(average(cleaned_list)))
    print(float(median(cleaned_list)))
    print(float(range(cleaned_list)))


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")

''' 
My results found in output 

1. phase0.txt:

cleaned_list = (69, 75, 84, 79, 72, 69, 93, 91, 72, 76, 69, 71, 60, 63, 67, 58, 63, 61, 65, 66, 62, 67, 61, 63, 61, 78, 62, 60, 59, 75, 65, 64, 60, 60, 63, 62, 68, 63, 61, 66, 60, 56, 56, 54, 54, 54, 79, 68, 55, 55, 56, 67, 58, 62, 60, 62, 70, 60, 55, 55, 57, 57, 56)

removed_values = ['', 'NO DATA', 'NO DATA']

sorted data for median = 54, 54, 54, 55, 55, 55, 55, 56, 56, 56, 56, 57, 57, 58, 58, 59, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 65, 65, 66, 66, 67, 67, 67, 68, 68, 69, 69, 69, 70, 71, 72, 72, 75, 75, 76, 78, 79, 79, 84, 91, 93]

avg = 64.58730158730158
 median = 62.0
 range = 39.0

 
2. phase1.txt
CLEANED LIST =(69, 57, 56, 84, 100, 83, 89, 75, 89, 90, 96, 89, 86, 86, 85, 86, 75, 88, 92, 66, 100, 89, 98, 90, 74, 88, 94, 89, 93, 83, 86, 84, 84, 91, 83, 84, 93, 91, 93, 91, 85, 102, 88, 89, 90, 90, 84, 87, 85, 110, 87, 96, 106, 96)

removed_values = ['NO DATA', '']

sorted data for median = [56, 57, 66, 69, 74, 75, 75, 83, 83, 83, 84, 84, 84, 84, 84, 85, 85, 85, 86, 86, 86, 86, 87, 87, 88, 88, 88, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 92, 93, 93, 93, 94, 96, 96, 96, 98, 100, 100, 102, 106, 110]


avg = 87.29629629629629
 median = 88.5
 range = 54.0

3.phase2.txt

CLEANED LIST =(69, 97, 88, 117, 108, 89, 79, 77, 106, 79, 99, 85, 88, 97, 97, 77, 83, 112, 75, 107, 96, 92, 86, 81, 83, 107, 79, 73, 75, 68, 80, 69, 77, 93, 69, 91, 85, 93, 83, 100, 83, 91, 92, 79, 89, 92, 71, 72, 88, 68, 98, 68, 101, 97, 74, 85, 80, 62, 58, 54)

removed_values = ['']

sorted data for median = [54, 58, 62, 68, 68, 68, 69, 69, 69, 71, 72, 73, 74, 75, 75, 77, 77, 77, 79, 79, 79, 79, 80, 80, 81, 83, 83, 83, 83, 85, 85, 85, 86, 88, 88, 88, 89, 89, 91, 91, 92, 92, 92, 93, 93, 96, 97, 97, 97, 97, 98, 99, 100, 101, 106, 107, 107, 108, 112, 117]

avg = 85.18333333333334
 median = 85.0
 range = 63.0

4. phase3.txt
CLEANED LIST =(69, 51, 56, 53, 56, 54, 57, 57, 64, 60, 58, 57, 56, 56, 55, 54, 55, 53, 52, 55, 97, 67, 58, 57, 54, 56, 53, 52, 59, 76, 66, 62, 62, 62, 52, 53, 50, 51, 50, 52, 52, 51, 80, 73, 95, 88, 67, 62, 64, 61, 57, 60, 56, 55, 54, 53, 53, 54, 52, 53, 52, 51, 51, 56, 54, 59, 56, 79, 74, 70, 65, 58, 57, 54, 54, 54, 54, 65, 99, 91, 66, 85, 63, 64, 61, 67)

removed_values = []

sorted data for median = [50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 58, 58, 58, 59, 59, 60, 60, 61, 61, 62, 62, 62, 62, 63, 64, 64, 64, 65, 65, 66, 66, 67, 67, 67, 69, 70, 73, 74, 76, 79, 80, 85, 88, 91, 95, 97, 99]


avg = 60.651162790697676
 median = 56.5
 range = 49.0

'''