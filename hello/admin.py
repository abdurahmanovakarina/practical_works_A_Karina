from django.contrib import admin
from .models import Question, Choice

# user: admin
# mail: python@mail.ru
# password: 1234


admin.site.register(Question)
admin.site.register(Choice)
