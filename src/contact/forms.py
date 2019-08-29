from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

SERVICES = (
    ('', 'Choose services'),
    ('Just a message', 'Just a mesage.'),
    ('A complaint', 'I want to make a complaint'),
    ('Web development', 'I need geetech team to build a web app for my team'),
    # ('Destop app development', 'I need geetech team to build a desktop app for my team'),
    # ('Mobile app development', 'I need geetech team to build a mobile app for my team'),
    ('Web site upgrade', 'I want to upgrade my existing website'),
    ('Web site Management', 'I want your team to manage my existing website')
)

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', required = True, max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'example'}))
    email = forms.EmailField(label='Your email', required = True, max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}))
    phone = forms.RegexField(label='Your phone number', regex=r'^\+?1?\d{11,13}$', widget=forms.TextInput(attrs={'placeholder': '08012345678'}))
    category = forms.ChoiceField(label='', choices=SERVICES)
    description = forms.CharField(label='Your description', required = True, max_length = 300, widget=forms.TextInput(attrs={'placeholder': 'Brief description of what you need us to do for you'}))
    message = forms.CharField(label='Your message', widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('name', css_class='col-md-4'),
    #             Column('email', css_class='col-md-4'),
    #             Column('phone', css_class='col-md-4'),
    #         ),
    #         Row(
    #             Column('category', css_class='col-md-12')
    #         ),
    #         Row(
    #             Column('message', css_class='col-md-12')
    #         ),
    #         Submit('submit', 'Contact Us', css_class='btn btn-danger btn-fill col-md-2 col-md-offset-5')
    #     )

# <div class="row">
#     <div class="col-md-8 col-md-offset-2">
#         <div class="contact-form">
#         {% if messages %}
#             <div class="alert alert-success">
#                 {% for message in messages %}
#                 <div{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</div>
#                 {% endfor %}
#             </div>
#         {% endif %}

#         {% crispy form %}
#         </div>
#     </div>
# </div>