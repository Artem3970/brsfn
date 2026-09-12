# Boristene Django site

## Run locally

```powershell
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Content management

Create an admin account with `python manage.py createsuperuser`, then open
`http://127.0.0.1:8000/admin/` to manage projects, events, partners,
achievements, media mentions, team members and FAQs.

Project pages use the dynamic route `/projects/<slug>/`. The existing
Unbreakable Ukraine presentation remains available at
`/projects/unbreakable-ukraine/` until its final media and source materials are
provided.
