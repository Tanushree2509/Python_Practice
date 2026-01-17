def index_of_first_occurance(row:list, elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    try:
        return row.index(elem)
    except ValueError:
        return -1

def index_of_last_occurance(row:list, elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    try:
        return len(row) - 1 - row[::-1].index(elem)
    except ValueError:
        return -1

def is_valid_coordinate(x:int, y:int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''
    if x < 0 or y < 0:
        return False
    if x >= len(M):
        return False
    return y < len(M[x])

def valid_adjacent_coordinates(x:int, y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
        (nx, ny)
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        if is_valid_coordinate(nx, ny, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''
    x, y = curr_coords
    for nx, ny in valid_adjacent_coordinates(x, y, M):
        if (nx, ny) != prev_coords and M[nx][ny] == value:
            return (nx, ny)
    return None

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    start_x = len(M) - 1
    start_y = index_of_last_occurance(M[start_x], 1)
    end_x = 0
    end_y = index_of_first_occurance(M[0], 1)

    curr = (start_x, start_y)
    prev = None
    path = [curr]

    while curr != (end_x, end_y):
        nxt = next_coordinate_with_value(curr, 1, M, prev)
        if not nxt:
            break
        path.append(nxt)
        prev, curr = curr, nxt
    return path

def print_path(M):
    for x, y in get_path_coordinates(M):
        print(f"({x}, {y})")
if __name__ == "__main__":
    rows = int(input("Enter number of rows in the matrix: "))
    matrix = []

    print("Enter each row as space-separated 0s and 1s:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        matrix.append(row)

    print("\nPath formed by 1s from last row to first row:")
    print_path(matrix)