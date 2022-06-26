#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Rest Framework imports.
from rest_framework import serializers

# Local imports.
from analyses.models import Analyses

class AnalysesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analyses
        fields = ['id', 'description', 'modality', 'status', 'customer']

