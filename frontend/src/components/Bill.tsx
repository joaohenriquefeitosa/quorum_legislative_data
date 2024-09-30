import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

interface Bill {
    id: number;
    title: string;
    supporters: { id: number; name: string }[];
    opposers: { id: number; name: string }[];
    primary_sponsor_name: string;
}

function Bill() {
    const navigate = useNavigate();
    const [bills, setBills] = useState<Bill[]>([]);

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

        const fetchBills = async () => {
            try {
                const response = await fetch(`${apiUrl}/bills`);

                if (!response.ok) {
                    throw new Error(`Error: ${response.statusText}`);
                }

                const data = await response.json();
                setBills(data);
            } catch (error) {
                console.error("Failed to fetch bills", error);
            }
        };

        fetchBills();
    }, []);

    return (
        <div className="form-box">
            <h2>Bills</h2>
            <h5 className='margin-0'><a href="" onClick={goBack}>Back</a></h5>
            <div className="form form-lg">
                <div className='table-responsive'>
                    {bills.length > 0 ? (
                        <table className="table table-striped table-hover">
                            <thead className="thead-dark">
                                <tr>
                                    <th>ID</th>
                                    <th>Bill Title</th>
                                    <th>Supporters</th>
                                    <th>Opposers</th>
                                    <th>Primary Sponsor</th>
                                </tr>
                            </thead>
                            <tbody>
                                {bills.map((bill) => (
                                    <tr key={bill.id}>
                                        <td>{bill.id}</td>
                                        <td>{bill.title}</td>
                                        <td>{bill.supporters.length}</td>
                                        <td>{bill.opposers.length}</td>
                                        <td>{bill.primary_sponsor_name}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    ) : (
                        <p>No bills found.</p>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Bill;
