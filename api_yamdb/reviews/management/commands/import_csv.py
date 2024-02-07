import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title, User

models = {
    'User': User,
    'Category': Category,
    'Comment': Comment,
    'Genre': Genre,
    'Review': Review,
    'Title': Title
}


class Command(BaseCommand):
    help = 'Команда импорта .csv файлов'

    def add_arguments(self, parser):
        parser.add_argument('name_file', type=str, help='Название файла csv')
        parser.add_argument(
            '--name_model',
            type=str,
            help='Название модели для добавления из файла csv'
        )

    def handle(self, *args, **kwargs):
        name_file = kwargs['name_file']
        name_model = kwargs['name_model']

        if name_model:
            name_model = name_model.title()
            model = models[name_model]
            with open(
                f'{settings.BASE_DIR}/static/data/{name_file}',
                'r',
                encoding='utf-8'
            ) as csvfile:
                reader = csv.DictReader(csvfile)
                model.objects.bulk_create(
                    model(**data) for data in reader
                )
                self.stdout.write(
                    self.style.SUCCESS('Данные из файла загружены')
                )
        else:
            with open(
                f'{settings.BASE_DIR}/static/data/{name_file}',
                'r',
                encoding='utf-8'
            ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    title = Title.objects.get(id=row['title_id'])
                    genre = Genre.objects.get(id=row['genre_id'])
                    title.genre.add(genre)
                self.stdout.write(
                    self.style.SUCCESS('Данные из файла загружены')
                )
