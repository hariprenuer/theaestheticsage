import React, { useState } from 'react';
import axios from 'axios';

const DOBForm = ({ onSuccess }) => {
  const [formData, setFormData] = useState({
    "latitude": 11.6643,
    "longitude": 78.1460,
    "date": 9,
    "month": 6,
    "year": 2005,
    "hour": 14,
    "minutes": 3
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log("changing")
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log("Submitted to backend:", formData);
      const res = await axios.post('http://localhost:8000/', formData);
      console.log("Response from backend:", res.data);

      if (onSuccess) onSuccess(res.data);  // Pass full data
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <h2 style={styles.heading}>Enter Birth Details</h2>
      {["latitude", "longitude", "date", "month", "year", "hour", "minutes"].map(field => (
        <div key={field} style={styles.row}>
          <label>{field.charAt(0).toUpperCase() + field.slice(1)}:</label>
          <input
            name={field}
            type="number"
            step="any"
            value={formData[field]}
            onChange={handleChange}
            required
          />
        </div>
      ))}
      <button type="submit" style={styles.button}>Submit</button>
    </form>
  );
};

const styles = {
  form: {
    maxWidth: '400px',
    margin: '20px auto',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '8px',
    fontFamily: 'Arial'
  },
  heading: {
    textAlign: 'center',
    marginBottom: '15px'
  },
  row: {
    display: 'flex',
    flexDirection: 'column',
    marginBottom: '10px'
  },
  button: {
    marginTop: '10px',
    padding: '8px 12px',
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    cursor: 'pointer',
    borderRadius: '4px'
  }
};

export default DOBForm;
