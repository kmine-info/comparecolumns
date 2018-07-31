
from django import forms

class VlookupForm(forms.Form):
    
    lookup_field1 = forms.CharField(widget=forms.Textarea(attrs={'rows': 25, 'cols': 120}))
    lookup_field2 = forms.CharField(widget=forms.Textarea(attrs={'rows': 25, 'cols': 120}))
    
    class Meta:
        fields=['lookup_field1','lookup_field2']
        
        
