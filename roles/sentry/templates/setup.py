# -*- coding: utf-8 -*-
#
#!{{ venv }}/bin/python
#
# Automatically creates a default superuser, team and project.

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config')

from sentry.models import User, Team, Organization, Project

admin, created = User.objects.get_or_create(
    username="{{ superuser_sentry.username }}",
    defaults={
        "is_superuser": True,
        "is_staff": True,
        "email": "{{ superuser_sentry.email }}"
    })

if created:
    admin.set_password("{{ superuser_sentry.password }}")
    admin.save()

organization, created = Organization.objects.get_or_create(
    name="{{ superuser_sentry.organization }}",
    defaults={"owner": admin})

team, created = Team.objects.get_or_create(
    name="{{ superuser_sentry.team }}",
    defaults={
        "owner": admin,
        "organization": organization
    })

Project.objects.get_or_create(
    name="{{ superuser_sentry.project }}",
    defaults={
        "team": team,
        "organization": organization,
        "platform": "{{ superuser_sentry.platform }}"
    })
