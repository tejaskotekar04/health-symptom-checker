import React from 'react';
import '../styles/ResultsDisplay.css';

function ResultsDisplay({ results, onReset }) {
  const getLikelihoodClass = (likelihood) => {
    return `likelihood-${likelihood.toLowerCase()}`;
  };

  return (
    <div className="results-container">
      <div className="results-header">
        <h2>Analysis Results</h2>
        <button onClick={onReset} className="reset-btn">New Analysis</button>
      </div>

      <div className="possible-diseases">
        <h3>Possible Conditions</h3>
        {results.possible_diseases.map((disease, index) => (
          <div key={index} className="disease-card">
            <div className="disease-header">
              <h4>{disease.name}</h4>
              <span className={`likelihood-badge ${getLikelihoodClass(disease.likelihood)}`}>
                {disease.likelihood} likelihood
              </span>
            </div>
            <p className="disease-description">{disease.description}</p>
          </div>
        ))}
      </div>

      <div className="precautions-section">
        <h3>Recommended Precautions</h3>
        <ul className="precautions-list">
          {results.precautions.map((precaution, index) => (
            <li key={index}>{precaution}</li>
          ))}
        </ul>
      </div>

      <div className="seek-help-section">
        <h3>⚠️ When to Seek Medical Help</h3>
        <p className="seek-help-text">{results.when_to_seek_help}</p>
      </div>

      <div className="disclaimer-section">
        <p className="disclaimer-text">
          <strong>Disclaimer:</strong> {results.disclaimer}
        </p>
      </div>
    </div>
  );
}

export default ResultsDisplay;