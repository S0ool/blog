from django import forms

from app.models import Post, Category, Comment


class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
