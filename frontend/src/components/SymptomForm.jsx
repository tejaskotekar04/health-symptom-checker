import React, { useState } from 'react';
import '../styles/SymptomForm.css';

function SymptomForm({ onSubmit, loading }) {
  const [formData, setFormData] = useState({
    symptoms: '',
    age: '',
    gender: '',
    duration: ''
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Clear error for this field
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  const validate = () => {
    const newErrors = {};
    
    if (!formData.symptoms.trim()) {
      newErrors.symptoms = 'Please describe your symptoms';
    }
    
    if (formData.age && (formData.age < 0 || formData.age > 120)) {
      newErrors.age = 'Please enter a valid age (0-120)';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (validate()) {
      // Convert age to number or null
      const dataToSubmit = {
        symptoms: formData.symptoms,
        age: formData.age ? parseInt(formData.age) : null,
        gender: formData.gender || null,
        duration: formData.duration || null
      };
      onSubmit(dataToSubmit);
    }
  };

  return (
    <div className="symptom-form-container">
      <h2>Enter Your Symptoms</h2>
      <form onSubmit={handleSubmit} className="symptom-form">
        <div className="form-group">
          <label htmlFor="symptoms">
            Symptoms <span className="required">*</span>
          </label>
          <textarea
            id="symptoms"
            name="symptoms"
            value={formData.symptoms}
            onChange={handleChange}
            placeholder="Describe your symptoms (e.g., headache, fever, cough, fatigue)"
            rows="4"
            disabled={loading}
            className={errors.symptoms ? 'error' : ''}
          />
          {errors.symptoms && <span className="error-text">{errors.symptoms}</span>}
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="age">Age</label>
            <input
              type="number"
              id="age"
              name="age"
              value={formData.age}
              onChange={handleChange}
              placeholder="Enter your age"
              min="0"
              max="120"
              disabled={loading}
              className={errors.age ? 'error' : ''}
            />
            {errors.age && <span className="error-text">{errors.age}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="gender">Gender</label>
            <select
              id="gender"
              name="gender"
              value={formData.gender}
              onChange={handleChange}
              disabled={loading}
            >
              <option value="">Select gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="duration">Duration of Symptoms</label>
          <input
            type="text"
            id="duration"
            name="duration"
            value={formData.duration}
            onChange={handleChange}
            placeholder="e.g., 2 days, 1 week"
            disabled={loading}
          />
        </div>

        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze Symptoms'}
        </button>
      </form>
    </div>
  );
}

export default SymptomForm;