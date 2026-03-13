from pathlib import Path


def test_model_artifact_exists():
    assert Path("model/artifact/model.joblib").exists()