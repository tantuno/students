
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _
import logging

from studentsdb.settings import ADMIN_EMAIL

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        #call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        #this helper object allows us to customize form
        self.helper =FormHelper()

        #form tag attributes
        self.helper.form_class = 'form_horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        #twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #form buttons
        self.helper.add_input(Submit('send_button', _(u'Send')))


    from_email = forms.EmailField(
    label=_(u"Your Email Address"))

    subject = forms.CharField(
    label=_(u"Email Subject"),
    max_length=128)

    message = forms.CharField(
    label=_(u"Email Body"),
    max_length=2560,
    widget=forms.Textarea)


@permission_required('auth.add_user')
def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = _(u"An error occured during email transfer. Please, "
                    "try again later.")
                logger = logging.getLogger(__name__)
                logger.exception(message)
            else:
                message = _(u"Message sent successfully!")
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))

    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form':form})
