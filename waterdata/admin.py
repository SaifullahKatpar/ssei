from django.contrib import admin
from .models import Ontology, Author

class OntologyAdmin(admin.ModelAdmin):
     filter_horizontal = ('authors',) #If you don't specify this, you will get a multiple select widget.

admin.site.register(Ontology,OntologyAdmin)
admin.site.register(Author)