import random, string
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def _slug_generator(instance, new_slug=None):
    """
    Unique slug generator for models having 'slug' and 'title' character fields.
    """
    max_length = instance._meta.get_field('slug').max_length
    if new_slug is not None:
        slug = new_slug
    else:
        title = instance.title
        slug = slugify(title.replace(" ", "_"))
    
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f'{slug}_{random_string_generator(size=4)}'
        return _slug_generator(instance, new_slug=new_slug)
    return slug