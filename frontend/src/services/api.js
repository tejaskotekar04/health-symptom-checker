const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const analyzeSymptoms = async (data) => {
    try {
        const response = await fetch(`${API_BASE_URL}/analyze-symptoms`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to analyze symptoms');
        }

        const result = await response.json();
        return result;
    } catch (error) {
        if (error.message.includes('Failed to fetch')) {
            throw new Error('Cannot connect to server. Please make sure the backend is running.');
        }
        throw error;
    }
};

export const checkHealth = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();
        return data;
    } catch (error) {
        throw new Error('Server health check failed');
    }
};