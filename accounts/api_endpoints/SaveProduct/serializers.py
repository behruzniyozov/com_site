from rest_framework.serializers import Serializer, IntegerField

class SaveProductSerializer(Serializer):
    id = IntegerField(required=True, help_text="ID of the product variant to save")
