## Инструменты разработки
## Стек:
    Python >= 3.8
    Django==4.1
    djangorestframework==3.13.1
    psycopg2-binary==2.9.3
    python-dotenv==0.20.0
    drf-yasg==1.21.3

# Старт
### 1) Клонировать репозиторий
    git clone ссылка_сгенерированная_в_вашем_репозитории
### 2) Создать образ
    docker-compose -f docker-compose.dev.yml build
### 3) Запустить контейнер
    sudo docker-compose -f docker-compose.dev.yml up
### 4)
### 5)Перейти по адресу
    http://127.0.0.1:8000/swagger/
### 6) Если нужно очистить БД
    docker-compose down -v
    