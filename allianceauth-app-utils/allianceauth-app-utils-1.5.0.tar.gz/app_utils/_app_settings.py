from .django import clean_setting

APPUTILS_ADMIN_NOTIFY_TIMEOUT = clean_setting("APPUTILS_ADMIN_NOTIFY_TIMEOUT", 86400)
"""Timeout for throttled admin notifications in seconds."""

APPUTILS_ESI_ERROR_LIMIT_THRESHOLD = clean_setting(
    "APPUTILS_ESI_ERROR_LIMIT_THRESHOLD", 25
)
"""ESI error limit remain threshold.

The number of remaining errors is counted down from 100 as errors occur.
Because multiple tasks may request the value simultaneously and get the same response,
the threshold must be above 0 to prevent the API from shutting down with a 420 error.
"""
