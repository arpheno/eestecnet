from froala_editor.widgets import FroalaEditor

__author__ = 'Arphen'


class EESTECEditor(FroalaEditor):
    def _media(self):
        css = {
            'all': ('froala_editor/css/font-awesome.min.css',
                    'froala_editor/css/froala_editor.min.css',
                    'froala_editor/css/froala-django.css')
        }
        js = ('froala_editor/js/froala_editor.min.js',)

        if self.include_jquery:
            js = ('froala_editor/js/libs/jquery-1.11.1.min.js',) + js

        if self.theme:
            css['all'] += ('froala_editor/css/themes/' + self.theme + '.css',)

        for plugin in self.plugins:
            js += ('froala_editor/js/plugins/' + plugin + '.min.js',)

        return Media(css=css, js=js)

