from rest_framework import serializers
from atracoes.models import Atracao

class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('nome', 'descricao' ,'horario_func','idade_minima','foto')