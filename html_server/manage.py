#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "html_server.settings")

    from django.core.management import execute_from_command_line

    command = sys.argv
    #command = "runserver 0.0.0.0:8000"

    execute_from_command_line(command)
