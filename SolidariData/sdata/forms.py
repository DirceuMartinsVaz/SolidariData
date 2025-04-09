from django import forms
from django.forms import inlineformset_factory
from .models import Family, Relative

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = '__all__'  # Include all fields, or specify specific ones
        labels = {
            'family_representative_name': 'Nome do representante da família',
            'family_representative_birthdate': 'Data de nascimento do representante da família',
            'family_representative_id': 'Número de identificação do representante da família',
            'family_address_street': 'Rua',
            'family_address_number': 'Número',
            'family_address_neighborhood': 'Bairro',
            'family_address_city': 'Cidade',
            'family_address_state': 'Estado',
            'family_address_zipcode': 'CEP',
            'family_address_complement': 'Complemento',
            'family_phone': 'Telefone',
            'family_note': 'Observações',
            'family_created': 'Data de cadastro',
            'family_updated': 'Data de atualização'
        }
        widgets = {
            'family_representative_birthdate': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}),
            'family_representative_id': forms.TextInput(attrs={'placeholder': 'XXX.XXX.XXX-XX'}),
            'family_address_street': forms.TextInput(attrs={'placeholder': 'Rua, Avenida, etc.'}),
            'family_address_zipcode': forms.TextInput(attrs={'placeholder': 'XXXXX-XXX'}),
            'family_phone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
        }
        error_messages = {
            'family_representative_name': {
                'max_length': "O nome do representante da família é muito longo.",
                'required': "Por favor, insira o nome do representante da família.",
            },
            'family_representative_birthdate': {
                'invalid': "Por favor, insira uma data válida no formato DD/MM/AAAA.",
            },
            'family_address_zipcode': {
                'invalid': "Insira um CEP válido no formato XXXXX-XXX.",
            },
            'family_phone': {
                'required': "O telefone da família é obrigatório.",
                'invalid': "Insira um número de telefone válido no formato (XX) XXXXX-XXXX.",
            },
            'family_representative_id': {
                'unique': "Este número de identificação já está cadastrado.",
            },
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.family_representative_birthdate:
            self.fields['family_representative_birthdate'].initial = self.instance.family_representative_birthdate.strftime('%d-%m-%Y')


class RelativeForm(forms.ModelForm):
    class Meta:
        model = Relative
        fields = ['relative_name', 'relative_birthdate', 'relative_relationship']
        widgets = {
            'relative_birthdate': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}),
            'relative_relationship': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {'relative_name': 'Nome do familiar', 'relative_birthdate': 'Data de nascimento do familiar', 'relative_relationship': 'Grau de parentesco'}
        error_messages = {
            'relative_name': {
                'max_length': "O nome do familiar é muito longo.",
                'required': "Por favor, insira o nome do familiar.",
            },
            'relative_birthdate': {
                'invalid': "Por favor, insira uma data válida no formato DD/MM/AAAA.",
            },
        }

# Define the inline formset for relatives
RelativeFormSet = inlineformset_factory(
    Family,
    Relative,
    form=RelativeForm,
    extra=1,  # Number of empty forms displayed
    can_delete=True,  # Allow users to delete relatives
    fields=['relative_name', 'relative_birthdate', 'relative_relationship'],  # Explicitly include only valid fields
)