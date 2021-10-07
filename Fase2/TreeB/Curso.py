class Curso():
    def __init__(self, id, name, ncredits, pre, obligatorio) :
        self.id = int(id)
        self.name = name
        self.ncredits = int(ncredits)
        self.pre = pre
        self.obligatorio = obligatorio
        