import tkinter as tk
import ChessPiece
import Move
from PIL import Image,ImageTk

Horizontal = 608
Vertical = 608

Num_of_blocks = 8

main =tk.Tk()
main.title("Main - ChessGame")
main.geometry(str(Horizontal)+"x"+str(Vertical))
main.configure(bg = "#ffffff")
canvas = tk.Canvas(
    main,
    bg = "#ffffff",
    height = 608,
    width = 608,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = ImageTk.PhotoImage(Image.open("CT1.jpg").resize((608,608), Image.ANTIALIAS))
#CT1은 CHESS문구 있는 버전, CT는 CHESS문구가 없는 버전
background = canvas.create_image(
    304, 304,
    image=background_img)
main.resizable(True, True)
BTNAI = tk.Button(text = "AI", font=("Courier", 40, "italic"), command= lambda: [main.destroy()])
BTNMU = tk.Button(text = "MULTI", font=("Courier", 40, "italic"), command = lambda: [main.destroy()])
BTNAI.place(x=248, y=250)
BTNMU.place(x=200, y=400)
main.mainloop()

theChessBoard =tk.Tk()
theChessBoard.title("Chess")
theChessBoard.geometry(str(Horizontal)+"x"+str(Vertical))
theChessBoard.resizable(True, True)

b1 = ImageTk.PhotoImage(Image.open("Icon/black_rook.png").resize((55,55), Image.ANTIALIAS))
b2 = ImageTk.PhotoImage(Image.open("Icon/black_knight.png").resize((55,55), Image.ANTIALIAS))
b3 = ImageTk.PhotoImage(Image.open("Icon/black_bishop.png").resize((55,55), Image.ANTIALIAS))
b4 = ImageTk.PhotoImage(Image.open("Icon/black_king.png").resize((55,55), Image.ANTIALIAS))
b5 = ImageTk.PhotoImage(Image.open("Icon/black_queen.png").resize((55,55), Image.ANTIALIAS))
b6 = ImageTk.PhotoImage(Image.open("Icon/black_pawn.png").resize((55,55), Image.ANTIALIAS))
w1 = ImageTk.PhotoImage(Image.open("Icon/white_rook.png").resize((55,55), Image.ANTIALIAS))
w2 = ImageTk.PhotoImage(Image.open("Icon/white_knight.png").resize((55,55), Image.ANTIALIAS))
w3 = ImageTk.PhotoImage(Image.open("Icon/white_bishop.png").resize((55,55), Image.ANTIALIAS))
w4 = ImageTk.PhotoImage(Image.open("Icon/white_king.png").resize((55,55), Image.ANTIALIAS))
w5 = ImageTk.PhotoImage(Image.open("Icon/white_queen.png").resize((55,55), Image.ANTIALIAS))
w6 = ImageTk.PhotoImage(Image.open("Icon/white_pawn.png").resize((55,55), Image.ANTIALIAS))
blank = ImageTk.PhotoImage(Image.open("Icon/Blank.png").resize((55,55), Image.ANTIALIAS))

#Make Board with Button whice has command
def MakeButton(x, y):
    global a
    if ChessPiece.Chess_Available_Move_Board[x][y] == "Move":
        BTN_Text = str(ChessPiece.Chess_Piece_Board[x][y])[2:]
        BTN_Color = "Light Green"
        BTN_TEXT_Color = "Black"
        a=blank
    elif ChessPiece.Chess_Available_Move_Board[x][y] == "Attack":
        BTN_Text = str(ChessPiece.Chess_Piece_Board[x][y])[2:]
        BTN_Color = "Red"
        if ChessPiece.Chess_Piece_Board[x][y][0] == "W":
            if BTN_Text == "Rook":
                a=w1
            elif BTN_Text == "Knight":
                a=w2
            elif BTN_Text == "Bishop":
                a=w3
            elif BTN_Text == "King":
                a=w4
            elif BTN_Text == "Queen":
                a=w5
            elif BTN_Text == "Pawn":
                a=w6
        elif ChessPiece.Chess_Piece_Board[x][y][0] == "B":
            if BTN_Text == "Rook":
                a=b1
            elif BTN_Text == "Knight":
                a=b2
            elif BTN_Text == "Bishop":
                a=b3
            elif BTN_Text == "King":
                a=b4
            elif BTN_Text == "Queen":
                a=b5
            elif BTN_Text == "Pawn":
                a=b6
        else:
            a=blank
        BTN_TEXT_Color = "Black"
    elif ChessPiece.Chess_Piece_Board[x][y] == "":
        BTN_Color = "White"
        BTN_TEXT_Color = "Black"
        BTN_Text = str(ChessPiece.Chess_Piece_Board[x][y])[2:]
        a=blank
    elif ChessPiece.Chess_Piece_Board[x][y][0] == "W":
        BTN_Color = "Ivory2"
        BTN_TEXT_Color = "Black"
        BTN_Text = str(ChessPiece.Chess_Piece_Board[x][y])[2:]
        if BTN_Text == "Rook":
            a=w1
        elif BTN_Text == "Knight":
            a=w2
        elif BTN_Text == "Bishop":
            a=w3
        elif BTN_Text == "King":
            a=w4
        elif BTN_Text == "Queen":
            a=w5
        elif BTN_Text == "Pawn":
            a=w6     
    elif ChessPiece.Chess_Piece_Board[x][y][0] == "B":
        BTN_Color = "Black"
        BTN_TEXT_Color = "White"
        BTN_Text = str(ChessPiece.Chess_Piece_Board[x][y])[2:]
        if BTN_Text == "Rook":
            a=b1
        elif BTN_Text == "Knight":
            a=b2
        elif BTN_Text == "Bishop":
            a=b3
        elif BTN_Text == "King":
            a=b4
        elif BTN_Text == "Queen":
            a=b5
        elif BTN_Text == "Pawn":
            a=b6
    BTN =tk.Button(theChessBoard, width= 70, height= 70, overrelief="solid", bg = BTN_Color , fg = BTN_TEXT_Color , image = a , command= lambda: Change(ChessPiece.Chess_Piece_Board[x][y],x,y))
    BTN.grid(row= x, column= y)

#Reset 64 Pieces According to Chess_Piece_Board
def MakeBoard():
    for i in range(Num_of_blocks ):
        for j in range(Num_of_blocks):
            MakeButton(i, j)

#Remove the "Move" Button and Replace Piece
def ResetBoard():
    for i in range(Num_of_blocks ):
        for j in range(Num_of_blocks):
            ChessPiece.Chess_Available_Move_Board[i][j] = ""

#Command on Button Reset Board and Mark Available Moves
def Change(Piece_name,x,y):
    if Move.Turn == 0: #White Turn
        try:
            if ChessPiece.Chess_Piece_Board[x][y][0] == "W":
                Move.Move(Move.Saved,x,y)
                ResetBoard()
                ChessPiece.Check_Available_Move(Piece_name,y,x)
            elif ChessPiece.Chess_Piece_Board[x][y][0] == "":
                ResetBoard()
            elif ChessPiece.Chess_Available_Move_Board[x][y] == "Attack": #When Attack the Black Piece
                Check = ChessPiece.Chess_Piece_Board[x][y]
                Move.Turn = 1
                Move.Move(Move.Saved,x,y)
                ResetBoard()
                if  Check == "B1King":
                    theChessBoard.destroy()
                    Over =tk.Tk()
                    Over.title("GameOver")
                    label=tk.Label(Over, text="White Won", width=10, height=5, fg="black", relief="solid")
                    label.pack()
                    Over.mainloop          
                        
        except IndexError as e:
            if ChessPiece.Chess_Available_Move_Board[x][y] != "":
                if ChessPiece.Chess_Available_Move_Board[x][y] != "":
                    Move.Turn = 1
                Move.Move(Move.Saved,x,y)
                ResetBoard()
                ChessPiece.Check_Available_Move(Piece_name,y,x)
            else:
                ResetBoard()              
    else: #Black Turn
        try:
            if ChessPiece.Chess_Piece_Board[x][y][0] == "B":
                Move.Move(Move.Saved,x,y)
                ResetBoard()
                ChessPiece.Check_Available_Move(Piece_name,y,x)
            elif ChessPiece.Chess_Piece_Board[x][y][0] == "":
                ResetBoard()
            elif ChessPiece.Chess_Available_Move_Board[x][y] == "Attack": #When Attack the White Piece
                Check = ChessPiece.Chess_Piece_Board[x][y]
                Move.Turn = 0
                Move.Move(Move.Saved,x,y)
                ResetBoard()
                if  Check == "W1King":
                    theChessBoard.destroy()
                    Over =tk.Tk()
                    Over.title("GameOver")
                    label=tk.Label(Over, text="Black Won", width=10, height=5, fg="black", relief="solid")
                    label.pack()
                    Over.mainloop     
        except IndexError as e:
            if ChessPiece.Chess_Available_Move_Board[x][y] != "":
                if ChessPiece.Chess_Available_Move_Board[x][y] != "":
                    Move.Turn = 0
                Move.Move(Move.Saved,x,y)
                ResetBoard()
                ChessPiece.Check_Available_Move(Piece_name,y,x)
            else:
                ResetBoard()
    MakeBoard()
    Move.Saved = Piece_name


#On strat make Board
ResetBoard()
ChessPiece.Placing_all_Piece()
MakeBoard()
theChessBoard.mainloop()

