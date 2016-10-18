class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.h,self.l,self.n = len(board),len(board[0]),0
        self.fdict = {}
        self.start = False
        self.board = board
        for i in range(0,self.h):
            for j in range(0,self.l):
                if self.fdict.get(i,{}).get(j,False) == True:
                    continue
                if self.board[i][j] == 'X':
                    self.start = True
                    self.checkEnd(i,j)
        return self.n

    def checkEnd(self,i,j):
        # check the end of the ship
        if self.board[i][j] == '.':
            if self.start:
                self.n += 1
                self.start = False
            self.recDict( i, j)
        else:
            self.recDict( i, j)
            if i+1 >= self.h:
                if j+1 >= self.l:
                    self.n += 1
                    self.start = False
                else:
                    self.checkEnd(i,j+1)
            else:
                if j+1 >= self.l:
                    self.checkEnd(i+1,j)
                else:
                    self.checkEnd(i,j+1)
                    self.checkEnd(i+1,j)

    def recDict(self, i, j):
        if self.fdict.get(i,False) == False:
            self.fdict[i] = {}
        self.fdict[i][j] = True