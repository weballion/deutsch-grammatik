# Deutsch: Грамматика

Тренажёр немецкой грамматики (A2–B2). Правила проекта — в [AGENTS.md](AGENTS.md).

- `index.html` — приложение: Telegram Mini App, без ИИ, грузит задания через `fetch('data/tasks.json')`, прогресс хранит в Telegram CloudStorage (локально — в `localStorage`).
- `data/blocks/<буква>.json` — источник правды: задания и настройки блока, один файл на блок (`A.json` … `M.json`). В `.gitignore`, не публикуется (как и `materials/`).
- `data/tasks.json` — собранный банк заданий, коммитится и публикуется, его грузит `index.html`; редактировать вручную не нужно.
- `scripts/build.py` — собрать `data/tasks.json` из `data/blocks/*.json` и проверить банк: `uv run scripts/build.py`.
- `scripts/validate.py` — только проверка уже собранного `data/tasks.json`: `uv run scripts/validate.py`.

Локальный просмотр: `python3 -m http.server 8000` → http://localhost:8000 (вне Telegram хранение — через `localStorage`).

Хостинг: статический сайт (например, GitHub Pages), ссылка задаётся в @BotFather как Mini App / кнопка меню бота.
