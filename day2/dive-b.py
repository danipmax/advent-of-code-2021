### DAY 2 ###
### TASK 2 ###
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

horizontal = 0
depth = 0
aim = 0
# add updated isntructions
for sub_list in directions_list:
    if sub_list[0] == "forward":
        horizontal += sub_list[1]
        depth += aim * sub_list[1]
    elif sub_list[0] == "down":
        aim += sub_list[1]
    elif sub_list[0] == "up":
        aim -= sub_list[1]

print(
    f"If you multiply your final horizontal position by your final depth you get {horizontal * depth}."
)
