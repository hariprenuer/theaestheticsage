from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic
import math
class chanhdirasubathuvam(basic):
    def __init__(self,name):
        super().__init__(name)
        self.data=self.aux.data
        suriyapaagai=self.data["suriyan"]["paagai"]
        suryapos=suriyapaagai*3600+self.data["suriyan"]["kalai"]*60+self.data["suriyan"]["vikalai"]
        chandhirapos=self.data["chandhiran"]["paagai"]*3600+self.data["chandhiran"]["kalai"]*60+self.data["chandhiran"]["vikalai"]
        self.moonintensity=(100/(180*3600))*(math.fabs(suryapos-chandhirapos))
        suriyapaagai=self.data["suriyan"]["paagai"]+180
        if suriyapaagai>360:
            suriyapaagai=suriyapaagai-360*int(suriyapaagai/360)
        suryapos=suriyapaagai*3600+self.data["suriyan"]["kalai"]*60+self.data["suriyan"]["vikalai"]
        chandhirapos=self.data["chandhiran"]["paagai"]*3600+self.data["chandhiran"]["kalai"]*60+self.data["chandhiran"]["vikalai"]
        if chandhirapos<=suryapos:
            self.chandhirasubathuvam=self.moonintensity
        else:
            if self.moonintensity>100:
                self.chandhirasubathuvam=100-(self.moonintensity-100)
                self.moonintensity=100-(self.moonintensity-100)
            else:
                self.chandhirasubathuvam=self.moonintensity