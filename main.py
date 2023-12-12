from pathlib import Path
import json
from csv import DictWriter


def json_to_csv(input_json_path: Path, output_csv_path: Path):
    with open(input_json_path, "r") as infile:
        json_data = json.load(infile)
        users = json_data["users"]
        with open(output_csv_path, "w") as outfile:
            writer = DictWriter(outfile, fieldnames=users[0].keys())
            writer.writeheader()
            writer.writerows(users)


if __name__ == "__main__":
    json_to_csv(Path("input.json"), Path("output.csv"))
