import {
  LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer
} from 'recharts';

const Graph = ({data}) => {
//   const [data, setData] = useState([]);

  return (
    <>
        <div style={{ width: '100%', height: 400 }}>

            <h2>Horoscope Timeline</h2>
            <ResponsiveContainer>
                <LineChart data={data.sample_val}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" tick={{ fontSize: 10 }} />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="value" stroke="#8884d8" strokeWidth={2} dot={false} />
                </LineChart>
            </ResponsiveContainer>
        </div>
        <h1>Detials</h1>
        <div>{data.dob}</div>
    </>
  );
};

export default Graph;
