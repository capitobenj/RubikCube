
class rbcube():
    def __init__(self):
        self.face_one=['A','A','A',
                        'A','A','A',
                        'A','A','A']
        self.face_two=['B','B','B',
                        'B','B','B',
                        'B','B','B']
        self.face_three=['C','C','C',
                        'C','C','C',
                        'C','C','C']
        self.face_four=['D','D','D',
                        'D','D','D',
                        'D','D','D']
        self.face_five=['E','E','E',
                        'E','E','E',
                        'E','E','E']
        self.face_six=['F','F','F',
                        'F','F','F',
                        'F','F','F']
        self.active=1
    def rotate_right(self, active):
        if self.active == 1 or self.active == 2 or self.active == 3 or self.active == 4:
            if active == 1:
                temp = self.face_four.copy() 
                self.face_four[0] = self.face_three[0]
                self.face_four[1] = self.face_three[1]
                self.face_four[2] = self.face_three[2]
                self.face_three[0] = self.face_two[0]
                self.face_three[1] = self.face_two[1]
                self.face_three[2] = self.face_two[2]
                self.face_two[0] = self.face_one[0]
                self.face_two[1] = self.face_one[1]
                self.face_two[2] = self.face_one[2]
                self.face_one[0] = temp[0]
                self.face_one[1] = temp[1]
                self.face_one[2] = temp[2]
            if active == 2:
                temp = self.face_four.copy() 
                self.face_four[0+3] = self.face_three[0+3]
                self.face_four[1+3] = self.face_three[1+3]
                self.face_four[2+3] = self.face_three[2+3]
                self.face_three[0+3] = self.face_two[0+3]
                self.face_three[1+3] = self.face_two[1+3]
                self.face_three[2+3] = self.face_two[2+3]
                self.face_two[0+3] = self.face_one[0+3]
                self.face_two[1+3] = self.face_one[1+3]
                self.face_two[2+3] = self.face_one[2+3]
                self.face_one[0+3] = temp[0+3]
                self.face_one[1+3] = temp[1+3]
                self.face_one[2+3] = temp[2+3]
            if active == 3:
                temp = self.face_four.copy() 
                self.face_four[0+6] = self.face_three[0+6]
                self.face_four[1+6] = self.face_three[1+6]
                self.face_four[2+6] = self.face_three[2+6]
                self.face_three[0+6] = self.face_two[0+6]
                self.face_three[1+6] = self.face_two[1+6]
                self.face_three[2+6] = self.face_two[2+6]
                self.face_two[0+6] = self.face_one[0+6]
                self.face_two[1+6] = self.face_one[1+6]
                self.face_two[2+6] = self.face_one[2+6]
                self.face_one[0+6] = temp[0+6]
                self.face_one[1+6] = temp[1+6]
                self.face_one[2+6] = temp[2+6]
        if self.active == 5:
            if active == 1:
                temp = self.face_five.copy()
                self.face_five[0] = self.face_four[0]
                self.face_five[1] = self.face_four[1]
                self.face_five[2] = self.face_four[2]
                temp2 = self.face_two.copy()
                self.face_two[0] = temp[0]
                self.face_two[1] = temp[1]
                self.face_two[2] = temp[2]
                temp = self.face_six.copy()
                self.face_six[0] = temp2[0]
                self.face_six[1] = temp2[1]
                self.face_six[2] = temp2[2]
                self.face_four[0] = temp[0]
                self.face_four[1] = temp[1]
                self.face_four[2] = temp[2]
            if active == 2:
                temp = self.face_five.copy()
                self.face_five[0+3] = self.face_four[0+3]
                self.face_five[1+3] = self.face_four[1+3]
                self.face_five[2+3] = self.face_four[2+3]
                temp2 = self.face_two.copy()
                self.face_two[0+3] = temp[0+3]
                self.face_two[1+3] = temp[1+3]
                self.face_two[2+3] = temp[2+3]
                temp = self.face_six.copy()
                self.face_six[0+3] = temp2[0+3]
                self.face_six[1+3] = temp2[1+3]
                self.face_six[2+3] = temp2[2+3]
                self.face_four[0+3] = temp[0+3]
                self.face_four[1+3] = temp[1+3]
                self.face_four[2+3] = temp[2+3]
            if active == 3:
                temp = self.face_five.copy()
                self.face_five[0+6] = self.face_four[0+6]
                self.face_five[1+6] = self.face_four[1+6]
                self.face_five[2+6] = self.face_four[2+6]
                temp2 = self.face_two.copy()
                self.face_two[0+6] = temp[0+6]
                self.face_two[1+6] = temp[1+6]
                self.face_two[2+6] = temp[2+6]
                temp = self.face_six.copy()
                self.face_six[0+6] = temp2[0+6]
                self.face_six[1+6] = temp2[1+6]
                self.face_six[2+6] = temp2[2+6]
                self.face_four[0+6] = temp[0+6]
                self.face_four[1+6] = temp[1+6]
                self.face_four[2+6] = temp[2+6]
        if self.active == 6:
            if active == 1:
                temp = self.face_five.copy()
                self.face_five[0] = self.face_four[0]
                self.face_five[1] = self.face_four[1]
                self.face_five[2] = self.face_four[2]
                temp2 = self.face_two.copy()
                self.face_two[0] = temp[0]
                self.face_two[1] = temp[1]
                self.face_two[2] = temp[2]
                temp = self.face_six.copy()
                self.face_six[0] = temp2[0]
                self.face_six[1] = temp2[1]
                self.face_six[2] = temp2[2]
                self.face_four[0] = temp[0]
                self.face_four[1] = temp[1]
                self.face_four[2] = temp[2]
            if active == 2:
                temp = self.face_five.copy()
                self.face_five[0+3] = self.face_four[0+3]
                self.face_five[1+3] = self.face_four[1+3]
                self.face_five[2+3] = self.face_four[2+3]
                temp2 = self.face_two.copy()
                self.face_two[0+3] = temp[0+3]
                self.face_two[1+3] = temp[1+3]
                self.face_two[2+3] = temp[2+3]
                temp = self.face_six.copy()
                self.face_six[0+3] = temp2[0+3]
                self.face_six[1+3] = temp2[1+3]
                self.face_six[2+3] = temp2[2+3]
                self.face_four[0+3] = temp[0+3]
                self.face_four[1+3] = temp[1+3]
                self.face_four[2+3] = temp[2+3]
            if active == 3:
                temp = self.face_five.copy()
                self.face_five[0+6] = self.face_four[0+6]
                self.face_five[1+6] = self.face_four[1+6]
                self.face_five[2+6] = self.face_four[2+6]
                temp2 = self.face_two.copy()
                self.face_two[0+6] = temp[0+6]
                self.face_two[1+6] = temp[1+6]
                self.face_two[2+6] = temp[2+6]
                temp = self.face_six.copy()
                self.face_six[0+6] = temp2[0+6]
                self.face_six[1+6] = temp2[1+6]
                self.face_six[2+6] = temp2[2+6]
                self.face_four[0+6] = temp[0+6]
                self.face_four[1+6] = temp[1+6]
                self.face_four[2+6] = temp[2+6]
    def rotate_left(self, active):
        if self.active == 1 or self.active == 2 or self.active == 3 or self.active == 4:
            if active == 1:
                temp = self.face_one.copy()
                self.face_one[0] = self.face_two[0]
                self.face_one[1] = self.face_two[1]
                self.face_one[2] = self.face_two[2]
                self.face_two[0] = self.face_three[0]
                self.face_two[1] = self.face_three[1]
                self.face_two[2] = self.face_three[2]
                self.face_three[0] = self.face_four[0]
                self.face_three[1] = self.face_four[1]
                self.face_three[2] = self.face_four[2]
                self.face_four[0] = temp[0]
                self.face_four[1] = temp[1]
                self.face_four[2] = temp[2]
            if active == 2:
                temp = self.face_one.copy()
                self.face_one[0+3] = self.face_two[0+3]
                self.face_one[1+3] = self.face_two[1+3]
                self.face_one[2+3] = self.face_two[2+3]
                self.face_two[0+3] = self.face_three[0+3]
                self.face_two[1+3] = self.face_three[1+3]
                self.face_two[2+3] = self.face_three[2+3]
                self.face_three[0+3] = self.face_four[0+3]
                self.face_three[1+3] = self.face_four[1+3]
                self.face_three[2+3] = self.face_four[2+3]
                self.face_four[0+3] = temp[0+3]
                self.face_four[1+3] = temp[1+3]
                self.face_four[2+3] = temp[2+3]
            if active == 3:
                temp = self.face_one.copy()
                self.face_one[0+6] = self.face_two[0+6]
                self.face_one[1+6] = self.face_two[1+6]
                self.face_one[2+6] = self.face_two[2+6]
                self.face_two[0+6] = self.face_three[0+6]
                self.face_two[1+6] = self.face_three[1+6]
                self.face_two[2+6] = self.face_three[2+6]
                self.face_three[0+6] = self.face_four[0+6]
                self.face_three[1+6] = self.face_four[1+6]
                self.face_three[2+6] = self.face_four[2+6]
                self.face_four[0+6] = temp[0+6]
                self.face_four[1+6] = temp[1+6]
                self.face_four[2+6] = temp[2+6]
        if self.active == 5:
            if active == 1:
                temp = self.face_six.copy()
                self.face_six[0] = self.face_two[0]
                self.face_six[1] = self.face_two[1]
                self.face_six[2] = self.face_two[2]
                self.face_two[0] = self.face_five[0]
                self.face_two[1] = self.face_five[1]
                self.face_two[2] = self.face_five[2]
                self.face_five[0] = self.face_four[0]
                self.face_five[1] = self.face_four[1]
                self.face_five[2] = self.face_four[2]
                self.face_four[0] = temp[0]
                self.face_four[1] = temp[1]
                self.face_four[2] = temp[2]
            if active == 2:
                temp = self.face_one.copy()
                self.face_one[0+3] = self.face_two[0+3]
                self.face_one[1+3] = self.face_two[1+3]
                self.face_one[2+3] = self.face_two[2+3]
                self.face_two[0+3] = self.face_three[0+3]
                self.face_two[1+3] = self.face_three[1+3]
                self.face_two[2+3] = self.face_three[2+3]
                self.face_three[0+3] = self.face_four[0+3]
                self.face_three[1+3] = self.face_four[1+3]
                self.face_three[2+3] = self.face_four[2+3]
                self.face_four[0+3] = temp[0+3]
                self.face_four[1+3] = temp[1+3]
                self.face_four[2+3] = temp[2+3]
            if active == 3:
                temp = self.face_one.copy()
                self.face_one[0+6] = self.face_two[0+6]
                self.face_one[1+6] = self.face_two[1+6]
                self.face_one[2+6] = self.face_two[2+6]
                self.face_two[0+6] = self.face_three[0+6]
                self.face_two[1+6] = self.face_three[1+6]
                self.face_two[2+6] = self.face_three[2+6]
                self.face_three[0+6] = self.face_four[0+6]
                self.face_three[1+6] = self.face_four[1+6]
                self.face_three[2+6] = self.face_four[2+6]
                self.face_four[0+6] = temp[0+6]
                self.face_four[1+6] = temp[1+6]
                self.face_four[2+6] = temp[2+6]
        if self.active == 6:
            if active == 1:
                temp = self.face_one.copy()
                self.face_one[0] = self.face_two[0]
                self.face_one[1] = self.face_two[1]
                self.face_one[2] = self.face_two[2]
                self.face_two[0] = self.face_three[0]
                self.face_two[1] = self.face_three[1]
                self.face_two[2] = self.face_three[2]
                self.face_three[0] = self.face_four[0]
                self.face_three[1] = self.face_four[1]
                self.face_three[2] = self.face_four[2]
                self.face_four[0] = temp[0]
                self.face_four[1] = temp[1]
                self.face_four[2] = temp[2]
            if active == 2:
                temp = self.face_one.copy()
                self.face_one[0+3] = self.face_two[0+3]
                self.face_one[1+3] = self.face_two[1+3]
                self.face_one[2+3] = self.face_two[2+3]
                self.face_two[0+3] = self.face_three[0+3]
                self.face_two[1+3] = self.face_three[1+3]
                self.face_two[2+3] = self.face_three[2+3]
                self.face_three[0+3] = self.face_four[0+3]
                self.face_three[1+3] = self.face_four[1+3]
                self.face_three[2+3] = self.face_four[2+3]
                self.face_four[0+3] = temp[0+3]
                self.face_four[1+3] = temp[1+3]
                self.face_four[2+3] = temp[2+3]
            if active == 3:
                temp = self.face_one.copy()
                self.face_one[0+6] = self.face_two[0+6]
                self.face_one[1+6] = self.face_two[1+6]
                self.face_one[2+6] = self.face_two[2+6]
                self.face_two[0+6] = self.face_three[0+6]
                self.face_two[1+6] = self.face_three[1+6]
                self.face_two[2+6] = self.face_three[2+6]
                self.face_three[0+6] = self.face_four[0+6]
                self.face_three[1+6] = self.face_four[1+6]
                self.face_three[2+6] = self.face_four[2+6]
                self.face_four[0+6] = temp[0+6]
                self.face_four[1+6] = temp[1+6]
                self.face_four[2+6] = temp[2+6]
    #def rotate_up(self, active):
    #    break
    #def rotate_down(self, active):
    #    break
    def change_face(self, face):
        self.active = face
    def print_all(self):
        if self.active == 1:
            print('Active face: ', self.active)
            print(self.face_five[0], self.face_five[1], self.face_five[2])
            print(self.face_five[0+3], self.face_five[1+3], self.face_five[2+3]," 5 ")
            print(self.face_five[0+6], self.face_five[1+6], self.face_five[2+6], "  2     3     4")
            print(self.face_one[0], self.face_one[1], self.face_one[2], self.face_two[0], self.face_two[1], self.face_two[2], self.face_three[0], self.face_three[1], self.face_three[2], self.face_four[0], self.face_four[1], self.face_four[2])
            print(self.face_one[0+3], self.face_one[1+3], self.face_one[2+3], self.face_two[0+3], self.face_two[1+3], self.face_two[2+3], self.face_three[0+3], self.face_three[1+3], self.face_three[2+3], self.face_four[0+3], self.face_four[1+3], self.face_four[2+3])
            print(self.face_one[0+6], self.face_one[1+6], self.face_one[2+6], self.face_two[0+6], self.face_two[1+6], self.face_two[2+6], self.face_three[0+6], self.face_three[1+6], self.face_three[2+6], self.face_four[0+6], self.face_four[1+6], self.face_four[2+6])
            print(self.face_six[0], self.face_six[1], self.face_six[2])
            print(self.face_six[0+3], self.face_six[1+3], self.face_six[2+3]," 6 ")
            print(self.face_six[0+6], self.face_six[1+6], self.face_six[2+6])
        elif self.active == 2:
            print('Active face: ', self.active)
            print("     ", self.face_five[0], self.face_five[1], self.face_five[2])
            print("    5", self.face_five[0+3], self.face_five[1+3], self.face_five[2+3])
            print("  1  ", self.face_five[0+6], self.face_five[1+6], self.face_five[2+6], "  3     4")
            print(self.face_one[0], self.face_one[1], self.face_one[2], self.face_two[0], self.face_two[1], self.face_two[2], self.face_three[0], self.face_three[1], self.face_three[2], self.face_four[0], self.face_four[1], self.face_four[2])
            print(self.face_one[0+3], self.face_one[1+3], self.face_one[2+3], self.face_two[0+3], self.face_two[1+3], self.face_two[2+3], self.face_three[0+3], self.face_three[1+3], self.face_three[2+3], self.face_four[0+3], self.face_four[1+3], self.face_four[2+3])
            print(self.face_one[0+6], self.face_one[1+6], self.face_one[2+6], self.face_two[0+6], self.face_two[1+6], self.face_two[2+6], self.face_three[0+6], self.face_three[1+6], self.face_three[2+6], self.face_four[0+6], self.face_four[1+6], self.face_four[2+6])
            print("     ", self.face_six[0], self.face_six[1], self.face_six[2])
            print("    6", self.face_six[0+3], self.face_six[1+3], self.face_six[2+3])
            print("     ", self.face_six[0+6], self.face_six[1+6], self.face_six[2+6])
        elif self.active == 3:
            print('Active face: ', self.active)
            print("          ", self.face_five[0], self.face_five[1], self.face_five[2])
            print("        5 ", self.face_five[0+3], self.face_five[1+3], self.face_five[2+3])
            print("  1       ", self.face_five[0+6], self.face_five[1+6], self.face_five[2+6], "     4")
            print(self.face_one[0], self.face_one[1], self.face_one[2], self.face_two[0], self.face_two[1], self.face_two[2], self.face_three[0], self.face_three[1], self.face_three[2], self.face_four[0], self.face_four[1], self.face_four[2])
            print(self.face_one[0+3], self.face_one[1+3], self.face_one[2+3], self.face_two[0+3], self.face_two[1+3], self.face_two[2+3], self.face_three[0+3], self.face_three[1+3], self.face_three[2+3], self.face_four[0+3], self.face_four[1+3], self.face_four[2+3])
            print(self.face_one[0+6], self.face_one[1+6], self.face_one[2+6], self.face_two[0+6], self.face_two[1+6], self.face_two[2+6], self.face_three[0+6], self.face_three[1+6], self.face_three[2+6], self.face_four[0+6], self.face_four[1+6], self.face_four[2+6])
            print("          ", self.face_six[0], self.face_six[1], self.face_six[2])
            print("        6 ", self.face_six[0+3], self.face_six[1+3], self.face_six[2+3])
            print("          ", self.face_six[0+6], self.face_six[1+6], self.face_six[2+6])
        elif self.active == 4:
            print('Active face: ', self.active)
            print("                ", self.face_five[0], self.face_five[1], self.face_five[2])
            print("              5 ", self.face_five[0+3], self.face_five[1+3], self.face_five[2+3])
            print("  1         2   ", self.face_five[0+6], self.face_five[1+6], self.face_five[2+6])
            print(self.face_one[0], self.face_one[1], self.face_one[2], self.face_two[0], self.face_two[1], self.face_two[2], self.face_three[0], self.face_three[1], self.face_three[2], self.face_four[0], self.face_four[1], self.face_four[2])
            print(self.face_one[0+3], self.face_one[1+3], self.face_one[2+3], self.face_two[0+3], self.face_two[1+3], self.face_two[2+3], self.face_three[0+3], self.face_three[1+3], self.face_three[2+3], self.face_four[0+3], self.face_four[1+3], self.face_four[2+3])
            print(self.face_one[0+6], self.face_one[1+6], self.face_one[2+6], self.face_two[0+6], self.face_two[1+6], self.face_two[2+6], self.face_three[0+6], self.face_three[1+6], self.face_three[2+6], self.face_four[0+6], self.face_four[1+6], self.face_four[2+6])
            print("                ", self.face_six[0], self.face_six[1], self.face_six[2])
            print("              6 ", self.face_six[0+3], self.face_six[1+3], self.face_six[2+3])
            print("                ", self.face_six[0+6], self.face_six[1+6], self.face_six[2+6])
        elif self.active == 5:
            print('Active face: ', self.active)
            print("     ", self.face_five[0], self.face_five[1], self.face_five[2])
            print("    A", self.face_five[0+3], self.face_five[1+3], self.face_five[2+3])
            print("  1  ", self.face_five[0+6], self.face_five[1+6], self.face_five[2+6], "  3     4")
            print(self.face_one[0], self.face_one[1], self.face_one[2], self.face_two[0], self.face_two[1], self.face_two[2], self.face_three[0], self.face_three[1], self.face_three[2], self.face_four[0], self.face_four[1], self.face_four[2])
            print(self.face_one[0+3], self.face_one[1+3], self.face_one[2+3], self.face_two[0+3], self.face_two[1+3], self.face_two[2+3], self.face_three[0+3], self.face_three[1+3], self.face_three[2+3], self.face_four[0+3], self.face_four[1+3], self.face_four[2+3])
            print(self.face_one[0+6], self.face_one[1+6], self.face_one[2+6], self.face_two[0+6], self.face_two[1+6], self.face_two[2+6], self.face_three[0+6], self.face_three[1+6], self.face_three[2+6], self.face_four[0+6], self.face_four[1+6], self.face_four[2+6])
            print("     ", self.face_six[0], self.face_six[1], self.face_six[2])
            print("    6", self.face_six[0+3], self.face_six[1+3], self.face_six[2+3])
            print("     ", self.face_six[0+6], self.face_six[1+6], self.face_six[2+6])
        elif self.active == 6:
            print('Active face: ', self.active)
            print("     ", self.face_five[0], self.face_five[1], self.face_five[2])
            print("    5", self.face_five[0+3], self.face_five[1+3], self.face_five[2+3])
            print("  1  ", self.face_five[0+6], self.face_five[1+6], self.face_five[2+6], "  3     4")
            print(self.face_one[0], self.face_one[1], self.face_one[2], self.face_two[0], self.face_two[1], self.face_two[2], self.face_three[0], self.face_three[1], self.face_three[2], self.face_four[0], self.face_four[1], self.face_four[2])
            print(self.face_one[0+3], self.face_one[1+3], self.face_one[2+3], self.face_two[0+3], self.face_two[1+3], self.face_two[2+3], self.face_three[0+3], self.face_three[1+3], self.face_three[2+3], self.face_four[0+3], self.face_four[1+3], self.face_four[2+3])
            print(self.face_one[0+6], self.face_one[1+6], self.face_one[2+6], self.face_two[0+6], self.face_two[1+6], self.face_two[2+6], self.face_three[0+6], self.face_three[1+6], self.face_three[2+6], self.face_four[0+6], self.face_four[1+6], self.face_four[2+6])
            print("     ", self.face_six[0], self.face_six[1], self.face_six[2])
            print("    A", self.face_six[0+3], self.face_six[1+3], self.face_six[2+3])
            print("     ", self.face_six[0+6], self.face_six[1+6], self.face_six[2+6])