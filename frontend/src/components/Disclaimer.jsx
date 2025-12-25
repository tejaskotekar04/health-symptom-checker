import React from 'react';
import '../styles/Disclaimer.css';

function Disclaimer() {
  return (
    <div className="disclaimer-banner">
      <span className="info-icon">ℹ️</span>
      <p>
        <strong>Important:</strong> This tool provides general health information only. 
        It is not a substitute for professional medical advice, diagnosis, or treatment. 
        Always consult a qualified healthcare provider for medical concerns.
      </p>
    </div>
  );
}

export default Disclaimer;