from collections import OrderedDict
from rest_framework_json_api.relations import ResourceRelatedField

class ResourceRelatedTeamField(ResourceRelatedField):
    def to_representation(self, value):
        return OrderedDict([
            ('id', str(value.pk)),
            ('name', value.name)
        ])