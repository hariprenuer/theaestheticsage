import React from "react";
import axios from 'axios';
export function Datafetching(props){
    React.useEffect(()=>{
      setTimeout(()=>{
        axios.get("http://127.0.0.1:8000/")
        .then(response=>{
            props.result(response.data)
        props.passer()})
        .catch(err=>{
            props.result(err);
          console.log(err,"error")
        })
        },1000)
    },[])
    return (
      <div>
        <p>{}</p>
      </div>
    )
  }