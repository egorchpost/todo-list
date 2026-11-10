# Todo list

A simple Django todo-list app with tasks and tags.

## Run locally

### Environment variables

Create a `.env` file from the example:
```bash
cp .env.example .env
```
Then, update the `SECRET_KEY` and `DEBUG` values in the .env file. 

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Features

- Tasks: content, creation datetime, optional deadline, done flag, many tags
- Tags: name only (many-to-many with tasks)
- Task list sorted: not done first, then done; newest first inside each group
- Create / edit / delete tasks and tags
- "Complete" / "Undo" button toggles a task and redirects back to the current page
- Sidebar (Home, Tags) on every page; 
- Frontend: Bootstrap 5 via CDN
