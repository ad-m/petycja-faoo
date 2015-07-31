from petition.forms import BaseSignatureForm, GiodoMixin, NewsletterMixin
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText
import swapper

Signature = swapper.load_model("petition", "Signature")


class CustomSignatureForm(GiodoMixin, NewsletterMixin, BaseSignatureForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignatureForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
                'first_name',
                'second_name',
                PrependedText('email', '@'),
                PrependedText('organization', '<i class="fa fa-users"></i>'),
                'giodo',
                'newsletter',
        )

    class Meta:
        model = Signature
        fields = ['first_name', 'second_name', 'email', 'newsletter', 'organization']
