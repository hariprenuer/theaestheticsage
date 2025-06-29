import React from "react";
export function Formhandler(props){
    return (
    <form onSubmit={props.submithandler}>
        <input type="number" className="form-control" 
            placeholder="longitude"
            value={props.input.longitude} name="longitude"
            onChange={props.handleInput} />
    
        <input type="number" className="form-control" 
            placeholder="latitude"
            value={props.input.latitude} name="latitude"
            onChange={props.handleInput} />
    
        <input type="number" className="form-control" 
            placeholder="date"
            value={props.input.date} name="date"
            onChange={props.handleInput} />
                            
        <input type="number" className="form-control" 
            placeholder="month"
            value={props.input.month} name="month"
            onChange={props.handleInput} />
                                   
        <input type="number" className="form-control" 
            placeholder="year"
            value={props.input.year} name="year"
            onChange={props.handleInput} />
                            
        <input type="number" className="form-control" 
            placeholder="hour"
            value={props.input.hour} name="hour"
            onChange={props.handleInput} />
                            
        <input type="number" className="form-control" 
            placeholder="minutes"
            value={props.input.minutes} name="minutes"
            onChange={props.handleInput} />
    
        <button type="submit" className="btn btn-primary mb-5">
            Submit
        </button>
  
    </form>)
  }