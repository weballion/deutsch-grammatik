"""Собрать data/tasks.json из data/blocks/*.json и проверить банк: uv run scripts/build.py"""
import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
blocks_dir = root / "data" / "blocks"

blocks = {}
tasks = []
for path in sorted(blocks_dir.glob("*.json")):
    k = path.stem
    data = json.loads(path.read_text(encoding="utf-8"))
    block_tasks = data.pop("tasks")
    blocks[k] = data
    tasks.extend(block_tasks)

out = {"blocks": blocks, "tasks": tasks}
(root / "data" / "tasks.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
print(f"data/tasks.json собран: {len(tasks)} заданий из {len(blocks)} блоков")
sys.stdout.flush()

result = subprocess.run(["uv", "run", "scripts/validate.py"], cwd=root)
sys.exit(result.returncode)
