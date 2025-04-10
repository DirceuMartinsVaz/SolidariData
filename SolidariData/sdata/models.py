from django.db import models

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
    relative_name = models.CharField(max_length=100)
    relative_gender = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], blank=True)
    relative_birthdate = models.DateField(null=True, blank=True)
    relative_relationship = models.CharField(max_length=50, blank=True, choices=GRAU_DE_PARENTESCO)
    relative_family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="relatives")

    def __str__(self):
        return self.relative_name
