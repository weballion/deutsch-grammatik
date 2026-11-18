"""Собрать банки заданий (data/blocks*/*.json) и слов (data/words/<уровень>/*.json) и проверить их: uv run scripts/build.py"""
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parent.parent

BANKS = [
    ("data/blocks", "data/tasks.json"),
    ("data/blocks_a1a2", "data/tasks_a1a2.json"),
]

ok = True
for blocks_rel, out_rel in BANKS:
    blocks_dir = root / blocks_rel
    if not blocks_dir.exists():
        continue
    blocks = {}
    tasks = []
    for path in sorted(blocks_dir.glob("*.json")):
        k = path.stem
        data = json.loads(path.read_text(encoding="utf-8"))
        block_tasks = data.pop("tasks")
        blocks[k] = data
        tasks.extend(block_tasks)
    out = {"blocks": blocks, "tasks": tasks, "updated": date.today().strftime("%d.%m.%Y")}
    (root / out_rel).write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"{out_rel} собран: {len(tasks)} заданий из {len(blocks)} блоков")
    sys.stdout.flush()
    result = subprocess.run(["uv", "run", "scripts/validate.py", out_rel], cwd=root)
    if result.returncode != 0:
        ok = False

for level in ("a2b2", "a1a2"):
    src = root / "data/words" / level
    if not src.exists():
        continue
    words = []
    for path in sorted(src.glob("*.json")):
        lesson = json.loads(path.read_text(encoding="utf-8"))
        words.extend(dict(w, lesson=lesson["lesson"]) for w in lesson["words"])
    out_rel = f"data/words_{level}.json"
    out = {"words": words, "updated": date.today().strftime("%d.%m.%Y")}
    (root / out_rel).write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"{out_rel} собран: {len(words)} слов")
    sys.stdout.flush()
    result = subprocess.run(["uv", "run", "scripts/validate_words.py", out_rel], cwd=root)
    if result.returncode != 0:
        ok = False

sys.exit(0 if ok else 1)
