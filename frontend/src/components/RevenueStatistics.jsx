import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';
import {API_URL} from '../Api';

export default function RevenueOverTimeChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/revenue-over-time`)
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="date" />
        <YAxis allowDecimals={false} />
        <Tooltip />
        <Line type="monotone" dataKey="total_revenue" stroke="#8884d8" />
      </LineChart>
    </ResponsiveContainer>
  );
}
