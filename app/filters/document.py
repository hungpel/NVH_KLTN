import django_filters

from app.models import Subject


class DocumentFilter(django_filters.FilterSet):
    subjects = django_filters.MultipleChoiceFilter(
        field_name="subjects",
        queryset=Subject.objects.all(),
    )
