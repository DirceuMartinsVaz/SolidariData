from django import forms
from django.forms import inlineformset_factory
from .models import Family, Relative, Event, Institution, InstitutionEvent, FamilyEvent, FamilyEventInstitution, InstitutionRepresentative

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = '__all__'  # Include all fields, or specify specific ones
        labels = {
            'family_representative_name': 'Nome do representante da família',
            'fanily_representative_gender': 'Gênero do representante da família',
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
            'family_note': forms.Textarea(attrs={'rows': 3}),
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
        fields = ['relative_name', 'relative_gender', 'relative_birthdate', 'relative_relationship', 'relative_phone']
        widgets = {
            'relative_birthdate': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}),
            'relative_relationship': forms.Select(attrs={'class': 'form-select'}),
            'relative_phone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
        }
        labels = {'relative_name': 'Nome do familiar', 'relative_gender': 'Gênero', 'relative_birthdate': 'Data de nascimento do familiar', 'relative_relationship': 'Grau de parentesco', 'relative_phone': 'Telefone'}
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
)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'event_name': 'Nome do Evento',
            'event_date': 'Data do Evento',
            'event_location_street': 'Rua',
            'event_location_number': 'Número',
            'event_location_neighborhood': 'Bairro',
            'event_location_city': 'Cidade',
            'event_location_state': 'Estado',
            'event_location_zipcode': 'CEP',
            'event_location_complement': 'Complemento',
            'event_institution': 'Instituição',
            'event_website': 'Website',
            'event_social_media': 'Mídias Sociais',
            'event_contact_person': 'Pessoa de Contato',
            'event_contact_phone': 'Telefone de Contato',
            'event_contact_email': 'Email de Contato',
            'event_description': 'Descrição',
            'event_note': 'Notas',
        }
        widgets = {
            'event_date': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}),
            'event_contact_phone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
            'event_location_zipcode': forms.TextInput(attrs={'placeholder': 'XXXXX-XXX'}),
        }

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'
        labels = {
            'institution_name': 'Nome da Instituição',
            'institution_type': 'Tipo',
            'institution_cnpj': 'CNPJ',
            'institution_address_street': 'Rua',
            'institution_address_number': 'Número',
            'institution_address_neighborhood': 'Bairro',
            'institution_address_city': 'Cidade',
            'institution_address_state': 'Estado',
            'institution_address_zipcode': 'CEP',
            'institution_address_complement': 'Complemento',
            'institution_phone': 'Telefone',
            'institution_email': 'Email',
            'institution_website': 'Website',
            'institution_social_media': 'Mídias Sociais',
            'institution_description': 'Descrição',
            'institution_note': 'Notas',
        }
        widgets = {
            'institution_cnpj': forms.TextInput(attrs={'placeholder': 'XX.XXX.XXX/XXXX-XX'}),
            'institution_phone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
            'institution_address_zipcode': forms.TextInput(attrs={'placeholder': 'XXXXX-XXX'}),
        }

class InstitutionEventForm(forms.ModelForm):
    class Meta:
        model = InstitutionEvent
        fields = '__all__'
        labels = {
            'institution_event_institution': 'Instituição',
            'institution_event_event': 'Evento',
            'institution_event_registration_date': 'Data de Registro',
        }
        widgets = {
            'institution_event_registration_date': forms.DateInput(attrs={'readonly': 'readonly'}),
        }

class FamilyEventForm(forms.ModelForm):
    class Meta:
        model = FamilyEvent
        fields = '__all__'
        labels = {
            'family_event_family': 'Família',
            'family_event_event': 'Evento',
            'family_event_registration_date': 'Data de Registro',
        }
        widgets = {
            'family_event_registration_date': forms.DateInput(attrs={'readonly': 'readonly'}),
        }

class FamilyEventInstitutionForm(forms.ModelForm):
    class Meta:
        model = FamilyEventInstitution
        fields = '__all__'
        labels = {
            'family_event': 'Família no Evento',
            'institution': 'Instituição',
            'assigned_date': 'Data de Atribuição',
        }
        widgets = {
            'assigned_date': forms.DateInput(attrs={'readonly': 'readonly'}),
        }

class InstitutionRepresentativeForm(forms.ModelForm):
    class Meta:
        model = InstitutionRepresentative
        fields = [
            'institution_representative_name',
            'institution_representative_gender',
            'institution_representative_birthdate',
            'institution_representative_id_number',
            'institution_representative_phone',
            'institution_representative_email',
            'institution_representative_note',
        ]
        widgets = {
            'institution_representative_birthdate': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}),
            'institution_representative_phone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
            'institution_representative_email': forms.EmailInput(attrs={'placeholder': 'email@exemplo.com'}),
        }
        labels = {
            'institution_representative_name': 'Nome do Representante',
            'institution_representative_gender': 'Gênero',
            'institution_representative_birthdate': 'Data de Nascimento',
            'institution_representative_id_number': 'Número de Identificação',
            'institution_representative_phone': 'Telefone',
            'institution_representative_email': 'Email',
            'institution_representative_note': 'Notas',
        }

# Define the inline formset for InstitutionRepresentative
InstitutionRepresentativeFormSet = inlineformset_factory(
    Institution,
    InstitutionRepresentative,
    fields=[
        'institution_representative_name',
        'institution_representative_gender',
        'institution_representative_birthdate',
        'institution_representative_id_number',
        'institution_representative_phone',
        'institution_representative_email',
        'institution_representative_note',
    ],
    extra=1,  # Number of empty forms displayed
    can_delete=True,  # Allow users to delete representatives
    widgets={
        'institution_representative_birthdate': forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}),
        'institution_representative_phone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
        'institution_representative_email': forms.EmailInput(attrs={'placeholder': 'email@exemplo.com'}),
    },
    labels={
        'institution_representative_name': 'Nome do Representante',
        'institution_representative_gender': 'Gênero',
        'institution_representative_birthdate': 'Data de Nascimento',
        'institution_representative_id_number': 'Número de Identificação',
        'institution_representative_phone': 'Telefone',
        'institution_representative_email': 'Email',
        'institution_representative_note': 'Notas',
    }
)