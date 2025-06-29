owners={"suriyan":["simmam"],"chandhiran":["kadagam"],"sevvaai":["mesham","viruchigam"],
        "budhan":["midhunam","kanni"],"guru":["dhanusu","meenam"],"sukiran":["rishabam","thulam"],
        "shani":["magaram","kumbam"]}
bavas=["mesham","rishabam","midhunam","kadagam","simmam","kanni","thulam",
       "viruchigam","dhanusu","magaram","kumbam","meenam"]
moolathirikonam=["mesham","rishabam","simmam","kanni","dhanusu","kumbam","thulam"]
aanrasi=["mesham","midhunam","simmam","thulam","dhanusu","kumbam"]
indhukadhir={"suriyan":30,"chandhiran":16,"sevvvai":6,"budhan":8,"guru":10,"sukiran":12,"shani":1}
def ownership(data):
    if data in bavas:
        for ele in owners:
            if data in owners[ele]:
                return ele
def ismoolathirikonam(data):
    if data in bavas:
        if data in moolathirikonam:
            return True
def aanpenrasi(data):
    if data in aanrasi:
        return "aanrasi"
    else:
        return "penrasi"
def contents(bava,data):
    contents=[]
    for classplanet in data:
        if bavas[data[classplanet]["kaalapurushan"]-1]==bava:
            contents.append(classplanet)
    return contents
def indhulagnam(data):
    chand=data["chandhiran"]["kaalapurushan"]+9
    if chand>12:
        chand=chand-12
    lag=data["lagnam"]["kaalapurushan"]+9
    if lag>12:
        lag=lag-12
    ind=indhukadhir[ownership(bavas[chand-2])]+indhukadhir[ownership(bavas[lag-2])]
    if ind>12:
        if ind%12==0:
            ind=12
        else:
            ind=int(ind%12)
    index=data["chandhiran"]["kaalapurushan"]-1+ind-1
    if index>=12:
        index=index-12*int(index/12)
    return bavas[index]
def withrespect(kaala1,kaala2):
    if kaala2>kaala1:
        return 13-(kaala2-kaala1)
    else:
        return kaala1-kaala2+1
def aarudalagnam(data):
    laglord=withrespect(data[ownership(bavas[data["lagnam"]["kaalapurushan"]-1])]["kaalapurushan"],data["lagnam"]["kaalapurushan"])
    index=data[ownership(bavas[data["lagnam"]["kaalapurushan"]-1])]["kaalapurushan"]+laglord-1
    if index>12:
        index=index-12*int(index/12)
    return bavas[index-1]