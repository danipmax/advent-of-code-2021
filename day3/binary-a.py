### DAY 3 ###
### TASK 1 ###
# I downloaded and saved the input file as a .txt because I was getting a 400 Bad Request Error when trying to open it with urllib.request.urlopen

f = open("input.txt", "r")
raw_input = f.read()
list_str = raw_input.split("\n")

# check if all the strings have the same length (this is not necessary, but i think it is a good practice)
list_of_len = [len(x) for x in list_str]
if list_of_len.count(list_of_len[0]) == len(list_of_len):
    print("All strings have the same length")
    number_len = list_of_len[0]
else:
    print("The list does not contain elements of the same length, check your input")
    quit()

# make a list of the bits in the first position, then a list of the bits in the second position and
# then find the most common bit on each list.

most_common = []
least_common = []
for i in range(number_len):
    # make the list
    list = [string[i] for string in list_str]
    # find the most common bit on the list
    high_freq = max(list, key=list.count)
    # find the least common bit on he list
    low_freq = min(list, key=list.count)
    most_common.append(high_freq)
    least_common.append(low_freq)

# Convert binary strings to decimal
gamma = int("".join(most_common), 2)
epsilon = int("".join(least_common), 2)

print(f"The power consumption of the submarine is {gamma * epsilon} units.")
