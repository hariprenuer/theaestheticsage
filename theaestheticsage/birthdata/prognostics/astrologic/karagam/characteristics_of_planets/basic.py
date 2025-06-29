from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.bavagam.base import bavahelpers as bh

class basic:
    def __init__(self,name,passer=None):
        self.name=name
        self.aux=ax.auxillarydata(self.name)
        if passer is not None:
            self.passer=passer
        self.bh=bh