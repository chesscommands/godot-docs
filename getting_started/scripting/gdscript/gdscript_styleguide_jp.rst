.. _doc_gdscript_styleguide_jp:

































GDScript表記規定
================================

.. 英語の原文：GDScript表記規定
   GDScript style guide
   ====================


































説明
------------

今回の説明では、優雅なGDScriptを記述するための規則が一覧化されている。
目標は、鮮やかで読みやすいコードの作成を推奨し、プロジェクト・討論・チュートリアル全体で一貫性を促進すること。
あわよくば、これは自動書式設定ツールの開発も促進するだろう。

GDScriptはPythonに近いため、今回はPythonの `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__ プログラミングスタイルガイドに触発されている。

.. note:: 

   Godotの組み込みスクリプトエディタは初期設定でこれらの規則の多くを使用する。
   今回はそのための手助けだ。

   （訳者：どういう意味？）





.. 英語の原文：説明
   Description
   -----------

   This styleguide lists conventions to write elegant GDScript. The goal is
   to encourage writing clean, readable code and promote consistency across
   projects, discussions, and tutorials. Hopefully, this will also
   encourage development of auto-formatting tools.

   Since GDScript is close to Python, this guide is inspired by Python's
   `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__ programming
   styleguide.

   .. note:: Godot's built-in script editor uses a lot of these conventions
             by default. Let it help you.



































コード構造
--------------------


.. 英語の原文：コード構造
   Code structure
   --------------

































字下げ(Indentation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

インデントの種類：Tab *(エディタのデフォルト)*

インデントサイズ：4 *(エディタのデフォルト)*

各インデントレベルは、それを含むブロックよりも1つ大きくなければならない。

**Good** ：

::

   for i in range(10):
       print("hello")

**Bad** ：

::

   for i in range(10):
     print("hello")

   for i in range(10):
           print("hello")

2つのインデントレベルを使用し、継続行を通常のコードブロックと区別する。

**Good** ：

::

   effect.interpolate_property(sprite, 'transform/scale',
               sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
               Tween.TRANS_QUAD, Tween.EASE_OUT)

訳者：どこがいいのか全く分からない。
要は、ピリオド区切りから4つ分の半角スペースをつけているからいいってこと？

**Bad** ：


::

   effect.interpolate_property(sprite, 'transform/scale',
       sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
       Tween.TRANS_QUAD, Tween.EASE_OUT)

訳者：何も考えずに半角スペース4つ分だけではだめと言うことかな。





.. 英語の原文：字下げ(Indentation)
   Indentation
   ~~~~~~~~~~~

   Indent type: Tabs *(editor default)*

   Indent size: 4 *(editor default)*

   Each indent level should be one greater than the block containing it.

   **Good**:

   ::

       for i in range(10):
           print("hello")

   **Bad**:

   ::

       for i in range(10):
         print("hello")

       for i in range(10):
               print("hello")

   Use 2 indent levels to distinguish continuation lines from
   regular code blocks.

   **Good**:

   ::

       effect.interpolate_property(sprite, 'transform/scale',
                   sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
                   Tween.TRANS_QUAD, Tween.EASE_OUT)

   **Bad**:

   ::

       effect.interpolate_property(sprite, 'transform/scale',
           sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
           Tween.TRANS_QUAD, Tween.EASE_OUT)


































空白行
~~~~~~~~~~~~

関数とクラス定義を2つの空白行(空行)で囲む。

::

   func heal(amount):
       health += amount
       health = min(health, max_health)
       emit_signal("health_changed", health)


   func take_damage(amount, effect=null):
       health -= amount
       health = max(0, health)
       emit_signal("health_changed", health)

関数内で1つの空行を使用して、論理セクションを区切る。














.. 英語の原文：空白行
   Blank lines
   ~~~~~~~~~~~

   Surround functions and class definitions with two blank lines:

   ::

       func heal(amount):
           health += amount
           health = min(health, max_health)
           emit_signal("health_changed", health)


       func take_damage(amount, effect=null):
           health -= amount
           health = max(0, health)
           emit_signal("health_changed", health)

   Use one blank line inside functions to separate logical sections.


































1行に1つの処理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1行に複数の処理を組み合わせるべからず。
Cプログラマに限らず、1つの条件処理を1行とする(三項演算子を除く)！

**Good** ：

::

   if position.x > width:
       position.x = 0

   if flag:
       print("flagged")

**Bad** ：

::

   if position.x > width: position.x = 0

   if flag: print("flagged")



.. 英語の原文：1行に1つの処理
   One statement per line
   ~~~~~~~~~~~~~~~~~~~~~~

   Never combine multiple statements on a single line. No, C programmers,
   not with a single line conditional statement (except with the ternary
   operator)!

   **Good**:

   ::

       if position.x > width:
           position.x = 0

       if flag:
           print("flagged")

   **Bad**:

   ::

       if position.x > width: position.x = 0

       if flag: print("flagged")


































不要な括弧を避ける
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

式及び条件処理で括弧を使用しないこと。
操作の順序に必要な場合を除き、読みやすさを低下させるだけの存在にしかならない。

訳者：本当か？

**Good** ：

::

   if is_colliding():
       queue_free()

**Bad** ：

::

   if (is_colliding()):
       queue_free()


.. 英語の原文：不要な括弧を避ける
   Avoid unnecessary parentheses
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Avoid parentheses in expressions and conditional statements. Unless
   necessary for order of operations, they only reduce readability.

   **Good**:

   ::

       if is_colliding():
           queue_free()

   **Bad**:

   ::

       if (is_colliding()):
           queue_free()

































空白
~~~~~~~~~~~~

演算子の前後及びコンマの後ろには常に1つのスペースを使用すること。
辞書参照や関数呼び出しで余分なスペースを割けたり、 "整列" が必要。

**Good** ：

::

   position.x = 5
   position.y = mpos.y + 10
   dict['key'] = 5
   myarray = [4, 5, 6]
   print('foo')

**Bad** ：

::

   position.x=5
   position.y = mpos.y+10
   dict ['key'] = 5
   myarray = [4,5,6]
   print ('foo')

**NEVER** ：

::

   x        = 100
   y        = 100
   velocity = 500


.. 英語の原文：空白
   Whitespace
   ~~~~~~~~~~

   Always use one space around operators and after commas. Avoid extra
   spaces in dictionary references and function calls, or to create "columns."

   **Good**:

   ::

       position.x = 5
       position.y = mpos.y + 10
       dict['key'] = 5
       myarray = [4, 5, 6]
       print('foo')

   **Bad**:

   ::

       position.x=5
       position.y = mpos.y+10
       dict ['key'] = 5
       myarray = [4,5,6]
       print ('foo')

   **NEVER**:

   ::

       x        = 100
       y        = 100
       velocity = 500

































命名規則
----------------

これらの命名規則は、Godotエンジンスタイルに従う。
違反する場合、組み込みの命名規則と衝突するため、見苦しくなる。


.. 英語の原文：命名規則
   Naming conventions
   ------------------

   These naming conventions follow the Godot Engine style. Breaking these
   will make your code clash with the built-in naming conventions, which is
   ugly.


































クラスのノード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PascalCaseを使用する： ``extends KinematicBody``

また、クラスを定数または変数にロードする場合：

::

   const MyCoolNode = preload('res://my_cool_node.gd')


.. 英語の原文：クラスのノード
   Classes and nodes
   ~~~~~~~~~~~~~~~~~

   Use PascalCase: ``extends KinematicBody``

   Also when loading a class into a constant or variable:

   ::

       const MyCoolNode = preload('res://my_cool_node.gd')


































関数と変数
~~~~~~~~~~~~~~~~~~~~

snake\_caseを使用： ``get_node()``

仮想メソッド(ユーザがオーバライドする必要がある関数)・プライベート関数・プライベート変数の前に単一のアンダースコア(_)を追加する：
``func _ready()``


.. 英語の原文：関数と変数
Functions and variables
~~~~~~~~~~~~~~~~~~~~~~~

Use snake\_case: ``get_node()``

Prepend a single underscore (\_) to virtual methods (functions the user
must override), private functions, and private variables:
``func _ready()``



































シグナル
~~~~~~~~~~~~~~~~

過去形を使用する(訳者：何が？)：

::

   signal door_opened
   signal score_changed


.. 英語の原文：シグナル
   Signals
   ~~~~~~~

   Use past tense:

   ::

       signal door_opened
       signal score_changed

































定数
~~~~~~~~~~~~

CONSTANT\_CASE・すべて大文字・アンダースコア(_)を使用して端午を区切る：
``const MAX_SPEED = 200``


.. 英語の原文：定数
   Constants
   ~~~~~~~~~

   Use CONSTANT\_CASE, all caps, with an underscore (\_) to separate words:
   ``const MAX_SPEED = 200``

































静的型付け
--------------------

Godot 3.1以降、GDScriptは :ref:`optional static typing<doc_gdscript_static_typing>` に対応している。

.. todo::

   リンクの確認。


.. 英語の原文：静的型付け
   Static typing
   -------------

   Since Godot 3.1, GDScript supports :ref:`optional static typing<doc_gdscript_static_typing>`.



































タイプヒント
~~~~~~~~~~~~~~~~~~~~~~~~

変数の名前の直後にスペースを入れずにコロンを配置し、可能であればGDScriptコンパイラに変数の型を推測させる。

**Good** ：

::

   onready var health_bar: ProgressBar = get_node("UI/LifeBar")

   var health := 0 # コンパイラはint型を使用する。

**Bad** ：

::

   # コンパイラは正確な型を推測できず、
   # ProgressBarの代わりにNodeを使ってしまった。
   onready var health_bar := get_node("UI/LifeBar") 

コンパイラに型のヒントを推測させるときは、コロンと統合を一緒に記述する：
``:=``

::

   var health := 0 # コンパイラはint型を使用する。

関数を定義するときに、戻り値の型の矢印の両側にスペースを追加する。

::

   func heal(amount: int) -> void:



.. 英語の原文：タイプヒント
   Type hints
   ~~~~~~~~~~

   Place the colon right after the variable's name, without a space, and let the GDScript compiler infer the variable's type when possible.


   **Good**:

   ::

      onready var health_bar: ProgressBar = get_node("UI/LifeBar")

      var health := 0 # The compiler will use the int type

   **Bad**:

   ::

      # The compiler can't infer the exact type and will use Node 
      # instead of ProgressBar
      onready var health_bar := get_node("UI/LifeBar") 

   When you let the compiler infer the type hint, write the colon and equal signs together: ``:=``.

   ::

      var health := 0 # The compiler will use the int type

   Add a space on either sides of the return type arrow when defining functions.

   ::

      func heal(amount: int) -> void:

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
