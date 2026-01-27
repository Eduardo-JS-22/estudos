from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuário', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex.: João Silva', 'class': 'form-control'}
    ))
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}
    ))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuário', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex.: João Silva', 'class': 'form-control'}
    ))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Ex.: joaosilva@xpto.com', 'class': 'form-control'}
    ))
    password1 = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Confirmação de Senha', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirme sua senha', 'class': 'form-control'}
    ))