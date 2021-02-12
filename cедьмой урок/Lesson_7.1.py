
class Matrix:
   
    def __init__(self, test_l1, test_l2):
        self.t1 = test_l1
        self.t2 = test_l2
 
    def matr_1(self):
        for i in range(len(self.t1)):
            for j in range(len(self.t1[i])):
                print("{:4d}".format(self.t1[i][j]), end="")
            print()
        print("\n")
                
    def matr_2(self):
        for i in range(len(self.t2)):
            for j in range(len(self.t2[i])):
                print("{:4d}".format(self.t2[i][j]), end="")
            print()
        print('\n')
    def __add__(self):
        mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.t1)):
            for j in range(len(self.t2[i])):
                 mat[i][j] = self.t1[i][j] + self.t2[i][j]
                   
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))
        


               
        
        


my_test = Matrix([[0, 5, 3], [1, 4, 2], [3, 2, 1]], [[4, 6, 8], [7, 9, 11], [5, 3, 2]])
my_test.matr_1()
my_test.matr_2()
print("Сумма матриц:\n", my_test.__add__())

            

            
        





