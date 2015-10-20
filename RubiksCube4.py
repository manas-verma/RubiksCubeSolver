def cycles(alg):
    x = Cube()
    x.read(alg)
    i = 1

    while not x.is_solved():
        x.read(alg)
        i += 1

    return i

def solver(x):

    moves = ['', ' U', " U'", " U2", ' F', " F'", " F2", ' R', " R'", ' R2', ' D', " D'", ' D2', ' B', " B'", ' B2', ' L', " L'", ' L2']

    for a in moves:
        for b in moves:
            for c in moves:
                sequence = c+b+a
                print(sequence)
                x.read(sequence)
                if x.is_solved():
                    print("Solution:" + sequence)
                    return sequence
                else:
                    x.read(inv(sequence))

def inv(alg):
    alg = alg.replace(')' , '').replace('(' , '').split(" ")

    for i in range(len(alg)):
        if len(alg[i]) == 2 and alg[i][1]=="'":
            alg[i] = alg[i][0]
        elif len(alg[i]) == 1:
            alg[i] += "'"

    inv_alg = ""

    for i in range(len(alg)):
        inv_alg += alg[len(alg) - i - 1] + " "

    return inv_alg.rstrip(" ")
                    



Tperm = "R U R' U' R' F R2 U' R' U' R U R' F'"
Jperm = "R U R' F' R U R' U' R' F R2 U' R' U'"
J2perm = "F2 L' U' r U2 l' U R' U' l2"
Yperm = "F R U' R' U' R U R' F' R U R' U' R' F R F'"
Hflip = "M' U M' U M' U M' U M' U' M' U' M' U' M' U'"
superflip = Hflip + " y " + Hflip + "y' x " + Hflip + " z2 " + Hflip + " x " + Hflip + " y " + Hflip + " z2"
t = superflip
t1 = "y " + Hflip + " z2 " + Hflip + " z2 y'"
t2 = "L2 U2 R2 B D2 L2 B2 U2 F2 U2 R D' L' R B2 F' R' B2 F"
t3 = "D F2 D' B2 D2 F2 D' U2 R2 U B' D' F' R2 B D L' R2 F2 R"
t4 = "D' R2 U F2 D F2 U2 L2 R2 D' B R' U' B2 F' D' R' B' U2 B'"
t5 = "F L2 B2 L2 R2 D2 F2 U2 B' U2 R' U L R' U2 F' U' B' F D B2"
t6 = "B2 R2 F2 U' R2 F2 U' B2 U' L2 U L F R2 F U' F2 U' R F'"




class Cube():

    # 0 = U , 1 = F, 2 = R, 3 = D, 4 = B, 5 = L, 6 = M, 7 = S, 8 = E
    # 0 = yellow, 1 = blue, 2 = red, 3 = orange, 4 = green, 5 = white
    # When cube is printed out, it is printed out in the following orientation
    #   U
    # L F R B
    #   D

    

    def __init__(self, scramble=" "):
        self.list = {'U': 0, 'F': 1, 'R': 2, 'D': 3, 'B': 4, 'L': 5, 'M': 6, 'S': 7, 'E': 8, 'y': 9, 'z': 10, 'x': 11, 'u': 12, 'f': 13, 'r': 14, 'd': 15, 'b': 16, 'l': 17} 
        self.color = {0: 'Y', 1: 'B', 2: 'R', 3: 'W', 4: 'G', 5: 'O'}
        self.letter = {0: 'U', 1: 'F', 2: 'R', 3: 'D', 4: 'B', 5: 'L'}
        self.set_up = {'UR': "R' U R U'",
                        'RU': "B' R B",
                        'UF': "",
                        'LU': "B L' B'",
                        'FU': "",
                        'UB': "",
                        'DL': "U' L2 U",
                        'RD': "B' R' B",
                        'BL': "U' L U",
                        'FD': "",
                        'UL': "L U' L' U",
                        'BU': "",
                        'DF': "",
                        'LD': "B L B'",
                        'DB': "",
                        'BD': "",
                        'DR': "U R2 U'",
                        'FL': "U' L' U",
                        'LF': "B L2 B'",
                        'BL': "U' L U",
                        'LB': "L' B L B'",
                        'BR': "U R' U'",
                        'RB': "R B' R' B",
                        'FR': "U R U'",
                        'RF': "B' R2 B"
                        }  #Set up moves for different edge pieces
        self.set_up_corner = {'DF': "",
                                'DU': "",
                                'UB': "",
                                'BF': "",
                                'BR': "U' L' U L U' L' U",
                                'RU': "U' L U L' U' L U",
                                'BL': "U' L U",
                                'UL': "L' U' L U",
                                'DL': "U' L2 U",
                                'FL': "R' U L U'",
                                'LB': "U' L' U",
                                'LU': "L' U' L' U",
                                'LF': "L2 U' L' U",
                                'LD': "L U' L' U",
                                'BU': "y R U R2 U' R'",
                                'DB': "U' L2 U L' U' L U",
                                'FD': "U' L' U L' U' L U",
                                'UF': "L U' L' U L' U' L U",
                                'RB': "",
                                'BD': "",
                                'DR': "",
                                'RF': "",
                                'UR': "",
                                'FU': "",
                                None: ""}

        self.stickers = [[] , [] , [] , [] , [] , []]
        for i in range(6):
            for _ in range(9):
                self.stickers[i].append(i)

        self.U = self.stickers[0]
        self.F = self.stickers[1]
        self.R = self.stickers[2]
        self.D = self.stickers[3]
        self.B = self.stickers[4]
        self.L = self.stickers[5]
        self.read(scramble)
        self.initial = self.stickers
        self.solution = ""


#To know when to stop solving:

    def is_solved(self):
        
        for i in range(6):
            for j in range(9):
                center = self.stickers[i][4]
                if self.stickers[i][j] != center:
                    return False
        return True

    def edges_solved(self):
        for i in range(6):
            for j in [1, 3, 5, 7]:
                center = self.stickers[i][4]
                if self.stickers[i][j] != center:
                    return False
        return True

    def corners_solved(self):
        for i in [0,1,3,4]:
            for j in [0, 2, 6, 8]:
                center = self.stickers[i][4]
                if self.stickers[i][j] != center:
                    return False
        return True


#Algorithms that hlep the algorithms that help the solving process:

    def edge_letter(self, face1, face2):
        # returns the position of an edge piece in (layer, number)
        # eg. self.edge(U, R) = (0, 5)
        # or self.edge(F, L) = (1, 3) 
        U = {'R': 5, 'F': 7, 'L': 3, 'B': 1} 
        F = {'U': 1, 'R': 5, 'D': 7, 'L': 3} 
        R = {'U': 1, 'F': 3, 'B': 5, 'D': 7}
        D = {'F': 1, 'R': 5, 'L': 3, 'B': 7}
        B = {'U': 1, 'R': 3, 'L': 5, 'D': 7}
        L = {'U': 1, 'F': 5, 'B': 3, 'D': 7}
        second_sticker = {'U': U, 'F': F, 'R':R, 'D':D, 'B':B, 'L':L}

        return (self.list[face1] , second_sticker[face1][face2])

    def edge_number(self, face1, face2):
        # returns the position of an edge piece in (layer, number)
        # eg. self.edge(0, 2) = (0, 5)
        # or self.edge(1, 5) = (1, 3) 
        U = {2: 5, 1: 7, 5: 3, 4: 1} 
        F = {0: 1, 2: 5, 3: 7, 5: 3} 
        R = {0: 1, 1: 3, 4: 5, 3: 7}
        D = {1: 1, 2: 5, 5: 3, 4: 7}
        B = {0: 1, 2: 3, 5: 5, 3: 7}
        L = {0: 1, 1: 5, 4: 3, 3: 7}
        second_sticker = {0: U, 1: F, 2:R, 3:D, 4:B, 5:L}

        return (face1 , second_sticker[face1][face2])

    def corner_letter(self, face1, face2):
        #e.g self.corner_letter(U, L) = (0,0)
        #If we maintain a clockwise naming system, the third letter makes no difference. So we will ignore this third letter.
        U = {'R': 8, 'F': 6, 'L': 0, 'B': 2} 
        F = {'U': 2, 'R': 8, 'D': 6, 'L': 0} 
        R = {'U': 2, 'F': 0, 'B': 8, 'D': 6}
        D = {'F': 2, 'R': 8, 'L': 0, 'B': 6}
        B = {'U': 2, 'R': 0, 'L': 8, 'D': 6}
        L = {'U': 2, 'F': 8, 'B': 0, 'D': 6}
        second_sticker = {'U': U, 'F': F, 'R':R, 'D':D, 'B':B, 'L':L}

        return (self.list[face1] , second_sticker[face1][face2])

    def corner_number(self, face1, face2):
        # returns the position of an edge piece in (layer, number)
        # eg. self.edge(0, 2) = (0, 5)
        # or self.edge(1, 5) = (1, 3) 
        U = {2: 8, 1: 6, 5: 0, 4: 2} 
        F = {0: 2, 2: 8, 3: 6, 5: 0} 
        R = {0: 2, 1: 0, 4: 8, 3: 6}
        D = {1: 2, 2: 8, 5: 0, 4: 6}
        B = {0: 2, 2: 0, 5: 8, 3: 6}
        L = {0: 2, 1: 8, 4: 0, 3: 6}
        second_sticker = {0: U, 1: F, 2:R, 3:D, 4:B, 5:L}

        return (face1 , second_sticker[face1][face2])


#Algorithms that help the solving process:

    def swap_move(self, sticker, M2):
        if (sticker == 'UF' and M2 == 0) or (sticker == 'DB' and M2 == 1):
            return "U2 M' U2 M'"
        elif (sticker == 'DB' and M2 == 0) or (sticker == 'UF' and M2 == 1):
            return "M U2 M U2"
        elif (sticker == 'FU' and M2 == 0) or (sticker == 'BD' and M2 == 1):
            return "F E R U R' E' R U' R' F' M2"
        elif (sticker == 'BD' and M2 == 0) or (sticker == 'FU' and M2 == 1):
            return "D2 F2 U M' U' F2 D2 U' M' U"
        elif sticker == 'BU':
            return "F' D R' F D' M2 D F' R D' F"
        elif sticker in self.set_up:
            return "M2"
        else:
            print("error")
            return None

    def swap_move_corner(self, sticker, R2):
        if (sticker == 'RB' and R2 == 0) or (sticker == 'RF' and R2 == 1):
            return "R' U R2 U' R' F' R U R2 U' R' F"
        elif (sticker == 'BD' and R2 == 0) or (sticker == 'FU' and R2 == 1):
            return "R U R' D r2 U' R U r2' U' D' R"
        elif (sticker == 'DR' and R2 == 0) or (sticker == 'UR' and R2 == 1):
            return "R2 U' R' F' r U R2 U' r' F R' U"
        elif (sticker == 'RF' and R2 == 0) or (sticker == 'RB' and R2 == 1):
            return "F' R U R2 U' R' F R U R2 U' R"
        elif (sticker == 'UR' and R2 == 0) or (sticker == 'DR' and R2 == 1):
            return "U' R F' r U R2 U' r' F R U R2"
        elif (sticker == 'FU' and R2 == 0) or (sticker == 'BD' and R2 == 1):
            return "R2 U' r x l2 U L U' R' U L' U' L' R' U"
        elif sticker == 'BU':
            return "F2"
        elif sticker in self.set_up_corner:
            return "R2"
        else:
            print("error")
            return None

    def unsolved_edge(self):  #unsolved edges that are NOT the DF piece
        
        
        for i in range(6):
            for j in range(6):
                if abs(j-i)!= 3 and j != i and not((i == 1 and j == 3) or (i == 3 and j == 1)):
                    A = self.edge_number(i, j)
                    B = self.edge_number(j, i)
                    A_center = self.stickers[A[0]][4]
                    B_center = self.stickers[B[0]][4]
                    A_sticker = self.stickers[A[0]][A[1]]
                    B_sticker = self.stickers[B[0]][B[1]]

                    if (A_sticker != A_center or B_sticker != B_center) and not ((A_sticker == 1 and B_sticker == 3) or (A_sticker == 3 and B_sticker == 1)):
                        return self.letter[self.stickers[A[0]][A[1]]] + self.letter[self.stickers[B[0]][B[1]]]
      
    def unsolved_corner_worse(self):  #unsolved edges that are NOT the DFR piece
        
        for i in range(6):
            for j in range(6):
                if abs(j-i)!= 3 and j != i and not((i == 3 and j == 1) or (i == 1 and j ==2) or (i == 2 and j == 3)):
                    k = self.third_sticker(i,j)
                    A = self.corner_number(i, j)
                    B = self.corner_number(j, k)
                    C = self.corner_number(k, i)

                    A_center = self.stickers[A[0]][4]
                    B_center = self.stickers[B[0]][4]
                    C_center = self.stickers[C[0]][4]
                    A_sticker = self.stickers[A[0]][A[1]]
                    B_sticker = self.stickers[B[0]][B[1]]
                    C_sticker = self.stickers[C[0]][B[1]]


                    if (A_sticker != A_center or B_sticker != B_center or C_sticker != C_center) and not ((A_sticker == 3 and B_sticker == 1) or (A_sticker == 1 and B_sticker == 2) or (A_sticker == 2 and B_sticker == 3)):
                        return self.letter[self.stickers[A[0]][A[1]]] + self.letter[self.stickers[B[0]][B[1]]]

    def unsolved_corner(self):
        for i in [0,3]:
            for j in [1,2,4,5]:
                if not((i == 3 and j == 1) or (i == 1 and j ==2) or (i == 2 and j == 3)):
                    k = self.third_sticker(i,j)

                    A = self.corner_number(i, j)
                    B = self.corner_number(j, k)
                    C = self.corner_number(k, i)

                    A_center = self.stickers[A[0]][4]
                    B_center = self.stickers[B[0]][4]
                    C_center = self.stickers[C[0]][4]

                    A_sticker = self.stickers[A[0]][A[1]]
                    B_sticker = self.stickers[B[0]][B[1]]
                    C_sticker = self.stickers[C[0]][C[1]]

                    if (A_sticker != A_center or B_sticker != B_center or C_sticker != C_center) and not ((A_sticker == 3 and B_sticker == 1) or (A_sticker == 1 and B_sticker == 2) or (A_sticker == 2 and B_sticker == 3)):
                        return self.letter[self.stickers[A[0]][A[1]]] + self.letter[self.stickers[B[0]][B[1]]]
      
    def third_sticker(self, i, j):
        x = Cube()

        for _ in range(5):
            x.read("z")
            if x.stickers[0][4]==i:
                break

        if x.stickers[0][4]!=i:
            for _ in range(5):
                x.read("x")
                if x.stickers[0][4]==i:
                    break

        for _ in range(5):
            x.read("y")
            if x.stickers[1][4]==j:
                break       

        return x.stickers[5][4] #Used in unsolved_corner(self)

#### New Corner Method:

    def find_white_corner(self):
        for i in [0,3]:
                for j in [1,2,4,5]:
                    k = self.third_sticker(i,j)

                    A = self.corner_number(i, j)
                    B = self.corner_number(j, k)
                    C = self.corner_number(k, i)
                    
                    if self.stickers[A[0]][A[1]] == 3 and i != 3:
                        return i, j, k
                    if self.stickers[B[0]][B[1]] == 3:
                        return j, k, i
                    if self.stickers[C[0]][C[1]] == 3:
                        return k, i, j


    def first_white_corner(self):
        layer, side1, side2 = self.find_white_corner()
        if layer == 3:
            return
        if layer == 0:
            self.solution += " " + self.letter[side1]+"2"
            self.do(self.letter[side1]+"2")
            print(self.letter[side1]+"2")
        elif side1==0:
            self.solution += " " + self.letter[side2]+"'"
            self.do(self.letter[side2]+"'")
            print(self.letter[side2]+"'")
        else:
            self.solution += " " + self.letter[side1]+"'"
            self.do(self.letter[side1]+"'")
            print(self.letter[side1]+"'")


    def white_corner_solved(self):
        for i in [0,2,6,8]:
            if self.stickers[3][i] != 3:
                return False
        return True
    def yellow_corner_solved(self):
        for i in [0,2,6,8]:
            if self.stickers[0][i] != 0:
                return False
        return True

    def solved_white_corners(self):
        a = []
        for i in [0,2,6,8]:
            if self.stickers[3][i] == 3:
                a.append(i)
        return a
    def unsolved_white_corners(self):
        a = []
        for i in [0,2,6,8]:
            if self.stickers[3][i] != 3:
                a.append(i)
        return a



    def white_corners(self):

        if len(self.solved_white_corners())==0:
            layer, side1, side2 = self.find_white_corner()
            self.first_white_corner()

        while not self.white_corner_solved():
            layer, side1, side2 = self.find_white_corner()
            unsolved = self.unsolved_white_corners()
            convert = [6,-1,8,-1,-1,-1,0,-1,2]
            unsolved_top = [convert[i] for i in unsolved]
            target = unsolved_top[0]
            if 0 in [layer, side1, side2]: #solving if the corner is in the top layer
                if layer == 0:
                    top_slot = self.corner_number(0,side1)[1]
                    U = layer
                    R = side1
                    F = side2
                elif side1 == 0:
                    top_slot = self.corner_number(0, side2)[1]
                    U = side1
                    R = side2
                    F = layer
                elif side2 == 0:
                    top_slot = self.corner_number(0, layer)[1]
                    U = side2
                    R = layer
                    F = side1
                #putting the corner on top of the unsolved space
                a = top_slot
                b = target
                if a+b==8:
                    set_up = "D2"
                elif (a,b) in [(0,6), (2,0), (6,8), (8,2)]:
                    set_up = "D'"
                elif (b,a) in [(0,6), (2,0), (6,8), (8,2)]:
                    set_up = "D"
                else:
                    set_up = ""
                R_ = self.letter[R]
                F_ = self.letter[F]
                if U == layer:
                    move = R_ + " U2 " + R_ + "' U' " + R_ + " U " + R_ + "'"
                elif R == layer:
                    move = R_ + " U " + R_ + "'"
                elif F == layer:
                    move = F_ + "' U' " + F_ 

            else:
                set_up = ""
                if layer == 3:
                    D = layer
                    F = side1
                    R = side2
                elif side1 == 3:
                    D = side1
                    F = side2
                    R = layer
                elif side2 == 3:
                    D = side2
                    F = layer
                    R = side1
                R_ = self.letter[R]
                F_ = self.letter[F]

                if R == layer:
                    move = R_ + " U " + R_ +"' U' " + R_ + " U " + R_ + "'"
                elif F == layer:
                    move = F_ + "' U' " + F_ +" U " + F_ + "' U' " + F_ 
                else:
                    move = ""
            self.solution += " " + set_up + " " + move + " " + inv(set_up) + "\n"
            self.do(set_up + " " + move + " " + inv(set_up))
            print(set_up + " " + move + " " + inv(set_up))



    def OLL(self):
        # returns whether is in a state or not and prints out move
        assert self.white_corner_solved()
        while not self.yellow_corner_solved():
            s = self.stickers
            if s[0][2]==0 and s[0][8]==0 and s[5][0]==0 and s[5][2]==0:
                move = "F R U R' U' F'"
            elif s[0][2]==0 and s[0][8]==0 and s[1][0]==0 and s[4][2]==0:
                move = "R U R' U' R' F R F'"
            elif s[0][0]==0 and s[0][8]==0 and s[1][0]==0 and s[2][2]==0:
                move = "F R U' R' U' R U R' F'"
            elif s[0][6]==0 and s[1][2]==0 and s[2][2]==0 and s[4][2]==0:
                move = "R U R' U R U2 R'"
            elif s[0][2]==0 and s[1][0]==0 and s[2][0]==0 and s[5][0]==0:
                move = "R U2 R' U' R U' R'"
            elif s[1][2]==0 and s[4][0]==0 and s[5][0]==0 and s[5][2]==0:
                move = "F R U R' U' R U R' U' F'"
            elif s[1][0]==0 and s[1][2]==0 and s[4][0]==0 and s[4][2]==0:
                move = "R2 U2 R U2 R2"
            else:
                move = "U"
            self.solution += " " + move + "\n"
            self.do(move)
            print(move)


    def PBL(self):
        assert self.white_corner_solved() and self.yellow_corner_solved()
        s = self.stickers
        T = -1 #0 = solved, 1 = diagonal, 2 = adjacent like Tperm
        B = -1
        for i in range(4):
            if s[1][0]==s[1][2] and s[2][0]==s[2][2] and s[4][0]==s[4][2] and s[5][0]==s[5][2]:
                T = 0
                break
            elif s[1][0]==s[4][2] and s[1][2]==s[4][0] and s[2][0]==s[5][2] and s[2][2]==s[5][0]:
                T = 1
                break
            elif s[1][0]==s[2][2] and s[1][2]==s[4][0] and s[2][0]==s[4][2] and s[5][0]==s[5][2]:
                T = 2
                break
            else:
                self.solution += " U"
                self.do("U")
                print("U")
        for i in range(4):
            if s[1][6]==s[1][8] and s[2][6]==s[2][8] and s[4][6]==s[4][8] and s[5][6]==s[5][8]:
                B = 0
                break
            elif s[1][6]==s[4][8] and s[1][8]==s[4][6] and s[2][6]==s[5][8] and s[2][8]==s[5][6]:
                B = 1
                break
            elif s[1][6]==s[2][8] and s[1][8]==s[4][6] and s[2][6]==s[4][8] and s[5][6]==s[5][8]:
                B = 2
                break
            else:
                self.solution += " D"
                self.do("D")
                print("D")
        if T==2 and B==0:
            move = "R U R' U' R' F R2 U' R' U' R U R' F'"
        elif T==0 and B==2:
            move = "R' U R' U' R' F R2 U' R' U' R U R' F' R2"
        elif T==1 and B==0:
            move = "F R U' R' U' R U R' F' R U R' U' R' F R F'"
        elif T==0 and B==1:
            move = "x2 F R U' R' U' R U R' F' R U R' U' R' F R F' x2"
        elif T==2 and B==2:
            move = "D' U R2 U' R2 U2 B2 U' B2"
        elif T==2 and B==1:
            move = "U R U' R F2 R' U R'"
        elif T==1 and B==2:
            move = "D L D' L F2 L' D L'"
        elif T==1 and B==1:
            move = "R2 F2 R2"
        else:
            move = ""

        self.solution += " " + move + "\n"
        self.do(move)
        print(move)

        fixu = ""
        fixd = ""

        if s[1][0]==s[1][4]:
            fixu = ""
        elif s[2][0]==s[1][4]:
            fixu = "U"
        elif s[4][0]==s[1][4]:
            fixu = "U2"
        elif s[5][0]==s[1][4]:
            fixu = "U'"

        if s[1][6]==s[1][4]:
            fixd = ""
        elif s[2][6]==s[1][4]:
            fixd = "D'"
        elif s[4][6]==s[1][4]:
            fixd = "D2"
        elif s[5][6]==s[1][4]:
            fixd = "D"
        self.solution += " " + fixu + " " + fixd
        self.do(fixu + " " + fixd)
        print(fixu + " " + fixd)


    def yellow_corners(self):
        self.OLL()

    def solve_all_corners(self):
        self.white_corners()
        self.OLL()
        self.PBL()

#### New Corner Method

#Written out solutions:

    def give_solution(self, scramble=""):
        
        if scramble != "":
            self.reset()
            self.read(scramble)
        self.solve()
        print(self.solution)

    def give_edge_solution(self, scramble=""):
        
        if scramble!="":
            self.reset()
            self.read(scramble)


        DF = self.edge_letter('D', 'F')
        FD = self.edge_letter('F', 'D')
      
        counter = 0
        limit = 40
        M2sliced = 0

        while not self.edges_solved() and counter < limit:  #change after better technique

            D = self.letter[self.stickers[DF[0]][DF[1]]] #The color (number of the layer) on the UR sticker
            F = self.letter[self.stickers[FD[0]][FD[1]]] #The color on the RU sticker

            self.read("M2")
            if self.edges_solved():
                print("Edges solved! (Needed an extra M2)")
                return
            self.read("M2")


            if M2sliced == 0:
                unsolved = self.unsolved_edge()
            else:
                self.read("M2")
                unsolved = self.unsolved_edge()
                self.read("M2")

            

            if unsolved == None and ((D == 'D' and F == 'F') or (D == 'F' and F == 'D')):
                set_up = ""
                swap = Tperm
            

            elif (D == 'D' and F == 'F') or (D == 'F' and F == 'D'):
                set_up = self.set_up[unsolved]
                swap = self.swap_move(unsolved, M2sliced)

            else:
                set_up = self.set_up[D+F]
                swap = self.swap_move(D+F, M2sliced)


            
            self.read(set_up + " " + swap + " " + inv(set_up))
            if set_up == "":
                print(swap)
            else:
                print(set_up + " " + swap + " " + inv(set_up))

            counter += 1
            M2sliced = 1 - M2sliced            


        if counter == limit:
            print("Congratulations, you found a bug!")        
        elif self.edges_solved() and not self.is_solved():
            print("There you go, that'll solve the edges.")
        elif self.is_solved():
            print("There you go, that'll solve it.")

    

        if counter == limit:
            print("Congratulations, you found a bug!")        
        elif self.corners_solved() and not self.is_solved():
            print("There you go, that'll solve the corners.")
        elif self.is_solved():
            print("There you go, that'll solve it.")


# The solving process:


    def solve(self, scramble=""):

        if scramble != "":
            self.reset
            self.read(scramble)

        a = solver(self)
        if a:
            self.solution += a


        for _ in range(5):
            self.read("z")
            if self.stickers[0][4]==0:
                break

        if self.stickers[0][4]!=0:
            for _ in range(5):
                self.read("x")
                if self.stickers[0][4]==0:
                    break

        for _ in range(5):
            self.read("y")
            if self.stickers[1][4]==1:
                break      

        while not self.is_solved():
            self.solve_all_corners()
            self.solve_edges()

    def solve_edges(self):
        DF = self.edge_letter('D', 'F')
        FD = self.edge_letter('F', 'D')
      
        counter = 0
        limit = 20
        M2sliced = 0

        while not self.edges_solved() and counter < limit :  #change after better technique

            D = self.letter[self.stickers[DF[0]][DF[1]]] #The color (number of the layer) on the UR sticker
            F = self.letter[self.stickers[FD[0]][FD[1]]] #The color on the RU sticker

            self.read("M2")
            if self.edges_solved():
                print("Edges solved! (Needed an extra M2)")
                return
            self.read("M2")


            if M2sliced == 0:
                unsolved = self.unsolved_edge()
            else:
                self.read("M2")
                unsolved = self.unsolved_edge()
                self.read("M2")

            

            if unsolved == None and ((D == 'D' and F == 'F') or (D == 'F' and F == 'D')):
                set_up = ""
                swap = Tperm
            

            elif (D == 'D' and F == 'F') or (D == 'F' and F == 'D'):
                set_up = self.set_up[unsolved]
                swap = self.swap_move(unsolved, M2sliced)

            else:
                set_up = self.set_up[D+F]
                swap = self.swap_move(D+F, M2sliced)

            self.solution += " " + set_up + " " + swap + " " + inv(set_up) + "\n"
            self.do(set_up + " " + swap + " " + inv(set_up))
            print(set_up + " " + swap + " " + inv(set_up))

            counter += 1
            M2sliced = 1 - M2sliced

            

            

        
        if counter == limit:
            print("Reached limit: Could not solve")        
        elif self.edges_solved() and not self.is_solved():
            print("Edges solved!")
        elif self.is_solved():
            print("Solved!")

        # if limit < 500:
        #     print("You're probably testing, limit is below 500")

    def solve_next_pair(self): #for testing purposes 

        DF = self.edge_letter('D', 'F')
        FD = self.edge_letter('F', 'D')
          
        D = self.letter[self.stickers[DF[0]][DF[1]]] #The color (number of the layer) on the UR sticker
        F = self.letter[self.stickers[FD[0]][FD[1]]] #The color on the RU sticker

            

        print("Sticker: " +D+F)
        print("If applicable, unsolved edge: " + self.unsolved_edge())
        unsolved = self.unsolved_edge()


           
        if (D == 'D' and F == 'F') or (D == 'F' and F == 'D'):
                set_up = self.set_up[unsolved]
                swap = self.swap_move(unsolved, 0)

        else:
                set_up = self.set_up[D+F]
                swap = self.swap_move(D+F, 0)

        
        self.do(set_up + " " + swap + " " + inv(set_up))
        print(set_up + " " + swap + " " + inv(set_up))

        print("Sticker: " +D+F)
        print("If applicable, unsolved edge: " + unsolved)
        print("____________________")
        


        D = self.letter[self.stickers[DF[0]][DF[1]]] #The color (number of the layer) on the UR sticker
        F = self.letter[self.stickers[FD[0]][FD[1]]] #The color on the RU sticker


        self.read("M2")
        print("Sticker: " +D+F)
        print("If applicable, unsolved edge: " + self.unsolved_edge())
        unsolved = self.unsolved_edge()
        self.read("M2")

        if (D == 'D' and F == 'F') or (D == 'F' and F == 'D'):
                set_up = self.set_up[unsolved]
                swap = self.swap_move(unsolved, 1)

        else:
                set_up = self.set_up[D+F]
                swap = self.swap_move(D+F, 1)

        self.do(set_up + " " + swap + " " + inv(set_up))
        print(set_up + " " + swap + " " + inv(set_up))

        print("Sticker: " +D+F)
        print("If applicable, unsolved edge: " + unsolved)
        print("____________________")
        print("____________________")

    def solve_corners(self):
        DF = self.corner_letter('D', 'F')
        FR = self.corner_letter('F', 'R')
          
        counter = 0
        limit = 20
        R2sliced = 0

        while not self.corners_solved() and counter < limit :  #change after better technique

            D = self.letter[self.stickers[DF[0]][DF[1]]] #The color (number of the layer) on the UR sticker
            F = self.letter[self.stickers[FR[0]][FR[1]]] #The color on the RU sticker

            self.read("R2")
            if self.corners_solved():
                print("Corners solved! (Needed an extra R2)")
                return
            self.read("R2")

            if R2sliced == 0:
                unsolved = self.unsolved_corner()
            elif R2sliced == 1:
                self.read("R2")
                unsolved = self.unsolved_corner()
                self.read("R2")
            else:
                print("something's wrong")
            
            if (D == 'D' and F == 'F') or (D == 'F' and F == 'R') or (D == 'R' and F == 'D'):
                set_up = self.set_up_corner[unsolved]
                swap = self.swap_move_corner(unsolved, R2sliced)

            else:
                set_up = self.set_up_corner[D+F]
                swap = self.swap_move_corner(D+F, R2sliced)

            self.do(set_up + " " + swap + " " + inv(set_up))
            print(set_up + " " + swap + " " + inv(set_up))

            counter += 1
            R2sliced = 1 - R2sliced

                

                

            
        if counter == limit:
            print("Reached limit: Could not solve")        
        elif self.corners_solved() and not self.is_solved():
            print("Corners solved!")
        elif self.is_solved():
            print("Solved!")

        # if limit < 500:
        #     print("You're probably testing, limit is below 500")



    def reset(self):
        self.stickers = [[] , [] , [] , [] , [] , []]
        for i in range(6):
            for _ in range(9):
                self.stickers[i].append(i)
        self.solution = ""
 
#The actual mechanics of the cube:

    def switch_cw(self, a , a_ , b, b_ , c , c_ , d , d_):
        
        self.stickers[a][a_] , self.stickers[b][b_] , self.stickers[c][c_] , self.stickers[d][d_] = self.stickers[b][b_] , self.stickers[c][c_] , self.stickers[d][d_], self.stickers[a][a_]  

    def switch_ccw(self, a , a_ , b, b_ , c , c_ , d , d_):

        self.stickers[a][a_] , self.stickers[b][b_] , self.stickers[c][c_] , self.stickers[d][d_] = self.stickers[d][d_] , self.stickers[a][a_] , self.stickers[b][b_] , self.stickers[c][c_] 
    
    def switch_double(self, a , a_ , b, b_ , c , c_ , d , d_):

        self.stickers[a][a_] , self.stickers[b][b_] , self.stickers[c][c_] , self.stickers[d][d_] = self.stickers[c][c_] , self.stickers[d][d_] , self.stickers[a][a_] , self.stickers[b][b_] 

    def print_cube(self):
        names = ['U' , 'F' , 'R' , 'D' , 'B' , 'L']

        for i in range(6):
            print(names[i], "layer:")
            print(self.color[self.stickers[i][0]], self.color[self.stickers[i][1]], self.color[self.stickers[i][2]])
            print(self.color[self.stickers[i][3]], self.color[self.stickers[i][4]], self.color[self.stickers[i][5]])
            print(self.color[self.stickers[i][6]], self.color[self.stickers[i][7]], self.color[self.stickers[i][8]])
            print()

    def cw(self, l):

        self.turn(l, self.switch_cw)

    def ccw(self, l):

        self.turn(l, self.switch_ccw)

    def double(self, l):

        self.turn(l, self.switch_double)

    def turn(self, l, switch):
        x = self.adjacent_list(l)
        if l < 9:
            if l < 6:
                switch(l, 0, l, 6, l, 8, l, 2)
                switch(l, 1, l, 3, l, 7, l, 5)

            for i in range(1,4):
                switch(x[0][0], x[0][i], x[1][0], x[1][i], x[2][0], x[2][i], x[3][0], x[3][i])
        else:
            if l < 12:
                a = 3
            else:
                a = 2

            if switch == self.switch_cw:
                for i in range(a):
                    self.turn(x[i][0], x[i][1])
            elif switch == self.switch_double:
                for i in range(a):
                    self.turn(x[i][0], switch)
            else:
                for i in range(a):
                    self.turn(x[i][0], x[i][2])

    def adjacent_list(self, l):
        
        #side layers
        if l == 0:
            return [ [1, 0, 1, 2] , [2, 0, 1, 2] , [4, 0, 1, 2] , [5, 0, 1, 2] ]

        elif l == 1:
            return [ [0, 6, 7, 8] , [5, 8, 5, 2] , [3, 2, 1, 0] , [2, 0, 3, 6] ]

        elif l == 2:
            return [ [0, 8, 5, 2] , [1, 8, 5, 2] , [3, 8, 5, 2] , [4, 0, 3, 6] ]

        elif l == 3:
            return [ [1, 6, 7, 8] , [5, 6, 7, 8] , [4, 6, 7, 8] , [2, 6, 7, 8] ]    

        elif l == 4:
            return [ [0, 2, 1, 0] , [2, 8, 5, 2] , [3, 6, 7, 8] , [5, 0, 3, 6] ]    

        elif l == 5:
            return [ [0, 0, 3, 6] , [4, 8, 5, 2] , [3, 0, 3, 6] , [1, 0, 3, 6] ]

        #slices:
        elif l == 6:
            return [ [0, 7, 4, 1] , [4, 1, 4, 7] , [3, 7, 4, 1] , [1, 7, 4, 1] ]

        elif l == 7:
            return [ [0, 5, 4, 3] , [5, 1, 4, 7] , [3, 3, 4, 5] , [2, 7, 4, 1] ]

        elif l == 8:
            return [ [5, 5, 4, 3] , [4, 5, 4, 3] , [2, 5, 4, 3] , [1, 5, 4, 3] ]

        #cube rotations:

        elif l < 12:
            if l % 2 != 0:
                return [ [(l%3), self.switch_cw, self.switch_ccw] ,  [(l%3 + 3), self.switch_ccw, self.switch_cw] , [(8 - l%3), self.switch_ccw, self.switch_cw]]
            else:
                return [ [(l%3), self.switch_cw, self.switch_ccw] ,  [(l%3 + 3), self.switch_ccw, self.switch_cw] , [(8 - l%3), self.switch_cw, self.switch_ccw]]

        #thick rotations:
        else:
            if l % 2 == 0:
                return [ [(l-12) , self.switch_cw, self.switch_ccw], [(8 - (l % 3)), self.switch_ccw, self.switch_cw]]
            else:
                return [ [(l-12) , self.switch_cw, self.switch_ccw], [(8 - (l % 3)), self.switch_cw, self.switch_ccw]]

    def parse(self, a):

        return a.replace(')' , '').replace('(' , '').split(" ")

    def read(self, a):
        a = a.lstrip(" ").rstrip(" ")
        x = self.parse(a)
        if a == "" or a == " ":
            return
        for i in range(len(x)):

            if len(x[i]) == 1:
                self.cw(self.list[x[i]])

            elif x[i][0] == '2':
                self.double(self.list[x[i][1]])

            elif x[i][1] == '2':
                self.double(self.list[x[i][0]])

            elif x[i][1] == "'":
                self.ccw(self.list[x[i][0]])

            else:
                print("invalid input")

    def do(self, a=""):
        self.read(a)
        self.print_cube()


#x = Cube()
result = []
solutions = []
length = []
average = 0
scrambles = ["R", 
            "D", 
            "R U F' D",
            "R U R' U'",
            "D2 B2 L2 B R2 U2 B L2 U2 R2 F' D R' D B2 L' F L' D2 U L",
            "F' L2 U2 F' D2 B2 F' U2 R2 B F' D' F2 L F2 D2 B' L2 F L U2",
            "D' F R' D' F L2 R' D B2 L R' D' L R' D2 R2 L F2 D2 L' F' D2 B D2 F",
            "D F R2 U R L F' L2 B U' L2 U R2 U L2 U B2 D2 R2 U",
            "L2 B U2 F D2 U2 F2 L2 F L2 D2 U' L2 D' F' R D' B' L R2",
            "R F' U2 R2 D2 L2 B U2 L' B2 L F2 L F2 L2 D2 F2 U2",
            "D L2 F2 D R2 B2 D B2 D2 B2 U F' D2 U R F R2 U L' R' D2",
            "U L2 F2 D' R2 D2 B2 U B2 F2 U B D2 F' L U B R U' R F'",
            "B2 L' B2 U2 L B2 F2 D2 R2 F2 L' U B' L R U2 B2 D2 U' F",
            "L2 U' R2 F2 R2 U L2 U F2 R2 F2 R D L2 R F2 R F' L2 B' R2",
            "U2 R' U R U R2 U R' U' R' U' R U2 R2 U2 R' U' R2 U2 R U2 R2 U R' U2",
            "U' M U' M U M U M2 U' M U M U' M2 U' M' U M2 U M2 U2 M2 U2 M U2"]

#scrambles = ['U', "U'", "U2", 'F', "F'", "F2", 'R', "R'", 'R2', 'D', "D'", 'D2', 'B', "B'", 'B2', 'L', "L'", 'L2']

# def _test(scrambles):

#     y = Cube()
#     r = []
#     wrong = 0

#     for s in scrambles:
#         y.do(s)
#         y.solve()
#         r.append(y.is_solved())
#         result.append(y.is_solved())
#         solutions.append(y.solution.replace("  "," ").replace("   "," ").replace("    "," ").replace("\n","").replace("U U U","U'").replace("D D D","D'").replace("U U","U2").replace("D D","D2").split(" "))
#         y.solution = ""
#         y.reset()

#     for i in range(len(r)):
#         if not r[i]:
#             print("Item:",i)
#             wrong += 1
#     for i in range(len(solutions)):
#         length.append(len(solutions[i]))
#     average = sum(length)/len(length)
    
#     return wrong, average

# print(_test(scrambles))







# 0 1 2
# 3 4 5
# 6 7 8


#             0 1 2                  8 7 6
#             3 4 5 (0)              5 4 3 (0)                         - U(0)
#             6 7 8                  2 1 0

# 0 1 2       0 1 2      0 1 2       0 1 2      0 1 2
# 3 4 5 (5)   3 4 5 (1)  3 4 5 (2)   3 4 5 (4)  3 4 5 (5)       - L(5) - F(1) - R(2) - B(4)
# 6 7 8       6 7 8      6 7 8       6 7 8      6 7 8

#             0 1 2                  8 7 6
#             3 4 5 (3)              5 4 3 (3)                         - D(3)
#             6 7 8                  2 1 0




# U = 0, F = 1, R = 2, D = 3, B = 4, L = 5

# (face, face) --> (layer, number)

# U = {'R': 5, 'F': 7, 'L': 3, 'B': 1} 
# F = {'U': 1, 'R': 5, 'D': 7, 'L': 3} 
# R = {'U': 1, 'F': 3, 'B': 5, 'D': 7}
# D = {'F': 1, 'R': 5, 'L': 3, 'B': 7}
# B = {'U': 1, 'R': 3, 'L': 5, 'D': 7}
# L = {'U': 1, 'F': 5, 'B': 3, 'D': 7}

# OR

# U = {2: 5, 1: 7, 5: 3, 4: 1} 
# F = {0: 1, 2: 5, 3: 7, 5: 3} 
# R = {0: 1, 1: 3, 4: 5, 3: 7}
# D = {1: 1, 2: 5, 5: 3, 4: 7}
# B = {0: 1, 2: 3, 5: 5, 3: 7}
# L = {0: 1, 1: 5, 4: 3, 3: 7}


##Junk Code:


        # elif l == 11:
        #     return [ [5, self.switch_ccw, self.switch_cw] ,  [6, self.switch_ccw, self.switch_cw] , [2, self.switch_cw, self.switch_ccw]]

        # elif l == 9:
        #     return [ [0, self.switch_cw, self.switch_ccw] ,  [8, self.switch_ccw, self.switch_cw] , [3, self.switch_ccw, self.switch_cw]]

        # elif l == 10:
        #     return [ [1, self.switch_cw, self.switch_ccw] ,  [7, self.switch_cw, self.switch_ccw] , [4, self.switch_ccw, self.switch_cw]]

   # elif U == 'R' and R == 'U':
            #     if self.stickers[0][3]==5 and self.stickers[5][2]==0:
            #         set_up = ""
            #         swap = Hflip
            #     else:
            #         set_up = self.set_up[self.unsolved_edge()]
            #         swap = self.swap[self.unsolved_edge()]























