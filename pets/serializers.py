from rest_framework import serializers
from pets.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def update(self, instance, validate_data):
        for field in Pet._meta.fields:
            if field.name != 'id' and validate_data.get(field.name):
                setattr(instance, field.name, validate_data[field.name])

            if field.name == 'assignedTo':
                setattr(instance, field.name, validate_data.get(field.name) or None)

        instance.save()
        return instance