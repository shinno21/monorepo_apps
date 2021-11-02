# monorepo_apps

モノレポ構成で、Angular+Django のアプリケーションを構成する。

Angular 用の CI/Django 用の CI を用意して push/PR の都度、必要な実行する。

## some_project

バックエンドの API(Django)

* 導入手順

```shell
$ cd ./some_project
$ pip install -r requrements.txt
$ pip install -r requrements_dev.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
$ cd ./fixtures
$ python manage.py loaddata ./init_some_api.json
$ python manage.py runserver
```

## any-project

フロントエンドの 画面(Angular)

* 導入手順

```shell
$ cd ./any-project
$ npm -g config set proxy http://user:password@proxy_server:port
$ npm -g config set https-proxy http://user:password@proxy_server:port
$ npm -g config set registry http://registry.npmjs.org/
$ npm i
$ ng serve
```
