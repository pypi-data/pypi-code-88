from django.core.management import BaseCommand
from sqlalchemy_schemadisplay import create_uml_graph

from vox_django.models import models


class Command(BaseCommand):
    help = 'Generates uml from models'

    def handle(self, *args, **kwargs):
        graph = create_uml_graph(models,
                                 show_operations=False,
                                 show_multiplicity_one=False)
        graph.write_png('schema.png')
