from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'rate', 'category', 'tags']
        labels = {
            'image': 'Изображение',
            'title': 'Заголовок',
            'content': 'Содержание',
            'rate': 'Оценка',
            'category': 'Категория',
            'tags': 'Теги'
        }
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if rate < 1 or rate > 5:
            raise forms.ValidationError('Неверная оценка')
        return rate


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Комментарий'}

