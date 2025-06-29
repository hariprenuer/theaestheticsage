import workassigner
baavaplanets={
1:([6,8,12],["suriyan","chandhiran","sevvaai"]),
2:([6,8,12],["guru"]),
3:([6,8,12],["sevvaai"]),
4:([6,8,12],["chandhiran","budhan"]),
5:([6,8,12],["guru"]),
6:([6,8,12],["shani"]),
7:([6,8,12],["sukiran"]),
8:([6,8,12],["shani"]),
9:([6,8,12],["suriyan","guru"]),
10:([6,8,12],["suriyan","budhan","shani","guru"]),
11:([6,8,12],["guru"]),
12:([6,8,12],["shani"]),
}
class masterclass:
    def __init__(self,name,baavam):
        self.name=name
        self.baavam=baavam
        self.generalaffectors=baavaplanets[self.baavam][1]
        self.sthanas=self.baavam
        self.karagplanets=baavaplanets[self.baavam][0]
        returned=workassigner.workassginer(self.name).graphers(self.generalaffectors,self.sthanas,self.karagaplanets)
        self.graphowners=returned[0]
        self.graphaffectors=returned[1]
        self.standardline=returned[2]
