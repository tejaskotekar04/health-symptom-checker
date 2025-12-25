import React from 'react';
import '../styles/ErrorMessage.css';

function ErrorMessage({ message, onClose }) {
  return (
    <div className="error-container">
      <div className="error-content">
        <span className="error-icon">❌</span>
        <p className="error-message">{message}</p>
        <button onClick={onClose} className="close-btn">✕</button>
      </div>
    </div>
  );
}

export default ErrorMessage;