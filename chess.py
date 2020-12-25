import intertools 
WHITE = "white"
BLACK = "black"




class Game:
    def __init__(self):
        self.playersturn = BLACK
        self.message = "this is where prompt will go"
        self.gameboard {}
        self.placepeice()
        print("chess programe. enter move in algebric notaion seprated by space")
        self.main()


    def placepeice (self):


for i in range(0,8):
        self.gameboard [(i,1)] =  Pawn(WHITE,uniDict[WHITE][Pawn],1)
        self.gameboard [(i,6)] =  Pawn(BLACK,uniDict[BLACK][Pawn],-1)

placers = [Rook,Knight,Bishops,Queen,King,Bishops,Knight,Rook]

    for i in range(0,8):
        self.gameboard [(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
        self.gameboard [((7-i),7)] = placers[i](BLACK,uniDict[WHITE][placers[i])
    placers.reverse()


    def main(self):

        while true:
            self.printboard()
            print(self.message)
            slef.message = ""
            starpos,endpos = self.parseinput()
        try:
                target = self.gameboard[starpos]
        except:self.message = "could not find piece, index probably out of range"
        target = None 

    if target:
        print("found"+str(target))
        if target.colour != self.playersturn:
            self.message = "you areen't allowed  to move that piece this turn"
            continue
        if target.isvalid(starpos)
