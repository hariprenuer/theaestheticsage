def appropirater(data):
    if data>360:
        data=data-360
    return data
def boundarygiver(data):
    if type(data)==str:
        data=[int(i) for i in data.split("-")]
    inp=data[0]-15
    if inp<0:
        inp=360+inp
    return ([appropirater(inp),data[1],data[2]],[appropirater(data[0]),data[1],data[2]],[appropirater(data[0]+15),data[1],data[2]])
def betweentwo(first):
    first=[int(i) for i in first.split("-")]
    giver=[]
    giver.append(boundarygiver(first))
    for mult in range(1,12):
        giver.append(boundarygiver([first[0]+(30*mult),first[1],first[2]]))
    return giver
class bavagachakaram:
    def __init__(self,data):
        self.lagnaspudam=data["lagnaspudam"]
        bavadic={}
        elements=betweentwo(self.lagnaspudam)
        for ele in range(1,13):
            bavadic[ele]=elements[ele-1]
        self.bavagacharam=bavadic.copy()