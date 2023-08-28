#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element between two lists.
    
    Args:
        my_list_1 (list): The first input list.
        my_list_2 (list): The second input list.
        list_length (int): The desired length of the resulting list.
        
    Returns:
        list: A new list with division results or 0 for failed divisions.
    """
    result_list = []  # Initialize an empty list for the division results
    
    for i in range(list_length):
        result = 0  # Initialize the division result
        
        try:
            num_1 = my_list_1[i]  # Get element from the first list
            num_2 = my_list_2[i]  # Get element from the second list
            
            if isinstance(num_1, (int, float)) and isinstance(num_2, (int, float)):
                # Check if both elements are integers or floats
                if num_2 == 0:
                    # Check if division by zero occurs
                    raise ZeroDivisionError
                result = num_1 / num_2  # Perform the division
            else:
                raise TypeError  # Raise TypeError for non-integer/float elements
                
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)  # Append the result to the result list
    
    return result_list  # Return the list of division results
