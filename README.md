🧠 AI Prompt Optimizer

A lightweight tool built with Streamlit + SQLite that helps users evaluate and improve their AI prompts.
It stores prompt history and assigns a quality score — useful for learning prompt engineering patterns.

🚀 Features

📝 Input & analyze prompts

📊 Auto-generated scoring system

💾 Saves prompt history in local DB

⚙️ Extensible architecture for OpenAI/GPT integration

🛠 Tech Stack
Component	Tech
UI	Streamlit
Storage	SQLite
Backend	Python
Future	GPT-4 API / scoring models
▶️ Run Locally
git clone <repo-url>
cd ai-prompt-optimizer
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt  # (optional later)
streamlit run src/app.py

📂 Project Structure
ai-prompt-optimizer/
 ├─ src/
 │   ├─ app.py
 │   └─ database.py
 ├─ assets/
 ├─ venv/
 ├─ .gitignore
 └─ README.md

🔧 Future Improvements

AI-powered scoring model using OpenAI API

User login system

Prompt comparison mode

Exportable analysis reports

✨ More upgrades coming soon.