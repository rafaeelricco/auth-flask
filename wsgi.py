import os

from dotenv import load_dotenv

from app.factory import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app("production")

if __name__ == "__main__":
    app.run(debug=True)
