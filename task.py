class Hesab:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balansi_artir(self, miktar):
        self.balans += miktar
        print("Balans artırıldı. Yeni balans:", self.balans)

    def pul_cixar(self, miqdar):
        if miqdar <= self.balans:
            self.balans -= miqdar
            print("Pul çıxarıldı. Yeni balans:", self.balans)
        else:
            print("Balansınızda kifayət qədər vəsait yoxdur.")

    def balansi_goster(self):
        print("Hesab nömrəsi:", self.hesab_nomresi)
        print("Balans:", self.balans)


class Kredit(Hesab):
    def __init__(self, hesab_nomresi, balans, kredit_meblegi):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meblegi = kredit_meblegi

    def kredit_ver(self):
        self.balans += self.kredit_meblegi
        print("Kredit hesabınıza əlavə edildi. Yeni balans:", self.balans)

    def kredit_odenisi(self):
        ayliq_odenis = self.kredit_meblegi / 12
        if ayliq_odenis <= self.balans:
            self.balans -= ayliq_odenis
            print("Kredit ödənişi həyata keçirildi. Yeni balans:", self.balans)
        else:
            print("Kredit ödənişi üçün kifayət qədər vəsait yoxdur.")


hesab1 = Kredit("123456", 5000, 10000)
hesab1.balansi_goster()
hesab1.kredit_ver()
hesab1.kredit_odenisi()
