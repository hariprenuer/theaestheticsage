tharkaalamithru=[2,3,4,10,11,12]
naturalrelation={"suriyan":{"mithru":["chandhiran","sevvaai","guru","suriyan"],"samam":["budhan"],"chathru":["shani","sukiran","rahu","kethu"]},
                 "chandhiran":{"mithru":["suriyan","budhan","chandhiran"],"samam":["guru","shani","sevvaai","sukiran"],"chathru":["rahu","kethu"]},
                 "sevvaai":{"mithru":["chandhiran","suriyan","guru","sevvaai"],"samam":["shani","sukiran","rahu","kethu"],"chathru":["budhan"]},
                 "budhan":{"mithru":["suriyan","sukiran","rahu","kethu","budhan"],"samam":["guru","sevvaai","shani"],"chathru":["chandhiran"]},
                 "guru":{"mithru":["chandhiran","sevvaai","suriyan","guru"],"samam":["shani"],"chathru":["budhan","sukiran","rahu","kethu"]},
                 "sukiran":{"mithru":["budhan","shani","rahu","kethu","sukiran"],"samam":["guru","sevvaai"],"chathru":["suriyan","chandhiran"]},
                 "shani":{"mithru":["budhan","sukiran","rahu","kethu","shani"],"samam":["guru"],"chathru":["suriyan","sevvaai","chandhiran"]},
                 "rahu":{"mithru":["budhan","sukiran","shani","kethu","rahu"],"samam":["sevvaai"],"chathru":["suriyan","guru","chandhiran"]},
                 "kethu":{"mithru":["budhan","sukiran","shani","rahu","kethu"],"samam":["sevvaai"],"chathru":["suriyan","guru","chandhiran"]}}
physicalpl=['suriyan','chandhiran','sevvaai','budhan','guru','sukiran','shani','rahu','kethu']
class positionalrelation:
    def __init__(self,data):
        self.data=data
        rel={}
        for pl in physicalpl:
            rel[pl]={"adhimithru":[],"mithru":[],"samam":[],"chathru":[],"adhichathru":[]}.copy()
        for pl in physicalpl:
            for pl2 in physicalpl:
                if pl!=pl2:
                    if self.data[pl2][pl] in tharkaalamithru and pl2 in naturalrelation[pl]["mithru"]:
                        rel[pl]["adhimithru"].append(pl2)
                    elif self.data[pl2][pl] in tharkaalamithru and pl2 in naturalrelation[pl]["samam"]:
                        rel[pl]["mithru"].append(pl2)
                    elif self.data[pl2][pl] in tharkaalamithru and pl2 in naturalrelation[pl]["chathru"]:
                        rel[pl]["samam"].append(pl2)
                    elif self.data[pl2][pl] not in tharkaalamithru and pl2 in naturalrelation[pl]["mithru"]:
                        rel[pl]["samam"].append(pl2)
                    elif self.data[pl2][pl] not in tharkaalamithru and pl2 in naturalrelation[pl]["samam"]:
                        rel[pl]["chathru"].append(pl2)
                    elif self.data[pl2][pl] not in tharkaalamithru and pl2 in naturalrelation[pl]["chathru"]:
                        rel[pl]["adhichathru"].append(pl2)
        self.positionalrelation=rel.copy()