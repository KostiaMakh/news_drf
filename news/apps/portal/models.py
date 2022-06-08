from django.urls import reverse
from django.db import models
from slugify import slugify


class BaseModel(models.Model):
    slug = models.CharField(max_length=250,
                            unique=True,
                            verbose_name='url')
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True


# Main project models
# Post model
class Post(BaseModel):
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              blank=True)
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag',
                                  blank=True)
    authors = models.ManyToManyField('Author')
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Created')
    updated_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Update')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(str(self.title))}'
        super(Post, self).save()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at', ]


# Categories model
class Category(BaseModel):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(self.title)}'
        super(Category, self).save()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title', ]


# Tags model
class Tag(BaseModel):

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(str(self.title))}'
        super(Tag, self).save()

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title', ]


# Authors information
class Author(models.Model):
    slug = models.CharField(max_length=250,
                            unique=True,
                            verbose_name='url')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    birthday = models.DateField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              blank=True)
    job = models.CharField(max_length=250,
                           blank=True)
    organization = models.ForeignKey('Organization',
                                     on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(str(self.surname))}-{slugify(str(self.name))}'
        super(Author, self).save()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['surname', ]


# Organizations model
class Organization(BaseModel):
    logo = models.ImageField(upload_to='photos/%Y/%m/%d',
                             blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('organization', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super(Organization, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(str(self.title))}'
        super(Organization, self).save()

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ['title', ]
