
import sys
import os

#sys.path.append('/Users/asakunotomohiro/Program/sphinx/source/gdscript.py')
#sys.path.append('/Users/asakunotomohiro/Program/gdscript/gdscript.py')
sys.path.append('/Users/asakunotomohiro/Program/gdscript')
#sys.path.append('../../../../gdscript/gdscript.py')

#import sphinx_rtd_theme
#html_theme = "sphinx_rtd_theme"
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

language = 'ja'
epub_language = 'ja'
#html_language = 'ja'   ←たぶん、こんな設定は無いと思うが、エラーにはならなかった。


sys.path.append(os.path.abspath('extensions'))
# GDScript を記事内で使うためのモジュール
extensions = ['gdscript']
# GDScript 設定ここまで ----------------


# TODOリストを使うためのモジュール(インストール不要で使えるようだ)
extensions += ['sphinx.ext.todo']

[extensions]
todo_include_todos=True
# TODOリスト設定ここまで -----------------------------------------


# tabsタグを使うためにモジュールをインストール
extensions += ['sphinx_tabs.tabs']
templates_path = ['_templates']
# tabsタグ設定ここまで -----------------------




# Weblate で翻訳された実績や進捗などをreStructuredTextで都合よく表示させることができない。
# そのため、外部からその情報を引っ張り込むことにした。
# それが以下の処理になる。
rst_epilog = """
.. |weblate_widget| image:: https://hosted.weblate.org/widgets/godot-engine/{image_locale}/godot-docs/287x66-white.png
    :alt: Translation status
    :target: https://hosted.weblate.org/engage/godot-engine{target_locale}/?utm_source=widget
""".format(
    image_locale='-' if language == 'en' else language,
    target_locale='' if language == 'en' else '/' + language
)




# 不自然な空白が表示される
#   https://sphinx-users.jp/reverse-dict/html/japanese.html
sys.path.insert(0, os.path.abspath('.')) # コメントを外します
#extensions += ['japanesesupport', 'その他の拡張'] # 加えます
extensions += ['japanesesupport'] # 加えます




# 以下、何をやっているのか全く分からない。
source_suffix = '.rst'
source_encoding = 'utf-8-sig'

master_doc = 'index_jp'

env_tags = os.getenv('SPHINX_TAGS')
if env_tags != None:
   for tag in env_tags.split(','):
       print("Adding Sphinx tag: %s" % tag.strip())
       tags.add(tag.strip())

language = os.getenv('READTHEDOCS_LANGUAGE', 'en')
is_i18n = tags.has('i18n')

exclude_patterns = ['_build']


from gdscript import GDScriptLexer
from sphinx.highlighting import lexers
lexers['gdscript'] = GDScriptLexer()

pygments_style = 'sphinx'
highlight_language = 'gdscript'
# ここまで、何をやっているのか全く分からない。



#language = ja
#language('ja')
today_fmt = '%Y/%m/%d'



def setup(app):
    app.add_stylesheet('myStyle.css')





html_use_smartypants = False




latex_docclass = {'manual': 'jsbook'}


# vim:set ts=4 sw=4 tw=0 fenc=utf-8:
