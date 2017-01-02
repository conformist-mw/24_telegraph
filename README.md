# 24_telegraph
Данное приложение представляет собой упрощённый аналог известного сервиса создания анонимный статей [telegraph](http://telegra.ph). 

Любой пользователь может разместить свою статью и получить уникальный адрес в интернете.

Посмотреть запущенный проект можно на сайте [heroku](https://heroku.com). Статьи хранятся в базе данных sqlite. Авторизация пользователя проходит по cookies. В таком случае статьи можно редактировать. 

## Установка
Для использования требуется установить зависимости, например так:
```
pip3 install -r requirements.txt
```
Далее требуется создать файл базы данных, для этого необходимо войти в интерактивный режим python и сделать следующее:
```python
 from server import db
 db.create_all()
```

## Запуск
Для запуска выполняем:
```
python3 server.py
```
переходим по [ссылке](http://localhost:5000) и заполняем поля своими данными.