# Health Symptom Checker 🏥

An AI-powered full-stack web application that analyzes patient symptoms and provides disease predictions with medical precautions using advanced language models.

## 🌟 Features

- **AI-Powered Analysis**: Leverages Groq AI (Llama 3.3 70B) for intelligent symptom analysis
- **Real-Time Predictions**: Instant disease predictions with severity rankings
- **Medical Precautions**: Evidence-based recommendations and actionable health advice
- **Data Persistence**: MySQL database integration for storing analysis history
- **Responsive UI**: Clean, modern interface built with React
- **REST API**: Well-structured FastAPI backend with complete CRUD operations

## 🛠️ Tech Stack

### Frontend
- React.js
- JavaScript (ES6+)
- CSS3
- Fetch API

### Backend
- FastAPI (Python)
- Groq AI API (Llama 3.3 70B)
- Pydantic
- Async/Await

### Database
- MySQL
- mysql-connector-python

## 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- MySQL 8.0+
- Groq API Key ([Get it here](https://console.groq.com))

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/health-symptom-checker.git
cd health-symptom-checker
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your credentials
```

### 3. Database Setup

Open MySQL Workbench and execute:
```sql
CREATE DATABASE symptom_checker;
USE symptom_checker;

CREATE TABLE symptom_analysis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symptoms TEXT NOT NULL,
    age INT,
    gender VARCHAR(20),
    duration VARCHAR(100),
    analysis_result JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_created_at (created_at)
);
```

Or run the provided schema:
```bash
mysql -u root -p < schema.sql
```

### 4. Frontend Setup

```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env
# Add your backend URL (default: http://localhost:8000)
```

## ⚙️ Configuration

### Backend `.env`
```env
GROQ_API_KEY=your_groq_api_key_here
ENVIRONMENT=development
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=symptom_checker
DB_PORT=3306
```

### Frontend `.env`
```env
REACT_APP_API_URL=http://localhost:8000
```

## 🏃 Running the Application

### Start Backend Server
```bash
cd backend
python main.py
# Server runs on http://localhost:8000
```

### Start Frontend Server
```bash
cd frontend
npm start
# Application opens on http://localhost:3000
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information and status |
| GET | `/health` | Health check endpoint |
| POST | `/analyze-symptoms` | Analyze symptoms and get predictions |

### Example Request
```json
POST /analyze-symptoms
{
  "symptoms": "headache, fever, cough",
  "age": 25,
  "gender": "male",
  "duration": "3 days"
}
```

### Example Response
```json
{
  "possible_diseases": [
    {
      "name": "Influenza",
      "likelihood": "high",
      "description": "A contagious respiratory illness..."
    }
  ],
  "precautions": [
    "Stay hydrated",
    "Get plenty of rest",
    "Monitor temperature"
  ],
  "when_to_seek_help": "Seek immediate help if...",
  "disclaimer": "This is not a medical diagnosis..."
}
```

## 🔐 Security

- All API keys and credentials are stored in `.env` files (not committed to Git)
- CORS middleware configured for secure client-server communication
- Input validation using Pydantic models
- Parameterized SQL queries to prevent injection attacks

## ⚠️ Disclaimer

This application is for **educational purposes only** and should **not** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Tejas Kotekar**

- GitHub: [tejaskotekar04](https://github.com/tejaskotekar04)
- LinkedIn: [Tejas Kotekar](https://www.linkedin.com/in/tejas-kotekar-0302b6227/)

## 🙏 Acknowledgments

- Groq AI for providing the Llama 3.3 70B model
- FastAPI for the excellent web framework
- React team for the frontend library

---

Made by Tejas Kotekar
