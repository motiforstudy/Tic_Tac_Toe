from ttt.board import make_the_board
from ttt.io import print_the_board_like_table, user_choice




create_the_board = make_the_board(3)
print(len(create_the_board))
print_by_line = print_the_board_like_table(create_the_board)
get_user_choice = user_choice(create_the_board)
print(get_user_choice)
print(type(get_user_choice[1]))