# Task 1
# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n,
# where n is a parameter. Analyze the time and space complexity of this operation.

def squared_nums(n):
    return [num*num for num in range(1, n+1)]

# The time complexity is liniar O(n) because iterates through each number and squares that number. 
# As we speak about space complexity on this, I think it's liniar O(n). The whole new list is getting created in memory.



# Task 2
# Implement a function to merge two pre-sorted lists into a single sorted list. 
# Analyze the time complexity of this operation.

def concatinated(list1, list2):
    merged_list = list1 + list2  
    merged_list.sort()  
    return merged_list

# The time complexity of this approach is O(n logn) because of sort() method.
# I think space complexity will be liniar O(n) since we just create a new list concatinating both.



# Task 3
# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. 
# Analyze the time complexity of this operation.


def dictionaries(dict1, dict2):
    merged_dict = {}
    
    for key, value in dict1.items():
        merged_dict[key] = value
    
    for key, value in dict2.items():
        merged_dict[key] = value
    
    return merged_dict

# The time complexity of this function is linear O(n) because we iterate through each key-value pair in the dictionary,
# then doing it again and overiding the existing value. The space complexity is liniar, but is there are more values 
# that need to be overriden it can become more complex.


# Task 4
# Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. 
# Analyze the time complexity of this operation.

def same_key_value_pairs(dict1, dict2):
    common = {}
    
    for key1, value1 in dict1.items():
        if key1 in dict2 and dict2[key1] == value1:
            common[key1] = value1
    
    return common

# I see the time complexity being liniar O(n) because of iteration through both dictionaties checking key-value pairs.
# But I this it also depends on the size of the dictionary. The space compexity in this case is constant O(1).