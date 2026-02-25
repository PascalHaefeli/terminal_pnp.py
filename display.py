# \u2014 is unicode for "em dash" (longer dash-character)
# used with '|' to list elements of dicts in a tree-like structure
def dict_keys(dictionary, name):
    print(f"\n---\n{name}")
    for i in dictionary:
        print(f"|\n| \u2014\u2014 {chr(151)}{i}")
    return None

def dict_keys_and_values(dictionary, name):
    print(f"\n---\n{name}")
    for i in dictionary:
        print(f"|\n| \u2014\u2014 {i}: {dictionary[i]}")
    return None

def dict_value_of_key(dictionary, key):
    print(f"\n---\n{key}\n-\n{dictionary[key]}")
    return None

def object_attributes(obj, name):
    dict_keys_and_values(obj.__dict__, name)
    return None

# custom display function for artifacts as artifacts are stored in a dict, where keys are associated with 4-tuples
# i made it directly in artifacts.py; structure is similar to that of dict_keys_and_values, but i couldn't just call it from there