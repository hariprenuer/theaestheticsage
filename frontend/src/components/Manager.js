import React, { useEffect, useState, useRef } from 'react';
import DOBForm from './DOBForm';
import D3InteractiveGraph from './D3InteractiveGraph';
import axios from 'axios';

function Manager() {
  const [data, setData] = useState(null);              // Whole backend data (including sample_val)
  const [graphData, setGraphData] = useState([]);      // Parsed sample_val
  const [editedPoints, setEditedPoints] = useState([]); // Points edited by user
  const [adjustedGraph, setAdjustedGraph] = useState(null); // Adjusted graph data
  const prevEditedPoints = useRef([]);

  // Extract graphData from backend
  useEffect(() => {
    if (data?.sample_val) {
      const parsed = data.sample_val.map(d => ({
        date: new Date(d.date),
        value: d.value,
      }));
      setGraphData(parsed);
    }
  }, [data]);

  // Periodic check to see if editedPoints changed every second
  useEffect(() => {
    const interval = setInterval(() => {
      if (
        editedPoints.length &&
        JSON.stringify(editedPoints) !== JSON.stringify(prevEditedPoints.current)
      ) {
        console.log('Sending adjusted request...');
        prevEditedPoints.current = editedPoints;

        axios.post('http://127.0.0.1:8000/adjust/', {
          original_data: data.sample_val,
          edited_points: editedPoints.map(p => ({
            date: p.date.toISOString().split('T')[0],
            value: p.value,
          })),
          x_range: [
            data.sample_val[0].date,
            data.sample_val[data.sample_val.length - 1].date,
          ],
        })
          .then(res => {
            console.log("received:")
            console.log(res.data.adjusted_data)
            const updated = res.data.adjusted_data.map(d => ({
              date: new Date(d.date),
              value: d.value,
            }));
            setAdjustedGraph(updated);
          })
          .catch(err => console.error('Error from /adjust:', err));
      }
    }, 1000);

    return () => clearInterval(interval); // Clean up
  }, [editedPoints, data]);

  return (
    <div className="App">
      {data ? (
        <D3InteractiveGraph
          data={adjustedGraph || graphData}
          graphData={adjustedGraph || graphData}
          setGraphData={setGraphData}
          editedPoints={editedPoints}
          setEditedPoints={setEditedPoints}
        />
      ) : (
        <DOBForm onSuccess={setData} />
      )}
    </div>
  );
}

export default Manager;
