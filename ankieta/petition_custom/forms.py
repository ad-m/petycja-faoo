from petition.forms import BaseSignatureForm
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from django.utils.translation import ugettext as _
import swapper

Signature = swapper.load_model("petition", "Signature")


class SignatureForm(BaseSignatureForm):
    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('Sign'), css_class="btn-sign btn-lg btn-block"))
        self.helper.layout = Layout(
                'first_name',
                'last_name',
                PrependedText('email', '@'),
                PrependedText('city', '<i class="fa fa-globe"></i>'),
                PrependedText('telephone', '<i class="fa fa-phone"></i>'),
                'giodo',
                'newsletter',
        )

    class Meta:
        model = Signature
