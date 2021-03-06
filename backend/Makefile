test: runflake
	python manage.py test --settings=kubar.settings.test
clear-tables:
	psql -d kubar_dev -Uveridens -c"DROP SCHEMA public CASCADE;CREATE SCHEMA public;GRANT ALL ON SCHEMA public TO postgres;GRANT ALL ON SCHEMA public TO public;COMMENT ON SCHEMA public IS 'standard public schema';"
runflake:
	@flake8 ./ --exclude='*venv,*venv_*,**migrations*,*settings*,*flake8*,manage.py,wsgi.py,wsgi-beta.py,__init__.py,*node_modules*, *LC_MESSAGES*' --ignore=E125,W605,W503
	
install-base:
	pip install -r ./requirements/base.txt
install-development:
	pip install -r ./requirements/development.txt
install-production:
	pip install -r ./requirements/production.txt
migrate:
	python manage.py migrate --settings=kubar.settings.development

install: install-base migrate
install-dev: install-development migrate
install-prod: install-production migrate
reset-db: clear-tables migrate
