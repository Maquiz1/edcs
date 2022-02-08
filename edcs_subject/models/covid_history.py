from django.db import models

from edcs_constants.choices import YES_NO
from edcs_lists.models import CovidSymptoms
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin
from ..choices import COVID_SYMPTOMS, COVID_VACCINE, QN82, QN87, QN88


class CovidInfectionHistory(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    think_had_covid = models.CharField(
        verbose_name="Do you know or think that you have had COVID-19?",
        max_length=15,
        choices=YES_NO,
        help_text="(if not sure, select No)",
    )

    date_think_had_covid = models.DateField(
        verbose_name="If yes, On what date did you first know or think you had COVID-19?",
        max_length=45,
    )

    have_covid_symptoms = models.CharField(
        verbose_name="Did you have any symptoms when you first knew or thought you had COVID-19?",
        max_length=45,
        choices=YES_NO,
    )

    covid_symptoms = models.ManyToManyField(
        CovidSymptoms,
        verbose_name="If yes, what symptoms did you have when you first had COVID-19?",
        related_name="covid_symptoms",
    )

    admitted_hospital = models.CharField(
        verbose_name="Were you admitted to hospital when you thought you had COVID-19? ",
        max_length=45,
        choices=YES_NO,
    )
    swab_test = models.CharField(
        verbose_name="Have you ever had a swab test of your nose and throat to test for COVID-19 infection? ",
        max_length=45,
        choices=YES_NO,
    )
    swab_test_results = models.CharField(
        verbose_name="If yes, What was the result/were the results of all swab tests you’ve had?",
        max_length=45,
        choices=QN82,
    )

    date_first_positive_test = models.DateField(
        verbose_name="If any positive test: What was the date of first positive test you’ve had?",
        max_length=45,
    )

    date_last_negative_test = models.DateField(
        verbose_name="If all tests negative: What was the date of last negative test you’ve had?",
        max_length=45,
    )

    covid_vaccinated = models.CharField(
        verbose_name="Have you ever been vaccinated against COVID-19?",
        max_length=15,
        choices=YES_NO,
    )
    covid_vaccine = models.CharField(
        verbose_name="If yes, what type of vaccination",
        max_length=45,
        choices=COVID_VACCINE,
    )

    vaccine_provider = models.CharField(
        verbose_name="If Yes who provided the vaccine",
        max_length=45,
        choices=QN87,
    )

    other_vaccine_provider = edcs_models.OtherCharField()

    no_covid_vaccine = models.CharField(
        verbose_name="How many doses have you received to date?",
        max_length=45,
        choices=QN88,
    )

    date_recent_vaccination = models.DateField(
        verbose_name="Date of most recent vaccination?",
        max_length=45,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Covid Infection History"
        verbose_name_plural = "Covid Infection History"
