from django.test import TestCase

# Create your tests here.

import pytest

from analyses.models import Analyses

@pytest.mark.django_db
def test_analyses_model():

    ## Given
    # Creamos un nuevo libro en la base de datos
    analysis = Analyses(
        description="RM de cerebro",
        modality="MRI-T1w",
        custome="Qubiotech",
        author="Isaac Asimov",
    )
    libro.save()

    ## When

    ## Then
    assert libro.title == "La fundación"
    assert libro.genre == "Ciencia ficción"
    assert libro.year == "1951"
    assert libro.author == "Isaac Asimov"
    assert libro.created_at
    assert libro.updated_at
    assert str(libro) == libro.title