from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import degreeofcloseness as dc
planetaries=["lagnam",'suriyan','chandhiran','sevvaai','budhan','guru','sukiran','shani','rahu','kethu']
class aspectationinfluence(basic):
    rateofasp={"suriyan":0.8,"chandhiran":0.8,"sevvaai":1,"budhan":0.8,"guru":1,"sukiran":0.8,"shani":1,"rahu":0.9,"kethu":0.9}
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.data=dc.degreeofcloseness(self.name,self.passer).closeness
        asp={}
        self.asp=self.aux.plas["grahapaarvai"]
        for pl in planetaries:
            asp[pl]=0
        for pl in planetaries:
            for ass in self.asp["mullupaarvai"][pl]:
                asp[pl]=self.data[pl]+self.rateofasp[ass]*self.data[ass]
            for ass1 in self.asp["kaalpaarvai"][pl]:
                asp[pl]=asp[pl]+self.rateofasp[ass1]*self.data[ass1]*0.25
            for ass2 in self.asp["araipaarvai"][pl]:
                asp[pl]=asp[pl]+self.rateofasp[ass2]*self.data[ass2]*0.5
            for ass3 in self.asp["mukaalpaarvai"][pl]:
                asp[pl]=asp[pl]+self.rateofasp[ass3]*self.data[ass3]*0.75
        self.aspinfluence=asp.copy()