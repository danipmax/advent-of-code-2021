### DAY 3 ###
### TASK 2 ###
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

# find the most common digit and isolate the elements of the input with the most common digit

# find the most common digit for the first bit
first_bit_list = [string[3] for string in list_str]
most_common = max(first_bit_list, key=first_bit_list.count)

# isolate all values that have 1 as first digit
matching = [s for s in list_str if s[3] == most_common]

list_str = sorted(list_str)
oxygen_rating_list = list_str
co2_rating_list = list_str
for i in range(number_len):
    oxygen_rating_first_bit_list = [string[i] for string in oxygen_rating_list]
    oxygen_rate_count_ones = oxygen_rating_first_bit_list.count("1")
    oxygen_rate_count_zeros = oxygen_rating_first_bit_list.count("0")
    oxygen_rating_most_common = max(
        oxygen_rating_first_bit_list, key=oxygen_rating_first_bit_list.count
    )
    if oxygen_rate_count_ones == oxygen_rate_count_zeros:
        oxygen_rating_list = [s for s in oxygen_rating_list if s[i] == "1"]
    else:
        oxygen_rating_list = [
            s for s in oxygen_rating_list if s[i] == oxygen_rating_most_common
        ]

    co2_rating_first_bit_list = [string[i] for string in co2_rating_list]
    co2_rating_count_ones = co2_rating_first_bit_list.count("1")
    co2_rating_count_zeros = co2_rating_first_bit_list.count("0")
    co2_rating_least_common = min(
        co2_rating_first_bit_list, key=co2_rating_first_bit_list.count
    )
    if co2_rating_count_ones == co2_rating_count_zeros:
        co2_rating_list = [s for s in co2_rating_list if s[i] == "0"]
    else:
        co2_rating_list = [
            s for s in co2_rating_list if s[i] == co2_rating_least_common
        ]
    # print(oxygen_rating_list)
    # print(co2_rating_list)

oxygen_rating = int(oxygen_rating_list[0], 2)
co2_rating = int(co2_rating_list[0], 2)

# print(oxygen_rating)
# print(co2_rating)

print(
    f"The life support rating of the submarine is {oxygen_rating * co2_rating} units."
)
