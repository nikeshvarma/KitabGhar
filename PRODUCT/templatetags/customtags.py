from django import template

register = template.Library()


@register.filter
def cover_image(images):
    return images.get(make_cover_image=True).image.url
