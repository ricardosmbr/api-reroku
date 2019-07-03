from rest_framework import serializers
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(serializers.ModelSerializer):
	atracoes = AtracaoSerializer(many=True)
	endereco = EnderecoSerializer()
	class Meta:
		model = PontoTuristico
		fields = ('id', 'nome', 'descricao','endereco','aprovado','foto','atracoes')