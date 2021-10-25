class theChessPiece:
    color = 0
    name = ""
    x = 0
    y = 0

#검은색 폰 정의
B1_Pawn = theChessPiece()
B1_Pawn.name = "B1Pawn"
B1_Pawn.x = 0
B1_Pawn.y = 6

B2_Pawn = theChessPiece()
B2_Pawn.name = "B2Pawn"
B2_Pawn.x = 1
B2_Pawn.y = 6

B3_Pawn = theChessPiece()
B3_Pawn.name = "B3Pawn"
B3_Pawn.x = 2
B3_Pawn.y = 6

B4_Pawn = theChessPiece()
B4_Pawn.name = "B4Pawn"
B4_Pawn.x = 3
B4_Pawn.y = 6

B5_Pawn = theChessPiece()
B5_Pawn.name = "B5Pawn"
B5_Pawn.x = 4
B5_Pawn.y = 6

B6_Pawn = theChessPiece()
B6_Pawn.name = "B6Pawn"
B6_Pawn.x = 5
B6_Pawn.y = 6

B7_Pawn = theChessPiece()
B7_Pawn.name = "B7Pawn"
B7_Pawn.x = 6
B7_Pawn.y = 6

B8_Pawn = theChessPiece()
B8_Pawn.name = "B8Pawn"
B8_Pawn.x = 7
B8_Pawn.y = 6

#검은색 왼쪽 룩 정의
B1_Rook = theChessPiece()
B1_Rook.name = "B1Rook"
B1_Rook.x = 0
B1_Rook.y = 7

#검은색 왼쪽 나이트 정의
B1_Knight = theChessPiece()
B1_Knight.name = "B1Knight"
B1_Knight.x = 1
B1_Knight.y = 7

#검은색 왼쪽 비숍정의
B1_Bishop = theChessPiece()
B1_Bishop.name = "B1Bishop"
B1_Bishop.x = 2
B1_Bishop.y = 7

#검은색 킹 정의
B1_King = theChessPiece()
B1_King.name = "B1King"
B1_King.x = 3
B1_King.y = 7

#검은색 퀸 정의
B1_Queen = theChessPiece()
B1_Queen.name = "B1Queen"
B1_Queen.x = 4
B1_Queen.y = 7

#검은색 오른쪽 비숍정의
B2_Bishop = theChessPiece()
B2_Bishop.name = "B2Bishop"
B2_Bishop.x = 5
B2_Bishop.y = 7

#검은색 오른쪽 나이트 정의
B2_Knight = theChessPiece()
B2_Knight.name = "B2Knight"
B2_Knight.x = 6
B2_Knight.y = 7

#검은색 오른쪽 룩 정의
B2_Rook = theChessPiece()
B2_Rook.name = "B2Rook"
B2_Rook.x = 7
B2_Rook.y = 7

#흰색 폰 정의
W1_Pawn = theChessPiece()
W1_Pawn.name = "W1Pawn"
W1_Pawn.x = 0
W1_Pawn.y = 1

W2_Pawn = theChessPiece()
W2_Pawn.name = "W2Pawn"
W2_Pawn.x = 1
W2_Pawn.y = 1

W3_Pawn = theChessPiece()
W3_Pawn.name = "W3Pawn"
W3_Pawn.x = 2
W3_Pawn.y = 1

W4_Pawn = theChessPiece()
W4_Pawn.name = "W4Pawn"
W4_Pawn.x = 3
W4_Pawn.y = 1

W5_Pawn = theChessPiece()
W5_Pawn.name = "W5Pawn"
W5_Pawn.x = 4
W5_Pawn.y = 1

W6_Pawn = theChessPiece()
W6_Pawn.name = "W6Pawn"
W6_Pawn.x = 5
W6_Pawn.y = 1

W7_Pawn = theChessPiece()
W7_Pawn.name = "W7Pawn"
W7_Pawn.x = 6
W7_Pawn.y = 1

W8_Pawn = theChessPiece()
W8_Pawn.name = "W8Pawn"
W8_Pawn.x = 7
W8_Pawn.y = 1

#흰색 왼쪽 룩 정의
W1_Rook = theChessPiece()
W1_Rook.name = "W1Rook"
W1_Rook.x = 0
W1_Rook.y = 0

#흰색 왼쪽 나이트 정의
W1_Knight = theChessPiece()
W1_Knight.name = "W1Knight"
W1_Knight.x = 1
W1_Knight.y = 0

#흰색 왼쪽 비숍정의
W1_Bishop = theChessPiece()
W1_Bishop.name = "W1Bishop"
W1_Bishop.x = 2
W1_Bishop.y = 0

#흰색 킹 정의
W1_King = theChessPiece()
W1_King.name = "W1King"
W1_King.x = 3
W1_King.y = 0

#흰색 퀸 정의
W1_Queen = theChessPiece()
W1_Queen.name = "W1Queen"
W1_Queen.x = 4
W1_Queen.y = 0

#흰색 오른쪽 비숍정의
W2_Bishop = theChessPiece()
W2_Bishop.name = "W2Bishop"
W2_Bishop.x = 5
W2_Bishop.y = 0

#흰색 오른쪽 나이트 정의
W2_Knight = theChessPiece()
W2_Knight.name = "W2Knight"
W2_Knight.x = 6
W2_Knight.y = 0


#흰색 오른쪽 룩 정의
W2_Rook = theChessPiece()
W2_Rook.name = "W2Rook"
W2_Rook.x = 7
W2_Rook.y = 0


def Place_Piece(Piecename):
    Chess_Piece_Board[Piecename.y][Piecename.x] = Piecename.name

#B는 아랫사람(검은말), 1은 왼쪽, 2는 오른쪽 말을 뜻함.
def Placing_all_Piece():
    Place_Piece(B1_Pawn)
    Place_Piece(B2_Pawn)
    Place_Piece(B3_Pawn)
    Place_Piece(B4_Pawn)
    Place_Piece(B5_Pawn)
    Place_Piece(B6_Pawn)
    Place_Piece(B7_Pawn)
    Place_Piece(B8_Pawn)
    Place_Piece(B1_Rook)
    Place_Piece(B1_Knight)
    Place_Piece(B1_Bishop)
    Place_Piece(B1_King)
    Place_Piece(B1_Queen)
    Place_Piece(B2_Bishop)
    Place_Piece(B2_Knight)
    Place_Piece(B2_Rook)
    Place_Piece(W1_Pawn)
    Place_Piece(W2_Pawn)
    Place_Piece(W3_Pawn)
    Place_Piece(W4_Pawn)
    Place_Piece(W5_Pawn)
    Place_Piece(W6_Pawn)
    Place_Piece(W7_Pawn)
    Place_Piece(W8_Pawn)
    Place_Piece(W1_Rook)
    Place_Piece(W1_Knight)
    Place_Piece(W1_Bishop)
    Place_Piece(W1_King)
    Place_Piece(W1_Queen)
    Place_Piece(W2_Bishop)
    Place_Piece(W2_Knight)
    Place_Piece(W2_Rook)

#체스 보드 맵 버튼에 보이는 텍스트의 조작을 위하여 구성
Chess_Piece_Board = [["","","","","","","",""],
                     ["","","","","","","",""],
                     ["","","","","","","",""],
                     ["","","","","","","",""],
                     ["","","","","","","",""],
                     ["","","","","","","",""],
                     ["","","","","","","",""],
                     ["","","","","","","",""]]

Chess_Available_Move_Board = [["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""]]

#말의 이동가능한 지점을 표시하기 위하여 사용 
def Check_Available_Move(Piece_Name, x , y):
    if Piece_Name != "":
        Color_str = str(Piece_Name)[0:1] 
        Piece_Name_str = str(Piece_Name)[2:]
    else:
        Color_str = "k"

    if Color_str == "B":
        if Piece_Name_str == "Rook":
            for t in range (4):
                px = x
                py = y
                blocked = 0
                for i in range (7):
                    if blocked == 0:
                        if t == 0:
                            py -= 1
                        elif t == 1:
                            py += 1
                        elif t == 2:
                            px -= 1
                        else:
                            px += 1
                        if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                            try:
                                if Chess_Piece_Board[py][px] != "":
                                    blocked = 1
                                    if Chess_Piece_Board[py][px][0] == "W":
                                        Chess_Available_Move_Board[py][px] = "Attack"
                                else:
                                    Chess_Available_Move_Board[py][px] = "Move"
                            except IndexError as e:
                                pass
                    else:
                        break
        elif Piece_Name_str == "Bishop":
                for t in range (4):
                    px = x 
                    py = y
                    blocked = 0
                    for i in range (7):
                        if blocked == 0:
                            if t == 0:
                                py -= 1
                                px -= 1

                            elif t == 1:
                                py += 1
                                px -= 1

                            elif t == 2:
                                py -= 1
                                px += 1

                            else:
                                py += 1
                                px += 1

                            if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                                try:
                                    if Chess_Piece_Board[py][px] != "":
                                        blocked = 1
                                        if Chess_Piece_Board[py][px][0] == "W":
                                            Chess_Available_Move_Board[py][px] = "Attack"
                                    else:
                                        Chess_Available_Move_Board[py][px] = "Move"
                                except IndexError as e:
                                    pass
                        else:
                            break
        elif Piece_Name_str == "Pawn":
            blocked = 0
            px = x 
            py = y
            if str(px + 1) == Piece_Name[1] and py == 6:
                py -= 1
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    if Chess_Available_Move_Board[py][px] == "":
                        if Chess_Piece_Board[py][px] == "":
                            Chess_Available_Move_Board[py][px] = "Move"
                        else:
                            blocked = 1
                if blocked == 0:
                    px = x 
                    py = y
                    py -= 2
                    if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                        if Chess_Available_Move_Board[py][px] == "":
                            if Chess_Piece_Board[py][px] == "":
                                Chess_Available_Move_Board[py][px] = "Move"  
            else:
                py -= 1
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    if Chess_Available_Move_Board[py][px] == "":
                        if Chess_Piece_Board[py][px] == "":
                            Chess_Available_Move_Board[py][px] = "Move"
            #폰의 대각선 이동(상대를 잡을 수 있을 때)
            px = x 
            py = y
            px += 1
            py -= 1
            if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                try:
                    if Chess_Piece_Board[py][px] != "":
                        if Chess_Piece_Board[py][px][0] == "W":
                            Chess_Available_Move_Board[py][px] = "Attack"
                except IndexError as e:
                    pass
            px = x 
            py = y
            px -= 1
            py -= 1
            if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                try:
                    if Chess_Piece_Board[py][px] != "":
                        if Chess_Piece_Board[py][px][0] == "W":
                            Chess_Available_Move_Board[py][px] = "Attack"
                except IndexError as e:
                    pass
        elif Piece_Name_str == "Knight":
            for t in range (8):
                px = x 
                py = y
                if t == 0:
                    px += 1
                    py += 2
                elif t == 1:
                    px += 2
                    py += 1
                elif t == 2:
                    px += 2
                    py -= 1
                elif t == 3:
                    px += 1
                    py -= 2
                elif t == 4:
                    px -= 1
                    py -= 2
                elif t == 5:
                    px -= 2
                    py -= 1
                elif t == 6:
                    px -= 2
                    py += 1
                else:
                    px -= 1
                    py += 2
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    try:
                        if Chess_Piece_Board[py][px] != "":
                            blocked = 1
                            if Chess_Piece_Board[py][px][0] == "W":
                                Chess_Available_Move_Board[py][px] = "Attack"
                        else:
                            Chess_Available_Move_Board[py][px] = "Move"
                    except IndexError as e:
                        pass
        elif Piece_Name_str == "King":
            for t in range (8):
                px = x 
                py = y
                if t == 0:
                    px += 1
                    py += 1

                elif t == 1:
                    px += 1

                elif t == 2:
                    px += 1
                    py -= 1

                elif t == 3:
                    py -= 1
                
                elif t == 4:
                    px -= 1
                    py -= 1

                elif t == 5:
                    px -= 1

                elif t == 6:
                    px -= 1
                    py += 1

                else:
                    py += 1
                    
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    try:
                        if Chess_Piece_Board[py][px] != "":
                            blocked = 1
                            if Chess_Piece_Board[py][px][0] == "W":
                                Chess_Available_Move_Board[py][px] = "Attack"
                        else:
                            Chess_Available_Move_Board[py][px] = "Move"
                    except IndexError as e:
                        pass
            if str(Chess_Piece_Board[0][0])[2:] == "Rook" and Chess_Piece_Board[0][1] == "" and Chess_Piece_Board[0][2] == "":
                Chess_Available_Move_Board[0][1] == "Move"
    
        elif Piece_Name_str == "Queen":
            for t in range (4):
                px = x 
                py = y
                blocked = 0
                for i in range (7):
                    if blocked == 0:
                        if t == 0:
                            py -= 1
                            px -= 1

                        elif t == 1:
                            py += 1
                            px -= 1

                        elif t == 2:
                            py -= 1
                            px += 1

                        else:
                            py += 1
                            px += 1

                        if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                            try:
                                if Chess_Piece_Board[py][px] != "":
                                    blocked = 1
                                    if Chess_Piece_Board[py][px][0] == "W":
                                        Chess_Available_Move_Board[py][px] = "Attack"
                                else:
                                    Chess_Available_Move_Board[py][px] = "Move"
                            except IndexError as e:
                                pass
                    else:
                        break
            for t in range (4):
                px = x 
                py = y
                blocked = 0
                for i in range (7):
                    if blocked == 0:
                        if t == 0:
                            py -= 1

                        elif t == 1:
                            py += 1

                        elif t == 2:
                            px -= 1

                        else:
                            px += 1

                        if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                            try:
                                if Chess_Piece_Board[py][px] != "":
                                    blocked = 1
                                    if Chess_Piece_Board[py][px][0] == "W":
                                        Chess_Available_Move_Board[py][px] = "Attack"
                                else:
                                    Chess_Available_Move_Board[py][px] = "Move"
                            except IndexError as e:
                                pass
                    else:
                        break
    elif Color_str == "W":
        if Piece_Name_str == "Rook":
            for t in range (4):
                px = x
                py = y
                blocked = 0
                for i in range (7):
                    if blocked == 0:
                        if t == 0:
                            py -= 1
                        elif t == 1:
                            py += 1
                        elif t == 2:
                            px -= 1
                        else:
                            px += 1
                        if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                            try:
                                if Chess_Piece_Board[py][px] != "":
                                    blocked = 1
                                    if Chess_Piece_Board[py][px][0] == "B":
                                        Chess_Available_Move_Board[py][px] = "Attack"
                                else:
                                    Chess_Available_Move_Board[py][px] = "Move"
                            except IndexError as e:
                                pass
                    else:
                        break
        elif Piece_Name_str == "Bishop":
            for t in range (4):
                px = x 
                py = y
                blocked = 0
                for i in range (7):
                    if blocked == 0:
                        if t == 0:
                            py -= 1
                            px -= 1

                        elif t == 1:
                            py += 1
                            px -= 1

                        elif t == 2:
                            py -= 1
                            px += 1

                        else:
                            py += 1
                            px += 1

                        if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                            try:
                                if Chess_Piece_Board[py][px] != "":
                                    blocked = 1
                                    if Chess_Piece_Board[py][px][0] == "B":
                                        Chess_Available_Move_Board[py][px] = "Attack"
                                else:
                                    Chess_Available_Move_Board[py][px] = "Move"
                            except IndexError as e:
                                pass
                    else:
                        break
        elif Piece_Name_str == "Pawn":
            blocked = 0
            px = x 
            py = y
            if str(px + 1) == Piece_Name[1] and py == 1:
                py += 1
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    if Chess_Available_Move_Board[py][px] == "":
                        if Chess_Piece_Board[py][px] == "":
                            Chess_Available_Move_Board[py][px] = "Move"
                        else:
                            blocked = 1
                if blocked == 0:
                    px = x 
                    py = y
                    py += 2
                    if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                        if Chess_Available_Move_Board[py][px] == "":
                            if Chess_Piece_Board[py][px] == "":
                                Chess_Available_Move_Board[py][px] = "Move"  
            else:
                py += 1
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    if Chess_Available_Move_Board[py][px] == "":
                        if Chess_Piece_Board[py][px] == "":
                            Chess_Available_Move_Board[py][px] = "Move"
            #폰의 대각선 이동(상대를 잡을 수 있을 때)
            
            px = x 
            py = y
            px += 1
            py += 1
            if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                try:
                    if Chess_Piece_Board[py][px] != "":
                        if Chess_Piece_Board[py][px][0] == "B":
                            Chess_Available_Move_Board[py][px] = "Attack"
                except IndexError as e:
                    pass
                
            px = x 
            py = y
            px -= 1
            py += 1
            if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                try:
                    if Chess_Piece_Board[py][px] != "":
                        if Chess_Piece_Board[py][px][0] == "B":
                            Chess_Available_Move_Board[py][px] = "Attack"
                except IndexError as e:
                    pass
        elif Piece_Name_str == "Knight":
            for t in range (8):
                px = x 
                py = y
                if t == 0:
                    px += 1
                    py += 2
                elif t == 1:
                    px += 2
                    py += 1
                elif t == 2:
                    px += 2
                    py -= 1
                elif t == 3:
                    px += 1
                    py -= 2
                elif t == 4:
                    px -= 1
                    py -= 2
                elif t == 5:
                    px -= 2
                    py -= 1
                elif t == 6:
                    px -= 2
                    py += 1
                else:
                    px -= 1
                    py += 2
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    try:
                        if Chess_Piece_Board[py][px] != "":
                            blocked = 1
                            if Chess_Piece_Board[py][px][0] == "B":
                                Chess_Available_Move_Board[py][px] = "Attack"
                        else:
                            Chess_Available_Move_Board[py][px] = "Move"
                    except IndexError as e:
                        pass

        elif Piece_Name_str == "King":
            for t in range (8):
                px = x 
                py = y
                if t == 0:
                    px += 1
                    py += 1

                elif t == 1:
                    px += 1

                elif t == 2:
                    px += 1
                    py -= 1

                elif t == 3:
                    py -= 1
                
                elif t == 4:
                    px -= 1
                    py -= 1

                elif t == 5:
                    px -= 1

                elif t == 6:
                    px -= 1
                    py += 1

                else:
                    py += 1
                    
                if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                    try:
                        if Chess_Piece_Board[py][px] != "":
                            blocked = 1
                            if Chess_Piece_Board[py][px][0] == "B":
                                Chess_Available_Move_Board[py][px] = "Attack"
                        else:
                            Chess_Available_Move_Board[py][px] = "Move"
                    except IndexError as e:
                        pass
        elif Piece_Name_str == "Queen":
            for t in range (4):
                px = x 
                py = y
                blocked = 0
                for i in range (7):
                    if blocked == 0:
                        if t == 0:
                            py -= 1
                            px -= 1

                        elif t == 1:
                            py += 1
                            px -= 1

                        elif t == 2:
                            py -= 1
                            px += 1

                        else:
                            py += 1
                            px += 1

                        if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                            try:
                                if Chess_Piece_Board[py][px] != "":
                                    blocked = 1
                                    if Chess_Piece_Board[py][px][0] == "B":
                                        Chess_Available_Move_Board[py][px] = "Attack"
                                else:
                                    Chess_Available_Move_Board[py][px] = "Move"
                            except IndexError as e:
                                pass
                    else:
                        break
            for t in range (4):
                px = x 
                py = y
                blocked = 0
                for i in range (7):
                    if blocked == 0:
                        if t == 0:
                            py -= 1

                        elif t == 1:
                            py += 1

                        elif t == 2:
                            px -= 1

                        else:
                            px += 1

                        if px <= 7 and py <= 7 and px >= 0 and py >= 0 :
                            try:
                                if Chess_Piece_Board[py][px] != "":
                                    blocked = 1
                                    if Chess_Piece_Board[py][px][0] == "B":
                                        Chess_Available_Move_Board[py][px] = "Attack"
                                else:
                                    Chess_Available_Move_Board[py][px] = "Move"
                            except IndexError as e:
                                pass

                    else:
                        break

    else:
        pass