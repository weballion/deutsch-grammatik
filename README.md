# Deutsch: Грамматика

Тренажёр немецкой грамматики (A2–B2 и A1–A2). Правила проекта — в [AGENTS.md](AGENTS.md).

- `index.html` — приложение: Telegram Mini App, без ИИ, грузит задания через `fetch`, прогресс хранит в Telegram CloudStorage (локально — в `localStorage`). Переключатель уровня в настройках.
- `data/blocks/<буква>.json` / `data/blocks_a1a2/<буква>.json` — источник правды: задания и настройки блока, по одному файлу на блок, отдельно для каждого уровня. В `.gitignore`, не публикуются (как и `materials/`).
- `data/tasks.json` / `data/tasks_a1a2.json` — собранные банки заданий, коммитятся и публикуются, их грузит `index.html`; редактировать вручную не нужно.
- `scripts/build.py` — собрать оба банка из `data/blocks*/*.json` и проверить их: `uv run scripts/build.py`.
- `scripts/validate.py` — проверка уже собранного банка: `uv run scripts/validate.py [путь]` (по умолчанию `data/tasks.json`).

Локальный просмотр: `python3 -m http.server 8000` → http://localhost:8000 (вне Telegram хранение — через `localStorage`).

Хостинг: статический сайт (например, GitHub Pages), ссылка задаётся в @BotFather как Mini App / кнопка меню бота.
