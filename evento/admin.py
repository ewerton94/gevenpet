from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import *

admin.site.register(Postagem, MarkdownxModelAdmin)
admin.site.register(Encaminhamento, MarkdownxModelAdmin)
admin.site.register(Instituicao)
admin.site.register(PET)
admin.site.register(Petiano)
admin.site.register(Documento)
admin.site.register(Atividade)
admin.site.register(GDT)
admin.site.register(Inscricao)
admin.site.register(Pauta)
admin.site.register(ComponenteDaMesa)
admin.site.register(Assembleia)
