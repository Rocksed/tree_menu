***Этот проект представляет собой реализацию деревообразного меню с использованием Django.
Установка***

>Клонируйте репозиторий на свой локальный компьютер.

bash

git clone https://github.com/Rocksed/tree_menu.git
___
>Установите зависимости.

bash

pip install -r requirements.txt
___
>Примените миграции.

bash

python manage.py migrate
___
>Создайте суперпользователя

bash

python manage.py createsuperuser
___
>Заполните БД данными

bash

python manage.py loaddata data
___
>Запустите сервер.

bash

python manage.py runserver

    Перейдите на http://localhost:8000/.