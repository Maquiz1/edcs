from edcs_dashboard.views.dashboard_list import ListboardView
from edcs_screening.models import SubjectScreening


class ScreeningListBoardView(ListboardView):
    listboard_url = "screening_listboard_url"
    listboard_model = "edcs_screening.subjectscreening"
    model_consent = "edcs_consent.subjectconsent"
    ordering = "-report_datetime"
    listboard_dashboard = "edcs_dashboard:screening_dashboard"

    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            subject_screening_add_url=self.next_add_screening,
            object_list=self.object_list_screening(SubjectScreening),
        )
        return context

    def get_subject_screening_add_url(self):
        return self.listboard_model_cls().get_absolute_url()

    def get_subject_consent_add_url(self):
        return self.listboard_model_consent().get_absolute_url()

    @property
    def screening_data(self):
        return SubjectScreening.objects.all().order_by(self.ordering).values()

    @property
    def next_add_screening(self):
        nxt = '?next='.join([self.get_subject_screening_add_url(), self.listboard_dashboard])
        return nxt
