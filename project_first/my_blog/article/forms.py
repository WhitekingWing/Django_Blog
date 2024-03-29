from django import forms
from .models import ArticlePost
class ArticlePostForm(forms.ModelForm):
	class Meta:
		model = ArticlePost
		#定义表单含有的字段
		fields = ('title', 'body', 'tags', 'avatar')