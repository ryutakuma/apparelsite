# DJango Framework to Docker Composer Template

# Outline
* 本プロジェクトはDocker Compose上にDJango Frameworkを設定するデフォルトテンプレートになります。

# Startup
~~~sh
$ docker compose up
or
$ docker compose up -d
~~~

## Recompile Startup
~~~sh
$ docker compose up --build
or
$ docker compose up --build -d
~~~

## Django起動コマンド
~~~sh
$ docker compose exec web python manage.py runserver 0.0.0.0:8000
~~~

## DJangoの操作（①）
~~~sh
$ docker compose exec web /bin/bash
~~~

## アプリの追加
~~~sh
# ①を実行しなかった場合
$ docker compose exec web python manage.py startapp [データ名 OR 処理単位]
# ①を実行した場合
$ python manage.py startapp [データ名 OR 処理単位]
~~~
