from TablaHash.Lista import Lista
class Nodo:
    def __init__(self,_key, carnet,note):
        self.key = _key
        self.carnet = carnet
        self.notes = Lista()
        self.notes.Insert(note)
        self.siguiente = None
    def Insert(self, note):
        self.notes.Insert(note)
        