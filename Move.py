from ChessPiece import Chess_Available_Move_Board, Chess_Piece_Board

def Move(Piece_Name, x,y):
    if Chess_Available_Move_Board[x][y] == "Move" or Chess_Available_Move_Board[x][y] == "Attack":
        Chess_Piece_Board[x][y] = ""
        for i in range(8):
            for t in range(8):
                if Chess_Piece_Board[i][t] == Saved:
                    Chess_Piece_Board[i][t] = ""
                else:
                    pass
        Chess_Piece_Board[x][y] = Piece_Name
    else:
        pass
Turn = 0
Saved = "" 
