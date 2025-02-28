from django import template

from .. import models

register = template.Library()


@register.simple_tag
def get_service_categories():
    return models.ServiceCategory.objects.all()


@register.simple_tag
def get_social_accounts():
    return models.SocialAccount.objects.all()


@register.simple_tag
def get_contact_info():
    return models.ContactInfo.load()


@register.simple_tag
def get_doctor_info():
    return models.DoctorInfo.load()


@register.simple_tag
def get_faq():
    return models.FAQ.objects.all()


@register.simple_tag
def get_gallery_categories():
    return models.GalleryCategory.objects.all()


@register.simple_tag
def get_video_reviews():
    return models.VideoReview.objects.all()
