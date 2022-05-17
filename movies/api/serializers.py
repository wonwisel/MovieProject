from rest_framework import serializers
from rest_framework import generics
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'tagline',
            'description',
            'image',
            'year',
            'url',
            'category',
        )


class MovieFilter(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):

        queryset = Movie.objects.all()
        username = self.request.query_params.get('')
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset
