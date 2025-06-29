import React, { useRef, useEffect } from "react";
import * as d3 from "d3";

const D3InteractiveGraph = ({ editedPoints, setEditedPoints, graphData, setGraphData, data }) => {
  const svgRef = useRef();
  const margin = { top: 20, right: 30, bottom: 40, left: 50 };
  const width = 800 - margin.left - margin.right;
  const height = 400 - margin.top - margin.bottom;

  // Parse input data
  useEffect(() => {
    if (!data?.sample_val || !Array.isArray(data.sample_val)) return;

    const parsed = data.sample_val.map(d => ({
      date: new Date(d.date),
      value: +d.value
    }));

    setGraphData(parsed);
  }, [data, setGraphData]);

  // Main drawing logic
  useEffect(() => {
    if (!graphData || graphData.length === 0) return;

    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();

    const xExtent = d3.extent(graphData, d => d.date);
    const yMax = d3.max(graphData, d => d.value) || 100;

    const xScale = d3.scaleTime()
      .domain(xExtent)
      .range([0, width]);

    const yScale = d3.scaleLinear()
      .domain([0, yMax * 1.1])
      .range([height, 0]);

    const xAxis = d3.axisBottom(xScale).tickFormat(d3.timeFormat("%Y-%m-%d"));
    const yAxis = d3.axisLeft(yScale);

    const line = d3.line()
      .defined(d => d && d.date && d.value != null)
      .x(d => xScale(d.date))
      .y(d => yScale(d.value))
      .curve(d3.curveMonotoneX);

    const zoom = d3.zoom()
      .scaleExtent([1, 10])
      .translateExtent([[0, 0], [width, height]])
      .extent([[0, 0], [width, height]])
      .on("zoom", (event) => {
        const newX = event.transform.rescaleX(xScale);
        gX.call(d3.axisBottom(newX).tickFormat(d3.timeFormat("%Y-%m-%d")));

        gLine.attr("d", line.x(d => newX(d.date)));
        gDots.attr("cx", d => newX(d.date));
      });

    const svgG = svg.append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    const gX = svgG.append("g")
      .attr("transform", `translate(0,${height})`)
      .call(xAxis);

    const gY = svgG.append("g").call(yAxis);

    const gLine = svgG.append("path")
      .datum(graphData)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 2)
      .attr("d", line);

    // Drag logic
    const drag = d3.drag()
      .on("drag", function (event, d) {
        const newY = Math.max(0, yScale.invert(event.y));
        d.value = newY;
        d3.select(this).attr("cy", yScale(d.value));
        gLine.attr("d", line(graphData));

        setEditedPoints(prev => {
          const exists = prev.find(p => +p.date === +d.date);
          if (exists) {
            return prev.map(p => +p.date === +d.date ? { ...d } : p);
          }
          return [...prev, { ...d }];
        });
      });

    const gDots = svgG.selectAll("circle")
      .data(graphData)
      .enter()
      .append("circle")
      .attr("cx", d => xScale(d.date))
      .attr("cy", d => yScale(d.value))
      .attr("r", 5)
      .attr("fill", "orange")
      .call(drag);

    svg.call(zoom);

  }, [graphData, setEditedPoints]);

  return (
    <div style={{ overflowX: 'auto' }}>
      <h2>Interactive Horoscope Timeline</h2>
      <svg
        ref={svgRef}
        width={width + margin.left + margin.right}
        height={height + margin.top + margin.bottom}
      />
      <h4>Edited Points to POST:</h4>
      <pre>
        {JSON.stringify(
          editedPoints.map(p => ({
            date: p.date.toISOString().slice(0, 10),
            value: +p.value.toFixed(2)
          })),
          null,
          2
        )}
      </pre>
    </div>
  );
};

export default D3InteractiveGraph;
