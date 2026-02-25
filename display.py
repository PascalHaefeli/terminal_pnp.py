test = {
    'a' : "desc1",
    'b' : "desc2"
    }

def display_dict_keys(dictionary):
    for i in dictionary:
        print(f"-\n{i}")
    return None

def display_dict_keys_and_values(dictionary):
    for i in dictionary:
        print(f"-\n{i}: {dictionary[i]}")
    return None

def display_dict_value_of_key(dictionary, key):
    print(f"{key}: {dictionary[key]}")
    return None

# custom display function for artifacts as artifacts are stored in a dict, where keys are associated with 4-tuples
# do it here for consistency or directly in artifacts.py?