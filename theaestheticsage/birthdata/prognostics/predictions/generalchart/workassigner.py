# from prognostics.astrologic.karagam import auxillarydata as ax  # was originally commented
# from prognostics.astrologic.karagam.grahabalam import shadbalahelper  # was originally commented
# from prognostics.astrologic.bavagam.ashtavarkam import ashtavarkam  # was originally commented
# from prognostics.astrologic.bavagam.aadibathiyam import positionsdasainvolved  # was originally commented
# from prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import relationalindex  # was originally commented
# from prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import postiongrade  # was originally commented
# from prognostics.astrologic.planetary_positions.panchangam.kochaaram import currentpositon  # was originally commented
# from prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import planetaryaspectations  # was originally commented

# shadbalaplanets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
# planets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
# ashtavarka=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
# bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
#            "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
# class workassginer:
#     def __init__(self,name):
#         self.name=name
#         self.data=ax.auxillarydata(self.name).data
#         self.positionsinvloved=positionsdasainvolved.postionsinvolved(self.name).planetinvolvement
#         self.dasa=positionsdasainvolved.postionsinvolved(self.name).dasa
#         self.grahasubathuvam=influence.characteristics(self.name).characteristics
#         self.shadbalam=shadbalahelper.datacollector(self.name)
#         self.posgrade=postiongrade.positionalrelation(self.data).positionalrelation
#         self.dasacooperation=relationalindex.relationalindex(self.posgrade,self.dasa).relationalindex
#         self.kochaaram=currentpositon.kocharam().nakshtarachaaram
#         self.ashtavarkam=ashtavarkam.ashtavarkam(self.name)
#         self.aadhibathiyam=positionsdasainvolved.postionsinvolved(self.name).aadhibathiyam
#         self.baavaadhibathiyam=positionsdasainvolved.postionsinvolved(self.name).wrt
#         self.grahapaarvai=planetaryaspectations.grahapaaravai(self.name).grahapaarvai
#         self.baavaparvai=planetaryaspectations.grahapaaravai(self.name).baavapaarvai
#     def graphers(self,generalaffectors,numofbavas,karagaplanets):
#         ownersofgraph=[]
#         planetsinthatbava=[]
#         aspectingbaava=[]
#         affectorsofgraph=[]
#         sthanas=[self.baavaadhibathiyam[num-1] for num in numofbavas]
#         for pl in planets:
#             for num in numofbavas:
#                 if num in self.aadhibathiyam[pl]:
#                     ownersofgraph.append(pl)
#                 if self.data[pl]["lagnam"]==num:
#                     planetsinthatbava.append(pl)
#         for bv in sthanas:
#             aspectingbaava=aspectingbaava+self.baavaparvai[0][bv]
#         subathuvam=0
#         count=0
#         for pl in aspectingbaava+planetsinthatbava+ownersofgraph+karagaplanets:
#             count+=1
#             subathuvam=subathuvam+self.grahasubathuvam[pl]*self.shadbalam[pl]
#         subathuvam=subathuvam/count
#         for bv in sthanas:
#             for plot in generalaffectors:
#                 index=bavaslist.index(bv)+plot
#                 if index>12:
#                     index=index-12
#                 index=self.baavaadhibathiyam.index(bavaslist[index-1])+1
#                 for pl in self.aadhibathiyam:
#                     if index in self.aadhibathiyam[pl]:
#                         affectorsofgraph.append(pl)
#         return (ownersofgraph,affectorsofgraph,subathuvam)