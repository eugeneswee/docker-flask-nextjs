import { useState, useEffect } from 'react';

const API_URL = process.env.API_URL;

export default function Home() {
    const [items, setItems] = useState([]);
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');

    useEffect(() => {
        fetchItems();
    }, []);

    const fetchItems = async () => {
        const response = await fetch(`${API_URL}/read`, {
            mode: 'cors'
        });
        const data = await response.json();
        setItems(data);
    };

    const createItem = async () => {
        await fetch(`${API_URL}/create`, {
            method: 'POST',
            mode: 'cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, description }),
        });
        fetchItems();
    };

    return (
        <div>
            <h1>My Items</h1>
            <input 
                type="text" 
                placeholder="Name" 
                value={name} 
                onChange={(e) => setName(e.target.value)} 
            />
            <input 
                type="text" 
                placeholder="Description" 
                value={description} 
                onChange={(e) => setDescription(e.target.value)} 
            />
            <button onClick={createItem}>Create Item</button>
            <h2>Items</h2>
            <ul>
                {items.map(item => (
                    <li key={item.id}>
                        {item.name}: {item.description}
                    </li>
                ))}
            </ul>
        </div>
    );
}
