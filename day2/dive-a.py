### DAY 2 ###

# I downloaded and saved the input file as a .txt because I was getting a 400 Bad Request Error when trying to open it with urllib.request.urlopen

f = open("input.txt", "r")
raw_input = f.read()
# I want to convert my input into 3 lists corresponding to up, down and forward.
# I can do it using itertools and then numpy or pandas and work with arrays and/or dataframes,
# however my goal is to rely on the Python Standard Library as much as possible and avoid importing any libraries.

list_str = raw_input.split("\n")

# convert the input to a list of lists. Each element of the lists comprises a string (direction) and an integer (value)
directions_list = []
for i in range(len(list_str)):
    sub_list = list_str[i].split(" ")
    sub_list[1] = int(sub_list[1])
    directions_list.append(sub_list)

# Convert the list of lists to a dictionary where the key will be the direction, and the value will be a list of
# all the integers corresponding to this value
directions_dict = {}
for sub_list in directions_list:
    # print(elem[0])
    if sub_list[0] not in directions_dict:
        directions_dict[sub_list[0]] = []
    directions_dict[sub_list[0]].append(sub_list[1])

# Add all the values in the list and assign the sumation of each list to the corresponding dictionary key
for key, value in directions_dict.items():
    directions_dict[key] = sum(value)

# get the values from the dict
horizontal = directions_dict.get("forward")
vertical = directions_dict.get("down") - directions_dict.get("up")

# do the maths
multiplication = horizontal * vertical

print(
    f"If you multiply your final horizontal position by your final depth you get {multiplication}."
)
