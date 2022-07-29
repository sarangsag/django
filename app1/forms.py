from django import forms

class add_proforms(forms.Form):
    # pid = forms.CharField(max_length=30)
    pcompany=forms.CharField(max_length=30)
    pname = forms.CharField(max_length=30)
    file=forms.ImageField()
    pram = forms.CharField(max_length=30)
    prom = forms.CharField(max_length=30)
    pcolor = forms.CharField(max_length=30)
    pprice = forms.IntegerField()
    pitems=forms.IntegerField()
