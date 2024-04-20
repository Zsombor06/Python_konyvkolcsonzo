class Konyv():
    def __init__(self,cim,vonalkod,szerzo,kiado,ev,nyelvkod,konyvtar):
        self.cim=cim
        self.vonalkod=vonalkod
        self.szerzo=szerzo
        self.kiado=kiado
        self.ev=ev
        self.nyelvkod=nyelvkod
        self.konyvtar=konyvtar

konyv1=Konyv("A gyűrűk ura","9900003334489","J.R.R Tolkien","Európa","2013","978-963-07-9562-3","A könyvtár")
konyvek=[konyv1]