from django import forms
from django.utils import timezone
from .models import WaitlistEntry

class WaitlistEntryCreateForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        today = timezone.now()
        qs = WaitlistEntry.objects.filter(
            email__iexact=email,
            timestamp__day=today
        )
        if qs.count() > 5:
            raise forms.ValidationError("Cannot enter this email again today. Try again tomorrow.")
        if email.endswith('@gmail.com'):
            raise forms.ValidationError('Cannot use gmail')
        # if WaitlistEntry.objects.filter(email=email).exists():
        #     raise forms.ValidationError("This email is already on the waitlist")
        return email
        
