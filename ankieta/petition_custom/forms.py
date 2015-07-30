from petition.forms import BaseSignatureForm
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText


class SignatureForm(BaseSignatureForm):
    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
                'first_name',
                'last_name',
                PrependedText('email', '@'),
                PrependedText('city', '<i class="fa fa-globe"></i>'),
                PrependedText('telephone', '<i class="fa fa-phone"></i>'),
                'giodo',
                'newsletter',
        )
