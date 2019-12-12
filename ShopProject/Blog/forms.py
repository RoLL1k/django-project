from django import forms
from .models import Tag, Post, Comment
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'tags']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'tags': forms.CheckboxSelectMultiple(),
		}


class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['title']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']

		widgets = {
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}

