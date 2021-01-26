def sudoku_solver(arr):
    ret_sample = [x[:] for x in arr]
    copy_arr = arr[:]
    solved = False
    while not solved:
        #print_game(copy_arr)
        #input()
        solved = True
        for row in range(0,9):
            for column in range(0,9):
                if copy_arr[row][column] == 0:
                    solved = False
                    list_of_checks = [check_not_in_row(copy_arr[row]),check_not_in_column(get_column(copy_arr, column)),check_not_in_matrix(row, column, copy_arr)]
                    for one_elem in list_of_checks:
                        if len(one_elem) == 1:
                            copy_arr[row][column] = one_elem[0]
                            
                            break
                    intersection_set = set()
                    intersection_set = set(list_of_checks[0]).intersection(list_of_checks[1])
                    intersection_set = intersection_set.intersection(list_of_checks[2])
                    if len(intersection_set) == 1:
                        copy_arr[row][column] = list(intersection_set)[0]
                        break
                    else:
                        values = get_corner(row, column)
                        list_of_sets = []
                        for elem in intersection_set:
                            for set_row in range(0 + values[0], 0 + values[0] + 3):
                                if set_row != row:
                                    list_of_sets.append(set(check_in_row(copy_arr[set_row])))
                            for set_column in range(0 + values[1], 0 + values[1] + 3):
                                if set_column != column:
                                    list_of_sets.append(set(check_in_column(get_column(copy_arr, set_column))))
                            check_sets_intersection = set.intersection(list_of_sets[0], list_of_sets[1], list_of_sets[2], list_of_sets[3])
                            if len(check_sets_intersection) == 0:
                                list_of_sets.clear()
                                continue
                            elif len(check_sets_intersection) == 1:
                                temp_list = list(check_sets_intersection)
                                if temp_list[0] == elem:
                                    copy_arr[row][column] = temp_list[0]
                                    break
                                else:
                                    list_of_sets.clear()
                                    break
                            else:
                               list_of_sets.clear()
                               break
                        
                        
                            
    print_game(copy_arr)
    if sudoku_checker(copy_arr):
        final_list = []
        for rows in ret_sample:
            str_row = [str(elem) for elem in rows]
            final_list.append("".join(str_row))
        print("".join(final_list))
        
    
            
def sudoku_loader(sudoku_strng):
    arr_ret = [[],[],[],[],[],[],[],[],[]]
    count = 0
    for row in range(0,9):
        for _ in range(0,9):
            arr_ret[row].append(int(sudoku_strng[count]))
            count += 1

    return arr_ret

def sudoku_checker(arr):
    # CHECK ROWS
    for row in range(0, 9):
        s_row = set(arr[row])
        if len(s_row) != 9: return False
        
        # CHECK COLUMN
        s_column = set()
        for column in range(0, 9):
            s_column.add(arr[column][row])
        if len(s_column) != 9: return False

    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            check_set = set()
            for s_row in range(0, 3):
                for s_column in range(0, 3):
                    check_set.add(arr[row + s_row][column + s_column])
            if len(check_set) != 9: return False
    return True


def print_game(arr):
    print("""             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}
             {} {} {} {} {} {} {} {} {}"""
          .format(arr[0][0], arr[0][1], arr[0][2], arr[0][3], arr[0][4], arr[0][5], arr[0][6], arr[0][7], arr[0][8],
                  arr[1][0], arr[1][1], arr[1][2], arr[1][3], arr[1][4], arr[1][5], arr[1][6], arr[1][7], arr[1][8],
                  arr[2][0], arr[2][1], arr[2][2], arr[2][3], arr[2][4], arr[2][5], arr[2][6], arr[2][7], arr[2][8],
                  arr[3][0], arr[3][1], arr[3][2], arr[3][3], arr[3][4], arr[3][5], arr[3][6], arr[3][7], arr[3][8],
                  arr[4][0], arr[4][1], arr[4][2], arr[4][3], arr[4][4], arr[4][5], arr[4][6], arr[4][7], arr[4][8],
                  arr[5][0], arr[5][1], arr[5][2], arr[5][3], arr[5][4], arr[5][5], arr[5][6], arr[5][7], arr[5][8],
                  arr[6][0], arr[6][1], arr[6][2], arr[6][3], arr[6][4], arr[6][5], arr[6][6], arr[6][7], arr[6][8],
                  arr[7][0], arr[7][1], arr[7][2], arr[7][3], arr[7][4], arr[7][5], arr[7][6], arr[7][7], arr[7][8],
                  arr[8][0], arr[8][1], arr[8][2], arr[8][3], arr[8][4], arr[8][5], arr[8][6], arr[8][7], arr[8][8]))
                  
                  


def get_corner(row, column):
    ret_val = []
    if row in range(0,3):
        ret_val.append(0)
    elif row in range(3,6):
        ret_val.append(3)
    else:
        ret_val.append(6)
        
    if column in range(0,3):
        ret_val.append(0)
    elif column in range(3,6):
        ret_val.append(3)
    else:
        ret_val.append(6)
    return ret_val


def check_not_in_row(row):
    not_in_row = []
    for num in range(1,10):
        if num not in row:
            not_in_row.append(num)
    return not_in_row


def check_in_row(row):
    in_row = []
    for num in range(1,10):
        if num in row:
            in_row.append(num)
    return in_row


def get_column(arr, column):
    column_list = []
    for num in range(0,9):
        column_list.append(arr[num][column])
    return column_list


def check_not_in_column(column):
    not_in_column = []
    for num in range(1,10):
        if num not in column:
            not_in_column.append(num)
    return not_in_column


def check_in_column(column):
    in_column = []
    for num in range(1,10):
        if num in column:
            in_column.append(num)
    return in_column


def get_matrix(row, column, arr):
    s_row = 0
    s_column = 0
    
    if row in range(0,3):
        s_row = 0
    elif row in range(3,6):
        s_row = 3
    else: s_row = 6

    if column in range(0,3):
        s_column = 0
    elif column in range(3,6):
        s_column = 3
    else: s_column = 6
    small_matrix = []
    for check_row in range(0,3):
        for check_column in range(0,3):
            small_matrix.append(arr[s_row + check_row][s_column + check_column])
    return small_matrix


def check_in_matrix(row, column, arr):
    s_matrix = get_matrix(row, column, arr)
    in_matrix = []
    for num in range(1,10):
        if num in s_matrix:
            in_matrix.append(num)
    return in_matrix

def check_not_in_matrix(row, column, arr):
    s_matrix = get_matrix(row, column, arr)
    not_in_matrix = []
    for num in range(1,10):
        if num not in s_matrix:
            not_in_matrix.append(num)
    return not_in_matrix
            


sudoku_solver(sudoku_loader("406751080208000470000000906530200000649130000007905100070829050062010038180007009"))
