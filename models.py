"""
Models for homepage_content
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

image_extension_validator = FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg', 'gif'])

class Reviews(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    rating_text = models.TextField()
    user_name = models.CharField(max_length=300, blank=False)
    user_image = models.FileField(upload_to='Index-Reviews', validators=[image_extension_validator])
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'homepage_management'
        verbose_name = _('Reviews')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return str(self.user_name)

class HomepageCourses(models.Model):
    """
    Model to store courses visible in index page.
    """
    homepage_course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    course_order_number = models.IntegerField()

    class Meta:
        app_label = 'homepage_management'
        verbose_name = _('Homepage Course')
        verbose_name_plural = _('Homepage Courses')

    def __str__(self):
        return str(self.homepage_course.display_name) +" "+ str(self.homepage_course)


class ComptiaCourses(models.Model):
    """
    Model to store comptia courses visible in comptia page.
    """
    comptia_course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    course_order_number = models.IntegerField()

    class Meta:
        app_label = 'homepage_management'
        verbose_name = _('Comptia Course')
        verbose_name_plural = _('Comptia Courses')

    def __str__(self):
        return str(self.comptia_course.display_name) +" "+ str(self.comptia_course)