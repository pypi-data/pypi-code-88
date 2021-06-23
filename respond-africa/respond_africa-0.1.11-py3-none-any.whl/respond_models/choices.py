from edc_constants.constants import FASTING, NEVER, NON_FASTING, OTHER

from .constants import MORE_THAN_HALF, NEARLY_EVERYDAY, NOT_AT_ALL, SEVERAL_DAYS

CONTACT = (
    ("tel", "Telephone conversation"),
    ("home", "Home visIt"),
    ("relative_at_clinic", "Relative visited the health facility"),
    ("patient_record", "Patient record / document"),
    (OTHER, "Other"),
)

DEATH_LOCATIONS = (
    ("home", "At home"),
    ("hospital_clinic", "Hospital/clinic"),
    (OTHER, "Elsewhere, please specify"),
)

FASTING_CHOICES = ((FASTING, "Fasting"), (NON_FASTING, "Non-fasting"))


INFORMANT = (
    ("spouse", "Spouse"),
    ("Parent", "Parent"),
    ("child", "Child"),
    ("healthcare_worker", "Healthcare Worker"),
    (OTHER, "Other"),
)


MISSED_PILLS = (
    ("today", "today"),
    ("yesterday", "yesterday"),
    ("earlier_this_week", "earlier this week"),
    ("last_week", "last week"),
    ("lt_month_ago", "less than a month ago"),
    ("gt_month_ago", "more than a month ago"),
    (NEVER, "have never missed taking my study pills"),
)

PHQ_CHOICES = (
    (NOT_AT_ALL, "Not at all"),
    (SEVERAL_DAYS, "Several days"),
    (MORE_THAN_HALF, "More than half the days"),
    (NEARLY_EVERYDAY, "Nearly everyday"),
)
