# Deutsch: Грамматика

Тренажёр немецкой грамматики (A2–B2). Правила проекта — в [AGENTS.md](AGENTS.md).

- `index.html` — приложение (сейчас версия из артефакта Claude, данные встроены в файл).
- `data/tasks.json` — банк заданий (источник правды для заданий).
- `scripts/validate.py` — проверка банка: `python3 scripts/validate.py`.

Локальный просмотр: `python3 -m http.server 8000` → http://localhost:8000

Следующий шаг: Telegram Mini App (раздел 9 AGENTS.md) — вынести данные из `index.html` в загрузку `data/tasks.json`, убрать ИИ, хранение через Telegram CloudStorage.
