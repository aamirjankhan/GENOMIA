import numpy as np

delta = lambda x, y, i, j: 1 if x[i] != y[j] else 0
solution = []

def find_solution(OPT, m, n):
    if m == 0 and n == 0:
        return

    # We can only do insert if n != 0, align if there are element in both x, y, etc.
    insert = OPT[m][n - 1] + 1 if n != 0 else float("inf")
    align = (
        OPT[m - 1][n - 1] + delta(x, y, m - 1, n - 1)
        if m != 0 and n != 0
        else float("inf")
    )
    delete = OPT[m - 1][n] + 1 if m != 0 else float("inf")

    best_choice = min(insert, align, delete)

    if best_choice == insert:
        solution.append("insert_" + str(y[n - 1]))
        return find_solution(OPT, m, n - 1)

    elif best_choice == align:
        solution.append("align_" + str(y[n - 1]))
        return find_solution(OPT, m - 1, n - 1)

    elif best_choice == delete:
        solution.append("remove_" + str(x[m - 1]))
        return find_solution(OPT, m - 1, n)


def Alignment(x, y):
    n= len(y)
    m= len(x)

    opt_matrix= [[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(1, m+1):
        opt_matrix[i][0]= i

    for j in range(1, n+1):
        opt_matrix[0][j]= j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            opt_matrix[i][j] = min(
                opt_matrix[i - 1][j - 1] + delta(x, y, i - 1, j - 1),
                opt_matrix[i - 1][j] + 1,
                opt_matrix[i][j - 1] + 1,
            )  # align, delete, insert respectively

    return opt_matrix[m][n]
    # for line in opt_matrix:
    #     print(line)


if __name__=='__main__':
    x= "TGACGTGC"
    y= "TCGACGTCA"
    optimal_edit_steps= Alignment(x, y)
    print(optimal_edit_steps)
    # find_solution(OPT, m, n)