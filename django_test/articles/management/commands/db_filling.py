from django.core.management.base import BaseCommand
from articles.models import Article, Tag
from mixer.backend.django import mixer

class Command(BaseCommand):
    def handle(self, *args, **options):

        art = mixer.cycle(5).blend(Article)
