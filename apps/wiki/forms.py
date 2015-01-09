from django.forms import ModelForm

from apps.news.widgets import EESTECEditor
from apps.wiki.models import WikiPage


class WikiForm(ModelForm):
    class Meta:
        model = WikiPage
        fields = ('name', 'content')
        widgets = {'content': EESTECEditor(include_jquery=False, options={
            'height': 600,
        })}
        # 'css': "/static/enet/css/wysiwyg.css"})}
