from rest_framework import serializers
from cells.models import *

class MindDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = mind
		fields = '__all__'

class CellDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = cell
		fields = '__all__'

class ArrowDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = arrow
		fields = '__all__'