# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


class MusicProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(MusicProfile, MusicProfileAdmin)


class InstrumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Instrument, InstrumentAdmin)

class StyleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Style, StyleAdmin)


class InfluenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Influence, InfluenceAdmin)
