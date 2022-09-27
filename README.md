# api_final
## Финальный учебный проект спринта от Яндекса по API
Развертывание на машине позволит протестировать реализацию GET, POST, PUT, PATCH, DEL запросов

К примеру, можно получить токен для входа через API

http://127.0.0.1:8000/api/v1/jwt/create/

Создавть новуый пост 

http://127.0.0.1:8000/api/v1/posts/


Добавить комментарий

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Ознакомиться с полным списком доступных API **после развертывания** можно по ссылке:

http://127.0.0.1:8000/redoc/

Также для API запросов рекомендуется использовать специальный софт, такой как Postman
https://www.postman.com/

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone (https://github.com/authorIsRight/api_final_yatube.git)

Cоздать и активировать виртуальное окружение:
```
python -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
