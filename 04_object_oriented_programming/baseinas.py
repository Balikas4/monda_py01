class Baseinas():
    def __init__(self, talpa, esantis_kiekis):
        self.__talpa = talpa
        self.__esantis_kiekis = 0
        self.__vandens_kiekio_pakeitimas(esantis_kiekis)

    def gauti_talpa(self):
        return self.__talpa
    
    def gauti_esanti_kieki(self):
        return self.__esantis_kiekis

    def __vandens_kiekio_pakeitimas(self, naujas_kiekis): ### __privatus metodas pvz pakeisti talpa
        if naujas_kiekis <= self.__talpa and naujas_kiekis >= 0:
            self.__esantis_kiekis = naujas_kiekis
        else:
            if naujas_kiekis < 0:
                self.__esantis_kiekis = 0
                print('Baseinas jau tuscias ispilti nera ka!')
            else:
                self.__esantis_kiekis = self.__talpa
                print('Baseinas jau pilnas! Netilps!')
        return self.__esantis_kiekis
        
    def vandens_papildymas(self, ipilamas_kiekis):
        return self.__vandens_kiekio_pakeitimas(self.__esantis_kiekis + abs(ipilamas_kiekis))
    
    def vandens_ispylimas(self, ispilamas_kiekis):
        return self.__vandens_kiekio_pakeitimas(self.__esantis_kiekis - abs(ispilamas_kiekis))    

vandens_parkas = Baseinas(2000, 4000)
print(f'Baseino talpa yra: {vandens_parkas.gauti_talpa()} litru! ir esantis kiekis: {vandens_parkas.gauti_esanti_kieki()}')