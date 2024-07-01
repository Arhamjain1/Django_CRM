from django.contrib.auth.forms import UserCreationForm # Creates Form
from django.contrib.auth.models import User # User model allowed us to create super user
from django import forms
from .models import Record
# We create a new form by extending Django's built-in UserCreationForm. This is like taking a basic form and adding our own custom fields and styles to it.
# A widget is the representation of a field on the web. It defines what HTML elements will be used to render the field. For example, forms.TextInput is a widget that renders a <input type="text"> HTML element.
# attrs: This is a dictionary where you can specify additional HTML attributes for the widget.
# class: This is one of the HTML attributes you can specify. In this context, it refers to the CSS class used for styling the input element. By setting 'class': 'form-control', we're applying Bootstrap's form-control class to this input field to make it look nice and consistent.

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    # model in the Meta class specifies which Django model this form is associated with

    class Meta:
        model = User  # This means that this form will be used to create or update User instances in the database.
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        # Above line specifies that the form should include these fields from the User model and the UserCreationForm.

    # the __init__ method is used to initialize the form and customize its fields.
    # By calling super(SignUpForm, self).__init__(*args, **kwargs), we ensure that the form is properly initialized by the parent class (UserCreationForm). This means all the default behavior and initializations done by UserCreationForm are preserved. Without this call, our customizations would override and potentially break the standard initialization process.

    def __init__(self, *args, **kwargs):
        # In Django, UserCreationForm is like the BaseCake class. It provides the basic functionality for creating a user form, including initializing the fields and handling validation.
        # Without this call to super(), the UserCreationForm's __init__ method wouldn't be executed, which means none of the default setup would happen. This could lead to missing fields or broken functionality.

        super(SignUpForm, self).__init__(*args, **kwargs)
     
        # self.fields['username']: Accesses the username field of the form.
     
        # .widget.attrs['class'] = 'form-control': Sets the HTML class attribute of the widget to form-control. This applies Bootstrap styling to make the field look good.
        self.fields['username'].widget.attrs['class'] = 'form-control'
        # .widget.attrs['placeholder'] = 'User Name': Sets the placeholder attribute for the username field. The placeholder is the text shown inside the input box when it is empty, giving the user a hint about what to enter.
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        # .label = '': Removes the label for the username field. By default, Django forms generate a label for each field, but setting it to an empty string removes it.
        self.fields['username'].label = ''
        # .help_text: Provides additional information to the user about what is required for this field. Here, it gives instructions about the allowed characters and length for the username. This help text is styled with Bootstrap classes for consistency.
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


#Create Add Record form
class AddRecordForm(forms.ModelForm):
    first_name= forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name","class":"form-control"}))
    last_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name","class":"form-control"}))
    email=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}))
    address=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}))
    city=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City","class":"form-control"}))
    state=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}))
    zipcode=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code","class":"form-control"}))


#The Meta class within the form specifies that the form should use the Record model and excludes the user field from the form.
    class Meta:
        model=Record
        exclude={"user",}