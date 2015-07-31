from petition.forms import SignatureForm
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText
import swapper

Signature = swapper.load_model("petition", "Signature")


class CustomSignatureForm(SignatureForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignatureForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
                'first_name',
                'second_name',
                PrependedText('email', '@'),
                PrependedText('city', '<i class="fa fa-globe"></i>'),
                PrependedText('telephone', '<i class="fa fa-phone"></i>'),
                'giodo',
                'newsletter',
        )

    class Meta:
        model = Signature
        fields = ['first_name', 'second_name', 'email', 'city', 'newsletter', 'telephone']
