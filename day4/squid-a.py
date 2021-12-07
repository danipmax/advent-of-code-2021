### DAY 4 ###
### TASK 1 ###

f = open("input.txt", "r")
raw_input = f.read()

# I want to iterate through the first line for 5 numbers
# Then check each board for matching rows or columns
#

list_str = raw_input.split("\n")

# get the list of the numbers called
list_numbers_called = [int(i) for i in list_str[0].split(",")]

# convert the cards to lists comprising five lists each. Each sublist is a row

list_of_cards_rows = []
card = []
for row in list_str[1:]:
    if row != "":
        row_list = [int(i) for i in row.split()]
        card.append(row_list)
    else:
        list_of_cards_rows.append(card)
        card = []
list_of_cards_rows.append(card)
list_of_cards_rows = [item for item in list_of_cards_rows if item != []]
# convert the list of cards where the sublists are rows, to a list of cards comrising 5 sublists per card
# with each sublist representing one column

list_of_cards_cols = []
for i in range(len(list_of_cards_rows)):
    card = []
    for j in range(5):
        row = list_of_cards_rows[i][j]
        column = []
        for m in range(5):
            col = list_of_cards_rows[i][m][j]
            column.append(col)
        card.append(column)
    list_of_cards_cols.append(card)

# call numbers
numbers_called = [
    list_numbers_called[:i] for i in range(0, len(list_numbers_called) + 1, 5)
]
# print(list_of_cards_rows)
# find winning cards
# call the numbers

for k in range(len(numbers_called)):

    for i in range(len(list_of_cards_cols)):
        for j in range(5):
            # compare each row and column from each card to the numbers called
            row_to_check = list_of_cards_rows[i][j]
            col_to_check = list_of_cards_cols[i][j]

            if (all(item in numbers_called[k] for item in row_to_check) == True) or (
                all(item in numbers_called[k] for item in col_to_check) == True
            ):
                print(list_of_cards_rows[i])
                print(numbers_called[k])
                print(i)
                print(k)
                quit()

# check rows and columns

# for k in range(len(numbers_called)):
#     for i in range(1, len(list_of_cards)):
#         for j in range(5):
#             row = list_of_cards[i][j]
#             column = []
#             for m in range(5):
#                 col = list_of_cards[i][m][j]
#                 column.append(col)

#             if (all(item in numbers_called[k] for item in row) == True) or (
#                 all(item in numbers_called[k] for item in column) == True
#             ):
#                 print(list_of_cards[i])
#                 print(numbers_called[k])
#                 print(i)
#                 print(k)
#                 # pick unmarked numbers
#                 flat_list_card = [item for row in list_of_cards[i] for item in row]
#                 print(flat_list_card)
#                 list_unmarked_numbers = [num for num in flat_list_card if num not in numbers_called[k]]
#                 quit()
#             else:
#                 continue
list_of_cards = list_of_cards_rows
print("nd")

# check rows
# for k in range(len(numbers_called)):
#     for i in range(1, len(list_of_cards)):
#         for j in range(5):
#             row = list_of_cards[i][j]
#             if all(item in numbers_called[k] for item in row) == True:
#                 print(list_of_cards[i])
#                 print(numbers_called[k])
#                 print(row)
#                 print(i)
#                 quit()

# check columns
# for k in range(len(numbers_called)):

#     for i in range(1, len(list_of_cards)):
#         for j in range(5):
#             column = []

#             for m in range(5):
#                 col = list_of_cards[i][m][j]
#                 column.append(col)
#             if all(item in numbers_called[k] for item in column) == True:
#                 print(list_of_cards[i])
#                 print(numbers_called[k])
#                 print(column)
#                 print(i)
#                 quit()
