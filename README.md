# API Yamdb

## API Yamdb дает возможность просматривать произведения (название, год выпуска, описание), ставить им оценки (от 1 до 10) и оставлять комментарии.

### Как запустить проект 

*Клонировать репозиторий*
```
git clone git@github.com:Kalmar4uk/api_yamdb.git
```

*Перейти в проект через командную строку*
```
cd api_yamdb
```

*Создать и активировать виртуальное окружение*
```
python source venv venv
```
```
source venv/Scrtipts/activate
```

*Обновить pip*
```
python -m pip install --upgrade pip
```

*Установить зависимости*
```
pip install -r requitements.txt
```

*Перейти в директорию с файлом manage.py, выполнить миграции и запустить*
```
cd api_api_yamdb
```
```
python manage.py migrate
```
```
python mange.py runserver
```
### После запуска можно отправлять запросы на эндпоинты проекта
**Ниже представлен короткий список эндпоинтов для получения Произведений, Категорий, Жанров, а так же Отзывов и Комментариев к произведениям**

**Полный список эндпоинтов проекта можно посмотреть на странице `127.0.0.1:8000/redoc`**

*Получить список всех произведений:*
```
127.0.0.1:8000/api/v1/titles/
```
*Получить конкретное произведение:*
```
127.0.0.1:8000/api/v1/titles/{id}/
```
*Получить список всех категорий:*
```
127.0.0.1:8000/api/v1/categories/
```
*Получить список всех жанров:*
```
127.0.0.1:8000/api/v1/genres/
```
*Получить список всех отзывов произведения:*
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
*Получить конкретный отзыв произведения:*
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
```
*Получить список всех комментариев к отзыву:*
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
*Получить конкретный комментарий к отзыву:*
```
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

### Так же предусмотрены Пользовательские роли

- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django — обладает правами администратора (admin)

### Добавление данных из файлов csv

*Перейти в директорию с файлом manage.py*
```
cd api_yamdb
```
*Прописать команду:*
```
python manage.py import_csv file_name.csv --model_name model
```
Где:
* *file_name.csv* - название файла для загрузки
* *--model_name model* - "--model_name" устанавливаетя для указания модели, "model" название модели в которую необходимо загрузить данные из файла
> "--model_name model" **не прописывается только в том случае, если загружается файл для таблицы ManyToMany, команда в таком случае будет** ```python manage.py import_csv file_name.csv```

**В проекте используется:**

Django 3.2.16
Django Rest Framework 3.12.4

**Работу выполнили:**

**Беспалов Роман** `https://github.com/Kalmar4uk`
**Лазарев Дмитрий** `https://github.com/d-lyzarev`
**Жуланов Олег** `https://github.com/DesperateBoy`
