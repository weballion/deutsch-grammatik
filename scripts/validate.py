"""Проверка банка заданий: uv run scripts/validate.py [путь_к_tasks.json]"""
import json,re,sys,collections
def norm(s): return re.sub(r"\s+"," ",re.sub(r"[.,!?;:\"«»„“”]"," ",s.lower())).strip()
def txt(v):
    """Поле может быть простой строкой или {ru,uk} — для проверок берём любой непустой вариант."""
    if isinstance(v,dict): return v.get("uk") or v.get("ru") or ""
    return v or ""
path=sys.argv[1] if len(sys.argv)>1 else "data/tasks.json"
d=json.load(open(path,encoding="utf-8"));B=d["blocks"];errs=[];seen={};ids=set()
for t in d["tasks"]:
    i=t.get("id");k=t.get("block");ty=t.get("type");tx=txt(t.get("text"))
    if i in ids: errs.append(f"{i}: повтор id")
    ids.add(i)
    if k not in B: errs.append(f"{i}: нет блока {k}"); continue
    if ty not in B[k]["types"]: errs.append(f"{i}: тип {ty} не разрешён в блоке {k}")
    if not t.get("answers"): errs.append(f"{i}: нет answers")
    for f in ("prompt","text","hint"):
        if not txt(t.get(f)): errs.append(f"{i}: пустое поле {f}")
    if ty in ("choice","fill") and "___" not in tx: errs.append(f"{i}: нет ___")
    if ty=="choice" and not any(norm(o)==norm(t["answers"][0]) for o in t.get("options",[])): errs.append(f"{i}: верного ответа нет в options")
    if ty=="fix" and any(a.strip()==tx.strip() for a in t["answers"]): errs.append(f"{i}: fix совпадает с ответом")
    if ty=="build":
        w=lambda s: sorted(norm(s).split())
        for a in t["answers"]:
            if w(" ".join(tx.split(" / ")))!=w(a): errs.append(f"{i}: слова не совпадают с ответом «{a}»")
    key=(k,norm(tx))
    if key in seen: errs.append(f"{i}: дубль {seen[key]}")
    seen[key]=i
c=collections.Counter(t["block"] for t in d["tasks"])
print("Заданий:",len(d["tasks"]),dict(sorted(c.items())))
print("\n".join(errs) if errs else "Ошибок нет")
sys.exit(1 if errs else 0)
