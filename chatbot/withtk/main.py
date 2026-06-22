from app.database import init_db
from app.ui import run_ui

if __name__ == "__main__":
    init_db()
    run_ui()
