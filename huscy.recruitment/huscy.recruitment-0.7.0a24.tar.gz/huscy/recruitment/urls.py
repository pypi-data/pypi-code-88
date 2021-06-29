from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from huscy.recruitment import views


router = DefaultRouter()
router.register('attributefiltersets', views.AttributeFilterSetViewSet)
router.register('experiments', views.ExperimentViewSet)
router.register('contacthistories', views.ContactHistoryViewSet, basename='contacthistory')

attributefilterset_router = NestedDefaultRouter(router, 'attributefiltersets',
                                                lookup='attributefilterset')
attributefilterset_router.register('participationrequests', views.ParticipationRequestViewSet,
                                   basename='participationrequest')

experiment_router = NestedDefaultRouter(router, 'experiments', lookup='experiment')
experiment_router.register('subjectgroups', views.SubjectGroupViewset, basename='subjectgroup')

urlpatterns = router.urls
urlpatterns += attributefilterset_router.urls
urlpatterns += experiment_router.urls
