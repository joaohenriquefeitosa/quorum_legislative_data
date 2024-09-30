import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();

    const goToBills = () => {
        navigate(`/bills/`);
    };

    const goToLegislators = () => {
        navigate(`/legislators/`);
    };

    return (
        <div className="form-box">
            <h2>Lesgislative Votes</h2>
            <div className='form'>
                <div className='flex justify-content-between'>
                    <div>
                        <button className="btn-primary-block" onClick={goToLegislators}>Legislators</button>
                    </div>

                    <div>
                        <button className="btn-primary-block" onClick={goToBills}>Bills</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Home;
