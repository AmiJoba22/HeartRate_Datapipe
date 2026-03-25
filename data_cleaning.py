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