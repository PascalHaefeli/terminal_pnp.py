import os

terminal_length = os.get_terminal_size()[0] - 2

def format_string(string):
    length = len(string)
    i = 1
    splits = 1
    while i <= length:
        if i % terminal_length == 0:
            space = get_last_space(string, i)
            if space == None:
                space = terminal_length * splits
            if string[space-2:space] != "\n|":
                string = string[0:space] + "\n|" + string[space:]
                i = space + 2
                length += 2
                splits += 1
        i += 1
    return string

def get_last_space(string, i):
    if i == " ":
        return i
    j = i
    while j > 0:
        if string[j] == " ":
            return j
        j -= 1
    return None

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

def dict_keys_and_values_long(dictionary, name):
    print(f"\n---\n{name}")
    for i in dictionary:
        text = format_string(dictionary[i])
        print(f"|\n| \u2014\u2014 {i}:\n| {text}")
    return None

def dict_value_of_key(dictionary, key):
    print(f"\n---\n{key}\n-\n{dictionary[key]}")
    return None

def object_attributes(obj, name):
    dict_keys_and_values(obj.__dict__, name)
    return None

# custom display function for artifacts as artifacts are stored in a dict, where keys are associated with 4-tuples
# i made it directly in artifacts.py; structure is similar to that of dict_keys_and_values, but i couldn't just call it from there

text = "You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius. As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range."
short = "this is a much shorter sample text for debugging! this is a much shorter sample text for debugging! this is a much shorter sample text for debugging!"
#print(format_string(text))

