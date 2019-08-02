from pathlib import Path
import json


def files(root):
    return list(Path(root).rglob('.cubist.json'))


def file_data(root):
    return [json.loads(f.read_text()) for f in files(root)]
