from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..models import LungCancerLabInvestigation


@admin.register(LungCancerLabInvestigation, site=edcs_subject_admin)
class LungCancerLabInvestigationAdmin(SimpleHistoryAdmin):
    fieldsets = (
        [
            None,
            {
                "fields": (
                    "report_datetime",
                ),
            },
         ],
        [
            "MUTATION ANALYSIS",
            {
                "fields": (
                    "biopsy_tissues_mutation",
                    "mutation_detected",
                ),
            },
        ],
        [
            "DNA METYLATION AGE ANALYSIS",
            {
                "fields": (
                    "dna_methylation_age",
                    "dna_methylation_result",
                ),
            },
        ],
        [
            "RADIOLOGY INVESTIGATIONS",
            {
                "fields": (
                    "brock_score",
                    "lungrads_score",
                    "luniris_score",
                ),
            },
        ],

        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "biopsy_tissues_mutation",
        "dna_methylation_age",
        "brock_score",
        "lungrads_score",
        "luniris_score",
    )

    list_filter = (
        "report_datetime",
        "biopsy_tissues_mutation",
        "dna_methylation_age",
        "brock_score",
        "lungrads_score",
        "luniris_score",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "biopsy_tissues_mutation": admin.VERTICAL,
        "dna_methylation_age": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}
