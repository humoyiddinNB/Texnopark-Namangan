
from django import forms
from .models import Phone, Laptop, Watch


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 2:
            raise forms.ValidationError('Ism 2 ta harfdan katta bolishi kerak')
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Narx manfiy bolishi mumkin emas")
        return price

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 5:
            raise forms.ValidationError("Komyuter nomi bunaqa kichik bolishi mumkinemas")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Naarxi 0 yoki misu bolishi mukin emas')
        return price

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 5:
            raise forms.ValidationError("Smartsoat nomi 5 ta harfdan uzun bolishi kerak")
        return name

    def cleac_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("narx noldan kichik yoki teng bolishi mumkin emas")
        return price