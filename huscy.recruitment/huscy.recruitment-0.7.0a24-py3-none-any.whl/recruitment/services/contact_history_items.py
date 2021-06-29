from huscy.recruitment.models import ContactHistoryItem
from huscy.recruitment.services.participation_requests import get_participation_requests


def get_contact_history_items(participation_request):
    return (ContactHistoryItem.objects.filter(participation_request=participation_request)
                                      .order_by('created_at'))


def get_contact_history_items_by_subject(subject, project=None):
    participation_requests = get_participation_requests(subject=subject)

    if project:
        participation_requests = participation_requests.filter(project=project)

    return (ContactHistoryItem.objects.filter(participation_request__in=participation_requests)
                                      .order_by('created_at'))


def create_contact_history_item(participation_request, status=0):
    return ContactHistoryItem.objects.create(participation_request=participation_request,
                                             status=status)
