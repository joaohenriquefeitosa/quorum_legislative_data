import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

interface Legislator {
    id: number;
    name: string;
    supported_bills: { id: number; title: string }[];
    opposed_bills: { id: number; title: string }[];
}

function Legislator() {
    const navigate = useNavigate();
    const [legislators, setLegislators] = useState<Legislator[]>([]);

    const goBack = (e: any) => {
        e.preventDefault();
        navigate('/');
    };

    useEffect(() => {
        const apiUrl = process.env.REACT_APP_BACKEND_URL;
        if (!apiUrl) {
            console.error("API URL is not set");
            return;
        }

        const fetchLegislators = async () => {
            try {
                const response = await fetch(`${apiUrl}/persons`);

                if (!response.ok) {
                    throw new Error(`Error: ${response.statusText}`);
                }

                const data = await response.json();
                setLegislators(data);
            } catch (error) {
                console.error("Failed to fetch legislators", error);
            }
        };

        fetchLegislators();
    }, []);

    return (
        <div className="form-box">
            <h2>Legislators</h2>
            <h5 className='margin-0'><a href="" onClick={goBack}>Back</a></h5>
            <div className="form form-lg">
                <div className='table-responsive'>
                    {legislators.length > 0 ? (
                        <table className="table table-striped table-hover">
                            <thead className="thead-dark">
                                <tr>
                                    <th>ID</th>
                                    <th>Legislator</th>
                                    <th>Supported Bills</th>
                                    <th>Opposed Bills</th>
                                </tr>
                            </thead>
                            <tbody>
                                {legislators.map((legislator) => (
                                    <tr key={legislator.id}>
                                        <td>{legislator.id}</td>
                                        <td>{legislator.name}</td>
                                        <td>{legislator.supported_bills.length}</td>
                                        <td>{legislator.opposed_bills.length}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    ) : (
                        <p>No legislators found.</p>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Legislator;
