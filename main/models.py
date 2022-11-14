from django.db import models

# Create your models here.
from django.utils.text import slugify


class Author(models.Model):
    author = models.CharField(max_length=200)
    author_id = models.CharField(max_length=200, null=True, blank=True)
    author_image = models.ImageField(null=True, blank=True, upload_to='images', default='p.jpg')

    def __str__(self):
        return f'{self.author} with Id--> {self.author_id}'

    def save(self, *args, **kwargs):
        if self.author_id is None:
            author_id = slugify(self.author)
            has_id = Author.objects.filter(author_id=author_id).exists()
            count = 1
            while has_id:
                count += 1
                author_id = slugify(self.author) + "-" + str(count)
                has_id = Author.objects.filter(author_id=author_id).exist()

        super().save(*args, **kwargs)


class RandomModel(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=2)
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'Data -- {self.name} '
