class rbcube:
    def __init__(self):
        self.face_one={'A','A','A',
                        'A','A','A',
                        'A','A','A'}
        self.face_two={'B','B','B',
                        'B','B','B',
                        'B','B','B'}
        self.face_three={'C','C','C',
                        'C','C','C',
                        'C','C','C'}
        self.face_four={'D','D','D',
                        'D','D','D',
                        'D','D','D'}
        self.face_five={'E','E','E',
                        'E','E','E',
                        'E','E','E'}
        self.face_six={'F','F','F',
                        'F','F','F',
                        'F','F','F'}
        self.active=1
        def rotate_right(self, active):
            if self.active is 1:
                if active is 1:
                    temp = face_one
                    self.face_one[0] = self.face_four[0]
                    self.face_one[1] = self.face_four[1]
                    self.face_one[2] = self.face_four[2]
                    temp2 = face_two
                    self.face_two[0] = temp[0]
                    self.face_two[1] = temp[1]
                    self.face_two[2] = temp[2]
                    temp = face_three
                    self.face_three[0] = temp2[0]
                    self.face_three[1] = temp2[1]
                    self.face_three[2] = temp2[2]
                    self.face_four[0] = temp[0]
                    self.face_four[1] = temp[1]
                    self.face_four[2] = temp[2]
                if active is 2:
                    temp = face_one
                    self.face_one[0+3] = self.face_four[0+3]
                    self.face_one[1+3] = self.face_four[1+3]
                    self.face_one[2+3] = self.face_four[2+3]
                    temp2 = face_two
                    self.face_two[0+3] = temp[0+3]
                    self.face_two[1+3] = temp[1+3]
                    self.face_two[2+3] = temp[2+3]
                    temp = face_three
                    self.face_three[0+3] = temp2[0+3]
                    self.face_three[1+3] = temp2[1+3]
                    self.face_three[2+3] = temp2[2+3]
                    self.face_four[0+3] = temp[0+3]
                    self.face_four[1+3] = temp[1+3]
                    self.face_four[2+3] = temp[2+3]
                if active is 3:
                    temp = face_one
                    self.face_one[0+6] = self.face_four[0+6]
                    self.face_one[1+6] = self.face_four[1+6]
                    self.face_one[2+6] = self.face_four[2+6]
                    temp2 = face_two
                    self.face_two[0+6] = temp[0+6]
                    self.face_two[1+6] = temp[1+6]
                    self.face_two[2+6] = temp[2+6]
                    temp = face_three
                    self.face_three[0+6] = temp2[0+6]
                    self.face_three[1+6] = temp2[1+6]
                    self.face_three[2+6] = temp2[2+6]
                    self.face_four[0+6] = temp[0+6]
                    self.face_four[1+6] = temp[1+6]
                    self.face_four[2+6] = temp[2+6]
            if self.active is 2:
                if active is 1:
                    temp = face_one
                    self.face_one[0] = self.face_four[0]
                    self.face_one[1] = self.face_four[1]
                    self.face_one[2] = self.face_four[2]
                    temp2 = face_two
                    self.face_two[0] = temp[0]
                    self.face_two[1] = temp[1]
                    self.face_two[2] = temp[2]
                    temp = face_three
                    self.face_three[0] = temp2[0]
                    self.face_three[1] = temp2[1]
                    self.face_three[2] = temp2[2]
                    self.face_four[0] = temp[0]
                    self.face_four[1] = temp[1]
                    self.face_four[2] = temp[2]
                if active is 2:
                    temp = face_one
                    self.face_one[0+3] = self.face_four[0+3]
                    self.face_one[1+3] = self.face_four[1+3]
                    self.face_one[2+3] = self.face_four[2+3]
                    temp2 = face_two
                    self.face_two[0+3] = temp[0+3]
                    self.face_two[1+3] = temp[1+3]
                    self.face_two[2+3] = temp[2+3]
                    temp = face_three
                    self.face_three[0+3] = temp2[0+3]
                    self.face_three[1+3] = temp2[1+3]
                    self.face_three[2+3] = temp2[2+3]
                    self.face_four[0+3] = temp[0+3]
                    self.face_four[1+3] = temp[1+3]
                    self.face_four[2+3] = temp[2+3]
                if active is 3:
                    temp = face_one
                    self.face_one[0+6] = self.face_four[0+6]
                    self.face_one[1+6] = self.face_four[1+6]
                    self.face_one[2+6] = self.face_four[2+6]
                    temp2 = face_two
                    self.face_two[0+6] = temp[0+6]
                    self.face_two[1+6] = temp[1+6]
                    self.face_two[2+6] = temp[2+6]
                    temp = face_three
                    self.face_three[0+6] = temp2[0+6]
                    self.face_three[1+6] = temp2[1+6]
                    self.face_three[2+6] = temp2[2+6]
                    self.face_four[0+6] = temp[0+6]
                    self.face_four[1+6] = temp[1+6]
                    self.face_four[2+6] = temp[2+6]
            if self.active is 3:
                if active is 1:
                    temp = face_one
                    self.face_one[0] = self.face_four[0]
                    self.face_one[1] = self.face_four[1]
                    self.face_one[2] = self.face_four[2]
                    temp2 = face_two
                    self.face_two[0] = temp[0]
                    self.face_two[1] = temp[1]
                    self.face_two[2] = temp[2]
                    temp = face_three
                    self.face_three[0] = temp2[0]
                    self.face_three[1] = temp2[1]
                    self.face_three[2] = temp2[2]
                    self.face_four[0] = temp[0]
                    self.face_four[1] = temp[1]
                    self.face_four[2] = temp[2]
                if active is 2:
                    temp = face_one
                    self.face_one[0+3] = self.face_four[0+3]
                    self.face_one[1+3] = self.face_four[1+3]
                    self.face_one[2+3] = self.face_four[2+3]
                    temp2 = face_two
                    self.face_two[0+3] = temp[0+3]
                    self.face_two[1+3] = temp[1+3]
                    self.face_two[2+3] = temp[2+3]
                    temp = face_three
                    self.face_three[0+3] = temp2[0+3]
                    self.face_three[1+3] = temp2[1+3]
                    self.face_three[2+3] = temp2[2+3]
                    self.face_four[0+3] = temp[0+3]
                    self.face_four[1+3] = temp[1+3]
                    self.face_four[2+3] = temp[2+3]
                if active is 3:
                    temp = face_one
                    self.face_one[0+6] = self.face_four[0+6]
                    self.face_one[1+6] = self.face_four[1+6]
                    self.face_one[2+6] = self.face_four[2+6]
                    temp2 = face_two
                    self.face_two[0+6] = temp[0+6]
                    self.face_two[1+6] = temp[1+6]
                    self.face_two[2+6] = temp[2+6]
                    temp = face_three
                    self.face_three[0+6] = temp2[0+6]
                    self.face_three[1+6] = temp2[1+6]
                    self.face_three[2+6] = temp2[2+6]
                    self.face_four[0+6] = temp[0+6]
                    self.face_four[1+6] = temp[1+6]
                    self.face_four[2+6] = temp[2+6]
            if self.active is 4:
                if active is 1:
                    temp = face_one
                    self.face_one[0] = self.face_four[0]
                    self.face_one[1] = self.face_four[1]
                    self.face_one[2] = self.face_four[2]
                    temp2 = face_two
                    self.face_two[0] = temp[0]
                    self.face_two[1] = temp[1]
                    self.face_two[2] = temp[2]
                    temp = face_three
                    self.face_three[0] = temp2[0]
                    self.face_three[1] = temp2[1]
                    self.face_three[2] = temp2[2]
                    self.face_four[0] = temp[0]
                    self.face_four[1] = temp[1]
                    self.face_four[2] = temp[2]
                if active is 2:
                    temp = face_one
                    self.face_one[0+3] = self.face_four[0+3]
                    self.face_one[1+3] = self.face_four[1+3]
                    self.face_one[2+3] = self.face_four[2+3]
                    temp2 = face_two
                    self.face_two[0+3] = temp[0+3]
                    self.face_two[1+3] = temp[1+3]
                    self.face_two[2+3] = temp[2+3]
                    temp = face_three
                    self.face_three[0+3] = temp2[0+3]
                    self.face_three[1+3] = temp2[1+3]
                    self.face_three[2+3] = temp2[2+3]
                    self.face_four[0+3] = temp[0+3]
                    self.face_four[1+3] = temp[1+3]
                    self.face_four[2+3] = temp[2+3]
                if active is 3:
                    temp = face_one
                    self.face_one[0+6] = self.face_four[0+6]
                    self.face_one[1+6] = self.face_four[1+6]
                    self.face_one[2+6] = self.face_four[2+6]
                    temp2 = face_two
                    self.face_two[0+6] = temp[0+6]
                    self.face_two[1+6] = temp[1+6]
                    self.face_two[2+6] = temp[2+6]
                    temp = face_three
                    self.face_three[0+6] = temp2[0+6]
                    self.face_three[1+6] = temp2[1+6]
                    self.face_three[2+6] = temp2[2+6]
                    self.face_four[0+6] = temp[0+6]
                    self.face_four[1+6] = temp[1+6]
                    self.face_four[2+6] = temp[2+6]
            if self.active is 5:
                if active is 1:
                    temp = face_five
                    self.face_five[0] = self.face_four[0]
                    self.face_five[1] = self.face_four[1]
                    self.face_five[2] = self.face_four[2]
                    temp2 = face_two
                    self.face_two[0] = temp[0]
                    self.face_two[1] = temp[1]
                    self.face_two[2] = temp[2]
                    temp = face_six
                    self.face_six[0] = temp2[0]
                    self.face_six[1] = temp2[1]
                    self.face_six[2] = temp2[2]
                    self.face_four[0] = temp[0]
                    self.face_four[1] = temp[1]
                    self.face_four[2] = temp[2]
                if active is 2:
                    temp = face_five
                    self.face_five[0+3] = self.face_four[0+3]
                    self.face_five[1+3] = self.face_four[1+3]
                    self.face_five[2+3] = self.face_four[2+3]
                    temp2 = face_two
                    self.face_two[0+3] = temp[0+3]
                    self.face_two[1+3] = temp[1+3]
                    self.face_two[2+3] = temp[2+3]
                    temp = face_six
                    self.face_six[0+3] = temp2[0+3]
                    self.face_six[1+3] = temp2[1+3]
                    self.face_six[2+3] = temp2[2+3]
                    self.face_four[0+3] = temp[0+3]
                    self.face_four[1+3] = temp[1+3]
                    self.face_four[2+3] = temp[2+3]
                if active is 3:
                    temp = face_five
                    self.face_five[0+6] = self.face_four[0+6]
                    self.face_five[1+6] = self.face_four[1+6]
                    self.face_five[2+6] = self.face_four[2+6]
                    temp2 = face_two
                    self.face_two[0+6] = temp[0+6]
                    self.face_two[1+6] = temp[1+6]
                    self.face_two[2+6] = temp[2+6]
                    temp = face_six
                    self.face_six[0+6] = temp2[0+6]
                    self.face_six[1+6] = temp2[1+6]
                    self.face_six[2+6] = temp2[2+6]
                    self.face_four[0+6] = temp[0+6]
                    self.face_four[1+6] = temp[1+6]
                    self.face_four[2+6] = temp[2+6]
            if self.active is 6:
                if active is 1:
                    temp = face_five
                    self.face_five[0] = self.face_four[0]
                    self.face_five[1] = self.face_four[1]
                    self.face_five[2] = self.face_four[2]
                    temp2 = face_two
                    self.face_two[0] = temp[0]
                    self.face_two[1] = temp[1]
                    self.face_two[2] = temp[2]
                    temp = face_six
                    self.face_six[0] = temp2[0]
                    self.face_six[1] = temp2[1]
                    self.face_six[2] = temp2[2]
                    self.face_four[0] = temp[0]
                    self.face_four[1] = temp[1]
                    self.face_four[2] = temp[2]
                if active is 2:
                    temp = face_five
                    self.face_five[0+3] = self.face_four[0+3]
                    self.face_five[1+3] = self.face_four[1+3]
                    self.face_five[2+3] = self.face_four[2+3]
                    temp2 = face_two
                    self.face_two[0+3] = temp[0+3]
                    self.face_two[1+3] = temp[1+3]
                    self.face_two[2+3] = temp[2+3]
                    temp = face_six
                    self.face_six[0+3] = temp2[0+3]
                    self.face_six[1+3] = temp2[1+3]
                    self.face_six[2+3] = temp2[2+3]
                    self.face_four[0+3] = temp[0+3]
                    self.face_four[1+3] = temp[1+3]
                    self.face_four[2+3] = temp[2+3]
                if active is 3:
                    temp = face_five
                    self.face_five[0+6] = self.face_four[0+6]
                    self.face_five[1+6] = self.face_four[1+6]
                    self.face_five[2+6] = self.face_four[2+6]
                    temp2 = face_two
                    self.face_two[0+6] = temp[0+6]
                    self.face_two[1+6] = temp[1+6]
                    self.face_two[2+6] = temp[2+6]
                    temp = face_six
                    self.face_six[0+6] = temp2[0+6]
                    self.face_six[1+6] = temp2[1+6]
                    self.face_six[2+6] = temp2[2+6]
                    self.face_four[0+6] = temp[0+6]
                    self.face_four[1+6] = temp[1+6]
                    self.face_four[2+6] = temp[2+6]
        def rotate_left(self, active):
            if self.active is 1:
                if active is 1:
                    temp = face_one
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
                if active is 2:
                    temp = face_one
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
                if active is 3:
                    temp = face_one
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
            if self.active is 2:
                if active is 1:
                    temp = face_one
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
                if active is 2:
                    temp = face_one
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
                if active is 3:
                    temp = face_one
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
            if self.active is 3:
                temp = face_one
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
                if active is 2:
                    temp = face_one
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
                if active is 3:
                    temp = face_one
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
            if self.active is 4:
                if active is 1:
                    temp = face_one
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
                if active is 2:
                    temp = face_one
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
                if active is 3:
                    temp = face_one
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
            if self.active is 5:
                if active is 1:
                    temp = face_six
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
                if active is 2:
                    temp = face_one
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
                if active is 3:
                    temp = face_one
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
            if self.active is 6:
                if active is 1:
                    temp = face_one
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
                if active is 2:
                    temp = face_one
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
                if active is 3:
                    temp = face_one
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
        def rotate_up(self, active):
            break
        def rotate_down(self, active):
            break
        def change_face(self, face):
            self.active = face
        def print_all(self):
            if self.active is 1:
                print("                     ",self.face_five)
                print(self.face_four,'Active one', self.face_one, self.face_two, self.face_three)
                print("                     ",self.face_six)
            elif self.active is 2:
                print("                     ",self.face_five)
                print(self.face_four, self.face_one, 'Active one', self.face_two, self.face_three)
                print("                     ",self.face_six)
            elif self.active is 3:
                print("                     ",self.face_five)
                print(self.face_four, self.face_one, self.face_two, 'Active one', self.face_three)
                print("                     ",self.face_six)
            elif self.active is 4:
                print("                     ",self.face_five)
                print('Active one', self.face_four, self.face_one, self.face_two, self.face_three)
                print("                     ",self.face_six)
            elif self.active is 5:
                print("                     ",'Active one', self.face_five)
                print(self.face_four,'Active one', self.face_one, self.face_two, self.face_three)
                print("                     ",self.face_six)
            elif self.active is 6:
                print("                     ",self.face_five)
                print(self.face_four, self.face_one, self.face_two, self.face_three)
                print("                     ", 'Active one', self.face_six)
            