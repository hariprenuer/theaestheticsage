const physicalpl=['suriyan','chandhiran','sevvaai','budhan','guru','sukiran','shani','rahu','kethu']
const keys=["adhichathru","chathru","samam","mithru","adhimithru"]
export const posgrade={
'suriyan': {'adhimithru': ['chandhiran', 'sevvaai'], 'mithru': ['budhan'], 'samam': ['guru', 'sukiran', 'shani', 'rahu'], 'chathru': [], 'adhichathru': ['kethu']},
'chandhiran': {'adhimithru': ['suriyan'], 'mithru': ['sevvaai', 'guru', 'shani'], 'samam': ['budhan', 'rahu', 'kethu'], 'chathru': ['sukiran'], 'adhichathru': []},
'sevvaai': {'adhimithru': ['suriyan', 'chandhiran'], 'mithru': ['sukiran'], 'samam': ['budhan', 'guru'], 'chathru': ['shani', 'rahu', 'kethu'], 'adhichathru': []},
'budhan': {'adhimithru': ['suriyan', 'rahu', 'kethu'], 'mithru': ['sevvaai', 'guru', 'shani'], 'samam': ['sukiran'], 'chathru': [], 'adhichathru': ['chandhiran']},
'guru': {'adhimithru': ['chandhiran'], 'mithru': ['shani'], 'samam': ['suriyan', 'sevvaai', 'budhan', 'sukiran'], 'chathru': [], 'adhichathru': ['rahu', 'kethu']}, 
'sukiran': {'adhimithru': ['shani', 'rahu', 'kethu'], 'mithru': ['sevvaai', 'guru'], 'samam': ['suriyan', 'budhan'], 'chathru': [], 'adhichathru': ['chandhiran']}, 
'shani': {'adhimithru': ['budhan', 'sukiran', 'kethu'], 'mithru': ['guru'], 'samam': ['suriyan', 'chandhiran', 'rahu'], 'chathru': [], 'adhichathru': ['sevvaai']}, 
'rahu': {'adhimithru': ['budhan', 'sukiran'], 'mithru': [], 'samam': ['suriyan', 'chandhiran', 'shani', 'kethu'], 'chathru': ['sevvaai'], 'adhichathru': ['guru']}, 
'kethu': {'adhimithru': ['budhan', 'sukiran', 'shani'], 'mithru': [], 'samam': ['chandhiran', 'rahu'], 'chathru': ['sevvaai'], 'adhichathru': ['suriyan', 'guru']}
}
export const currentdasa=[
'shani', 
'budhan',
 'chandhiran', 
 'sukiran', 
 'budhan', 
 'rahu', 
 'suriyan', 
 'budhan', 
 'kethu', 
 'budhan']

//  {'shani': 83.33333333333333, 'budhan': 47.22222222222222, 'chandhiran': 55.55555555555556, 'sukiran': 61.111111111111114, 'rahu': 77.77777777777777, 'suriyan': 61.111111111111114, 'kethu': 77.77777777777777}
function presencechecker(ele,data){
    // console.log("presence",data,data.length!=0)
    let result=false;
    if (data.length!=0){
    data.forEach(element=>{
        if (element==ele) result=!result})}
    return result;
}
function valuegiver(pos,dasa){
    let index={}
    for (let ind=0;ind<dasa.length;ind=ind+1){
        let plcont=dasa[ind]
        let amt=0
        let exarray=[];
        dasa.slice(0,ind).forEach(element => exarray.push(element));
        dasa.slice(ind+1,).forEach(element => exarray.push(element));
        for (let plx of exarray){
            for (let key of keys){ 
                if (presencechecker(plx,pos[plcont][key]))amt=amt+keys.indexOf(key)*25
                }
            }
        index[plcont]=amt/((dasa.length)-1)
    }
    // return index
}

export class Relationalindex{
    constructor(dasa){
        this.posgrade=posgrade;
        this.dasa=dasa;
    }
    thefinal(){
        return valuegiver(this.posgrade,this.dasa)
    }
}
// export default Relationalindex; 