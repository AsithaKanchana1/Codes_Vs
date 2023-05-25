def ConstBoard(board):
    print("current State of the Noard \n\n");
    for i in range(0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if (board[i]==0):
            print("_ ", end=" ");
        if (board[i]==-1):
            print("X ",end=" ");
        if (board[i]==1):
            print("O ",end=" ");
    print("\n\n");

def User1Tern(board):
    pos = input("Enter X 's Position fron [1,2,...9]");
    pos = int(pos);
    if(board[pos-1]!=0):
        print("Wrong MOve...");
        exit()
    board[pos-1]=-1;
def User2Tern(board):
    pos = input("Enter O 's Position fron [1,2,...9]");
    pos = int(pos);
    if(board[pos-1]!=0):
        print("Wrong MOve...");
        exit()
    board[pos-1]=1;
