# yourtutor
## develope code with docker
```bash
docker-compose -f docker-compose.local.yml up --build
```
It'll create local dev backend and frontend servers and auto refresh code 
## for backend devs without docker
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r requirements-test.txt
export DATABASE_URI=sqlite:////tmp/analizer_api.db
pip install -e .
backend db upgrade
backend init
gunicorn -w 2 -b 0.0.0.0:5000 backend.wsgi:app --preload
```

## frontend devs must use docker