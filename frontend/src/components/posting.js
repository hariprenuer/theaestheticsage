import React from "react";
import axios from "axios";
import { Formhandler } from "./birthdataform";
export function Dataposting(props){
    const [input,manipulate]=React.useState({
      longitude:"",
      latitude: "",
      date: "",
      month: "",
      year: "",
      hour: "",
      minutes: ""
    })
    React.useEffect(()=>{
        if (props.sub){
        axios.post("http://127.0.0.1:8000/",{
          "longitude":input.longitude,
          "latitude": input.latitude,
          "date": input.date,
          "month": input.month,
          "year": input.year,
          "hour": input.hour,
          "minutes": input.minutes})
        .then(res=>{console.log(res)})
        .catch(err=>{console.log(err)})}
    },[props.sub])
    const handleinput=eve=>{manipulate(prev=>{return {...prev,[eve.target.name]:Number(eve.target.value)}})}
    const submithandler=eve=>{
      eve.preventDefault()
      //console.log("submitted",input)
      props.submit()
    }
    return (
      <div>
        <Formhandler input={input} handleInput={handleinput} submithandler={submithandler}/>
      </div>
    )
  }
  