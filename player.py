class rektangel:
    def __init__ (self, höjd, bred):
        self.höjd = höjd
        self.bred = bred

    def räkna_arean(self):
        return self.bred*self.höjd
    def set_höjd(self, höjd):
        self.höjd = höjd
    

rektangel1 = rektangel(3,4)
rektangel1.set_höjd(7)
print(rektangel1.räkna_arean())
