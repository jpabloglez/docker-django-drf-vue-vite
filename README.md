# Vue3 (Vite+Typescript) and Django (DRF)
  
This will setup, using docker-compose, a basic Django + DRF + Vuejs `(vue-cli project)` project.
* Reference: [django-drf-vuejs](https://github.com/devsar/django-drf-vuejs)

## First steps 
Start (and build if needed) containers with the command:
  - `docker-compose up -d --build`

Create Django tables on DB:
  - `docker-compose run backend migrate`

Create super user:
- Option A:
``` 
docker exec -it backend bash
python manage.py createsuperuser
- admin@admin.com
- admin
````
- Option B:
  - `docker-compose run backend createsuperuser`

Start all containers:
  - `docker-compose up`

# How to use it
First, be sure to complete `First steps` (described above).
Then, after you start all containers (with `docker-compose up`, you are free to start coding the backend or frontend (the code will be auto-reloaded, both the backend and frontend, each time you save the files in your editor).


# Directory structure

  - File `docker-compose.yml`: Orchestrate all containers settings
  - Directory `dockerfiles`: 
    - File `backend`: Dockerfile to setup Django + DRF
    - File `frontend`: Dockerfile to setup Vuejs-Vite...
  - File `Pipfile` and `Pipfile.lock`: [Pipenv](https://pipenv.readthedocs.io/en/latest/) files
  - Directory `src`:
    - Directory `backend`: Here is the Django + DRF project.
    - Drirectory `frontend`: Here is the Vuejs project.

# About the backend

## Python version

DRF container uses `python:latest` (more info at `https://hub.docker.com/_/python/`. To know which version is running on the container, run: `docker-compose run backend python --version`

## Django related things

  > Question: Can i run `manage.py` scripts from my host? If `true`, how?
  - Answer: Yes you can. Just remember to start your commands with: 

    `docker-compose run backend <any manage.py option here>`

    So for example, if you want to get `manage.py` help, you would write: 

    `docker-compose run backend help`

    Lets suppose you want to list the migrations, you would write:

    `docker-compose run backend showmigrations`

    Another example, if you want to get a `python` shell (command `python manage.py shell`), you would write:

    `docker-compose run backend shell`

  > Question: Can i run `django-admin` script from my host? If `true`, how?

  - Answer: Yes you can. Just remember to start your commands with: 

    `docker-compose run backend django-admin <your options here>`

    So for example, to get `django-admin` help, you would write:

    `docker-compose run backend django-admin help`

    Another example, if you want to get a `db shell`, you would write:

    `docker-compose run backend django-admin dbshell`

  > Question: How can i create a django app?

  - Answer: Just use the command:

    `docker-compose run backend startapp <your app name here>`

    You will found the recently created app inside `src/backend`

  > Question: Do i need to install requirements locally on my system?

  - Answer: Not if you dont want. As described above, you should be able to excecute all django commands as described above.

## (optional) Install requirements locally on your host 

  - Install `pipenv` with your distro package manager, or as you prefer.
  - In the same directory where `Pipfile` and `Pipfile.lock` exists, run: `pipenv install`
  - Done, now you are able to add your bugs at `src/backend`

# About the frontend 

## (optional) Install `vue-cli` locally on your host

  - Create a directory where `npm i -g ...` will be installed. Run: `mkdir ~/.npm-global`
  - Let `npm` where to find installed packages. Run: `npm config set prefix '~/.npm-global'`
  - Let your `bash` knows where `excecutable` installed by `npm` are. Run: ` echo "export PATH=~/.npm-global/bin:$PATH" >> ~/.bashrc `. Apply changes made on `$PATH` running: `source ~/.bashrc`, or open a new terminal. 
  - Install `@vue-cli`, run: `npm install -g @vue/cli`
  - Install `@vue/cli-init`, run: `npm install -g @vue/cli-init`

___________________________________________________________________________

## Vue3+Vite webpack fresh install
We are preparing the base components to develop our project

* Reference: [Starting up a new Vue 3 project with Vite and Docker](https://dev.to/jiprochazka/starting-up-a-new-vue-3-project-with-vite-and-docker-3355)

## Webpack with docker
Follow next steps:
```
docker-compose up -d
```
Create a new Vite project inside container
``` 
docker exec -it frontend /bin/bash

* Change app folder permissions
chown 1000:1000 app
# chown www-data:www-data app

npm init @vitejs/app
```
When prompted select Vue as your favourite framework. Then, edit the vite.config.js by adding the server object:
```js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 8000
  },
  plugins: [vue()]
})
```
Also edit the started package.json file to add the host parameter
```js
...
"scripts": {
    "dev": "vite --host",
...
```

You can now install de JS dependencies in your project
```
npm install
```
And you are ready to go:
```
npm run dev
```

## DB Postgres
In order to setup the backend with the Postgres DB it is necessary to edit the DB properties in the settings.py file
References: [in this link](https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial)

Also, we will need to build up, in the first place, the db service for Postgres in the docker-compose.yml without declaring a volume to store db files. Then we can migrate the models running backend service:
```
docker exec backend python manage.py migrate
```
And then build-up again the Postgres service using the appropiate volume to store db files.
