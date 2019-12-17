.. _doc_gdscript_jp:


GDScriptの基本
============================

.. 英語の原文：GDScriptの基本
   GDScript basics
   ===============


































概論
------------

*GDScript* は、コンテンツの作成に使用される動的に型付けされた高レベルのプログラミング言語に当たる。
`Python <https://en.wikipedia.org/wiki/Python_%28programming_language%29>`_
に似た構文を使う(ブロックはインデント区切りであり、多くのキーワードが似ている)。
その目標は、Godot Engine向けに最適化され、Godot Engineと緊密に統合され、コンテンツの作成と統合に優れた柔軟性を提供することにある。



.. 英語の原文：概論
   Introduction
   ------------

   *GDScript* is a high-level, dynamically typed programming language used to
   create content. It uses a syntax similar to
   `Python <https://en.wikipedia.org/wiki/Python_%28programming_language%29>`_
   (blocks are indent-based and many keywords are similar). Its goal is
   to be optimized for and tightly integrated with Godot Engine, allowing great
   flexibility for content creation and integration.



































GDScriptが作られた経緯
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

初期段階では、 `Lua <https://www.lua.org>`__ スクリプト言語をエンジンとして使っていた。
Luaは高速動作だが、(フォールバックを使用して)オブジェクト指向システムへのバインディングを作成するのは複雑で遅く、膨大な量のコードを必要とした。
`Python <https://www.python.org>`__ で同様の実験後、埋め込みが難しいことも判明した。

出荷されたゲームに使用された最後のサードパーティのスクリプト言語は、
`Squirrel <http://squirrel-lang.org>`__
だったが、同様に不採用になった。
その時点で、Godotの(特定の部分の)性能を引き出すには、カスタムスクリプト言語でしか実現できないことが判明した。

- Godotはノードにスクリプトを埋め込む。
  ほとんどの言語は、これを念頭に置いて設計されていない。
- Godotは、2Dおよび3D数学にいくつかの組み込みデータ型を使用する。
  ほとんどのスクリプト言語はこれを提供せずに、バインドするのだが、それは非効率になる。
- Godotは、ネットまたはディスクからデータをリフティング(訳者：取り出すこと？)及び初期化するためにスレッドを頻繁に使用する。
  ほとんどのインタプリタ言語は、適していない。
- Godotには、既にリソース用のメモリ管理モデルがあり、ほとんどのスクリプト言語は独自の機能を提供しているため、作業とバグが重複してしまう。
- バインディングコードは常に乱雑であり、いくつかの障害ポイント・予期しないバグ・保守性の低下があげられる。

.. todo::

   訳者：バインディングコードとは何？

これらの考慮事項の結果として *GDScript* が作られた。
GDScript言語とインタプリタは、LuaとSquirrelのバインディングコード自体より小さくなり、同等の機能を備えることができた。
時間が経つにつれ、組み込み言語を持つことは、大きな利点があることを実感できた。


.. 英語の原文：GDScriptが作られた経緯
   History
   ~~~~~~~

   In the early days, the engine used the `Lua <https://www.lua.org>`__
   scripting language. Lua is fast, but creating bindings to an object
   oriented system (by using fallbacks) was complex and slow and took an
   enormous amount of code. After some experiments with
   `Python <https://www.python.org>`__, it also proved difficult to embed.

   The last third party scripting language that was used for shipped games
   was `Squirrel <http://squirrel-lang.org>`__, but it was dropped as well.
   At that point, it became evident that a custom scripting language could
   more optimally make use of Godot's particular architecture:

   -  Godot embeds scripts in nodes. Most languages are not designed with
      this in mind.
   -  Godot uses several built-in data types for 2D and 3D math. Script
      languages do not provide this, and binding them is inefficient.
   -  Godot uses threads heavily for lifting and initializing data from the
      net or disk. Script interpreters for common languages are not
      friendly to this.
   -  Godot already has a memory management model for resources, most
      script languages provide their own, which results in duplicate
      effort and bugs.
   -  Binding code is always messy and results in several failure points,
      unexpected bugs and generally low maintainability.

   The result of these considerations is *GDScript*. The language and
   interpreter for GDScript ended up being smaller than the binding code itself
   for Lua and Squirrel, while having equal functionality. With time, having a
   built-in language has proven to be a huge advantage.


































GDScript例
~~~~~~~~~~~~~~~~~~~~

一部の人々は構文を見ることで理解を深めることができるため、GDScriptでの見え方を簡単な例で示す。

::

   # ファイルを1つのクラスとして扱う。

   # 継承

   extends BaseClass

   # (オプション) カスタムアイコン付きのクラス定義

   class_name MyClass, "res://path/to/optional/icon.svg"

   # メンバ変数

   var a = 5
   var s = "Hello"
   var arr = [1, 2, 3]
   var dict = {"key": "value", 2: 3}
   var typed_var: int
   var inferred_type := "String"

   # 定数

   const ANSWER = 42
   const THE_NAME = "Charly"

   # 列挙型(Enums)

   enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
   enum Named {THING_1, THING_2, ANOTHER_THING = -1}

   # 組込みのベクトル型

   var v2 = Vector2(1, 2)
   var v3 = Vector3(1, 2, 3)

   # 関数(Function) ←訳者：メソッドと言うべきでは？

   func some_function(param1, param2):
     var local_var = 5

     if param1 < local_var:
         print(param1)
     elif param2 > 5:
         print(param2)
     else:
         print("Fail!")

     for i in range(20):
         print(i)

     while param2 != 0:
         param2 -= 1

     var local_var2 = param1 + 3
     return local_var2

   # 関数は、base/parentクラスの同じ名前の関数をオーバーライドする。.
   # それでもそれらを呼び出す場合は '.' を使用する (他の言語で言うならば、 'super' メソッド呼び出しに相当する).

   func something(p1, p2):
       .something(p1, p2)

   # 内部クラス

   class Something:
       var a = 10

   # コンストラクタ

   func _init():
       print("Constructed!")
       var lv = Something.new()
       print(lv.a)

C・C++・C#などの静的型付け言語の経験があり、以前に動的型付け言語を触ったことがない場合は、
:ref:`doc_gdscript_more_efficiently`
のチュートリアルを参照すること。


.. todo::

   リンクの確認。


.. 英語の原文：GDScript例
   Example of GDScript
   ~~~~~~~~~~~~~~~~~~~

   Some people can learn better by taking a look at the syntax, so
   here's a simple example of how GDScript looks.

   ::

       # A file is a class!

       # Inheritance

       extends BaseClass

       # (optional) class definition with a custom icon

       class_name MyClass, "res://path/to/optional/icon.svg"

       # Member variables

       var a = 5
       var s = "Hello"
       var arr = [1, 2, 3]
       var dict = {"key": "value", 2: 3}
       var typed_var: int
       var inferred_type := "String"

       # Constants

       const ANSWER = 42
       const THE_NAME = "Charly"

       # Enums

       enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
       enum Named {THING_1, THING_2, ANOTHER_THING = -1}

       # Built-in vector types

       var v2 = Vector2(1, 2)
       var v3 = Vector3(1, 2, 3)

       # Function

       func some_function(param1, param2):
           var local_var = 5

           if param1 < local_var:
               print(param1)
           elif param2 > 5:
               print(param2)
           else:
               print("Fail!")

           for i in range(20):
               print(i)

           while param2 != 0:
               param2 -= 1

           var local_var2 = param1 + 3
           return local_var2

       # Functions override functions with the same name on the base/parent class.
       # If you still want to call them, use '.' (like 'super' in other languages).

       func something(p1, p2):
           .something(p1, p2)

       # Inner class

       class Something:
           var a = 10

       # Constructor

       func _init():
           print("Constructed!")
           var lv = Something.new()
           print(lv.a)

   If you have previous experience with statically typed languages such as
   C, C++, or C# but never used a dynamically typed one before, it is advised you
   read this tutorial: :ref:`doc_gdscript_more_efficiently`.



































言語
------------

以下に、GDScriptの概要を示す。
配列または他のオブジェクトで使用できるメソッドなどの詳細は、リンク先で調べる必要が出てくる。


.. 英語の原文：言語
   Language
   --------

   In the following, an overview is given to GDScript. Details, such as which
   methods are available to arrays or other objects, should be looked up in
   the linked class descriptions.


































識別子
~~~~~~~~~~~~

アルファベット( ``a`` to ``z`` and ``A`` to ``Z`` )・
数字( ``0`` to ``9`` )・
それらを_で区切る文字列が識別子として許可されている。
しかし、識別子を数字で始めてはならない。
そして、大小文字を区別して識別子が存在する
( ``foo`` は、 ``FOO`` と異なる)。


.. 英語の原文：識別子
   Identifiers
   ~~~~~~~~~~~

   Any string that restricts itself to alphabetic characters (``a`` to
   ``z`` and ``A`` to ``Z``), digits (``0`` to ``9``) and ``_`` qualifies
   as an identifier. Additionally, identifiers must not begin with a digit.
   Identifiers are case-sensitive (``foo`` is different from ``FOO``).



































キーワード
~~~~~~~~~~~~~~~~~~~~

以下は、言語でサポートされているキーワード一覧になる。
キーワードは予約語(トークン)であるため、識別子として使用できない。
演算子( ``in`` ・ ``not`` ・ ``and`` ・ ``or`` など)および次のセクションに一覧化されている組み込み型の名前も予約されている。

キーワードごとのオタクになりたい場合に備え、
`GDScript tokenizer <https://github.com/godotengine/godot/blob/master/modules/gdscript/gdscript_tokenizer.cpp>`_
に定義している。

.. csv-table:: キーワード一覧表
   :header: キーワード, 説明
   :widths: 5, 5

   if, `if/else/elif`_ 参照。
   elif, `if/else/elif`_ 参照。
   else, `if/else/elif`_ 参照。
   for, for_ 参照。
   while, while_ 参照。
   match, match_ 参照。
   break, 現在の ``for`` または ``while`` ループの実行を終了する。
   continue, すぐに ``for`` または ``while`` ループの次の処理に飛ぶ。
   pass, ステートメントが構文的に必要であるが、コードの実行が望ましくない場合に使用される。空の関数で。
   return, 関数から値を返す。
   class, クラスを定義する。
   extends, 現在のクラスで拡張するクラスを定義する。
   is, 変数が特定のクラスを拡張するか、特定の組み込み型であるかをテストする。
   as, 可能であれば、値を指定された方にキャストする。
   self, 現在のクラスインスタンスを参照する。
   tool, エディタでスクリプトを実行する。
   signal, シグナルを定義する。
   func, 関数を定義する。
   static, 静的関数を定義する。静的メンバ変数は許可されていない。
   const, 定数を定義する。
   enum, 列挙型を定義する。
   var, 変数を定義する。
   onready, スクリプトが接続されているノードとその子がシーンツリーの一部になったとき、変数を初期化する。
   export, 接続されているリソースとともに変数を保存し、エディタで表示及び変更可能にする。
   setget, 変数のセッタおよびゲッタ関数を定義する。
   breakpoint, デバッガブレークポイントのエディタヘルパ
   preload, クラスまたは変数をプリロードする。 :ref:`Classes as resources <Classes_as_resources_jump>` を参照すること。
   yield, コルーチンサポート。 `Coroutines with yield`_ を参照すること。
   assert, 条件をアサートし、失敗時にエラーを記録する。デバッグ以外のビルドでは無視される。 `Assert keyword`_ を参照すること。
   remote, ネットワーキングRPCアノテーション。 :ref:`high-level multiplayer docs <doc_high_level_multiplayer>` を参照すること。
   master, ネットワーキングRPCアノテーション。 :ref:`high-level multiplayer docs <doc_high_level_multiplayer>` を参照すること。
   puppet, ネットワーキングRPCアノテーション。 :ref:`high-level multiplayer docs <doc_high_level_multiplayer>` を参照すること。
   remotesync, ネットワーキングRPCアノテーション。 :ref:`high-level multiplayer docs <doc_high_level_multiplayer>` を参照すること。
   mastersync, ネットワーキングRPCアノテーション。 :ref:`high-level multiplayer docs <doc_high_level_multiplayer>` を参照すること。
   puppetsync, ネットワーキングRPCアノテーション。 :ref:`high-level multiplayer docs <doc_high_level_multiplayer>` を参照すること。
   PI, PI定数。
   TAU, TAU定数。
   INF, 無限大定数。比較に使用する。
   NAN, NAN(数値ではない)定数。比較に使用する。



.. 英語の原文：キーワード
   Keywords
   ~~~~~~~~

   The following is the list of keywords supported by the language. Since
   keywords are reserved words (tokens), they can't be used as identifiers.
   Operators (like ``in``, ``not``, ``and`` or ``or``) and names of built-in types
   as listed in the following sections are also reserved.

   Keywords are defined in the `GDScript tokenizer <https://github.com/godotengine/godot/blob/master/modules/gdscript/gdscript_tokenizer.cpp>`_
   in case you want to take a look under the hood.

   +------------+---------------------------------------------------------------------------------------------------------------+
   |  Keyword   | Description                                                                                                   |
   +============+===============================================================================================================+
   | if         | See `if/else/elif`_.                                                                                          |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | elif       | See `if/else/elif`_.                                                                                          |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | else       | See `if/else/elif`_.                                                                                          |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | for        | See for_.                                                                                                     |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | while      | See while_.                                                                                                   |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | match      | See match_.                                                                                                   |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | break      | Exits the execution of the current ``for`` or ``while`` loop.                                                 |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | continue   | Immediately skips to the next iteration of the ``for`` or ``while`` loop.                                     |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | pass       | Used where a statement is required syntactically but execution of code is undesired, e.g. in empty functions. |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | return     | Returns a value from a function.                                                                              |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | class      | Defines a class.                                                                                              |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | extends    | Defines what class to extend with the current class.                                                          |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | is         | Tests whether a variable extends a given class, or is of a given built-in type.                               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | as         | Cast the value to a given type if possible.                                                                   |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | self       | Refers to current class instance.                                                                             |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | tool       | Executes the script in the editor.                                                                            |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | signal     | Defines a signal.                                                                                             |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | func       | Defines a function.                                                                                           |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | static     | Defines a static function. Static member variables are not allowed.                                           |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | const      | Defines a constant.                                                                                           |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | enum       | Defines an enum.                                                                                              |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | var        | Defines a variable.                                                                                           |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | onready    | Initializes a variable once the Node the script is attached to and its children are part of the scene tree.   |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | export     | Saves a variable along with the resource it's attached to and makes it visible and modifiable in the editor.  |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | setget     | Defines setter and getter functions for a variable.                                                           |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | breakpoint | Editor helper for debugger breakpoints.                                                                       |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | preload    | Preloads a class or variable. See `Classes as resources`_.                                                    |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | yield      | Coroutine support. See `Coroutines with yield`_.                                                              |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | assert     | Asserts a condition, logs error on failure. Ignored in non-debug builds. See `Assert keyword`_.               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | remote     | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | master     | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | puppet     | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | remotesync | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | mastersync | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | puppetsync | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | PI         | PI constant.                                                                                                  |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | TAU        | TAU constant.                                                                                                 |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | INF        | Infinity constant. Used for comparisons.                                                                      |
   +------------+---------------------------------------------------------------------------------------------------------------+
   | NAN        | NAN (not a number) constant. Used for comparisons.                                                            |
   +------------+---------------------------------------------------------------------------------------------------------------+



































演算子(オペレータ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

以下は、サポートされる演算子とその優先順位一覧。

.. csv-table:: 演算子一覧表
   :header: **演算子** , **説明**
   :widths: 5, 5

   ``x[index]`` ,サブスクリプション(最高優先度)
   ``x.attribute`` ,属性リファレンス
   ``is`` ,インスタンスタイプチェッカー
   ``~`` ,ビット単位のNOT
   ``-x`` ,負/単項否定
   ``*`` ・ ``/`` ・ ``%`` ,乗算/除算/剰余
   ,                  これらの演算子の動作はC++と同じ。
   ,                  整数の除算は少数を返すのでは無く、切り捨てられ、%演算子はintでのみ使用できる。
   ,                  (floatの場合は "fmod" )
   ``+`` ,配列の追加/連結
   ``-`` ,減算
   ``<<`` ・ ``>>`` ,ビットシフト
   ``&`` ,ビット単位のAND
   ``^`` ,ビット単位のXOR
   ``|`` ,ビット単位のOR
   ``<`` ・ ``>`` ・ ``==`` ・ ``!=`` ・ ``>=`` ・ ``<=`` ,比較
   ``in`` ,内容テスト
   ``!`` ・ ``not`` ,BoolのNOT
   ``and`` ・ ``&&`` ,BoolのAND
   ``or`` ・ ``||`` ,BoolのOR
   ``if x else`` ,三項演算子 if/else
   ``=`` ・ ``+=`` ・ ``-=`` ・ ``*=`` ・ ``/=`` ・ ``%=`` ・ ``&=`` ・ ``|=`` ,割り当て(最低優先度)

.. todo::

   訳者：改行を故意に入れたい場合は、CSV形式の表では対応できないだろう。
   通常の表に置き換え直す必要があるだろう。




.. 英語の原文：演算子(オペレータ)
   Operators
   ~~~~~~~~~

   The following is the list of supported operators and their precedence.

   +---------------------------------------------------------------+-----------------------------------------+
   | **Operator**                                                  | **Description**                         |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``x[index]``                                                  | Subscription (highest priority)         |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``x.attribute``                                               | Attribute reference                     |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``is``                                                        | Instance type checker                   |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``~``                                                         | Bitwise NOT                             |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``-x``                                                        | Negative / Unary negation               |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``*`` ``/`` ``%``                                             | Multiplication / Division / Remainder   |
   |                                                               |                                         |
   |                                                               | These operators have the same behavior  |
   |                                                               | as C++. Integer division is truncated   |
   |                                                               | rather than returning a fractional      |
   |                                                               | number, and the % operator is only      |
   |                                                               | available for ints ("fmod" for floats)  |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``+``                                                         | Addition / Concatenation of arrays      |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``-``                                                         | Subtraction                             |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``<<`` ``>>``                                                 | Bit shifting                            |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``&``                                                         | Bitwise AND                             |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``^``                                                         | Bitwise XOR                             |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``|``                                                         | Bitwise OR                              |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``<`` ``>`` ``==`` ``!=`` ``>=`` ``<=``                       | Comparisons                             |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``in``                                                        | Content test                            |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``!`` ``not``                                                 | Boolean NOT                             |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``and`` ``&&``                                                | Boolean AND                             |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``or`` ``||``                                                 | Boolean OR                              |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``if x else``                                                 | Ternary if/else                         |
   +---------------------------------------------------------------+-----------------------------------------+
   | ``=`` ``+=`` ``-=`` ``*=`` ``/=`` ``%=`` ``&=`` ``|=``        | Assignment (lowest priority)            |
   +---------------------------------------------------------------+-----------------------------------------+

































型
~~~~~~

.. csv-table:: 型(リテラル)一覧表
   :header: **型** , **説明**
   :widths: 5, 5

   ``45`` ,整数の10進数
   ``0x8F51`` ,整数の16進数
   ``0b101010`` ,整数の2進数(バイナリ)
   ``3.14`` ・ ``58.1e-10`` ,浮動小数点数(実数)
   ``"Hello"`` ・ ``"Hi"`` ,Strings
   ``"""Hello"""`` ,文字列
   ``@"Node/Label"`` , :ref:`class_NodePath` またはStringName
   ``$NodePath`` , ``get_node("NodePath")`` の省略形



.. 英語の原文：型
   Literals
   ~~~~~~~~

   +--------------------------+----------------------------------------+
   | **Literal**              | **Type**                               |
   +--------------------------+----------------------------------------+
   | ``45``                   | Base 10 integer                        |
   +--------------------------+----------------------------------------+
   | ``0x8F51``               | Base 16 (hexadecimal) integer          |
   +--------------------------+----------------------------------------+
   | ``0b101010``             | Base 2 (binary) integer                |
   +--------------------------+----------------------------------------+
   | ``3.14``, ``58.1e-10``   | Floating-point number (real)           |
   +--------------------------+----------------------------------------+
   | ``"Hello"``, ``"Hi"``    | Strings                                |
   +--------------------------+----------------------------------------+
   | ``"""Hello"""``          | Multiline string                       |
   +--------------------------+----------------------------------------+
   | ``@"Node/Label"``        | :ref:`class_NodePath` or StringName    |
   +--------------------------+----------------------------------------+
   | ``$NodePath``            | Shorthand for ``get_node("NodePath")`` |
   +--------------------------+----------------------------------------+


































コメント
~~~~~~~~~~~~~~~~

``#`` から行末まで処理されずに無視され、コメントと見なす。

::

   # This is a comment.

.. _doc_gdscript_builtin_types:

.. 英語の原文：コメント
   Comments
   ~~~~~~~~

   Anything from a ``#`` to the end of the line is ignored and is
   considered a comment.

   ::

       # This is a comment.

   .. _doc_gdscript_builtin_types:


































組み込み型
--------------------

組み込み型は、スタックに割り当てられる。
それらは値として渡される。
これは、各割り当てで、または関数に引数として渡すときにコピーが作成されることを意味する。
唯一の例外は、 ``Array`` および ``Dictionaries`` で、これらは参照によって渡されるため共有される。
（ ``PoolByteArray`` などのプールされた配列は、値として渡される。）

訳者：プールとは？

.. 英語の原文：組み込み型
   Built-in types
   --------------

   Built-in types are stack-allocated. They are passed as values. This means a copy
   is created on each assignment or when passing them as arguments to functions.
   The only exceptions are ``Array``\ s and ``Dictionaries``, which are passed by
   reference so they are shared. (Pooled arrays such as ``PoolByteArray`` are still
   passed as values.)


































基本的な組み込み型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GDScriptの変数は、いくつかの組み込み型に割り当てることができる。

訳者：そもそも組み込み型とは何？

.. 英語の原文：基本的な組み込み型
   Basic built-in types
   ~~~~~~~~~~~~~~~~~~~~

   A variable in GDScript can be assigned to several built-in types.


































null(ナル)
^^^^^^^^^^^^^^^^^^^^

``null`` は情報を含まない空のデータ型であり、他の値を割り当てることはできない。

.. 英語の原文：null(ナル)
   null
   ^^^^

   ``null`` is an empty data type that contains no information and can not
   be assigned any other value.




































bool(ブール)
^^^^^^^^^^^^^^^^^^^^^^^^

bool型には、 ``true`` および ``false`` のみを代入することができる。

.. 英語の原文：bool(ブール)
   bool
   ^^^^

   The Boolean data type can only contain ``true`` or ``false``.



































int
^^^^^^

整数データ型には、整数(正負)のみを代入できる。

.. 英語の原文：int
   int
   ^^^

   The integer data type can only contain integer numbers (both negative
   and positive).



































float
^^^^^^^^^^

浮動小数点数(実数)を代入できる。

.. 英語の原文：float
   float
   ^^^^^

   Used to contain a floating-point value (real numbers).




































:ref:`String <class_String>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Unicode形式 <https://en.wikipedia.org/wiki/Unicode>`_ の文字列には、
`標準のC言語で使われるエスケープシーケンス文字 <https://en.wikipedia.org/wiki/Escape_sequences_in_C>`_
を使うことができる。
:ref:`doc_gdscript_printf` も支援対象になっているため、参照すること。。

.. todo::

   リンクの確認。



.. 英語の原文：String
   :ref:`String <class_String>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   A sequence of characters in `Unicode format <https://en.wikipedia.org/wiki/Unicode>`_.
   Strings can contain
   `standard C escape sequences <https://en.wikipedia.org/wiki/Escape_sequences_in_C>`_.
   GDScript also supports :ref:`doc_gdscript_printf`.



































ベクター組み込み型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. 英語の原文：ベクター組み込み型
   Vector built-in types
   ~~~~~~~~~~~~~~~~~~~~~



































:ref:`Vector2 <class_Vector2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``x`` および ``y`` 軸を含む2Dベクトル型。
配列としてアクセスすることもできる。

.. 英語の原文：Vector2
   :ref:`Vector2 <class_Vector2>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   2D vector type containing ``x`` and ``y`` fields. Can also be
   accessed as array.



































:ref:`Rect2 <class_Rect2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2つのベクター軸(x・y)含む2D長方形型。
``position`` および ``size`` の2種類。
また、 ``position + size`` である ``end`` 軸を含んでいる。

.. todo::

   訳者：全く理解できない。

   フィールドを軸と訳したが、改悪(誤訳)か？


.. 英語の原文：Rect2
   :ref:`Rect2 <class_Rect2>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   2D Rectangle type containing two vectors fields: ``position`` and ``size``.
   Also contains an ``end`` field which is ``position + size``.




































:ref:`Vector3 <class_Vector3>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``x`` ・ ``y`` ・ ``z`` 軸を含む3Dベクトル型。
配列としてアクセスできる。



.. 英語の原文：Vector3
   :ref:`Vector3 <class_Vector3>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   3D vector type containing ``x``, ``y`` and ``z`` fields. This can also
   be accessed as an array.



































:ref:`Transform2D <class_Transform2D>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2D変換に使用される3x2マトリクス。


.. 英語の原文：Transform2D 
   :ref:`Transform2D <class_Transform2D>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      3×2 matrix used for 2D transforms.




































:ref:`Plane <class_Plane>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``normal`` ベクトル場と ``d`` スカラ距離を含む正規化された形式の3D平面型。

.. 英語の原文：Plane
   :ref:`Plane <class_Plane>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   3D Plane type in normalized form that contains a ``normal`` vector field
   and a ``d`` scalar distance.



































:ref:`Quat <class_Quat>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

クォータニオンは、3D回転を表すために使用されるデータ型。
回転の補完に役立つ。


.. 英語の原文：Quat
   :ref:`Quat <class_Quat>`
   ^^^^^^^^^^^^^^^^^^^^^^^^

   Quaternion is a datatype used for representing a 3D rotation. It's
   useful for interpolating rotations.



































:ref:`AABB <class_AABB>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

軸に沿った境界ボックス(または3Dボックス)には、 ``position`` と ``size`` の2つのベクトルフィールドが含まれる。
また、 ``position + size`` である ``end`` 軸を含んでいる。


.. 英語の原文：AABB
   :ref:`AABB <class_AABB>`
   ^^^^^^^^^^^^^^^^^^^^^^^^

   Axis-aligned bounding box (or 3D box) contains 2 vectors fields: ``position``
   and ``size``. Also contains an ``end`` field which is
   ``position + size``.




































:ref:`Basis <class_Basis>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3Dの回転とスケールに使用される3x3マトリクス。
3つのベクタフィールド( ``x`` ・ ``y`` ・ ``z`` )が含まれており、3Dベクタの配列としてアクセスできる。


.. 英語の原文：Basis
   :ref:`Basis <class_Basis>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   3x3 matrix used for 3D rotation and scale. It contains 3 vector fields
   (``x``, ``y`` and ``z``) and can also be accessed as an array of 3D
   vectors.




































:ref:`Transform <class_Transform>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D変換には、基底(Basis)フィールド ``basis`` とVector3フィールド ``origin`` が含まれる。


.. 英語の原文：Transform
   :ref:`Transform <class_Transform>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   3D Transform contains a Basis field ``basis`` and a Vector3 field
   ``origin``.


































エンジンの組み込み型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. 英語の原文：エンジンの組み込み型
   Engine built-in types
   ~~~~~~~~~~~~~~~~~~~~~




































:ref:`Color <class_Color>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

カラーデータ型には、 ``r`` ・ ``g`` ・ ``b`` ・ ``a`` フィールドが含まれている。
また、色相/彩度/値を表す ``h`` ・ ``s`` ・ ``v`` としてアクセスできる。


.. 英語の原文：Color
   :ref:`Color <class_Color>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   Color data type contains ``r``, ``g``, ``b``, and ``a`` fields. It can
   also be accessed as ``h``, ``s``, and ``v`` for hue/saturation/value.




































:ref:`NodePath <class_NodePath>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

主にシーンシステムで使用されるノードへのコンパイル済みPath。
文字列との間で簡単に割り当てることができる。


.. 英語の原文：NodePath
   :ref:`NodePath <class_NodePath>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Compiled path to a node used mainly in the scene system. It can be
   easily assigned to, and from, a String.




































:ref:`RID <class_RID>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

リソースID(RID)。
サーバは、汎用RIDを使用して不透明データを参照する。



.. 英語の原文：RID
   :ref:`RID <class_RID>`
   ^^^^^^^^^^^^^^^^^^^^^^

   Resource ID (RID). Servers use generic RIDs to reference opaque data.




































:ref:`Object <class_Object>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

組み込み型ではない基本クラス。


.. 英語の原文：Object
   :ref:`Object <class_Object>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Base class for anything that is not a built-in type.



































コンテナの組み込み型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. 英語の原文：コンテナの組み込み型
   Container built-in types
   ~~~~~~~~~~~~~~~~~~~~~~~~



































:ref:`Array <class_Array>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

他の配列または辞書を含む、任意のオブジェクト型の一般的なシーケンス。
配列は動的にサイズ変更できる。
配列には ``0`` から始まる添え字が付けられる。
負の添え字は最後から数える。

::

   var arr = []
   arr = [1, 2, 3]
   var b = arr[1] # 変数bには2が代入される。
   var c = arr[arr.size() - 1] # 変数bには3が代入される。
   var d = arr[-1] # 直近処理と同じ結果を導く短縮記法(変数b=3)
   arr[0] = "Hi!" # 値1を"Hi!"に置き換える。
   arr.append(4) # 配列末尾に追加 ["Hi!", 2, 3, 4].

GDScriptの配列は、速度を上げるためにメモリ内で線形に割り当てる。
そのため、大きな配列(数万個以上の要素)がメモリの断片化を引き起こす可能性がある。
これが懸念される場合は、特別な配列型を使う必要がある。
これらは単一のデータ型のみを代入可能にすることで、メモリの断片化を回避し、メモリの使用量を減らす。
しかし、アトミックであり、一般的な配列よりも実行速度が遅くなる。
従い、大規模なデータセットにのみ使用することを勧める。

- :ref:`PoolByteArray <class_PoolByteArray>`: バイト配列(0〜255の整数)
- :ref:`PoolIntArray <class_PoolIntArray>`: 整数配列
- :ref:`PoolRealArray <class_PoolRealArray>`: 浮動小数点数配列
- :ref:`PoolStringArray <class_PoolStringArray>`: 文字列配列
- :ref:`PoolVector2Array <class_PoolVector2Array>`: :ref:`Vector2 <class_Vector2>` 型配列
- :ref:`PoolVector3Array <class_PoolVector3Array>`: :ref:`Vector3 <class_Vector3>` 型配列
- :ref:`PoolColorArray <class_PoolColorArray>`: :ref:`Color <class_Color>` 型配列

.. todo::

   リンクの確認。



.. 英語の原文：Array
   :ref:`Array <class_Array>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   Generic sequence of arbitrary object types, including other arrays or dictionaries (see below).
   The array can resize dynamically. Arrays are indexed starting from index ``0``.
   Negative indices count from the end.

   ::

       var arr = []
       arr = [1, 2, 3]
       var b = arr[1] # This is 2.
       var c = arr[arr.size() - 1] # This is 3.
       var d = arr[-1] # Same as the previous line, but shorter.
       arr[0] = "Hi!" # Replacing value 1 with "Hi!".
       arr.append(4) # Array is now ["Hi!", 2, 3, 4].

   GDScript arrays are allocated linearly in memory for speed.
   Large arrays (more than tens of thousands of elements) may however cause
   memory fragmentation. If this is a concern, special types of
   arrays are available. These only accept a single data type. They avoid memory
   fragmentation and use less memory, but are atomic and tend to run slower than generic
   arrays. They are therefore only recommended to use for large data sets:

   - :ref:`PoolByteArray <class_PoolByteArray>`: An array of bytes (integers from 0 to 255).
   - :ref:`PoolIntArray <class_PoolIntArray>`: An array of integers.
   - :ref:`PoolRealArray <class_PoolRealArray>`: An array of floats.
   - :ref:`PoolStringArray <class_PoolStringArray>`: An array of strings.
   - :ref:`PoolVector2Array <class_PoolVector2Array>`: An array of :ref:`Vector2 <class_Vector2>` objects.
   - :ref:`PoolVector3Array <class_PoolVector3Array>`: An array of :ref:`Vector3 <class_Vector3>` objects.
   - :ref:`PoolColorArray <class_PoolColorArray>`: An array of :ref:`Color <class_Color>` objects.





































:ref:`Dictionary <class_Dictionary>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

一意のキーによって参照される値を含む連想コンテナ

::

   var d = {4: 5, "A key": "A value", 28: [1, 2, 3]}
   d["Hi!"] = 0
   d = {
       22: "value",
       "some_key": 2,
       "other_key": [2, 3, 4],
       "more_key": "Hello"
   }

Luaスタイルのテーブル構文のサポートされている。
Luaスタイルは、 ``:`` の代わりに ``=`` を使い、文字列のキーをマークするために引用符を使用しない(コーディング量が減る)。
ただし、GDScript識別子のように、この形式で記述されたキーは数字で始めることはできない。

::

   var d = {
       test22 = "value",
       some_key = 2,
       other_key = [2, 3, 4],
       more_key = "Hello"
   }

キーを既存の辞書に追加するには、既存のキーのようにキーにアクセスして割り当てる。

::

   var d = {} # 空の辞書を作成する。
   d.waiting = 14 # 文字列 "waiting" をキーとして追加し、14の値を割り当てる。
   d[4] = "hello" # 整数14の値をキーとして追加し、 "hello" の文字列を割り当てる。
   d["Godot"] = 3.01 # 文字列 "Godot" をキーとして追加し、3.01の値を割り当てる。



.. 英語の原文：Dictionary
   :ref:`Dictionary <class_Dictionary>`
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Associative container which contains values referenced by unique keys.

   ::

       var d = {4: 5, "A key": "A value", 28: [1, 2, 3]}
       d["Hi!"] = 0
       d = {
           22: "value",
           "some_key": 2,
           "other_key": [2, 3, 4],
           "more_key": "Hello"
       }

   Lua-style table syntax is also supported. Lua-style uses ``=`` instead of ``:``
   and doesn't use quotes to mark string keys (making for slightly less to write).
   Note however that like any GDScript identifier, keys written in this form cannot
   start with a digit.

   ::

       var d = {
           test22 = "value",
           some_key = 2,
           other_key = [2, 3, 4],
           more_key = "Hello"
       }

   To add a key to an existing dictionary, access it like an existing key and
   assign to it::

       var d = {} # Create an empty Dictionary.
       d.waiting = 14 # Add String "waiting" as a key and assign the value 14 to it.
       d[4] = "hello" # Add integer 4 as a key and assign the String "hello" as its value.
       d["Godot"] = 3.01 # Add String "Godot" as a key and assign the value 3.01 to it.




































データ
------------

.. 英語の原文：データ
   Data
   ----


































変数
~~~~~~~~~~~~

変数は、クラスメンバまたは関数のローカルとして存在する。
それらは ``var`` キーワードで作成され、オプションで初期化時に値を割り当てることができる。

::

   var a # Data type is 'null' by default.
   var b = 5
   var c = 3.8
   var d = b + c # 変数は、常に順番に初期化される。

変数には、オプションで型指定を含めることができる。
型が指定された場合、変数は常に同じ型を持つことが強制され、異なる型の代入時にエラーを発生させる。

型は、変数名の後ろに ``:(コロン)`` 記号を使用して変数宣言で指定し、その後に型を続ける。

::

   var my_vector2: Vector2
   var my_node: Node = Sprite.new()

変数が宣言内で初期化されている場合、型を推測できるため、型名を省略できる。

::

   var my_vector2 := Vector2() # 'my_vector2' is of type 'Vector2'
   var my_node := Sprite.new() # 'my_node' is of type 'Sprite'

型の推論は、割り当てられた値に定義された型がある場合のみ可能になる。
そうでない場合、エラーが発生する。

以下、有効な型を示す。

- 組み込み型（Array, Vector2, int, String, etc.）
- エンジンクラス（Node, Resource, Reference, etc.）
- 定数にスクリプトリソースが含まれる場合（ ``const MyScript = preload("res://my_script.gd")`` を宣言した場合は ``MyScript`` ）
- 同じスクリプト内の他のクラス・スコープ（ 同じスコープ内の ``class InnerClass`` 内で ``class NestedClass`` を宣言した場合は ``InnerClass.NestedClass`` ）
- ``class_name`` キーワードで宣言されたスクリプトクラス





.. 英語の原文：変数
   Variables
   ~~~~~~~~~

   Variables can exist as class members or local to functions. They are
   created with the ``var`` keyword and may, optionally, be assigned a
   value upon initialization.

   ::

       var a # Data type is 'null' by default.
       var b = 5
       var c = 3.8
       var d = b + c # Variables are always initialized in order.

   Variables can optionally have a type specification. When a type is specified,
   the variable will be forced to have always that same type, and trying to assign
   an incompatible value will raise an error.

   Types are specified in the variable declaration using a ``:`` (colon) symbol
   after the variable name, followed by the type.

   ::

       var my_vector2: Vector2
       var my_node: Node = Sprite.new()

   If the variable is initialized within the declaration, the type can be inferred, so
   it's possible to omit the type name::

       var my_vector2 := Vector2() # 'my_vector2' is of type 'Vector2'
       var my_node := Sprite.new() # 'my_node' is of type 'Sprite'

   Type inference is only possible if the assigned value has a defined type, otherwise
   it will raise an error.

   Valid types are:

   - Built-in types (Array, Vector2, int, String, etc.).
   - Engine classes (Node, Resource, Reference, etc.).
   - Constant names if they contain a script resource (``MyScript`` if you declared ``const MyScript = preload("res://my_script.gd")``).
   - Other classes in the same script, respecting scope (``InnerClass.NestedClass`` if you declared ``class NestedClass`` inside the ``class InnerClass`` in the same scope).
   - Script classes declared with the ``class_name`` keyword.



































キャスティング
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

肩付き変数に割り当てる値には、互換性のある型を必要とする。
特定の型、特にオブジェクト型の値を強制する場合は、 キャスト演算子 ``as`` を使う。

オブジェクト型間でキャストした場合、値が同じ型またはキャスト型のサブタイプは、同じオブジェクトになる。

::

   var my_node2D: Node2D
   my_node2D = $Sprite as Node2D # SpriteはNode2Dのサブタイプであるため機能する。

値がサブタイプでない場合、キャスト操作は ``null`` 値になる。

::

   var my_node2D: Node2D
   my_node2D = $Button as Node2D # ButtonはNode2Dのサブタイプでは無いため、 'null' になる。

組み込み型の場合、可能な場合は強制的に変換される。
そうでない場合、エンジンはエラーを発生させる。

::

   var my_int: int
   my_int = "123" as int # 文字列はintに変換できる。
   my_int = Vector2() as int # Vector2はintに変換できない。そのためエラーになる。

キャストは、シーンツリーとのやりとりに、タイプセーフな変数を改善するのにも役立つ。

::

   # 変数がSprite型であると推測する。
   var my_sprite := $Character as Sprite

   # $AnimPlayerがAnimationPlayerでない場合は、メソッド 'play()' があっても失敗する。
   ($AnimPlayer as AnimationPlayer).play("walk")





.. 英語の原文：キャスティング
   Casting
   ^^^^^^^

   Values assigned to typed variables must have a compatible type. If it's needed to
   coerce a value to be of a certain type, in particular for object types, you can
   use the casting operator ``as``.

   Casting between object types results in the same object if the value is of the
   same type or a subtype of the cast type.

   ::

       var my_node2D: Node2D
       my_node2D = $Sprite as Node2D # Works since Sprite is a subtype of Node2D

   If the value is not a subtype, the casting operation will result in a ``null`` value.

   ::

       var my_node2D: Node2D
       my_node2D = $Button as Node2D # Results in 'null' since a Button is not a subtype of Node2D

   For built-in types, they will be forcibly converted if possible, otherwise the
   engine will raise an error.

   ::

       var my_int: int
       my_int = "123" as int # The string can be converted to int
       my_int = Vector2() as int # A Vector2 can't be converted to int, this will cause an error

   Casting is also useful to have better type-safe variables when interacting with
   the scene tree::

       # Will infer the variable to be of type Sprite.
       var my_sprite := $Character as Sprite

       # Will fail if $AnimPlayer is not an AnimationPlayer, even if it has the method 'play()'.
       ($AnimPlayer as AnimationPlayer).play("walk")

































定数
~~~~~~~~~~~~

定数は変数に似ているが、定数または定数式で無ければならず、初期化時に割り当てる必要がある。

::

   const A = 5
   const B = Vector2(20, 20)
   const C = 10 + 20 # 定数式
   const D = Vector2(20, 30).x # 定数式：20
   const E = [1, 2, 3, 4][0] # 定数式：1
   const F = sin(20) # 'sin()' は定数式で使用できる。
   const G = x + 20 # 無効； 定数式ではない。
   const H = A + 20 # 定数式：25

定数の型は割り当てられた値から推測されるが、明示的な型指定が可能になっている。

::

   const A: int = 5
   const B: Vector2 = Vector2()

互換性の内方の値を割り当てた場合、エラーが発生する。



.. 英語の原文：定数
   Constants
   ~~~~~~~~~

   Constants are similar to variables, but must be constants or constant
   expressions and must be assigned on initialization.

   ::

       const A = 5
       const B = Vector2(20, 20)
       const C = 10 + 20 # Constant expression.
       const D = Vector2(20, 30).x # Constant expression: 20.
       const E = [1, 2, 3, 4][0] # Constant expression: 1.
       const F = sin(20) # 'sin()' can be used in constant expressions.
       const G = x + 20 # Invalid; this is not a constant expression!
       const H = A + 20 # Constant expression: 25.

   Although the type of constants is inferred from the assigned value, it's also
   possible to add explicit type specification::

       const A: int = 5
       const B: Vector2 = Vector2()

   Assigning a value of an incompatible type will raise an error.



































列挙型(Enums)
^^^^^^^^^^^^^^^^^^^^^^^^^^

列挙型は基本的に定数の短縮形であり、定数に連続した整数を割り当てたい場合に、非常に便利だ。

enumに名前を渡したとき、すべてのキーがその名前の定数辞書内に配置される。

.. important::

   Godot 3.1以降では、名前付き列挙型のキーはグローバル定数として登録されない。
   列挙の名前( ``Name.KEY`` )を前に付けてアクセスする必要がある。
   以下の例を参照すること。

::

   enum {TILE_BRICK, TILE_FLOOR, TILE_SPIKE, TILE_TELEPORT}
   # 上記のenumは、下記の宣言と同じ。
   const TILE_BRICK = 0
   const TILE_FLOOR = 1
   const TILE_SPIKE = 2
   const TILE_TELEPORT = 3

   enum State {STATE_IDLE, STATE_JUMP = 5, STATE_SHOOT}
   # 上記のenumは、下記の宣言と同じ。
   const State = {STATE_IDLE = 0, STATE_JUMP = 5, STATE_SHOOT = 6}
   # State.STATE_IDLEなどで値にアクセスする, etc.



.. 英語の原文：列挙型(Enums)
   Enums
   ^^^^^

   Enums are basically a shorthand for constants, and are pretty useful if you
   want to assign consecutive integers to some constant.

   If you pass a name to the enum, it will put all the keys inside a constant
   dictionary of that name.

   .. important: In Godot 3.1 and later, keys in a named enum are not registered
                 as global constants. They should be accessed prefixed by the
                 enum's name (``Name.KEY``); see an example below.

   ::

       enum {TILE_BRICK, TILE_FLOOR, TILE_SPIKE, TILE_TELEPORT}
       # Is the same as:
       const TILE_BRICK = 0
       const TILE_FLOOR = 1
       const TILE_SPIKE = 2
       const TILE_TELEPORT = 3

       enum State {STATE_IDLE, STATE_JUMP = 5, STATE_SHOOT}
       # Is the same as:
       const State = {STATE_IDLE = 0, STATE_JUMP = 5, STATE_SHOOT = 6}
       # Access values with State.STATE_IDLE, etc.




































関数(Functions)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関数は常に `class <Classes_>`_ に属する。
変数look-upのスコープ優先順位は、ローカル⇒クラスメンバ⇒グローバルの順だ。
``self`` 変数は常に利用可能であり、クラスメンバにアクセスするためのオプションとして提供されるが、必ずしも必要ではない(Pythonとは異なり、関数の最初の引数として送信 *すべきではない* )。

.. todo::

   リンクの確認。


::

   func my_function(a, b):
       print(a)
       print(b)
       return a + b  # 戻り値は任意の存在だ。付けなければ 'null' を返す。

関数は、いつでも ``return`` 可能になっている。
初期設定の戻り値は、 ``null`` 。

関数には、引数及び戻り値の型指定を含めることができる。
引数の型は、変数に同様の方法で追加できる。

::

   func my_function(a: int, b: String):
       pass

関数の引数にデフォルト値がある場合、型を推測する。

::

   func my_function(int_arg := 42, String_arg := "string"):
       pass

関数の戻り値の型は、矢印トークン( ``->`` )を使用して、引数リストの後に指定する。

::

   func my_int_function() -> int:
       return 0

戻り値の型が **must** の関数は、適切な値を返す。
型を ``void`` に設定した場合、関数は何も返さないことを意味する。
Void関数は ``return`` でその関数から抜けられるが、値を返すことはできない。

::

   void_function() -> void:
       return # 値は返せない。

.. note:: 

   非Void関数は、 **常に** 値を返す必要があるため、コードに分岐ステートメント( ``if`` / ``else`` コンストラクトなど)がある場合、すべての可能な分岐点に戻り値が必要になる。
   例えば、 ``if`` ブロック内に ``return`` があり、その後にない場合、そしてそのブロック内に処理が走らなければ、関数は有効な値を返さないため、エディタはエラーを発生させる。


.. 英語の原文：関数(Functions)
   Functions
   ~~~~~~~~~

   Functions always belong to a `class <Classes_>`_. The scope priority for
   variable look-up is: local → class member → global. The ``self`` variable is
   always available and is provided as an option for accessing class members, but
   is not always required (and should *not* be sent as the function's first
   argument, unlike Python).

   ::

       func my_function(a, b):
           print(a)
           print(b)
           return a + b  # Return is optional; without it 'null' is returned.

   A function can ``return`` at any point. The default return value is ``null``.

   Functions can also have type specification for the arguments and for the return
   value. Types for arguments can be added in a similar way to variables::

       func my_function(a: int, b: String):
           pass

   If a function argument has a default value, it's possible to infer the type::

       func my_function(int_arg := 42, String_arg := "string"):
           pass

   The return type of the function can be specified after the arguments list using
   the arrow token (``->``)::

       func my_int_function() -> int:
           return 0

   Functions that have a return type **must** return a proper value. Setting the
   type as ``void`` means the function doesn't return anything. Void functions can
   return early with the ``return`` keyword, but they can't return any value.

   ::

       void_function() -> void:
           return # Can't return a value

   .. note:: Non-void functions must **always** return a value, so if your code has
             branching statements (such as an ``if``/``else`` construct), all the
             possible paths must have a return. E.g., if you have a ``return``
             inside an ``if`` block but not after it, the editor will raise an
             error because if the block is not executed, the function won't have a
             valid value to return.


































参照関数(Referencing functions)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pythonとは異なり、関数はGDScriptのファーストクラスオブジェクトでは **ない** 。
つまり、変数への保存や引数として別に関数に渡すことや他の関数から戻してもらうことはできない。
これは性能上の理由による。

訳者：そもそも参照関数とは何？
Pythonで調べても出てこないぞ!?

実行時に関数を名前で参照するには(例えば、変数に保存・引数として別の関数に渡すなど)、 ``call`` または ``funcref`` ヘルパーを使う必要がある。

::

   # 名前で関数を呼ぶのに1行記述をする。
   my_node.call("my_function", args)

   # 参照関数を保存する。
   var my_func = funcref(my_node, "my_function")
   # 保存した参照関数を呼び出す。
   my_func.call_func(args)


.. 英語の原文：参照関数(Referencing functions)
   Referencing functions
   ^^^^^^^^^^^^^^^^^^^^^

   Contrary to Python, functions are *not* first-class objects in GDScript. This
   means they cannot be stored in variables, passed as an argument to another
   function or be returned from other functions. This is for performance reasons.

   To reference a function by name at run-time, (e.g. to store it in a variable, or
   pass it to another function as an argument) one must use the ``call`` or
   ``funcref`` helpers::

       # Call a function by name in one step.
       my_node.call("my_function", args)

       # Store a function reference.
       var my_func = funcref(my_node, "my_function")
       # Call stored function reference.
       my_func.call_func(args)



































静的関数(Static functions)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

関数は静的に宣言できる。
関数が静的な場合、インスタンスメンバ変数または ``self`` にアクセスできない。
これは主にヘルパー関数のライブラリを作成するのに便利になる。

::

   static func sum2(a, b):
       return a + b




.. 英語の原文：静的関数(Static functions)
   Static functions
   ^^^^^^^^^^^^^^^^

   A function can be declared static. When a function is static, it has no
   access to the instance member variables or ``self``. This is mainly
   useful to make libraries of helper functions::

       static func sum2(a, b):
           return a + b



































ステートメントと制御フロー
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ステートメントは標準であり、割り当て・関数呼び出し・制御フロー制御などにできる(以下を参照)。
ステートメントセパレータとしての ``;`` は完全にオプションになる。


.. 英語の原文：ステートメントと制御フロー
   Statements and control flow
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Statements are standard and can be assignments, function calls, control
   flow structures, etc (see below). ``;`` as a statement separator is
   entirely optional.


































if/else/elif
^^^^^^^^^^^^^^^^^^^^^^^^

単純条件ならば、 ``if`` / ``else`` / ``elif`` 構文の利用でまかなえる。
条件を囲む括弧は利用可能だが、必須ではない。
タブインデントの性質上、インデントを揃えるために、 ``else``/``if`` の代わりに、 ``elif`` の利用が望ましいだろう。

::

   if [expression]:
       statement(s)
   elif [expression]:
       statement(s)
   else:
       statement(s)

短いステートメントは、条件と同じ行に記述できる。

::

   if 1 + 1 == 2: return 2 + 2
   else:
       var x = 3 + 3
       return x

場合により、Bool式に基づき、異なる初期値の割り当てが可能になっている。
この場合は、三項if式が便利だろう。

::

   var x = [value] if [expression] else [value]
   y += 3 if y < 10 else -1



.. 英語の原文：if/else/elif
   if/else/elif
   ^^^^^^^^^^^^

   Simple conditions are created by using the ``if``/``else``/``elif`` syntax.
   Parenthesis around conditions are allowed, but not required. Given the
   nature of the tab-based indentation, ``elif`` can be used instead of
   ``else``/``if`` to maintain a level of indentation.

   ::

       if [expression]:
           statement(s)
       elif [expression]:
           statement(s)
       else:
           statement(s)

   Short statements can be written on the same line as the condition::

       if 1 + 1 == 2: return 2 + 2
       else:
           var x = 3 + 3
           return x

   Sometimes, you might want to assign a different initial value based on a
   boolean expression. In this case, ternary-if expressions come in handy::

       var x = [value] if [expression] else [value]
       y += 3 if y < 10 else -1




































while
^^^^^^^^^^

単純ループ(繰り返し)は、 ``while`` 構文の利用でこなせる。
ループは、 ``break`` で処理を中断するか、 ``continue`` で処理を継続できる。

::

   while [expression]:
       statement(s)


.. 英語の原文：while
   while
   ^^^^^

   Simple loops are created by using ``while`` syntax. Loops can be broken
   using ``break`` or continued using ``continue``:

   ::

       while [expression]:
           statement(s)




































for
^^^^^^^^^

配列やテーブルなどの範囲を反復処理するには、 *for* ループを使用する。
配列を反復処理させた場合、現在の配列要素がループ変数に格納される。
辞書を反復処理する場合、 *index* はループ変数に保存される。

::

   for x in [5, 7, 11]:
       statement # Loop iterates 3 times with 'x' as 5, then 7 and finally 11.

   var dict = {"a": 0, "b": 1, "c": 2}
   for i in dict:
       print(dict[i]) # Prints 0, then 1, then 2.

   for i in range(3):
       statement # Similar to [0, 1, 2] but does not allocate an array.

   for i in range(1, 3):
       statement # Similar to [1, 2] but does not allocate an array.

   for i in range(2, 8, 2):
       statement # Similar to [2, 4, 6] but does not allocate an array.

   for c in "Hello":
       print(c) # Iterate through all characters in a String, print every letter on new line.

   for i in 3:
       statement # Similar to range(3)

   for i in 2.2:
       statement # Similar to range(ceil(2.2))



.. 英語の原文：for
   for
   ^^^

   To iterate through a range, such as an array or table, a *for* loop is
   used. When iterating over an array, the current array element is stored in
   the loop variable. When iterating over a dictionary, the *index* is stored
   in the loop variable.

   ::

       for x in [5, 7, 11]:
           statement # Loop iterates 3 times with 'x' as 5, then 7 and finally 11.

       var dict = {"a": 0, "b": 1, "c": 2}
       for i in dict:
           print(dict[i]) # Prints 0, then 1, then 2.

       for i in range(3):
           statement # Similar to [0, 1, 2] but does not allocate an array.

       for i in range(1, 3):
           statement # Similar to [1, 2] but does not allocate an array.

       for i in range(2, 8, 2):
           statement # Similar to [2, 4, 6] but does not allocate an array.

       for c in "Hello":
           print(c) # Iterate through all characters in a String, print every letter on new line.

       for i in 3:
           statement # Similar to range(3)

       for i in 2.2:
           statement # Similar to range(ceil(2.2))
































matchと言うなのswitch-case文
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``match`` ステートメントは、プログラムの実行を分岐するために使用される。
他の多くの言語で見られる ``switch`` ステートメントに相当するが、いくつかの追加機能を追加している。

訳者：機能追加したからと言う理由で名前を変えるのは止めて欲しい。
パターンマッチ演算子などの正規表現関係かと思ったぞ。
その割に、以下説明のC言語のようなフォールスルー記述ができ、バグを生みやすくなる(簡潔に記述できるのも確かだが)。


以下、基本構文

::

   match [expression]:
       [pattern](s):
           [block]
       [pattern](s):
           [block]
       [pattern](s):
           [block]

**以下switchステートメントオタク向けの価値観破壊手順**

1. ``switch`` を ``match`` に置き換える。
2. ``case`` を削除する。
3. ``break`` を削除する。
   デフォルトで ``break`` したくない場合は、フォールスルーに ``continue`` を使用する。
4. ``default`` を単一のアンダースコアに変更する(下記の6パターン内で説明)。

**以下、制御フロー**

patternは上から下に一致する(switch-case文そのものの挙動)。
patternが一致した場合、対応ブロックが実行される(switch-case文で言えば、caseの挙動の説明)。
その後、実行は ``match`` ステートメントの下で実行される。
フォールスルーが必要な場合は、 ``continue`` を使用して現在のブロックで実行を停止し、その下のブロックをチェックできる(訳者：どういう意味？)。

以下、6つのパターンタイプがある。

- 一定パターン
    数字や文字列などの定数プリミティブ

    ::

    match x:
        1:
            print("We are number one!")
        2:
            print("Two are better than one!")
        "test":
            print("Oh snap! It's a string!")

- 可変パターン
    変数/列挙型の内容に一致する。

    ::

    match typeof(x):
        TYPE_REAL:
            print("float")
        TYPE_STRING:
            print("text")
        TYPE_ARRAY:
            print("array")

- ワイルドカードパターン(グログや正規表現 **ではない** )
    このパターンはすべてに一致する。
    単一のアンダースコアとして書かれている。

    他言語の ``switch`` ステートメントの ``default`` に相当使用ができる。

    ::

    match x:
        1:
            print("It's one!")
        2:
            print("It's one times two!")
        _:
            print("It's not 1 or 2. I don't care to be honest.")

- バインディングパターン
    新しい変数名を用いて、ワイルドカードパーンと同様に、すべてに一致する。
    特に、配列と辞書に対して役立つ。

    ::

    match x:
        1:
            print("It's one!")
        2:
            print("It's one times two!")
        var new_var:
            print("It's not 1 or 2, it's ", new_var)

- 配列パターン
    配列に一致する。
    すべての要素は、パターンそのものなので、ネストできる。

    配列の長さは最初に試され、パターンと同じサイズで無ければならない。
    異なる場合は、パターンに一致しない。

    **オープンエンド配列** ： 最後のサブパターン ``..`` を作成することにより、配列をパターンより大きくすることができる。

    すべてのサブパターンはコンマで区切る必要がある。

    ::

    match x:
        []:
            print("Empty array")
        [1, 3, "test", null]:
            print("非常に特殊な配列")
        [var start, _, "test"]:
            print("最初の要素は", start, ", そして、最後の要素は \"test\"")
        [42, ..]:
            print("オープンエンド配列")

- 辞書パターン
    配列パターンと同様に機能する。
    すべてのキーは一定のパターンで無ければならない。

    辞書の長さは最初に試され、パターンと同じサイズで無ければならない。
    異なる場合は、パターンに一致しない。

    **オープンエンド辞書** ： 最後のサブパターン ``..`` を作成することにより、辞書をパターンより大きくすることができる。

    すべてのサブパターンはコンマで区切る必要がある。

    値を指定しない場合、キーの存在のみがチェックされる。

    値パターンは、キーパターンと ``:`` で区切られる。

    ::

    match x:
        {}:
            print("空の辞書")
        {"name": "Dennis"}:
            print("nameはDennis")
        {"name": "Dennis", "age": var age}:
            print("Dennisは", age, "歳だ。")
        {"name", "age"}:
            print("名前と年齢はあるがDennisではないorz")
        {"key": "godotisawesome", ..}:
            print("1つのエントリのみをチェックし、残りを無視した。")

- 複数パターン
    複数のパターンをコンマ区切りで指定が可能。
    これらのパターンには、バインディングを含めることはできない。

    ::

    match x:
        1, 2, 3:
            print("It's 1 - 3")
        "Sword", "Splash potion", "Fist":
            print("Yep, you've taken damage")






.. 英語の原文：matchと言うなのswitch-case文
   match
   ^^^^^

   A ``match`` statement is used to branch execution of a program.
   It's the equivalent of the ``switch`` statement found in many other languages, but offers some additional features.

   Basic syntax::

       match [expression]:
           [pattern](s):
               [block]
           [pattern](s):
               [block]
           [pattern](s):
               [block]


   **Crash-course for people who are familiar with switch statements**:

   1. Replace ``switch`` with ``match``.
   2. Remove ``case``.
   3. Remove any ``break``\ s. If you don't want to ``break`` by default, you can use ``continue`` for a fallthrough.
   4. Change ``default`` to a single underscore.


   **Control flow**:

   The patterns are matched from top to bottom.
   If a pattern matches, the corresponding block will be executed. After that, the execution continues below the ``match`` statement.
   If you want to have a fallthrough, you can use ``continue`` to stop execution in the current block and check the ones below it.

   There are 6 pattern types:

   - Constant pattern
       Constant primitives, like numbers and strings::

           match x:
               1:
                   print("We are number one!")
               2:
                   print("Two are better than one!")
               "test":
                   print("Oh snap! It's a string!")


   - Variable pattern
       Matches the contents of a variable/enum::

           match typeof(x):
               TYPE_REAL:
                   print("float")
               TYPE_STRING:
                   print("text")
               TYPE_ARRAY:
                   print("array")


   - Wildcard pattern
       This pattern matches everything. It's written as a single underscore.

       It can be used as the equivalent of the ``default`` in a ``switch`` statement in other languages::

           match x:
               1:
                   print("It's one!")
               2:
                   print("It's one times two!")
               _:
                   print("It's not 1 or 2. I don't care to be honest.")


   - Binding pattern
       A binding pattern introduces a new variable. Like the wildcard pattern, it matches everything - and also gives that value a name.
       It's especially useful in array and dictionary patterns::

           match x:
               1:
                   print("It's one!")
               2:
                   print("It's one times two!")
               var new_var:
                   print("It's not 1 or 2, it's ", new_var)


   - Array pattern
       Matches an array. Every single element of the array pattern is a pattern itself, so you can nest them.

       The length of the array is tested first, it has to be the same size as the pattern, otherwise the pattern doesn't match.

       **Open-ended array**: An array can be bigger than the pattern by making the last subpattern ``..``.

       Every subpattern has to be comma-separated.

       ::

           match x:
               []:
                   print("Empty array")
               [1, 3, "test", null]:
                   print("Very specific array")
               [var start, _, "test"]:
                   print("First element is ", start, ", and the last is \"test\"")
               [42, ..]:
                   print("Open ended array")

   - Dictionary pattern
       Works in the same way as the array pattern. Every key has to be a constant pattern.

       The size of the dictionary is tested first, it has to be the same size as the pattern, otherwise the pattern doesn't match.

       **Open-ended dictionary**: A dictionary can be bigger than the pattern by making the last subpattern ``..``.

       Every subpattern has to be comma separated.

       If you don't specify a value, then only the existence of the key is checked.

       A value pattern is separated from the key pattern with a ``:``.

       ::

           match x:
               {}:
                   print("Empty dict")
               {"name": "Dennis"}:
                   print("The name is Dennis")
               {"name": "Dennis", "age": var age}:
                   print("Dennis is ", age, " years old.")
               {"name", "age"}:
                   print("Has a name and an age, but it's not Dennis :(")
               {"key": "godotisawesome", ..}:
                   print("I only checked for one entry and ignored the rest")

   - Multiple patterns
       You can also specify multiple patterns separated by a comma. These patterns aren't allowed to have any bindings in them.

       ::

           match x:
               1, 2, 3:
                   print("It's 1 - 3")
               "Sword", "Splash potion", "Fist":
                   print("Yep, you've taken damage")



































クラス
~~~~~~~~~~~~

初期設定では、すべてのスクリプトファイルは名前のないクラスに相当する。
この場合、相対パスまたは絶対パスのいずれかを使用して、ファイルのパスを使用してのみ参照できる。
例えば、スクリプトファイルに ``character.gd`` と言う名前を付けた場合、以下のプログラムになる。

::

   # Character.gdから継承

   extends res://path/to/character.gd

   # character.gdを読み込み、そこから新しいノードインスタンスを作成する。

   var Character = load("res://path/to/character.gd")
   var character_node = Character.new()

代わりに、クラスに名前を付け、Godotエディタで新しい型として登録できる。
そのためには、 ``class_name`` キーワードを使用する。
オプションのカンマの後ろに画像へのPathを追加して、アイコンとして使用できる。
エディタに、新しいアイコンのクラスが表示される。

::

   # Item.gd

   extends Node

   class_name Item, "res://interface/icons/item.png"

.. image:: img/class_name_editor_register_example.png

クラスファイルの例を次に示す。

::

   # Saved as a file named 'character.gd'.

   class_name Character

   var health = 5

   func print_health():
       print(health)

   func print_this_script_three_times():
       print(get_script())
       print(ResourceLoader.load("res://character.gd"))
       print(Character)

.. note:: 

   Godotのクラス構文は小さくまとまっている。
   メンバ変数または関数のみを含めることができる。
   静的関数を使用できるが、静的メンバ変数は使用できない。
   同様に、インスタンスを作成するたびにエンジンは変数を初期化する。
   これには配列と辞書が含まれる。
   これは、ユーザが知らなくてもスクリプトを個別のスレッドで初期化できるため、スレッドセーフの精神に基づいて動く。


.. 英語の原文：クラス
   Classes
   ~~~~~~~

   By default, all script files are unnamed classes. In this case, you can only
   reference them using the file's path, using either a relative or an absolute
   path. For example, if you name a script file ``character.gd``::

      # Inherit from Character.gd

      extends res://path/to/character.gd

      # Load character.gd and create a new node instance from it

      var Character = load("res://path/to/character.gd")
      var character_node = Character.new()

   Instead, you can give your class a name to register it as a new type in Godot's
   editor. For that, you use the ``class_name`` keyword. You can add an
   optional comma followed by a path to an image, to use it as an icon. Your class
   will then appear with its new icon in the editor::

      # Item.gd

      extends Node

      class_name Item, "res://interface/icons/item.png"

   .. image:: img/class_name_editor_register_example.png

   Here's a class file example:

   ::

       # Saved as a file named 'character.gd'.

       class_name Character

       var health = 5

       func print_health():
           print(health)

       func print_this_script_three_times():
           print(get_script())
           print(ResourceLoader.load("res://character.gd"))
           print(Character)


   .. note:: Godot's class syntax is compact: it can only contain member variables or
             functions. You can use static functions, but not static member variables. In the
             same way, the engine initializes variables every time you create an instance,
             and this includes arrays and dictionaries. This is in the spirit of thread
             safety, since scripts can be initialized in separate threads without the user
             knowing.



































継承
^^^^^^^^^^^^

クラス(ファイルそのもの)は、以下から継承できる。

- グローバルクラス。
- 別クラスファイル
- 別クラスファイル内の内部クラス

多重継承は許可されていない。

継承は ``extends`` キーワードを使用する。

::

   # グローバルクラスを継承/拡張する。
   extends SomeClass

   # 別クラスファイルを継承/拡張する。
   extends "somefile.gd"

   # 別クラスファイルの内部クラスを継承/拡張する。
   extends "somefile.gd".SomeInnerClass

特定のインスタンスが特定のクラスを継承しているかどうかを確認するには、 ``is`` キーワードを使用する。

::

   # Cache the enemy class.
   const Enemy = preload("enemy.gd")

   # [...]

   # Use 'is' to check inheritance.
   if (entity is Enemy):
       entity.apply_damage()

*親クラス* (要は、現在のクラスの ``extend`` )の関数を呼び出すには、関数名の前に ``.`` を追加する。

::

   .base_func(args)

これは、拡張クラスの関数が親クラスの同じ名前の関数を置き換えるため、特に役立つ。
そして、それらを呼び出す場合は、接頭辞に ``.`` を付ける
(他の言語で言えば、 ``super`` キーワードのこと)。

::

   func some_func(x):
       .some_func(x) # Calls the same function on the parent class.

.. note:: 

   ``_init`` などのデフォルト関数および ``_enter_tree`` ・ ``_exit_tree`` ・ ``_process`` ・ ``_physics_process`` などのほとんどの通知は、すべての親クラスで自動呼び出しされる。
   それらをオーバーロードするときにそれらを明示的に呼び出す必要は無い。






.. 英語の原文：継承
   Inheritance
   ^^^^^^^^^^^

   A class (stored as a file) can inherit from:

   - A global class.
   - Another class file.
   - An inner class inside another class file.

   Multiple inheritance is not allowed.

   Inheritance uses the ``extends`` keyword::

       # Inherit/extend a globally available class.
       extends SomeClass

       # Inherit/extend a named class file.
       extends "somefile.gd"

       # Inherit/extend an inner class in another file.
       extends "somefile.gd".SomeInnerClass


   To check if a given instance inherits from a given class,
   the ``is`` keyword can be used::

       # Cache the enemy class.
       const Enemy = preload("enemy.gd")

       # [...]

       # Use 'is' to check inheritance.
       if (entity is Enemy):
           entity.apply_damage()

   To call a function in a *parent class* (i.e. one ``extend``-ed in your current
   class), prepend ``.`` to the function name::

       .base_func(args)

   This is especially useful because functions in extending classes replace
   functions with the same name in their parent classes. If you still want to
   call them, you can prefix them with ``.`` (like the ``super`` keyword
   in other languages)::

       func some_func(x):
           .some_func(x) # Calls the same function on the parent class.

   .. note:: Default functions like  ``_init``, and most notifications such as
             ``_enter_tree``, ``_exit_tree``, ``_process``, ``_physics_process``,
             etc. are called in all parent classes automatically.
             There is no need to call them explicitly when overloading them.



































クラスコンストラクタ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

クラスのインスタンス化で呼び出されるクラスコンストラクタの名前は ``_init`` になっている。
前述のように、親クラスのコンストラクタは、クラスを継承するときに自動呼び出しされる。
そのため、通常は ``._init()`` を明示呼び出し不要だ。

上記の ``.some_func`` の例のような通常の関数呼び出しとは異なり、継承されたクラスのコンストラクタが引数を取る場合、次のように渡される。

::

   func _init(args).(parent_args):
       pass

これは例を交えて詳細に説明する。

::

   # State.gd (継承クラス)
   var entity = null
   var message = null

   func _init(e=null):
       entity = e

   func enter(m):
       message = m


   # Idle.gd (継承クラス)
   extends "State.gd"

   func _init(e=null, m=null).(e):
       # 'e' で何かをする。
       message = m

留意すべきことがある。

1. 継承クラス( ``State.gd`` )が引数(この場合は ``e`` )を取る ``_init`` コンストラクタを定義している場合、継承クラス( ``Idle.gd`` ) *同様* に ``_init`` を定義し、``State.gd`` から ``_init`` に適切な引数を渡す必要がある。
2. ``Idle.gd`` は、親クラス ``State.gd`` とは異なる数の引数を持つことができる。
3. 上記の例では、 ``State.gd`` コンストラクタに渡される ``e`` は、 ``Idle.gd`` に渡される ``e`` と同じ。
4. ``Idle.gd`` の ``_init`` コンストラクタが0個の引数を取る場合、何もしなくても ``State.gd`` 親クラスに値を渡す必要がある。
   これにより、変数だけでなく、ベースコンストラクタでもリテラルを渡すことができる(以下、例)。

   ::

   # Idle.gd

   func _init().(5):
       pass



.. 英語の原文：クラスコンストラクタ
   Class Constructor
   ^^^^^^^^^^^^^^^^^

   The class constructor, called on class instantiation, is named ``_init``. As
   mentioned earlier, the constructors of parent classes are called automatically
   when inheriting a class. So, there is usually no need to call ``._init()``
   explicitly.

   Unlike the call of a regular function, like in the above example with
   ``.some_func``, if the constructor from the inherited class takes arguments,
   they are passed like this::

       func _init(args).(parent_args):
          pass

   This is better explained through examples. Consider this scenario::

       # State.gd (inherited class)
       var entity = null
       var message = null

       func _init(e=null):
           entity = e

       func enter(m):
           message = m


       # Idle.gd (inheriting class)
       extends "State.gd"

       func _init(e=null, m=null).(e):
           # Do something with 'e'.
           message = m

   There are a few things to keep in mind here:

   1. If the inherited class (``State.gd``) defines a ``_init`` constructor that takes
      arguments (``e`` in this case), then the inheriting class (``Idle.gd``) *must*
      define ``_init`` as well and pass appropriate parameters to ``_init`` from ``State.gd``.
   2. ``Idle.gd`` can have a different number of arguments than the parent class ``State.gd``.
   3. In the example above, ``e`` passed to the ``State.gd`` constructor is the same ``e`` passed
      in to ``Idle.gd``.
   4. If ``Idle.gd``'s ``_init`` constructor takes 0 arguments, it still needs to pass some value
      to the ``State.gd`` parent class, even if it does nothing. This brings us to the fact that you
      can pass literals in the base constructor as well, not just variables. eg.::

       # Idle.gd

       func _init().(5):
           pass




































内部クラス
^^^^^^^^^^^^^^^^^^^^

クラスファイルには内部クラスを含めることができる。
内部クラスは ``class`` キーワードを使用して定義される。
それらは ``ClassName.new()`` 関数を使用してインスタンス化される。

::

   # クラスファイル内

   # このクラスファイルの内部クラス
   class SomeInnerClass:
   var a = 5
   func print_value_of_a():
       print(a)

   # これは、クラスファイルのメインクラスのコンストラクタ
   func _init():
       var c = SomeInnerClass.new()
       c.print_value_of_a()



.. 英語の原文：内部クラス
   Inner classes
   ^^^^^^^^^^^^^

   A class file can contain inner classes. Inner classes are defined using the
   ``class`` keyword. They are instanced using the ``ClassName.new()``
   function.

   ::

       # Inside a class file.

       # An inner class in this class file.
       class SomeInnerClass:
           var a = 5
           func print_value_of_a():
               print(a)

       # This is the constructor of the class file's main class.
       func _init():
           var c = SomeInnerClass.new()
           c.print_value_of_a()


































.. _Classes_as_resources_jump:

リソースとしてのクラス
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ファイルとして保存されたクラスは、 :ref:`resources <class_GDScript>` として扱う。
他のクラスでアクセスするには、ディスクから読み込む必要がある。
これは ``load`` または ``preload`` 関数を使用する(以下参照)。
ロードされたクラスリソースのインスタンス化は、クラスオブジェクトで ``new`` 関数を呼び出すことで行える。

::

   # load()を呼び出すときにクラスリソースをloadする。
   var my_class = load("myclass.gd")

   # コンパイル時に一度だけクラスをpreloadする。
   const MyClass = preload("myclass.gd")

   func _init():
       var a = MyClass.new()
       a.some_function()

.. _doc_gdscript_exports_jp:

.. todo::

   リンクの確認。


.. 英語の原文：リソースとしてのクラス
   Classes as resources
   ^^^^^^^^^^^^^^^^^^^^

   Classes stored as files are treated as :ref:`resources <class_GDScript>`. They
   must be loaded from disk to access them in other classes. This is done using
   either the ``load`` or ``preload`` functions (see below). Instancing of a loaded
   class resource is done by calling the ``new`` function on the class object::

       # Load the class resource when calling load().
       var my_class = load("myclass.gd")

       # Preload the class only once at compile time.
       const MyClass = preload("myclass.gd")

       func _init():
           var a = MyClass.new()
           a.some_function()

   .. _doc_gdscript_exports:



































エクスポート
~~~~~~~~~~~~~~~~~~~~~~~~

クラスのメンバをエクスポートできる。
これは、それらの値が添付(アタッチ)されているリソース(例えば、 :ref:`scene <class_PackedScene>` )とともに保存されることを意味する。
プロパティエディタで編集することもできる。
エクスポートは ``export`` キーワードを使用して行われる。

.. todo::

   リンクの確認。


::

   extends Button

   export var number = 5 # 値は保存され、プロパティエディタに表示される。

エクスポートされた変数は、定数式に初期化されるか、exportキーワードへの引数の形式でエクスポートヒントを持つ必要がある(以下を参照)。

訳者：エクスポートヒントとは？

メンバ変数をエクスポートすることの基本的な利点の1つは、エディタで表示及び編集できること。
このようにして、アーティストやゲームデザイナは、後でプログラムの実行方法に影響を与える値を変更できる。
このために、特別なエクスポート構文が提供されている。

::

   # エクスポートされた値が定数または定数式を割り当てる場合、
   # その型が推測され、エディタで使用される。

   export var number = 5

   # エクスポートは、エディタで使用される基本データ型を引数として使用する。

   export(int) var number

   # エクスポートは、ヒントとして使用するリソースタイプを取ることもできる。

   export(Texture) var character_face
   export(PackedScene) var scene_file
   # この方法で使用できるリソースタイプは多数ある。
   # それらを一覧化するには次のようにする。
   export(Resource) var resource

   # 整数と文字列は列挙値を示唆する。

   # エディタは、0・1・2として列挙する。
   export(int, "Warrior", "Magician", "Thief") var character_class
   # エディタは、文字列名で列挙する。
   export(String, "Rebecca", "Mary", "Leah") var character_name

   # 名前付き列挙値

   # エディタは、THING_1・THING_2・ANOTHER_THINGとして列挙する。
   enum NamedEnum {THING_1, THING_2, ANOTHER_THING = -1}
   export (NamedEnum) var x

   # Pathの文字列

   # 文字列は、ファイルへのPath。
   export(String, FILE) var f
   # 文字列は、ディレクトリへのPath。
   export(String, DIR) var f
   # 文字列は、ファイルへのPathであり、ヒントとして提供されるカスタムフィルタになる。
   export(String, FILE, "*.txt") var f

   # グローバルファイルシステムでPathを使用することも可能だが、
   # ツールスクリプトでのみ使用可能(以下を参照)。

   # 文字列は、グローバルファイルシステム内のPNGファイルへのPath。
   export(String, FILE, GLOBAL, "*.png") var tool_image
   # 文字列は、グローバルファイルシステム内のディレクトリへのPath。
   export(String, DIR, GLOBAL) var tool_dir

   # MULTILINE設定は、複数の行に渡って編集するための大きな入力フィールドを表示するように、エディタに指示する。
   export(String, MULTILINE) var text

   # エディタ入力範囲の制限

   # 0から20の整数値を許可する。
   export(int, 20) var i
   # -10から20の整数値を許可する。
   export(int, -10, 20) var j
   # 0.2刻みで、-10から20の浮動小数点値を許可する。
   export(float, -10, 20, 0.2) var k
   # 値 'y = exp(x)' を許可する。
   # 'y' は、100から1000の間で変化し、20刻みに進む。
   # エディタは値を簡単に編集するためのスライダを提供する。
   export(float, EXP, 100, 1000, 20) var l

   # イージングヒント付きの浮動小数点数

   # 編集時に 'ease()' 関数の視覚的表現を表示する。
   export(float, EASE) var transition_speed

   # 色

   # 赤・緑・青の値として指定された色(アルファ値は常に1)
   export(Color, RGB) var col
   # 赤・緑・青・アルファ値として与えられた色
   export(Color, RGBA) var col

   # シーン内の別のノードもエクスポートできる。

   export(NodePath) var node

エディタでスクリプトが実行されていない場合もエクスポートされたプロパティは引き続き編集可能であることに注意すること(以下の ``tool`` を参照すること)。




.. 英語の原文：エクスポート
   Exports
   ~~~~~~~

   Class members can be exported. This means their value gets saved along
   with the resource (e.g. the :ref:`scene <class_PackedScene>`) they're attached
   to. They will also be available for editing in the property editor. Exporting
   is done by using the ``export`` keyword::

       extends Button

       export var number = 5 # Value will be saved and visible in the property editor.

   An exported variable must be initialized to a constant expression or have an
   export hint in the form of an argument to the export keyword (see below).

   One of the fundamental benefits of exporting member variables is to have
   them visible and editable in the editor. This way, artists and game designers
   can modify values that later influence how the program runs. For this, a
   special export syntax is provided.

   ::

       # If the exported value assigns a constant or constant expression,
       # the type will be inferred and used in the editor.

       export var number = 5

       # Export can take a basic data type as an argument, which will be
       # used in the editor.

       export(int) var number

       # Export can also take a resource type to use as a hint.

       export(Texture) var character_face
       export(PackedScene) var scene_file
       # There are many resource types that can be used this way, try e.g.
       # the following to list them:
       export(Resource) var resource

       # Integers and strings hint enumerated values.

       # Editor will enumerate as 0, 1 and 2.
       export(int, "Warrior", "Magician", "Thief") var character_class
       # Editor will enumerate with string names.
       export(String, "Rebecca", "Mary", "Leah") var character_name

       # Named enum values

       # Editor will enumerate as THING_1, THING_2, ANOTHER_THING.
       enum NamedEnum {THING_1, THING_2, ANOTHER_THING = -1}
       export (NamedEnum) var x

       # Strings as paths

       # String is a path to a file.
       export(String, FILE) var f
       # String is a path to a directory.
       export(String, DIR) var f
       # String is a path to a file, custom filter provided as hint.
       export(String, FILE, "*.txt") var f

       # Using paths in the global filesystem is also possible,
       # but only in tool scripts (see further below).

       # String is a path to a PNG file in the global filesystem.
       export(String, FILE, GLOBAL, "*.png") var tool_image
       # String is a path to a directory in the global filesystem.
       export(String, DIR, GLOBAL) var tool_dir

       # The MULTILINE setting tells the editor to show a large input
       # field for editing over multiple lines.
       export(String, MULTILINE) var text

       # Limiting editor input ranges

       # Allow integer values from 0 to 20.
       export(int, 20) var i
       # Allow integer values from -10 to 20.
       export(int, -10, 20) var j
       # Allow floats from -10 to 20, with a step of 0.2.
       export(float, -10, 20, 0.2) var k
       # Allow values 'y = exp(x)' where 'y' varies between 100 and 1000
       # while snapping to steps of 20. The editor will present a
       # slider for easily editing the value.
       export(float, EXP, 100, 1000, 20) var l

       # Floats with easing hint

       # Display a visual representation of the 'ease()' function
       # when editing.
       export(float, EASE) var transition_speed

       # Colors

       # Color given as red-green-blue value (alpha will always be 1)
       export(Color, RGB) var col
       # Color given as red-green-blue-alpha value
       export(Color, RGBA) var col

       # Another node in the scene can be exported, too.

       export(NodePath) var node

   It must be noted that even if the script is not being run while in the
   editor, the exported properties are still editable (see below for
   ``tool``).


































ビットフラグのエクスポート
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ビットフラグとして使用される整数は、1つのプロパティに複数の ``true``/``false`` (Bool)値を格納できる。
エクスポートヒント ``int, FLAGS`` を使用した場合、エディタから設定できる。

::

   # 整数のビットを個別に編集する。
   export(int, FLAGS) var spell_elements = ELEMENT_WIND | ELEMENT_WATER

フラグを特定の数の名前付きフラグに制限することもできる。
構文は列挙構文に似ている。

::

   # エディタから指定されたフラグのいずれかを設定する。
   export(int, FLAGS, "Fire", "Water", "Earth", "Wind") var spell_elements = 0

この例では、 ``Fire`` の値は1・ ``Water`` の値は2・ ``Earth`` の値は4・ ``Wind`` の値は8を設定している。
通常、定数はそれに応じて定義する必要がある(例： ``const ELEMENT_WIND = 8`` など)。

ビットフラグを使用するには、ビット単位の操作をある程度理解する必要がある。
疑わしい場合は、代わりにBool変数をエクスポートする必要がある。

訳者：疑わしい？意味が分からない。


.. 英語の原文：ビットフラグのエクスポート
   Exporting bit flags
   ^^^^^^^^^^^^^^^^^^^

   Integers used as bit flags can store multiple ``true``/``false`` (boolean)
   values in one property. By using the export hint ``int, FLAGS``, they
   can be set from the editor::

       # Individually edit the bits of an integer.
       export(int, FLAGS) var spell_elements = ELEMENT_WIND | ELEMENT_WATER

   Restricting the flags to a certain number of named flags is also
   possible. The syntax is similar to the enumeration syntax::

       # Set any of the given flags from the editor.
       export(int, FLAGS, "Fire", "Water", "Earth", "Wind") var spell_elements = 0

   In this example, ``Fire`` has value 1, ``Water`` has value 2, ``Earth``
   has value 4 and ``Wind`` corresponds to value 8. Usually, constants
   should be defined accordingly (e.g. ``const ELEMENT_WIND = 8`` and so
   on).

   Using bit flags requires some understanding of bitwise operations. If in
   doubt, boolean variables should be exported instead.


































配列のエクスポート
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

配列のエクスポートは機能するが、重要な注意事項がある。
通常の配列はすべてのクラスインスタンスに対してローカルに作成されるが、エクスポートされた配列はすべてのインスタンス間で *共有* される。
つまり、1つのインスタンスで編集した場合、他のすべてのインスタンスに影響すると言うこと。
エクスポートされた配列は初期化子を持てるが、定数式に限定される。

::

   # すべてのインスタンス間で共有されるエクスポートされた配列
   # デフォルト値は定数式で無ければならない。

   export var a = [1, 2, 3]

   # エクスポートされた配列は、型を指定できる(以前と同じヒントを使用)。

   export(Array, int) var ints = [1,2,3]
   export(Array, int, "Red", "Green", "Blue") var enums = [2, 1, 0]
   export(Array, Array, float) var two_dimensional = [[1.0, 2.0], [3.0, 4.0]]

   # デフォルト値は省略可能だが、割り当てられない場合はnullになる。

   export(Array) var b
   export(Array, PackedScene) var scenes

   # 型付き配列も機能し、初期化された空限定になる。

   export var vector3s = PoolVector3Array()
   export var strings = PoolStringArray()

   # インスタンスごとにローカルに作成された通常の配列。
   # デフォルト値にはランタイム値を含めることはできるが、エクスポートはできない。

   var c = [a, 2, 3]



.. 英語の原文：配列のエクスポート
   Exporting arrays
   ^^^^^^^^^^^^^^^^

   Exporting arrays works, but with an important caveat: while regular
   arrays are created local to every class instance, exported arrays are *shared*
   between all instances. This means that editing them in one instance will
   cause them to change in all other instances. Exported arrays can have
   initializers, but they must be constant expressions.

   ::

       # Exported array, shared between all instances.
       # Default value must be a constant expression.

       export var a = [1, 2, 3]

       # Exported arrays can specify type (using the same hints as before).

       export(Array, int) var ints = [1,2,3]
       export(Array, int, "Red", "Green", "Blue") var enums = [2, 1, 0]
       export(Array, Array, float) var two_dimensional = [[1.0, 2.0], [3.0, 4.0]]

       # You can omit the default value, but then it would be null if not assigned.

       export(Array) var b
       export(Array, PackedScene) var scenes

       # Typed arrays also work, only initialized empty:

       export var vector3s = PoolVector3Array()
       export var strings = PoolStringArray()

       # Regular array, created local for every instance.
       # Default value can include run-time values, but can't
       # be exported.

       var c = [a, 2, 3]


































セッター/ゲッター(Setters/getters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

何らかの理由でクラスのメンバ変数がいつ変更されるかを知ることは、しばしば役立つ。
また、何らかの方法でアクセスをカプセル化することが望ましい場合もある。

このため、GDScriptは ``setget`` キーワードを使用して、 *setter/getter* 構文を提供する。
変数定義の直後に使用する。

::

   var variable = value setget setterfunc, getterfunc

``variable`` の値が *external* ソースによって変更されるたびに(要はクラスでのローカル使用からでは無く)、 *setter* 関数(上記の ``setterfunc`` )が呼び出される。
これは、値が変更される *前* に発生する。
*setter* は、新しい値をどう処理するかを決定する必要がある。
逆に、 ``variable`` にアクセスする場合、 *getter* 関数(上記の ``getterfunc`` )は目的の値を ``return`` が必要になる。
以下に例を示す。

::

   var myvar setget my_var_set, my_var_get

   func my_var_set(new_value):
       my_var = new_value

   func my_var_get():
       return my_var # getterは値を返す必要がある。

*setter* または *getter* 関数のいずれかを省略できる。

::

   # setterのみ。
   var my_var = 5 setget myvar_set
   # getterのみ(コンマに注意)。
   var my_var = 5 setget ,myvar_get

Get/Settersは、入力を検証するために、ツールスクリプトまたはプラグインでエディタに変数をエクスポートする場合に特に便利になっている。

前述のように、 *local* アクセスはsetterとgetterをきっかけに *動かない* 。
これの実例は以下の通り。

::

   func _init():
       # setter/getterをトリガーにしない。
       my_integer = 5
       print(my_integer)

       # setter/getterをトリガーにする。
       self.my_integer = 5
       print(self.my_integer)




.. 英語の原文：セッター/ゲッター(Setters/getters)
   Setters/getters
   ~~~~~~~~~~~~~~~

   It is often useful to know when a class' member variable changes for
   whatever reason. It may also be desired to encapsulate its access in some way.

   For this, GDScript provides a *setter/getter* syntax using the ``setget`` keyword.
   It is used directly after a variable definition:

   ::

       var variable = value setget setterfunc, getterfunc

   Whenever the value of ``variable`` is modified by an *external* source
   (i.e. not from local usage in the class), the *setter* function (``setterfunc`` above)
   will be called. This happens *before* the value is changed. The *setter* must decide what to do
   with the new value. Vice versa, when ``variable`` is accessed, the *getter* function
   (``getterfunc`` above) must ``return`` the desired value. Below is an example::

       var myvar setget my_var_set, my_var_get

       func my_var_set(new_value):
           my_var = new_value

       func my_var_get():
           return my_var # Getter must return a value.

   Either of the *setter* or *getter* functions can be omitted::

       # Only a setter.
       var my_var = 5 setget myvar_set
       # Only a getter (note the comma).
       var my_var = 5 setget ,myvar_get

   Get/Setters are especially useful when exporting variables to editor in tool
   scripts or plugins, for validating input.

   As said, *local* access will *not* trigger the setter and getter. Here is an
   illustration of this:

   ::

       func _init():
           # Does not trigger setter/getter.
           my_integer = 5
           print(my_integer)

           # Does trigger setter/getter.
           self.my_integer = 5
           print(self.my_integer)

































ツールモード
~~~~~~~~~~~~~~~~~~~~~~~~

デフォルトでは、スクリプトはエディタ内で実行されず、エクスポートできるプロパティのみを変更する。
場合により、ゲームコードを実行しない、もしくは手動で実行しない限り、エディタ内での実行が望ましい場合がある。
このためには、 ``tool`` キーワードが存在し、ファイルの先頭に配置する必要がある。

::

   tool
   extends Button

   func _ready():
       print("Hello")

.. warning:: 

   ツールスクリプト(特にスクリプトの所有者自身)で ``queue_free()`` または ``free()`` でノードを解放するときは注意すること。
   ツールスクリプトはエディタでコードを実行するため、それらを誤用した場合、エディタがクラッシュする可能性がある。



















.. 英語の原文：ツールモード
   Tool mode
   ~~~~~~~~~

   By default, scripts don't run inside the editor and only the exported
   properties can be changed. In some cases, it is desired that they do run
   inside the editor (as long as they don't execute game code or manually
   avoid doing so). For this, the ``tool`` keyword exists and must be
   placed at the top of the file::

       tool
       extends Button

       func _ready():
           print("Hello")

   .. warning:: Be cautious when freeing nodes with ``queue_free()`` or ``free()``
                in a tool script (especially the script's owner itself). As tool
                scripts run their code in the editor, misusing them may lead to
                crashing the editor.


































メモリ管理
~~~~~~~~~~~~~~~~~~~~

クラスが :ref:`class_Reference` を継承する場合、使用されなくなったインスタンスは解放される。
ガーベージコレクタは存在せず、参照カウンタのみある。
デフォルトでは、継承を定義しないすべてのクラスは **Reference(参照)** を拡張する。
これが望ましくない場合、クラスは :ref:`class_Object` を手動で継承し、instance.free()を呼び出す必要がある。
解放できない参照サイクルを回避するために、弱い参照を作成するための ``weakref`` 関数が提供されている。

あるいは、参照を使用しない場合、オブジェクトが解放されたかどうかを確認するために ``is_instance_valid(instance)`` を使う。

.. _doc_gdscript_signals_jp:

.. todo::

   リンクの確認。


.. 英語の原文：メモリ管理
   Memory management
   ~~~~~~~~~~~~~~~~~

   If a class inherits from :ref:`class_Reference`, then instances will be
   freed when no longer in use. No garbage collector exists, just
   reference counting. By default, all classes that don't define
   inheritance extend **Reference**. If this is not desired, then a class
   must inherit :ref:`class_Object` manually and must call instance.free(). To
   avoid reference cycles that can't be freed, a ``weakref`` function is
   provided for creating weak references.

   Alternatively, when not using references, the
   ``is_instance_valid(instance)`` can be used to check if an object has been
   freed.

   .. _doc_gdscript_signals:


































シグナル
~~~~~~~~~~~~~~~~

シグナルは、他のオブジェクトが反応できるオブジェクトからメッセージを送信するツール。
クラスのカスタムシグナルを作成するには、 ``signal`` キーワードを使う。

::

   extends Node

   # health_depletedと言うなのシグナル
   signal health_depleted

.. note::

   シグナルは `Callback <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_ メカニズムになる。
   また、一般的なプログラミングパターンであるオブザーバの役割も果たす。
   詳細はGame Programming Patterns電子本の `Observer tutorial <https://gameprogrammingpatterns.com/observer.html>`_ を参照すること。

:ref:`class_Button` や :ref:`class_RigidBody` のようなノードの組み込みシグナルを接続するのと同じ方法で、これらのシグナルをメソッドに接続できる。

以下の例では、 ``Character`` ノードから ``health_depleted`` シグナルを ``Game`` ノードに接続する。
``Character`` ノードがシグナルを発したとき、ゲームノードの ``_on_Character_health_depleted`` が呼び出される。

.. todo::

   リンクの確認。

::

   # Game.gd

   func _ready():
       var character_node = get_node('Character')
       character_node.connect("health_depleted", self, "_on_Character_health_depleted")

   func _on_Character_health_depleted():
       get_tree().reload_current_scene()

シグナルとともに必要な数の引数を発行できる。

これが便利な例になる。
画面上のライフバーをアニメーションで健康状態の変化に反応させたいが、シーンツリーではユーザインタフェイスをプレイヤーとは別の前提にする。

``Character.gd`` スクリプトで、 ``health_changed`` シグナルを定義し、それを :ref:`Object.emit_signal() <class_Object_method_emit_signal>` で送信する。
シーンツリー上位の ``Game`` ノードから :ref:`Object.connect() <class_Object_method_connect>` メソッドを使用し、 ``Lifebar`` に接続する。

訳者：誤訳になっている可能性がある。

::

   # Character.gd

   ...
   signal health_changed

   func take_damage(amount):
       var old_health = health
       health -= amount

   # キャラクタがダメージを負うたびに、health_changedシグナルを発信する。
   emit_signal("health_changed", old_health, health)
   ...

::

   # Lifebar.gd

   # ここでは、キャラクタのhealth_changedシグナルが発行されたときにコールバックとして使用する関数を定義する。

   ...
   func _on_Character_health_changed(old_value, new_value):
       if old_value > new_value:
           progress_bar.modulate = Color.red
       else:
           progress_bar.modulate = Color.green

   # `animate` は、バーを埋めたり空にするアニメーションを作成するユーザ定義関数だと想像すること。
   progress_bar.animate(old_value, new_value)
   ...

.. note::

   シグナルを使用するには、クラスは ``Object`` クラスまたは ``Node`` ・ ``KinematicBody`` ・ ``Control`` ... のようにそれを拡張する任意の型を拡張する必要がある。

``Game`` ノードでは、 ``Character`` と ``Lifebar`` ノードの両方を取得し、シグナルを発するキャラクタをレシーバ(この場合は ``Lifebar`` ノード)に接続する。

訳者：レシーバとは？

::

   # Game.gd

   func _ready():
       var character_node = get_node('Character')
       var lifebar_node = get_node('UserInterface/Lifebar')

   character_node.connect("health_changed", lifebar_node, "_on_Character_health_changed")

これにより、 ``Lifebar`` は ``Character`` ノードに結合せずに健康状態の変化に反応できる。

シグナル定義後に、括弧でオプションの引数名を記述できる。

::

   # 2つの引数を転送するシグナルを定義する。
   signal health_changed(old_value, new_value)

これらの引数はエディタのノードドックに表示され、Godotはそれらを使用してコールバック関数を生成できる。
ただし、シグナルを発行するときに、任意の数の引数を発行できる。
正しい値を出力するのは開発者に委ねられている。

.. image:: img/gdscript_basics_signals_node_tab_1.png

GDScriptは、値の配列をシグナルとメソッド間の接続にバインドできる。
シグナルが発行されたとき、コールバック関数はバインドされた値を受け取る。
これらのバインドされた引数は各接続に固有であり、値は同じまま。

この値の配列を使用して、発行されたシグナル自体では必要なすべてのデータにアクセスできない場合、接続に追加の定数情報を追加できる。

訳者：は？

上記の例に基づき、 ``Player1 took 22 damage.`` など各キャラクタが受けたダメージのログを画面に表示する。
``health_changed`` シグナルは、ダメージを受けたキャラクタの名前を与えない。
そのため、ゲーム内のコンソールにシグナルを接続するときに、バインド配列引数にキャラクタの名前を追加できる。

::

   # Game.gd

   func _ready():
       var character_node = get_node('Character')
       var battle_log_node = get_node('UserInterface/BattleLog')

   character_node.connect("health_changed", battle_log_node, "_on_Character_health_changed", [character_node.name])

``BattleLog`` ノードは、追加の引数としてバインド配列の各要素を受け取る。

::

   # BattleLog.gd

   func _on_Character_health_changed(old_value, new_value, character_name):
       if not new_value <= old_value:
           return
       var damage = old_value - new_value
       label.text += character_name + " took " + str(damage) + " damage."



.. 英語の原文：シグナル
   Signals
   ~~~~~~~

   Signals are a tool to emit messages from an object that other objects can react
   to. To create custom signals for a class, use the ``signal`` keyword.

   ::

      extends Node

      # A signal named health_depleted
      signal health_depleted

   .. note::

      Signals are a `Callback
      <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_
      mechanism. They also fill the role of Observers, a common programming
      pattern. For more information, read the `Observer tutorial
      <https://gameprogrammingpatterns.com/observer.html>`_ in the
      Game Programming Patterns ebook.

   You can connect these signals to methods the same way you connect built-in
   signals of nodes like :ref:`class_Button` or :ref:`class_RigidBody`.

   In the example below, we connect the ``health_depleted`` signal from a
   ``Character`` node to a ``Game`` node. When the ``Character`` node emits the
   signal, the game node's ``_on_Character_health_depleted`` is called::

      # Game.gd

      func _ready():
         var character_node = get_node('Character')
         character_node.connect("health_depleted", self, "_on_Character_health_depleted")

      func _on_Character_health_depleted():
         get_tree().reload_current_scene()

   You can emit as many arguments as you want along with a signal.

   Here is an example where this is useful. Let's say we want a life bar on screen
   to react to health changes with an animation, but we want to keep the user
   interface separate from the player in our scene tree.

   In our ``Character.gd`` script, we define a ``health_changed`` signal and emit
   it with :ref:`Object.emit_signal() <class_Object_method_emit_signal>`, and from
   a ``Game`` node higher up our scene tree, we connect it to the ``Lifebar`` using
   the :ref:`Object.connect() <class_Object_method_connect>` method::

       # Character.gd

       ...
       signal health_changed

       func take_damage(amount):
           var old_health = health
           health -= amount

           # We emit the health_changed signal every time the
           # character takes damage
           emit_signal("health_changed", old_health, health)
       ...

   ::

       # Lifebar.gd

       # Here, we define a function to use as a callback when the
       # character's health_changed signal is emitted

       ...
       func _on_Character_health_changed(old_value, new_value):
           if old_value > new_value:
               progress_bar.modulate = Color.red
           else:
               progress_bar.modulate = Color.green

           # Imagine that `animate` is a user-defined function that animates the
           # bar filling up or emptying itself
           progress_bar.animate(old_value, new_value)
       ...

   .. note::

       To use signals, your class has to extend the ``Object`` class or any
       type extending it like ``Node``, ``KinematicBody``, ``Control``...

   In the ``Game`` node, we get both the ``Character`` and ``Lifebar`` nodes, then
   connect the character, that emits the signal, to the receiver, the ``Lifebar``
   node in this case.

   ::

      # Game.gd

      func _ready():
         var character_node = get_node('Character')
         var lifebar_node = get_node('UserInterface/Lifebar')

         character_node.connect("health_changed", lifebar_node, "_on_Character_health_changed")

   This allows the ``Lifebar`` to react to health changes without coupling it to
   the ``Character`` node.

   You can write optional argument names in parentheses after the signal's
   definition::

      # Defining a signal that forwards two arguments
      signal health_changed(old_value, new_value)

   These arguments show up in the editor's node dock, and Godot can use them to
   generate callback functions for you. However, you can still emit any number of
   arguments when you emit signals; it's up to you to emit the correct values.

   .. image:: img/gdscript_basics_signals_node_tab_1.png

   GDScript can bind an array of values to connections between a signal
   and a method. When the signal is emitted, the callback method receives
   the bound values. These bound arguments are unique to each connection,
   and the values will stay the same.

   You can use this array of values to add extra constant information to the
   connection if the emitted signal itself doesn't give you access to all the data
   that you need.

   Building on the example above, let's say we want to display a log of the damage
   taken by each character on the screen, like ``Player1 took 22 damage.``. The
   ``health_changed`` signal doesn't give us the name of the character that took
   damage. So when we connect the signal to the in-game console, we can add the
   character's name in the binds array argument::

      # Game.gd

      func _ready():
         var character_node = get_node('Character')
         var battle_log_node = get_node('UserInterface/BattleLog')

         character_node.connect("health_changed", battle_log_node, "_on_Character_health_changed", [character_node.name])

   Our ``BattleLog`` node receives each element in the binds array as an extra argument::

      # BattleLog.gd

      func _on_Character_health_changed(old_value, new_value, character_name):
         if not new_value <= old_value:
            return
         var damage = old_value - new_value
         label.text += character_name + " took " + str(damage) + " damage."



































歩留まりのあるコルーチン
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GDScriptは、 :ref:`yield<class_@GDScript_method_yield>` 組み込み関数を介して、 `coroutines <https://en.wikipedia.org/wiki/Coroutine>`_ のサポートを提供する。
``yield()`` を呼び出したとき、現在の関数からすぐに戻り、戻り値と同じ関数の現在の凍結状態が返される。
この結果のオブジェクトで ``resume()`` を呼び出した場合、実行が継続され、関数が返す物がすべて返される。
再開したときに、状態オブジェクトは無効になる。
以下、例。

.. todo::

   リンクの確認。


::

   func my_func():
       print("Hello")
       yield()
       print("world")

   func _ready():
       var y = my_func()
       # 関数の状態は 'y' に保存される。
       print("my dear")
       y.resume()
       # 'y' が再開され、現在は無効な状態になっている。

以下、上記のプログラムの出力結果。

::

   Hello
   my dear
   world

``yield()`` と ``resume()`` の間で値を渡すこともできる。
以下、例。

::

   func my_func():
       print("Hello")
       print(yield())
       return "cheers!"

   func _ready():
       var y = my_func()
       # 関数の状態は 'y' に保存される。
       print(y.resume("world"))
       # 'y' が再開され、現在は無効な状態になっている。

以下、上記のプログラムの出力結果。

::

   Hello
   world
   cheers!



.. 英語の原文：歩留まりのあるコルーチン
   Coroutines with yield
   ~~~~~~~~~~~~~~~~~~~~~

   GDScript offers support for `coroutines <https://en.wikipedia.org/wiki/Coroutine>`_
   via the :ref:`yield<class_@GDScript_method_yield>` built-in function. Calling ``yield()`` will
   immediately return from the current function, with the current frozen
   state of the same function as the return value. Calling ``resume()`` on
   this resulting object will continue execution and return whatever the
   function returns. Once resumed, the state object becomes invalid. Here is
   an example::

       func my_func():
          print("Hello")
          yield()
          print("world")

       func _ready():
           var y = my_func()
           # Function state saved in 'y'.
           print("my dear")
           y.resume()
           # 'y' resumed and is now an invalid state.

   Will print::

       Hello
       my dear
       world

   It is also possible to pass values between ``yield()`` and ``resume()``,
   for example::

       func my_func():
          print("Hello")
          print(yield())
          return "cheers!"

       func _ready():
           var y = my_func()
           # Function state saved in 'y'.
           print(y.resume("world"))
           # 'y' resumed and is now an invalid state.

   Will print::

       Hello
       world
       cheers!


































コルーチンとシグナル
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``yield`` を使用する真の強みは、シグナルと組み合わせる場合にある。
``yield`` は2つの引数(オブジェクトとシグナル)を受け入れる。
シグナルを受信したとき、実行が再開される。
以下、例。

::

   # 次のフレームの実行を再開する。
   yield(get_tree(), "idle_frame")

   # アニメーションの再生が完了後に実行再開。
   yield(get_node("AnimationPlayer"), "finished")

   # 5秒の待機後に、実行再開
   yield(get_tree().create_timer(5.0), "timeout")

コルーチン自体は、無効な状態に移行したときに ``completed`` シグナルを使う。
以下、例。

::

   func my_func():
       yield(button_func(), "completed")
       print("All buttons were pressed, hurray!")

   func button_func():
       yield($Button0, "pressed")
       yield($Button1, "pressed")

``my_func`` は両方のボタンが押されたときに実行を継続する。



.. 英語の原文：コルーチンとシグナル
   Coroutines & signals
   ^^^^^^^^^^^^^^^^^^^^

   The real strength of using ``yield`` is when combined with signals.
   ``yield`` can accept two arguments, an object and a signal. When the
   signal is received, execution will recommence. Here are some examples::

       # Resume execution the next frame.
       yield(get_tree(), "idle_frame")

       # Resume execution when animation is done playing.
       yield(get_node("AnimationPlayer"), "finished")

       # Wait 5 seconds, then resume execution.
       yield(get_tree().create_timer(5.0), "timeout")

   Coroutines themselves use the ``completed`` signal when they transition
   into an invalid state, for example::

       func my_func():
           yield(button_func(), "completed")
           print("All buttons were pressed, hurray!")

       func button_func():
           yield($Button0, "pressed")
           yield($Button1, "pressed")

   ``my_func`` will only continue execution once both buttons have been pressed.


































準備中のキーワード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ノードを使用する場合、変数内のシーンの一部への参照を保持することが一般的に行われる。
シーンはアクティブなシーンツリーに入るときのみ設定されることが保証されているため、サブノードは ``Node._ready()`` への呼び出しが行われたときのみ取得できる。

::

   var my_label

   func _ready():
       my_label = get_node("MyLabel")

これは、特にノードと外部参照が積み重なる場合、少し面倒になる。
このため、GDScriptには ``onready`` キーワードがあり、これは ``_ready()`` が呼び出されるまでメンバ変数の初期化を延期する。
上記のコードを1行で置き換えることができる。

::

   onready var my_label = get_node("MyLabel")



.. 英語の原文：準備中のキーワード
   Onready keyword
   ~~~~~~~~~~~~~~~

   When using nodes, it's common to desire to keep references to parts
   of the scene in a variable. As scenes are only warranted to be
   configured when entering the active scene tree, the sub-nodes can only
   be obtained when a call to ``Node._ready()`` is made.

   ::

       var my_label

       func _ready():
           my_label = get_node("MyLabel")

   This can get a little cumbersome, especially when nodes and external
   references pile up. For this, GDScript has the ``onready`` keyword, that
   defers initialization of a member variable until ``_ready()`` is called. It
   can replace the above code with a single line::

       onready var my_label = get_node("MyLabel")
































キーワードをアサート
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``assert`` キーワードは、デバッグビルドの条件を確認するために使用できる。
これらのアサーションは、非デバッグビルドでは無視される。
つまり、引数として渡された式は、リリースモードでエクスポートされたプロジェクトでは評価されない。
このため、アサーションには副作用のある式が含まれていてはならない。
それ以外の場合、スクリプトの動作は、プロジェクトがデバッグビルドで実行されるかどうかによって異なる。

::

   # 'i' が0であることを確認する。 'i' が0でない場合、アサーションエラーが発生する。
   assert(i == 0)

エディタからプロジェクトを実行する場合、アサーションエラーの発生によりプロジェクトは一時停止する。


.. 英語の原文：キーワードをアサート
   Assert keyword
   ~~~~~~~~~~~~~~

   The ``assert`` keyword can be used to check conditions in debug builds. These
   assertions are ignored in non-debug builds. This means that the expression
   passed as argument won't be evaluated in a project exported in release mode.
   Due to this, assertions must **not** contain expressions that have
   side effects. Otherwise, the behavior of the script would vary
   depending on whether the project is run in a debug build.

   ::

       # Check that 'i' is 0. If 'i' is not 0, an assertion error will occur.
       assert(i == 0)

   When running a project from the editor, the project will be paused if an
   assertion error occurs.


.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
