import { useEffect, useState } from 'react';
import { PieChart, Pie, Cell, Legend, Tooltip, ResponsiveContainer } from 'recharts';
import {API_URL} from '../Api';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

export default function RoomTypePieChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/room-type-stats/`)
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <ResponsiveContainer width="100%" height={300}>
      <PieChart>
        <Pie data={data} dataKey="count" nameKey="name" outerRadius={100} fill="#8884d8" label>
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>
        <Tooltip />
        <Legend />
      </PieChart>
    </ResponsiveContainer>
  );
}
