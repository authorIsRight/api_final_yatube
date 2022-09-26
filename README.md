# api_final
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone (https://github.com/authorIsRight/api_final_yatube.git)

Cоздать и активировать виртуальное окружение:

python -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

Ознакомиться со список доступных API:
http://127.0.0.1:8000/redoc/