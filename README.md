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

# Flask REST API feature development 
### Setup
- Add model to `backend/models/newmodel.py`
- Add model to `__all__` in 'backend/models/__init__.py`
- Add new resource to `backend/api/resources/newresource.py`
- Add new resources (MyNewResource, MyNewList) to `__all__` in `backend/api/resources/__init__.py`
### Create route
- Import resources into `backend/api/views.py`
- Import resource schema into `backend/api/views.py`
- Add line `api.add_resource(MyNewList, "/mynew")`
- Add lines 
```
apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)
```