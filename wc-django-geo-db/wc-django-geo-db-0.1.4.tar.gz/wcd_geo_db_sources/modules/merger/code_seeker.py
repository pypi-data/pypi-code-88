from django.utils.module_loading import import_string


__all__ = 'get_code_seeker_registry',


def get_code_seeker_registry():
    from wcd_geo_db_sources.conf import settings

    if settings.SOURCE_MERGE_CODE_SEEKER_REGISTRY:
        return import_string(settings.SOURCE_MERGE_CODE_SEEKER_REGISTRY)

    return None
