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


def calc_rating(list, rating):
    """
    This function calculates the rating (oxygen or co2) using the relevant bit criteria.

    Parameters:
        list (list): list of binary values(strings)
        rating (str): the name rating we are calculating ("oxygen" or "co2")
    Returns:
        value (int): decimal value of the rating calculated
    """
    rating_list = list

    for i in range(len(list[0])):
        rating_bit_list = [string[i] for string in rating_list]
        count_ones = rating_bit_list.count("1")
        count_zeros = rating_bit_list.count("0")
        if rating == "oxygen":
            most_least_common = max(rating_bit_list, key=rating_bit_list.count)
            tie_value = "1"  # value assigned in case 0 and 1 are equally common
        elif rating == "co2":
            most_least_common = min(rating_bit_list, key=rating_bit_list.count)
            tie_value = "0"  # value assigned in case 0 and 1 are equally common
        if count_ones == count_zeros:
            rating_list = [s for s in rating_list if s[i] == tie_value]
        else:
            rating_list = [s for s in rating_list if s[i] == most_least_common]

    rating = int(rating_list[0], 2)
    return rating


oxygen_rating = calc_rating(list_str, "oxygen")
co2_rating = calc_rating(list_str, "co2")

print(
    f"The life support rating of the submarine is {oxygen_rating * co2_rating} units."
)
