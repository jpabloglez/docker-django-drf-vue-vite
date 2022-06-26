# To avoid error: django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet
import django
django.setup()

from django.test import TestCase

# Create your tests here.

import pytest

from analyses.models import Analyses

@pytest.mark.django_db
def test_analyses_model():

    analysis = Analyses(
        description="RM de cerebro",
        modality="MRI-T1w",
        status="Finished",
        customer="Qubiotech",
    )
    analysis.save()

    assert analysis.description == analysis.description
    assert analysis.modality == analysis.modality
    assert analysis.status == analysis.status
    assert analysis.customer == analysis.customer