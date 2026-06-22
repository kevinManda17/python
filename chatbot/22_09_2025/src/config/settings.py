import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")


def _int_env(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except ValueError:
        return default


def _float_env(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, str(default)))
    except ValueError:
        return default


class Settings:
    # API keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "").strip()
    HF_API_TOKEN: str = os.getenv("HUGGINGFACEHUB_API_TOKEN", "").strip()

    # Models
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2",
    )
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "local").strip().lower()
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-5.4-mini")
    TTS_MODEL: str = os.getenv("TTS_MODEL", "gpt-4o-mini-tts")
    TTS_VOICE: str = os.getenv("TTS_VOICE", "alloy")
    TEMPERATURE: float = _float_env("TEMPERATURE", 0.2)
    RETRIEVAL_TOP_K: int = _int_env("RETRIEVAL_TOP_K", 4)

    # Paths
    DATA_DIR: str = os.getenv("DATA_DIR", str(BASE_DIR / "data"))
    PDF_DIR: str = os.getenv("PDF_DIR", str(Path(DATA_DIR) / "pdfs"))
    VECTOR_STORE_DIR: str = os.getenv(
        "VECTOR_STORE_DIR",
        str(Path(DATA_DIR) / "vector_store"),
    )
    TEMP_DIR: str = os.getenv("TEMP_DIR", str(Path(DATA_DIR) / "temp"))

    # Processing
    CHUNK_SIZE: int = _int_env("CHUNK_SIZE", 1000)
    CHUNK_OVERLAP: int = _int_env("CHUNK_OVERLAP", 200)


settings = Settings()
