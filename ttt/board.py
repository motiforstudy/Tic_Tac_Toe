



def make_the_board (len_of_matrix) -> list[list]:

    matrix = []

    for i in range(len_of_matrix):

        vector = []

        for x in range(len_of_matrix):

            vector.append("_")

        matrix.append(vector)

    return matrix