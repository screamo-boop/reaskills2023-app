# Simple stupid app

## Quickstart (develop)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
flask run
```

## Quickstart (production)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
gunicorn 'app:app'
```
