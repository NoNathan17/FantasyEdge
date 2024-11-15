from django.contrib import admin
from .models import Player, Quarterback, RunningBack, WideReciever, TightEnd, Kicker, Defense

admin.site.register(Player)
admin.site.register(Quarterback)
admin.site.register(RunningBack)
admin.site.register(WideReciever)
admin.site.register(TightEnd)
admin.site.register(Kicker)
admin.site.register(Defense)