DevNest AI — Python Code Analysis Platform

An AI-powered web application that helps beginner programmers
understand, learn from, and fix errors in their Python code.

<img width="1915" height="862" alt="Home Page" src="https://github.com/user-attachments/assets/134aead0-9549-4e4b-8d53-005043569593" />


What is DevNest?
DevNest analyzes Python code and provides beginner-friendly feedback
through three modes:

Explain — understands what the error means in plain language
Learn — teaches the concept behind the error
Fix — suggests how to correct the code

Built as a graduation senior project at Arab Open University, Bahrain.

Screenshots
Home Page
<img width="1915" height="862" alt="Home Page" src="https://github.com/user-attachments/assets/84f603af-28b6-40c1-90f3-da0732f59eb9" />

Features Overview
<img width="997" height="885" alt="Featurs Overview" src="https://github.com/user-attachments/assets/8652ba74-102a-4d93-8967-98bed6fa7bcc" />

Code Analyzer
<img width="1904" height="912" alt="Code Analyzer" src="https://github.com/user-attachments/assets/ea85f4d0-577c-430e-8342-89548e8c22b4" />

Code History
<img width="1227" height="674" alt="Code History" src="https://github.com/user-attachments/assets/9f5ff07b-a537-4d2c-9139-37ef74833b9b" />

AI Explanation History
<img width="1278" height="567" alt="AI Explanation History" src="https://github.com/user-attachments/assets/267190f3-d5af-4a57-a2b1-3b062ce4116e" />


Login & Register
<img width="433" height="540" alt="Login Page" src="https://github.com/user-attachments/assets/4ef90c96-c5f5-42c1-bc90-41862133ce9b" />

<img width="394" height="657" alt="Resgister Page" src="https://github.com/user-attachments/assets/4f724e13-2554-44fc-b45a-1ed3aa095bbe" />


Tech Stack
LayerTechnologyBackendFastAPI, SQLAlchemyDatabaseSQLiteFrontendHTML, CSS, JavaScriptAI ModelOllama (Qwen2.5-Coder)AnalysisPylint, Radon, AST pattern matchingAuthJWT-based authentication

Features

107+ error codes with beginner-friendly explanations
Real-time code analysis with grade, cyclomatic complexity, and maintainability score
Three interactive tabs: Explain, Learn, Fix
Personal code history with 100+ saved analyses
User authentication and session management
Cyberpunk-themed responsive UI


How to Run Locally
Requirements

Python 3.10+
Ollama installed and running with Qwen2.5-Coder model

Steps
1. Clone the repository
git clone https://github.com/moazsaeed711-code/DevNest-AI.git
cd DevNest-AI
2. Create and activate virtual environment
cd backend
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Start Ollama in a separate terminal
ollama run qwen2.5-coder
5. Run the backend
uvicorn main:app --reload
6. Open the frontend
Open frontend/index.html in your browser

Creating an Account & Saving History
DevNest includes a full user authentication system so you can save and revisit your code analysis sessions.
To register:

Open the app and click Register on the login page
Enter a username, email, and password
Click Create Account

To sign in:

Enter your username and password on the login page
Click Sign In

To view your history:

Click History in the navigation bar
Switch between Code Analysis and AI Explanations tabs
Click View Details on any saved session to revisit it


Your analysis history is saved automatically every time you analyze code while logged in.


Project Structure
DevNest-AI/
├── backend/
│ ├── main.py
│ ├── rule_engine.py
│ ├── models.py
│ └── requirements.txt
├── frontend/
│ ├── index.html
│ ├── analyzer.html
│ └── assets/
└── screenshots/

Author
Moaz Mahmoud Saeed
B.Sc. Information Technology & Computing
Arab Open University, Bahrain
LinkedIn
