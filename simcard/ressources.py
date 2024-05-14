from import_export import resources
from .models import SimCard

class SIMRessource(resources.ModelResource):
    class Meta:
        model = SimCard
        exclude = ['id', 'created_at', 'updated_at']