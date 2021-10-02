from Homeworks.Homeworks import Homeworks
class Nodo():
    def __init__(self, value):
        self.next = None
        self.back = None
        self.up = None
        self.down = None
        self.right = None
        self.left = None
        self.value = value
        
    def __init__(self):
        self.next = None
        self.back = None
        self.up = None
        self.down = None
        self.right = None
        self.left = None
        self.homeworks = Homeworks()
    
    def getList(self):
        return self.homeworks
        
    def Insert_in_list(self,row,column, homework):
        self.homeworks.Insert(row,column,homework,)
