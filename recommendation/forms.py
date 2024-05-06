from django import forms

class UserIDForm(forms.Form):
    user_id = forms.IntegerField(
        label="MovieLens User ID",
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter User ID'})
    )