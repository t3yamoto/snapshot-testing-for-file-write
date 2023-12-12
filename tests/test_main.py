from src.main import json_to_csv
from pathlib import Path


def test_json_to_csv(snapshot, tmp_path):
    output_csv_path = Path(tmp_path / "output.csv")
    json_to_csv(Path("input.json"), output_csv_path)

    snapshot.snapshot_dir = Path("tests/snapshots")
    snapshot.assert_match(output_csv_path.read_text(), "snapshot.csv")
