class Nodo:
    def __init__(self,student):
        self.student = student
        self.heigth = 0
        self.left = self.right = None

    def getStudent(self):
        return self.student
    