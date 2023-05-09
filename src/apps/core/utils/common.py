import re
import string
import random

# from django.utils.text import slugify

def is_telephone_number_invalid(telephone_number):
    if telephone_number == None:
        return True
    elif re.search(r'\b0\d{2,3}\d{8}\b', telephone_number):
        return False
    else:
        return True


# def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
# 
# def unique_slug_generator(instance, new_slug=None):
#     """
#     This is for a Django project and it assumes your instance
#     has a model with a slug field and a title character (char) field.
#     """
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(instance.title, allow_unicode=True)
# 
#     Klass = instance.__class__
#     qs_exists = Klass.objects.filter(slug=slug).exists()
#     if qs_exists:
#         new_slug = "{slug}-{randstr}".format(
#                     slug=slug,
#                     randstr=random_string_generator(size=4)
#                 )
#         return unique_slug_generator(instance, new_slug=new_slug)
#     return slug
