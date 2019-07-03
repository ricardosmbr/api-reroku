from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):

    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('nome', 'descricao','endereco__linha1')
    #campo unico
    lookup_field = 'nome'

    def get_queryset(self):
    	id = self.request.query_params.get('id',None)
    	nome = self.request.query_params.get('nome',None)
    	descricao = self.request.query_params.get('descricao',None)
    	queryset = PontoTuristico.objects.all()

    	if id:
    		queryset = PontoTuristico.objects.filter(pk=id)
    	if nome:
    		queryset = queryset.filter(nome__iexact=nome)
    	if descricao:
    		queryset = queryset.filter(descricao__iexact=descricao)

    	return queryset

    # retorna a llista de um recurso
    def list(self, request, *args, **kargs):
    	return super(PontoTuristicoViewSet, self).list(request, *args, **kargs)

    def create(self, request, *args, **kargs):
    	#return Response({'Ola':request.data['nome']})
    	return super(PontoTuristicoViewSet, self).create(request, *args, **kargs)

    def destroy(self, request, *args, **kargs):
    	return super(PontoTuristicoViewSet, self).destroy(request, *args, **kargs)

    # retorna um recurso
    def retrieve(self, request, *args, **kargs):
    	return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kargs)

    def update(self, request, *args, **kargs):
    	return super(PontoTuristicoViewSet, self).update(request, *args, **kargs)

    def partial_update(self, request, *args, **kargs):
    	return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request,pk=None):
    	return Response({'Ola'})

