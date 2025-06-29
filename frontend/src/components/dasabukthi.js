const dasayears={
    "suriyan":6,
    "chandhiran":10,
    "sevvaai":7,
    "rahu":18,
    "guru":16,
    "shani":19,
    "budhan":17,
    "kethu":7,
    "sukiran":20,
}
const yeartoms=31556952000;
const hourtoms=3600000;
const timeunits=[12,30,24,60,60,1000];
export const planets=["suriyan","chandhiran","sevvaai","rahu","guru","shani","budhan","kethu","sukiran"]

export function listchanger(pl){
    let change=[];
    if (pl in dasayears){
        for (let i=planets.indexOf(pl);i<=planets.indexOf(pl)+8;i+=1){
            let count=(i>8)?i-9:i;
            change.push(planets[count]);
        }
    return change;
    }
}
function tomsconverter(data){
    let val=0;
    function product(index){
        let returner=1;
        if (index>=0){
            for (let item=0;item<index+1;item+=1) returner=returner*timeunits[item]
            return returner;}
        else return 1;
    }
    for (let cou=0;cou<data.length;cou+=1) val=val+(data[cou]*yeartoms)/(product(cou-1));
    
    return val;
}

function stringtoarray(data){
    return data.split("-").map(ele=>Number(ele))
}

function agecal(dob,tob){
    const datenow= new Date();
    const date=[datenow.getDate(),datenow.getMonth(),datenow.getFullYear()];
    const time=[datenow.getHours(),datenow.getMinutes(),datenow.getSeconds()];
    let year,month,day,hours,minutes,seconds;
    year=(date[2]>dob[2])?date[2]-dob[2]:0;
    if (date[1]>dob[1]) month=date[1]-dob[1];
    else{ year=year-1;month=date[1]+13-dob[1];}
    if (date[0]>dob[0]) day=date[0]-dob[0];
    else{ month=month-1; day=date[0]+30-dob[0];}
    let count=0;
    for (let i=dob[2];i<date[2];i+=1){count+=((i%4==0 && i%100!=0) || i%400==0)?1:0;}
    day+=count;
    if (day>30) {day-=30;month+=1;}
    hours=(tob[0]>time[0])?tob[0]-time[0]:time[0]-tob[0];
    if (tob[1]<time[1]) {minutes=time[1]-tob[1]}
    else {minutes=time[1]+60-tob[1];hours-=1;}
    if (tob[2]==undefined) tob[2]=0
    if (tob[2]<time[2]) {seconds=time[2]-tob[2]}
    else {seconds=time[2]+60-tob[2];minutes-=1;}
    let valueoflarge=(year+(month+(day/30))/12)*yeartoms+(hours+(minutes+(seconds/60))/60)*hourtoms;
    return valueoflarge;
}

function influcencerduration(data){
    let value=1;
    let nof=0;
    if (data.length!=1){
        for (let pl of data){
            if (pl in dasayears) value=value*dasayears[pl]
            else nof+=1;
        }
        return (value/(Math.pow(120,data.length-nof-1)))*yeartoms}
    }
function planetaryinfluencers(dob,tob,dasairuppu,iruppugraha){
    let age=agecal(dob,tob);
    const order=12;
    let influencers=[];
    let diff;
    let iruppudasa=tomsconverter(dasairuppu);
    let cond=(age>iruppudasa)?true:false;
    let amt=0;
    if (cond) {;
        diff=age-iruppudasa;
        let index=planets.indexOf(iruppugraha)+1;
        index=(index>8)?index-8:index;
    iruppugraha=planets[index]}
    for (let pl of listchanger(iruppugraha)){
        amt+=dasayears[pl]*yeartoms;
        if (amt>diff) {
            amt-=dasayears[pl]*yeartoms;
            influencers.push(pl);
            break}
    }
    for (let nan=0;nan<(order-1);nan+=1) influencers.push(NaN)
    for (let count=1;count<(order-1);count+=1){
        let notinclude=0
        for (let pl of listchanger(influencers[count-1])){
            influencers[count]=pl;
            amt=amt+influcencerduration(influencers);
            if (amt>diff){
                influencers[count]=pl;
                amt=amt-influcencerduration(influencers);
                break
            }
            else{
                notinclude+=1;
                if (notinclude==9){
                    console.log("WARNING not included!",influencers[count-1]);}
                }
            }
        if (notinclude==9){
            console.log("WARNING not included!",influencers[count-1]);}
        }

    return influencers;
}
export class Dasabukthi{
    constructor(dob,tob,iruppudasa,iruppuplanet){
        this.dob=stringtoarray(dob);
        this.tob=stringtoarray(tob);
        this.iruppudasa=stringtoarray(iruppudasa);
        this.iruppuplanet=(iruppuplanet in dasayears)?iruppuplanet:"";
        this.age=agecal(this.dob,this.tob);
        // console.log("created")
        this.change=planetaryinfluencers(this.dob,this.tob,this.iruppudasa,this.iruppuplanet);
    }
    changeit(){
        return planetaryinfluencers(this.dob,this.tob,this.iruppudasa,this.iruppuplanet);
    }
}
// export default Dasabukthi;