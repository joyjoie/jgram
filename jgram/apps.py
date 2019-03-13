from django.apps import AppConfig


class JgramConfig(AppConfig):
    name = 'jgram'
    
    def ready(self):
        import jgram.signals