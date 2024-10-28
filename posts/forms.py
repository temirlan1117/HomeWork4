from .models import Post, Comment, Tag
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

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rate', 'image', 'tags']

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


class SearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={
        'placeholder': "Введите текст для поиска",
        'class': 'form-control'}))

    tag = forms.ModelMultipleChoiceField(required=False,
                                    queryset=Tag.objects.all(),
                                    widget=forms.CheckboxSelectMultiple,)
    orderings = (
        ("title", "По названию"),
        ("-title", "По названию в обратном порядке"),
        ("rate", "По рейтингу"),
        ("-rate", "По рейтингу в обратном порядке"),
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания в обратном порядке")
    )
    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'class': 'form-control'}))