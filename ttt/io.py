



def print_the_board_like_table (matrix) -> None:

    for i in matrix:

        print (i)

    return  None


def user_choice (matrix) -> list[int]:

    user_decision_height = input("please enter your location of height: ")
    user_decision_width = input("please enter your location of width: ")

    good_input = True

    while good_input:
        try:
            change_to_int_the_height = int(user_decision_height)
            change_to_int_the_width = int(user_decision_width)
            good_input = False
        except:
            print("please enter good location")
            user_decision_height = input("please enter your location of height: ")
            user_decision_width = input("please enter your location of width: ")

    user_location = [change_to_int_the_height, change_to_int_the_width]

    return user_location


def check_user_choice()
    if change_to_int_the_height >= len(matrix) - 1:
        good_input = False
    elif change_to_int_the_width >= len(matrix) - 1:
        good_input = False