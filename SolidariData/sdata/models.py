from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Family(models.Model):
    BRAZILIAN_STATES = [('AC', 'Acre'),('AL', 'Alagoas'),('AP', 'Amapá'),('AM', 'Amazonas'),('BA', 'Bahia'),('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),('ES', 'Espírito Santo'),('GO', 'Goiás'),('MA', 'Maranhão'),('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),('MG', 'Minas Gerais'),('PA', 'Pará'),('PB', 'Paraíba'),('PR', 'Paraná'),('PE', 'Pernambuco'),
        ('PI', 'Piauí'),('RJ', 'Rio de Janeiro'),('RN', 'Rio Grande do Norte'),('RS', 'Rio Grande do Sul'),('RO', 'Rondônia'),
        ('RR', 'Roraima'),('SC', 'Santa Catarina'),('SP', 'São Paulo'),('SE', 'Sergipe'),('TO', 'Tocantins'),
    ]
    family_id = models.AutoField(primary_key=True)
    family_representative_name = models.CharField(max_length=100, db_index=True)
    family_representative_gender = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], blank=True)
    family_representative_birthdate = models.DateField(null=True, blank=True)
    family_representative_id = models.CharField(max_length=14, unique=True)
    family_address_street = models.CharField(max_length=65)
    family_address_number = models.CharField(max_length=10)
    family_address_neighborhood = models.CharField(max_length=65)
    family_address_city = models.CharField(max_length=65)
    family_address_state = models.CharField(max_length=2, choices=BRAZILIAN_STATES, blank=True, default='SP')
    family_address_zipcode = models.CharField(max_length=10, blank=True)
    family_address_complement = models.CharField(max_length=255, blank=True)
    family_phone = models.CharField(max_length=15, blank=True)
    family_note = models.TextField(blank=True)
    family_created = models.DateTimeField(auto_now_add=True)
    family_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.family_representative_name


class Relative(models.Model):
    GRAU_DE_PARENTESCO = [
        ('pai', 'Pai'),
        ('mae', 'Mãe'),
        ('irmao/irmã', 'Irmão/Irmã'),
        ('filho/filha', 'Filho/Filha'),
        ('cônjuge', 'Cônjuge'),
        ('avô/avó', 'Avô/Avó'),
        ('neto/neta', 'Neto/Neta'),
        ('outro', 'Outro')
    ]
    relative_id = models.AutoField(primary_key=True, editable=False)
    relative_name = models.CharField(max_length=100, db_index=True)
    relative_gender = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], blank=True)
    relative_birthdate = models.DateField(null=True, blank=True)
    relative_relationship = models.CharField(max_length=50, blank=True, choices=GRAU_DE_PARENTESCO)
    relative_family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="relatives")
    relative_phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.relative_name


class Institution(models.Model):
    institution_id = models.AutoField(primary_key=True)
    institution_name = models.CharField(max_length=100, db_index=True)
    institution_type = models.CharField(max_length=11, choices=[('comunitária', 'Comunitária'), ('privada', 'Privada'), ('pública', 'Pública'), ('religiosa', 'Religiosa'), ('outra', 'Outra')], blank=True)
    institution_cnpj = models.CharField(max_length=18, unique=True, blank=True)
    institution_address_street = models.CharField(max_length=65)
    institution_address_number = models.CharField(max_length=10)
    institution_address_neighborhood = models.CharField(max_length=65)
    institution_address_city = models.CharField(max_length=65)
    institution_address_state = models.CharField(max_length=2, choices=Family.BRAZILIAN_STATES, blank=True, default='SP')
    institution_address_zipcode = models.CharField(max_length=10, blank=True)
    institution_address_complement = models.CharField(max_length=255, blank=True)
    institution_phone = models.CharField(max_length=15, blank=True)
    institution_email = models.EmailField(blank=True)
    institution_website = models.URLField(blank=True)
    institution_social_media = models.CharField(max_length=255, blank=True)
    institution_description = models.TextField(blank=True)
    institution_note = models.TextField(blank=True)
    institution_created = models.DateTimeField(auto_now_add=True)
    institution_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.institution_name

class InstitutionRepresentative(models.Model):
    institution_representative_id = models.AutoField(primary_key=True)
    institution_representative_name = models.CharField(max_length=100, db_index=True)
    institution_representative_gender = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], blank=True)
    institution_representative_birthdate = models.DateField(null=True, blank=True)
    institution_representative_id_number = models.CharField(max_length=14, unique=True)
    institution_representative_address_street = models.CharField(max_length=65)
    institution_representative_address_number = models.CharField(max_length=10)
    institution_representative_address_neighborhood = models.CharField(max_length=65)
    institution_representative_address_city = models.CharField(max_length=65)
    institution_representative_address_state = models.CharField(max_length=2, choices=Family.BRAZILIAN_STATES, blank=True, default='SP')
    institution_representative_address_zipcode = models.CharField(max_length=10, blank=True)
    institution_representative_address_complement = models.CharField(max_length=255, blank=True)
    institution_representative_phone = models.CharField(max_length=15, blank=True)
    institution_representative_email = models.EmailField(blank=True)
    institution_representative_note = models.TextField(blank=True)
    institution_representative_institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="representatives")
    institution_representative_created = models.DateTimeField(auto_now_add=True)
    institution_representative_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.institution_representative_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100, db_index=True)
    event_date = models.DateField()
    event_location_street = models.CharField(max_length=65)
    event_location_number = models.CharField(max_length=10)
    event_location_neighborhood = models.CharField(max_length=65)
    event_location_city = models.CharField(max_length=65)
    event_location_state = models.CharField(max_length=2, choices=Family.BRAZILIAN_STATES, blank=True, default='SP')
    event_location_zipcode = models.CharField(max_length=10, blank=True)
    event_location_complement = models.CharField(max_length=255, blank=True)
    event_institution = models.ForeignKey(
        Institution, 
        on_delete=models.SET_NULL,  # Use SET_NULL to allow the field to be null if the institution is deleted
        blank=True, 
        null=True,  # Add null=True to allow null values
        related_name="events"
    )
    event_website = models.URLField(blank=True)
    event_social_media = models.CharField(max_length=255, blank=True)
    event_contact_person = models.CharField(max_length=100, blank=True)
    event_contact_phone = models.CharField(max_length=15, blank=True)
    event_contact_email = models.EmailField(blank=True)
    event_description = models.TextField(blank=True)
    event_note = models.TextField(blank=True)
    event_created = models.DateTimeField(auto_now_add=True)
    event_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name

class InstitutionEvent(models.Model):
    institution_event_id = models.AutoField(primary_key=True)
    institution_event_institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="institution_events", db_index=True)
    institution_event_event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="institution_events", db_index=True)
    institution_event_registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.institution_event_institution} - {self.institution_event_event}"

class FamilyEvent(models.Model):
    family_event_id = models.AutoField(primary_key=True)
    family_event_family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="family_events", db_index=True)
    family_event_event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="family_events", db_index=True)
    family_event_registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.family_event_family} - {self.family_event_event}"

class FamilyEventInstitution(models.Model):
    family_event = models.OneToOneField(FamilyEvent, on_delete=models.CASCADE, related_name="institution_assignment", db_index=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="assigned_family_events", db_index=True)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.family_event:
            raise ValidationError("A FamilyEvent must be associated with this assignment.")
        if not self.institution:
            raise ValidationError("An Institution must be assigned to this FamilyEvent.")

    def __str__(self):
        return f"{self.family_event} - {self.institution}"
