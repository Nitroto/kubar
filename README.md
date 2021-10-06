# Kubar Events manager based on Django REST framework and Svelte

## Tech stack

### Web

- [Svelte 3](https://svelte.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [GraphQL](https://graphql.org/)
- [rollup.js](https://rollupjs.org/)
- [Svelte Material UI](https://sveltematerialui.com/)

### Mobile

- [React Native](https://reactnative.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [expo](https://expo.io/)

### Backend

- [Python 3.9](https://www.python.org/)
- [Django 3.2.8](https://www.djangoproject.com/)
- [Graphene Django](https://docs.graphene-python.org/)
- [Django GraphQL JWT](https://django-graphql-jwt.domake.io/)
- [Django GraphQL Auth ](https://django-graphql-auth.readthedocs.io/)
- [gunicorn](https://gunicorn.org/)
- [Whitenoise](http://whitenoise.evans.io/)

## Instructions

### Set environment variables

- `DATABASE_URL` - For example: `postgres://USER:PASSWORD@HOST:PORT/NAME`
- `SECRET_KEY` - Create one with:
    ```
    $ python
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    ```
- `DEBUG` - Default value False for Development environment should be True
- `ALLOWED_HOSTS` - add allowed hosts, default is empty
  list. [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `SSL_REQUIRE` - Default value True for Development environment should be False

.env file can be used, put it in settings folder `backend/kubar/settings`

### Running locally

Backend Django server (port 8000):  
`$ python backend/manage.py runserver --settings=kubar.settings.development`

Frontend Svelte server (port 8080):  
`$ cd frontend/web`  
`$ npm run dev`

### Deploying to Heroku

- Use the
  buildpack [negativetwelve/heroku-buildpack-subdir](https://github.com/negativetwelve/heroku-buildpack-subdir):  
  ```$ heroku buildpacks:set https://github.com/negativetwelve/heroku-buildpack-subdir```
- This uses the `.buildpacks` definition in the app root
