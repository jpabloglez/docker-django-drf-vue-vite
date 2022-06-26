from faker import Faker
fake = Faker()

# python manage.py shell
from analyses.models import Analyses
a = Analyses(description="RM sin contraste", modality="MRT T1w", customer="Qubiotech", status="Finished")
a.save()
Analyses.objects.all()

# >>> from analyses.models import Analyses
# >>> Analyses.objects.all()