import psycopg2
from psycopg2 import Error
import os
import json
from typing import Optional, Dict
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "symptom_checker")
        self.port = int(os.getenv("DB_PORT", 5432))
        self.connection = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print("Successfully connected to PostgreSQL database")
            return True
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            return False
    
    # ... rest of the code stays the same
    def disconnect(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
    
    def save_analysis(
        self,
        symptoms: str,
        age: Optional[int],
        gender: Optional[str],
        duration: Optional[str],
        analysis_result: dict
    ) -> Optional[int]:
        """Save symptom analysis to database"""
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()
            
            cursor = self.connection.cursor()
            
            query = """
                INSERT INTO symptom_analysis 
                (symptoms, age, gender, duration, analysis_result)
                VALUES (%s, %s, %s, %s, %s)
            """
            
            analysis_json = json.dumps(analysis_result)
            values = (symptoms, age, gender, duration, analysis_json)
            
            cursor.execute(query, values)
            self.connection.commit()
            
            analysis_id = cursor.lastrowid
            cursor.close()
            
            print(f"Analysis saved with ID: {analysis_id}")
            return analysis_id
            
        except Error as e:
            print(f"Error saving analysis: {e}")
            return None

# Singleton instance
db = Database()
