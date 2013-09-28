# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MusicProfile, Instrument, Influence, UserInfluence, UserInstrument, UserRating


class MusicProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(MusicProfile, MusicProfileAdmin)


class InstrumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Instrument, InstrumentAdmin)


class InfluenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Influence, InfluenceAdmin)
