from django.contrib import admin

from .models import Clue, Relation, PersonOfInterst, Incident

admin.site.register(Clue)
admin.site.register(Relation)
admin.site.register(PersonOfInterst)
admin.site.register(Incident)
