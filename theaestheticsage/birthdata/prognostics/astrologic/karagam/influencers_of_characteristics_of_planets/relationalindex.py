physicalpl=['suriyan','chandhiran','sevvaai','budhan','guru','sukiran','shani','rahu','kethu']
keys=["adhichathru","chathru","samam","mithru","adhimithru"]
class relationalindex:
    def __init__(self,positional,dasacombo):
        #print("relaational index",positional)
        self.posrel=positional
        self.combo=dasacombo
        index={}
        for ind in range(len(self.combo)):
            plcont=self.combo[ind]
            amt=0
            for plx in self.combo[0:ind]+self.combo[ind+1:]:
                for key in keys:
                    if plx in self.posrel[plcont][key]:
                        amt=amt+keys.index(key)*25
            index[plcont]=amt/(len(dasacombo)-1)
        self.relationalindex=index.copy()