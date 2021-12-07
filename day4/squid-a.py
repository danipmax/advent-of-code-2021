### DAY 4 ###
### TASK 1 ###

f = open("input.txt", "r")
raw_input = f.read()

# I want to iterate through the first line for 5 numbers
# Then check each board for matching rows or columns
#

list_str = raw_input.split("\n")

# get a list of the numbers called
list_numbers_called = [int(i) for i in list_str[0].split(",")]
list_sets_called = [
    list_numbers_called[i : i + 5] for i in range(0, len(list_numbers_called), 5)
]  # i don't know if i need the whole list or if i just need to call them +5 at each iteration

# convert the cards to lists comprising five lists each

list_of_cards = []
card = []
for row in list_str[1:]:
    if row != "":
        row_list = [int(i) for i in row.split()]
        card.append(row_list)
    else:
        list_of_cards.append(card)
        card = []
list_of_cards.append(card)


# find winning card

# call numbers


numbers_called = [
    list_numbers_called[:i] for i in range(0, len(list_numbers_called) + 1, 5)
]

# check rows
for k in range(len(numbers_called)):
    for i in range(1, len(list_of_cards)):
        for j in range(5):
            row = list_of_cards[i][j]
            if all(item in numbers_called[k] for item in row) == True:
                print(list_of_cards[i])
                print(numbers_called[k])
                print(row)
                # quit()

    # check columns
for k in range(len(numbers_called)):

    for i in range(1, len(list_of_cards)):
        for j in range(5):
            column = []

            for m in range(5):
                col = list_of_cards[i][m][j]
                column.append(col)
            if all(item in numbers_called[k] for item in column) == True:
                print(list_of_cards[i])
                print(numbers_called[k])
                print(column)
                print(i)
                quit()
