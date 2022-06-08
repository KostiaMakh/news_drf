from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (Author,
                     Post,
                     Category,
                     Tag,
                     Organization)


class AuthorBiographyAdminForm(forms.ModelForm):
    biography = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Author
        fields = '__all__'


class PostContentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorBiographyAdminForm
    save_on_top = True
    fields = (
        'name',
        'surname',
        'birthday',
        'biography',
        'job',
        'organization',
        'photo'
    )

    class Meta:
        model = Author
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostContentAdminForm
    save_on_top = True
    fields = (
        'title',
        'content',
        'category',
        'tags',
        'authors',
        'is_published',
        'photo'
    )

    class Meta:
        model = Post
        fields = '__all__'


class TagAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = (
        'title',
    )

    class Meta:
        model = Tag
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = (
        'title',
        'description',
    )

    class Meta:
        model = Category
        fields = '__all__'


class OrganizationAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = (
        'title',
        'description',
        'logo',
    )

    class Meta:
        model = Category
        fields = '__all__'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Organization, OrganizationAdmin)
