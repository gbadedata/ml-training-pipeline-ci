from pathlib import Path
import joblib


def load_model(model_path: str):
    path = Path(model_path)
    if not path.exists():
        raise FileNotFoundError(f"Model artifact not found at {path}")
    return joblib.load(path)