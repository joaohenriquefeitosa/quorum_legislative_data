import './App.css';
import { Routes, Route }  from 'react-router-dom';
import Home from './components/Home';
import Bill from './components/Bill';
import Legislator from './components/Legislator';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/bills/" element={<Bill />} />
      <Route path="/legislators/" element={<Legislator />} />
    </Routes>
  );
}

export default App;
