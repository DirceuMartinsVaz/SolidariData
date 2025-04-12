import os
import django
import random

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SolidariData.settings")
django.setup()

# Import models
from sdata.models import Family, Relative, Event, Institution, InstitutionEvent, FamilyEvent, FamilyEventInstitution

# Sample data
names = [
    "João", "Maria", "Carlos", "Ana", "Lucas", "Beatriz", "Pedro", "Fernanda", "Bruno", "Paula",
    "Gabriel", "Isabela", "Rafael", "Juliana", "Rodrigo", "Camila", "Daniel", "Larissa", "Eduardo", "Carolina",
    "Thiago", "Michele", "Felipe", "Vanessa", "Gustavo", "Amanda", "Diego", "Marcela", "Fernando", "Natália"
]

surnames = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Almeida", "Ferreira", "Costa", "Gomes",
    "Martins", "Rocha", "Barros", "Mendes", "Ribeiro", "Correia", "Farias", "Monteiro", "Cardoso", "Vieira",
    "Teixeira", "Carvalho", "Araújo", "Moura", "Castro", "Moreira", "Nunes", "Pinheiro", "Cavalcanti", "Freitas"
]

genders = ["masculino", "feminino", "outro"]
states = ['SP', 'RJ', 'MG', 'RS', 'BA', 'PE', 'PR', 'SC']
relationships = ['pai', 'mae', 'irmao/irmã', 'filho/filha', 'cônjuge', 'avô/avó', 'neto/neta', 'outro']
institution_types = ['comunitária', 'privada', 'pública', 'religiosa', 'outra']

def random_date(start_year=1950, end_year=2025):
    """Generates a random date within a given range."""
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Simplified to avoid invalid dates
    return f"{year}-{month:02d}-{day:02d}"

def seed_data(num_families=50, num_institutions=20, num_events=30):
    # Seed Families and Relatives
    for _ in range(num_families):
        family = Family(
            family_representative_name=f"{random.choice(names)} {random.choice(surnames)}",
            family_representative_gender=random.choice(genders),
            family_representative_birthdate=random_date(1950, 1990),
            family_representative_id=f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}",
            family_address_street=f"Rua {random.choice(names)}",
            family_address_number=str(random.randint(1, 1500)),
            family_address_neighborhood="Bairro Aleatório",
            family_address_city=random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador"]),
            family_address_state=random.choice(states),
            family_address_zipcode=f"{random.randint(10000, 99999)}-{random.randint(100, 999)}",
            family_address_complement="Casa",
            family_phone=f"{random.randint(10, 99)}{random.randint(90000, 99999)}-{random.randint(1000, 9999)}",
            family_note="Família adicionada automaticamente para testes e exemplos."
        )
        family.save()

        # Create relatives (1 to 5 relatives per family)
        for _ in range(random.randint(1, 5)):
            relative = Relative(
                relative_name=f"{random.choice(names)} {random.choice(surnames)}",
                relative_gender=random.choice(genders),
                relative_birthdate=random_date(1980, 2015),
                relative_relationship=random.choice(relationships),
                relative_phone=f"{random.randint(10, 99)}{random.randint(90000, 99999)}-{random.randint(1000, 9999)}",
                relative_family=family
            )
            relative.save()

    # Seed Institutions
    for _ in range(num_institutions):
        institution = Institution(
            institution_name=f"Instituição {random.choice(names)}",
            institution_type=random.choice(institution_types),
            institution_cnpj=f"{random.randint(10, 99)}.{random.randint(100, 999)}.{random.randint(100, 999)}/{random.randint(1000, 9999)}-{random.randint(10, 99)}",
            institution_address_street=f"Rua {random.choice(names)}",
            institution_address_number=str(random.randint(1, 1500)),
            institution_address_neighborhood="Bairro Aleatório",
            institution_address_city=random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador"]),
            institution_address_state=random.choice(states),
            institution_address_zipcode=f"{random.randint(10000, 99999)}-{random.randint(100, 999)}",
            institution_address_complement="Prédio",
            institution_phone=f"{random.randint(10, 99)}{random.randint(90000, 99999)}-{random.randint(1000, 9999)}",
            institution_email=f"{random.choice(names).lower()}@instituicao.com",
            institution_description="Instituição adicionada automaticamente para testes e exemplos.",
            institution_note="Nota de exemplo."
        )
        institution.save()

    # Seed Events
    for _ in range(num_events):
        event = Event(
            event_name=f"Evento {random.choice(names)}",
            event_date=random_date(2023, 2025),
            event_location_street=f"Rua {random.choice(names)}",
            event_location_number=str(random.randint(1, 1500)),
            event_location_neighborhood="Bairro Aleatório",
            event_location_city=random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador"]),
            event_location_state=random.choice(states),
            event_location_zipcode=f"{random.randint(10000, 99999)}-{random.randint(100, 999)}",
            event_location_complement="Auditório",
            event_description="Evento gerado automaticamente para testes.",
            event_note="Nota de exemplo."
        )
        event.save()

        # Assign institutions to events (1 to 3 institutions per event)
        for _ in range(random.randint(1, 3)):
            institution_event = InstitutionEvent(
                institution_event_institution=random.choice(Institution.objects.all()),
                institution_event_event=event
            )
            institution_event.save()

        # Assign families to events (1 to 5 families per event)
        for _ in range(random.randint(1, 5)):
            family_event = FamilyEvent(
                family_event_family=random.choice(Family.objects.all()),
                family_event_event=event
            )
            family_event.save()

    # Seed FamilyEventInstitution
    for family_event in FamilyEvent.objects.all():
        family_event_institution = FamilyEventInstitution(
            family_event=family_event,
            institution=random.choice(Institution.objects.all())
        )
        family_event_institution.save()

    print(f"{num_families} families, {num_institutions} institutions, and {num_events} events have been seeded successfully!")

# Call the function to seed data
seed_data()
