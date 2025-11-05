# lodge_app/forms.py (For forms in views)
from django import forms
from .models import Guest, Payment, Lodge,Room

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'phone', 'id_number', 'check_in', 'check_out', 'room']
        labels = {
            'name': ('Full Name'),
            'phone': ('Phone Number'),
            'id_number': ('ID/Passport Number'),
            'check_in': ('Check-in Date'),
            'check_out': ('Check-out Date'),
            'room': ('Select Room'),
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg rounded-pill px-4',
                'placeholder': ('Enter your full name'),
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control form-control-lg rounded-pill px-4',
                'placeholder': ('e.g., +255 757 179 698'),
                'required': True,
            }),
            'id_number': forms.TextInput(attrs={
                'class': 'form-control form-control-lg rounded-pill px-4',
                'placeholder': ('Enter your ID or Passport number'),
                'required': True,
            }),
            'check_in': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control form-control-lg rounded-pill px-4',
                'required': True,
            }),
            'check_out': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control form-control-lg rounded-pill px-4',
                'required': True,
            }),
            'room': forms.Select(attrs={
                'class': 'form-control form-control-lg rounded-pill px-4',
                'required': True,
            }),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'method']



class LodgeForm(forms.ModelForm):
    class Meta:
        model = Lodge
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['logo'].widget.attrs.update({
            'role': 'uploadcare-uploader',
            'data-public-key': '7d9194fea899e270b144',
        })



class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

   
    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'role': 'uploadcare-uploader',
            'data-public-key': '7d9194fea899e270b144',
        })



from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number (optional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter message subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message here...',
                'rows': 5
            }),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.replace(' ', '').replace('-', '').replace('+', '').isdigit():
            raise forms.ValidationError("Please enter a valid phone number")
        return phone