from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'username'}
        )
    )
    senha = forms.CharField(
        label= 'Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password'
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'username'}
        )
    )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget= forms.EmailInput(
            attrs={'class':'form-control',
                   'placeholder':'email@email.com'}
        )
    )

    senha = forms.CharField(
        label= 'Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite uma senha'
            }
        )
    )

    senha_confirma = forms.CharField(
        label= 'Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite a senha novamente'
            }
        )
    )