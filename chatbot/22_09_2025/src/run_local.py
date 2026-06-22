#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

from config.settings import BASE_DIR, settings


def main():
    for directory in [settings.PDF_DIR, settings.VECTOR_STORE_DIR, settings.TEMP_DIR]:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Dossier verifie: {directory}")

    env_file = BASE_DIR / ".env"
    example_file = BASE_DIR / ".env.example"
    if not env_file.exists() and example_file.exists():
        env_file.write_text(example_file.read_text(encoding="utf-8"), encoding="utf-8")
        print("Fichier .env cree depuis .env.example")

    os.chdir(BASE_DIR)
    subprocess.run(
        ["streamlit", "run", "src/main.py", "--server.port=8501"],
        check=False,
    )


if __name__ == "__main__":
    main()
