import React from 'react';
import '../styles/LoadingSpinner.css';

function LoadingSpinner() {
  return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p>Analyzing your symptoms...</p>
    </div>
  );
}

export default LoadingSpinner;