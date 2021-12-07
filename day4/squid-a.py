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


def lists_cards(list_str):
    """
    This function produces two lists of the cards available. They
    comprise lists that represent the cards. Each card comprises of five sublists.
    In the first case, the sublists represent the rows of the cards and in the second
    case, the sublist represent the columns of the cards.
    Parameters:
        list (list): list of numbers (int)
    Returns:
        list_of_cards_rows, list_of_cards_cols (tuple): list of cards
    """
    # convert the cards to lists comprising five lists each. Each sublist is a row
    list_of_cards_rows = []
    card = []
    for row in list_str[2:]:
        if row != "":
            row_list = [int(i) for i in row.split()]
            card.append(row_list)
        else:
            list_of_cards_rows.append(card)
            card = []
    list_of_cards_rows.append(card)

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
    return list_of_cards_rows, list_of_cards_cols


cards = lists_cards(list_str)

# call numbers
numbers_called = [
    list_numbers_called[:i] for i in range(0, len(list_numbers_called) + 1, 5)
]
# print(list_of_cards_rows)


# find winning cards
# call the numbers


def card_check(numbers_called, list_of_cards):
    for k in range(len(numbers_called)):

        for i in range(len(list_of_cards[0])):
            for j in range(5):
                # compare each row and column from each card to the numbers called
                row_to_check = list_of_cards[0][i][j]
                col_to_check = list_of_cards[1][i][j]

                if all(item in numbers_called[k] for item in row_to_check) == True:
                    flat_list_card = [
                        item for row in list_of_cards[0][i] for item in row
                    ]
                    return flat_list_card
                elif all(item in numbers_called[k] for item in col_to_check) == True:
                    flat_list_card = [
                        item for row in list_of_cards[1][i] for item in row
                    ]
                    return flat_list_card, numbers_called[k]


result = card_check(numbers_called, cards)
unmarked_numbers = [value for value in result[0] if value not in result[1]]
score = sum(unmarked_numbers) * result[1][-1]
print(score)

# find common elements between 2 lists and remove them from the first
# find common elements:
# remove them from the card


# kei = card_check(numbers_called, list_of_cards_cols, list_of_cards_rows)
# print(kei)

#
