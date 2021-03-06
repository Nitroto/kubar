# Kubar Events manager based on Django REST framework and Svelte 

This gives you [JSON Web Token](https://jwt.io/) auth and a few extra files to help you deploy with heroku.

## Tech stack

### Web
- [Svelte 3](https://svelte.dev/) with [TypeScript](https://www.typescriptlang.org/)
- [webpack](https://webpack.js.org/)

### Mobile
- [React Native](https://reactnative.dev/)
- [expo](https://expo.io/)

### Backend
- [Python 3.9.2](https://www.python.org/)
- [Django 3.1.7](https://www.djangoproject.com/) with ([Django REST framework](https://www.django-rest-framework.org/))
- [gunicorn](https://gunicorn.org/)
- [Whitenoise](http://whitenoise.evans.io/en/stable/)

## Instructions

### Set environment variables
- `DATABASE_URL`. For example: `postgres://USER:PASSWORD@HOST:PORT/NAME`
- `DJANGO_SECRET_KEY`. Create one with:  
    ```
    $ python
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    ```

### Running locally

Backend Django server (port 8000):  
`$ python backend/manage.py runserver --settings=kubar.settings.development`

Frontend Svelte server (port 8080):  
`$ cd frontend/web`  
`$ npm run dev`  


### Deploying to Heroku
- Use the buildpack [negativetwelve/heroku-buildpack-subdir](https://github.com/negativetwelve/heroku-buildpack-subdir):  
```$ heroku buildpacks:set https://github.com/negativetwelve/heroku-buildpack-subdir```
- This uses the `.buildpacks` definition in the app root
