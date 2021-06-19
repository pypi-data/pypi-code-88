#!/usr/bin/env python
import os
import sys

{% if python_path %}
sys.path.insert(0, '{{python_path}}')
{% endif %}
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{django_settings_module}}")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
