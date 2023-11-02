import logging
from django.views import View
from lms.djangoapps.homepage_management.models import ComptiaCourses
from common.djangoapps.edxmako.shortcuts import render_to_response
log = logging.getLogger(__name__)

class ComptiaCoursesView(View):

    def get(self, request):

        try:
            context = {}
            context['courses'] = ComptiaCourses.objects.filter(is_active=True).order_by("course_order_number")
            # import pdb;pdb.set_trace()
            return render_to_response("courseware/courses-comptia.html", context)
        except Exception as e:
            log.error(e)
            return render_to_response("courseware/courses-comptia.html", context)
