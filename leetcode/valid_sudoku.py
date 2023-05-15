class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for sudoku_row in board:
            
            row_duplicates = {

            }

            for row_cell in sudoku_row:

                # if it's a blank (.) then continue

                if(row_cell == "."):
                    continue 

                if row_duplicates.get(row_cell) is not None:
                    # this value has already shown up on this row 
                    return False

                else:
                    row_duplicates[row_cell] = 1

            
        # validate the columns
        
        for i in range(0, 9):

            cell_duplicates = {}

            for column in range(0, 9):
                
                if(board[column][i] ==  "."):
                    continue 

                if cell_duplicates.get(board[column][i]) is not None:
                    return False
                else:
                    cell_duplicates[board[column][i]] = 1

        
        # i represents the "row" of the subbox in the 9x9 grid 
        for i in range(0, 3):
            
            # j represents the column of the subbox in the 9x9 grid 

            for j in range(0, 3):

                # row offset: + (i*3)
                # column offset: + (j * 3)
                
                found_characters_subbox = {}
                
                # k represents the first cell of each subbox
                subgrid_values = {}
                some_not_blank = False 

                for k in range(0, 3):
                    base = board[ i*3 ][k + j * 3]
                    base_2 = board[ i*3 + 1 ][k + j*3]
                    base_3 = board[ i * 3 + 2][k + j*3]
                    

                    if base != "." and subgrid_values.get(base) is not None:
                            return False
                    else:
                         subgrid_values[base] = 1
                    
                    if base_2 != "." and subgrid_values.get(base_2) is not None:
                            return False
                    else:
                         subgrid_values[base_2] = 1
                    
                    if base_3 != "." and subgrid_values.get(base_3) is not None:
                            return False
                    else:
                         subgrid_values[base_3] = 1

                    
                    # if base != '.' or base_2 != '.' or base_3 != '.':
                    #      some_not_blank = True
                
                # if some_not_blank == False:
                #     return False 

                    
                    # check if any are not empty 

                    # print(base,  "-", base_2, " -", base_3)
                
                # print("\n")
            
        
        return True 
