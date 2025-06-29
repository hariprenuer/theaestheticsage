dictthithi={"prathamai":["thulam","magaram"],"thuthiyai":["dhanush","magaram"],"thiruthiyai":["magaram","simmam"],"chathurthi":["kumbam","rishabam"],
               "panchami":["midhunam","kanni"],"sashti":["mesham","simmam"],"sapthami":["dhanush","kadagam"],"ashtami":["midhunam","kanni"],
               "navami":["simmam","viruchigam"],"dhasami":["simmam","viruchigam"],"ekadasi":["dhanush","meenam"],"dhuvadasi":["thulam","magaram"],
               "dhriyadasi":["rishabam","simmam"],"chathurdasi":["midhunam","kanni","dhanush","meenam"]}
class thithisunya:
    def __init__(self,thithi):
        if thithi in dictthithi:
            self.thithisumyarasi=dictthithi[thithi]