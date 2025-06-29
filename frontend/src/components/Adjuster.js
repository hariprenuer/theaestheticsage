import axios from 'axios';

const Adjuster=async (orig,edit,range)=>{
    const res = await axios.post('http://localhost:8000/adjust', {
        "original_data":orig,
        "edited_points":edit,
        "x_range":range
    });
    return res.data // Pass full data
    } 
export default Adjuster;