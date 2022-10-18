class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir_array = [[0,1], [1,0],[-1,0],[-1,1],[0,-1],[-1,-1],[1,-1],[1,1]] # Create an dir_array to store all directions of neighboring values
        
        m = len(board)  # length of rows
        n = len(board[0]) # length of columns
       
        
        for i in range(m):  # run until the length of rows
            for j in range(n):  # run until the length of columns
                count = 0

                for r, c in dir_array:
                    nr = r+i    #nr is the neighboring row 
                    nc = c+j    #nc is the neighboring column
                    
                    
                    if nr >= 0 and nr < m and nc >= 0 and nc < n: # if nr is greater than or equal to 0 and less than m and nc is greater than or equal to 0 and less than n
                        if board[nr][nc] == -1 or board[nr][nc] == 1: # if board[nr][nc] is equal to -1 or board[nr][nc] is equal to 1
                            count+=1 # increment count by 1
                            
                if board[i][j] == 1: # if the board[i][j] is equal to 1
                    if count < 2 or count > 3: # if count is less than 2 or greater than 3
                        board[i][j] = -1 # change the value to -1
                        
                else:   
                    if count == 3:  # if the count is equal to 3 
                        board[i][j] = 2 # change the value to 2
                        
        for i in range(m):  # for the length of rows
            for j in range(n):  # for the length of columns
                if board[i][j] == -1:   # if board[i][j] is equal to -1 
                    board[i][j] = 0 # change tha value to 0
                elif board[i][j] == 2:  # if board[i][j] is equal to 2 
                    board[i][j] = 1 # change the value to 1