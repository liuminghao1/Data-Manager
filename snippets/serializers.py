# -*- coding:utf-8  -*-
from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django import forms

#class SnippetSerializer(serializers.Serializer):
#    pk = serializers.Field()
#    title =serializers.CharField(required=False, max_length=100)
#    code = serializers.CharField(max_length=100000)
#    code = serializers.CharField(widget=forms.Select(attrs={'class':'selector'}))
#    linenos = serializers.BooleanField(required=False)
#    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#    style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def restore_object(self,attrs,instance=None):
        if instance:
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance
        return Sinpper(**attrs)
