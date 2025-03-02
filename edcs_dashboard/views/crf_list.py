from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edcs_crf.crfs import enrollment_crf
from edcs_dashboard.views.subject_list import CrfListBoardView


class CrfListView(CrfListBoardView):
    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/crf_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            crfs=enrollment_crf,
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
