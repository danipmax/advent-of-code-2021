### DAY 1 ###

# I downloaded and saved the input file as a .txt because I was getting a 400 Bad Request Error when trying to open it with urllib.request.urlopen


def input_to_list(file):
    """
    This function converts the input for the challenge to a list of integers.

    Parameters:
        file (str): The name of the file that contains ths input.

    Returns:
        list_int (list): A list of integers
    """

    f = open(file, "r")
    raw_input = f.read()
    list_str = raw_input.split()
    list_int = list(map(int, list_str))
    return list_int


def count_increase(list_int):
    """
    This function calculates the number of times a measurement increases.
    This is the answer to the first puzzle.

    Parameters:
        list_int (list): list of measurements(integers)

    Returns:
        n (int): number of times a measurement inctreases.
    """

    n = 0
    for i in range(len(list_int) - 1):
        if list_int[i + 1] > list_int[i]:
            n += 1

    # Another way to do it is to use a list comrehension:

    # increase_array = [
    # "increase" for i in range(len(list_int) - 1) if list_int[i + 1] > list_int[i]
    # ]
    # n = len(increase_array)
    return n


def three_measurement_window_sum(list_int):
    """
    This function calculates the sums of all three-measurement sliding windows in the list.
    This is part of the answer to the second puzzle.

    Parameters:
        list_int (list): list of measurements(integers)

    Returns:
        new_list (list): list of sums of all three-measurement sliding windows (integers).
    """

    new_list = []
    for i in range(len(list_int) - 2):
        window_value = list_int[i] + list_int[i + 1] + list_int[i + 2]
        new_list.append(window_value)
    return new_list


def main():

    input = "input.txt"
    list_of_measurements = input_to_list(input)
    #### ANSWER TO THE FIRST PUZZLE ####
    larger_measurements = count_increase(list_of_measurements)
    print(
        f"{larger_measurements} measurements are larger than the previous measurement."
    )
    #### ANSWER TO THE SECOND PUZZLE ####
    window_measurements = three_measurement_window_sum(list_of_measurements)
    # I am using the function "count_increase" to calculate the number of sums that are larger than the previous sum"
    larger_sums = count_increase(window_measurements)
    print(f"{larger_sums} sums are larger than the previous sum.")


if __name__ == "__main__":

    main()
