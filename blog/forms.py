from django import forms

class PostForm (forms.Form):
  
  title = forms.CharField(label='Title', max_length=256, )
  body = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}), label='Post')