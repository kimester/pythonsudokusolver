def find_next_empty(puzzle):
    #finds the next row,col on the puzzle that's not filled yet --> rep with -1
    #return row, col tuple (or(None, None) if there is none)
    
    #keep in mind that we are using 0-8 for our indices
    for r in range(9): #each row in range 9
        for c in range (9): #range (9) is 0,1,2,...8
            if puzzle 

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    #our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return wheater a soulution exists
    # mutates puzzle to be the solution ( if solution exists)
    
    #step1: choose somehwere on the puzzle to make a guess 
    row, col = find_next_empty(puzzle)