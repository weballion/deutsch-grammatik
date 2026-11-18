"""Проверка банка слов: uv run scripts/validate_words.py data/words_a2b2.json"""
import collections
import json
import sys

POS = {"noun", "verb", "adj", "other"}
ARTICLES = ("der ", "die ", "das ")


def check(words):
    """Вернуть список ошибок банка слов."""
    errs, ids, des = [], set(), {}
    for w in words:
        i = w.get("id")
        if i in ids:
            errs.append(f"{i}: повтор id")
        ids.add(i)
        for f in ("de", "pos", "ru", "uk", "lesson"):
            if not w.get(f):
                errs.append(f"{i}: пустое поле {f}")
        ex = w.get("ex") or {}
        if not all(ex.get(f) for f in ("de", "ru", "uk")):
            errs.append(f"{i}: нет примера ex {{de, ru, uk}}")
        if w.get("pos") not in POS:
            errs.append(f"{i}: неизвестная часть речи {w.get('pos')}")
        if w.get("pos") == "noun" and not w.get("de", "").startswith(ARTICLES):
            errs.append(f"{i}: существительное без артикля")
        key = w.get("de", "").lower()
        if key in des:
            errs.append(f"{i}: дубль {des[key]} ({w.get('de')})")
        des[key] = i
    c = collections.Counter(w.get("pos") for w in words)
    if any(n < 4 for n in c.values()):
        errs.append(f"меньше 4 слов в части речи — не набрать варианты: {dict(c)}")
    return errs, c


path = sys.argv[1] if len(sys.argv) > 1 else "data/words_a2b2.json"
words = json.load(open(path, encoding="utf-8"))["words"]
errs, c = check(words)
print("Слов:", len(words), dict(sorted(c.items())))
print("\n".join(errs) if errs else "Ошибок нет")
sys.exit(1 if errs else 0)
