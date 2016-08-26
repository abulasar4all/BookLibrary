from django import forms

class FormReview(forms.Form):
	"""
	Forms for reviewing book
	"""

	is_favourite = forms.BooleanField(
		label = "Favourite?",
		help_text = "In your top 100 book of all time",
		required=False  #For every boolean field required is needed
	)

	review = forms.CharField(
		widget = forms.Textarea,
		min_length =  300,
		error_messages = {
			'required': "Please enter review",
			'min_length': "Please write atleast 300 words(You have written %(show_value)s)"
		}
	)