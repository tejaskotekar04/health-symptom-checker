import React, { useState } from 'react';
import SymptomForm from './components/SymptomForm';
import ResultsDisplay from './components/ResultsDisplay';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';
import Disclaimer from './components/Disclaimer';
import { analyzeSymptoms } from './services/api';
import './styles/App.css';

function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [results, setResults] = useState(null);

  const handleAnalyze = async (formData) => {
    setLoading(true);
    setError(null);
    setResults(null);

    try {
      const response = await analyzeSymptoms(formData);
      setResults(response);
    } catch (err) {
      setError(err.message || 'Failed to analyze symptoms. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setResults(null);
    setError(null);
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <span className="app-logo-text">💚</span>
          <h1>Clinixa Health</h1>
        </div>
        <p>AI-powered symptom analysis and health recommendations</p>
      </header>

      <main className="app-main">
        <div className="container">
          <Disclaimer />
          
          <SymptomForm onSubmit={handleAnalyze} loading={loading} />
          
          {loading && <LoadingSpinner />}
          
          {error && <ErrorMessage message={error} onClose={() => setError(null)} />}
          
          {results && <ResultsDisplay results={results} onReset={handleReset} />}
        </div>
      </main>

      <footer className="app-footer">
        <p>&copy; Clinixa Health. AI powered substitute for medical advice.</p>
      </footer>
    </div>
  );
}

export default App;