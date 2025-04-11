import os
import django
import random

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SolidariData.settings")
django.setup()

# Import models
import random
from sdata.models import Family, Relative

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

##### names = ["João", "Maria", "Carlos", "Ana", "Lucas", "Beatriz", "Pedro", "Fernanda", "Bruno", "Paula"]
genders = ["masculino", "feminino", "outro"]
states = ['SP', 'RJ', 'MG', 'RS', 'BA', 'PE', 'PR', 'SC']
relationships = ['pai', 'mae', 'irmao/irmã', 'filho/filha', 'cônjuge', 'avô/avó', 'neto/neta', 'outro']

def random_date(start_year=1950, end_year=2020):
    """Generates a random date within a given range."""
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Simplified to avoid invalid dates
    return f"{year}-{month:02d}-{day:02d}"

def seed_data(num_families=100):
    for i in range(num_families):
        # Create family
        family = Family(
            family_representative_name = f"{random.choice(names)} {random.choice(surnames)}",
            #####family_representative_name=f"{random.choice(names)} {random.choice(names)}",
            family_representative_gender=random.choice(genders),
            family_representative_birthdate=random_date(1950, 1990),
            family_representative_id=f"{random.randint(10000000000, 99999999999)}",
            family_address_street=f"Rua {random.choice(names)}",
            family_address_number=str(random.randint(1, 500)),
            family_address_neighborhood="Bairro Aleatório",
            family_address_city=random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador"]),
            family_address_state=random.choice(states),
            family_address_zipcode=f"{random.randint(10000, 99999)}-{random.randint(100, 999)}",
            family_address_complement="Casa",
            family_phone=f"{random.randint(10, 99)}{random.randint(900000000, 999999999)}",
            family_note="Família adicionada automaticamente para testes e exemplos."
        )
        family.save()

        # Create relatives (1 to 5 relatives per family)
        num_relatives = random.randint(1, 5)
        for relative in range(num_relatives):
            relative = Relative(
                relative_name = f"{random.choice(names)} {random.choice(surnames)}",
                ####relative_name=f"{random.choice(names)} {random.choice(names)}",
                relative_gender=random.choice(genders),
                relative_birthdate=random_date(1980, 2015),
                relative_relationship=random.choice(relationships),
                relative_phone=f"{random.randint(10, 99)}{random.randint(900000000, 999999999)}",
                relative_family=family
            )
            relative.save()

    print(f"{num_families} families and their relatives have been seeded successfully!")

# Call the function to seed data
seed_data()
