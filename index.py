class VanPhong:
    def __init__(self, chieudai, chieucao):
        self.ChieuDai = chieudai
        self.chieucao = chieucao

    def get_chieudai(self):
        return self.ChieuDai

    def get_chiecao(self):
        return self.chieucao

    def show_info(self):
        print("chieudai:", self.chieuDai, "sqft")
        print("chieucao:", self.chieucao)


class Phong1(VanPhong):
    def __init__(self, chieudai,chieucao, chieurong):
         super().__init__(chieudai, chieucao)
         self.chieurong = chieurong
         
    def dientich(self):
        print(self.ChieuDai * self.chieurong)

    def printchieucao(self):
        return self.chieucao

    def show_info(self):
        super().show_info()
        print("Floor:", self.floor)


class Phong2 (VanPhong):
    def __init__(self, chieudai,chieucao, chieurong):
         super().__init__(chieudai, chieucao)
         self.chieurong = chieurong
         
    def dientich(self):
        print(self.ChieuDai * self.chieurong)

    def printchieucao(self):
        return self.chieucao

    def show_info(self):
        super().show_info()
        print("Floor:", self.floor)

properties= [Phong1 (800, 2, 5), Phong2 (1500, 4, 1000)]

for property in  properties:
    property.show_info()
    print()