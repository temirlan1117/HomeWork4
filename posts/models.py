from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to = 'posts/', null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=100)
    rate =models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE, related_name='posts',
                                 null=True, blank=True)
    tags = models.ManyToManyField('Tag'
                                  , related_name='posts', blank=True, )

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


