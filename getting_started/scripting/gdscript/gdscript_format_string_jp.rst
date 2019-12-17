.. _doc_gdscript_printf_jp:


































GDScript書式文章
====================================

GDScriptは、テキストを再利用できる *format strings* と呼ばれる機能を提供しており、テキストテンプレートを再利用して、類似した文字列を簡単に作成できる。

フォーマット文字列は、特定のプレースホルダ文字シーケンスを含むことを除き、通常の文字列と全く同じ。
これらのプレースホルダは、フォーマット文字列に渡される引数に簡単に置き換えることができる。

例えば、プレースホルダとして ``%s`` を使用した場合、書式文字列 ``"Hello %s, how are you?`` を簡単に ``"Hello World, how are you?"`` に置き換える。
プレースホルダが文字列の中央にあることに注意すること。
書式文字列なしでそれを変更するのは結果に見合わない労力を必要とする。


.. 英語の原文：GDScript書式文章
   GDScript format strings
   =======================

   GDScript offers a feature called *format strings*, which allows reusing text
   templates to succinctly create different but similar strings.

   Format strings are just like normal strings, except they contain certain
   placeholder character-sequences. These placeholders can then easily be replaced
   by parameters handed to the format string.

   As an example, with ``%s`` as a placeholder, the format string ``"Hello %s, how
   are you?`` can easily be changed to ``"Hello World, how are you?"``. Notice
   the placeholder is in the middle of the string; modifying it without format
   strings could be cumbersome.

































GDScriptでの使用
--------------------------------

今回は、具体的なGDScriptの例を示す。

::

   # プレースホルダ '%s' でフォーマット文字列を定義する
   var format_string = "We're waiting for %s."

   # '%' 演算子を使用した場合、プレースホルダは目的の値に置き換えられる。
   var actual_string = format_string % "Godot"

   print(actual_string)
   # 出力結果："We're waiting for Godot."

プレースホルダは常に ``%`` で始まるが、次の1つ以上の文字である *format specifier* は、指定された値を文字列に変換する方法を決定する。

上記の例で見られる ``%s`` は、最も単純なプレースホルダであり、ほとんどのユースケースで機能する。
暗黙の文字列変換または ``str()`` が変換するのと同じメソッドで値を変換する。
文字列は変更されず、Bool値は ``"True"`` または ``"False"`` に変わり、整数または実数は小数になる。
他の型は、通常人間が読める文字列でデータを返す。

GDScriptでテキストをフォーマットする別の方法、要は、 ``String.format()`` メソッドもある。
文字列内のキーのすべての出現を対応値に置き換える。
このメソッドは、キー/値が対になった配列または辞書を処理できる。

配列は、キー・インデックス・混合スタイルとして使用できる(以下の例を参照すること)。
順序は、インデックスまたは混合スタイルの配列が使用される場合にのみ重要になる。

以下、GDScriptの簡単な例。

::

   # フォーマット文字列の定義
   var format_string = "We're waiting for {str}"

   # 'format' メソッドを使用し、 'str' プレースホルダを置き換える。
   var actual_string = format_string.format({"str": "Godot"})

   print(actual_string)
   # 出力結果："We're waiting for Godot"

他にも `format specifiers`_ がある。
しかし、それらは ``%`` 演算子を使用する場合にのみ適用可能だ。

.. todo::

   リンクが切れているため、つなぐこと。


.. 英語の原文：GDScriptでの使用
   Usage in GDScript
   -----------------

   Examine this concrete GDScript example:

   ::

       # Define a format string with placeholder '%s'
       var format_string = "We're waiting for %s."

       # Using the '%' operator, the placeholder is replaced with the desired value
       var actual_string = format_string % "Godot"

       print(actual_string)
       # Output: "We're waiting for Godot."

   Placeholders always start with a ``%``, but the next character or characters,
   the *format specifier*, determines how the given value is converted to a
   string.

   The ``%s`` seen in the example above is the simplest placeholder and works for
   most use cases: it converts the value by the same method by which an implicit
   String conversion or ``str()`` would convert it. Strings remain unchanged,
   Booleans turn into either ``"True"`` or ``"False"``, an integral or real number
   becomes a decimal, other types usually return their data in a human-readable
   string.

   There is also another way to format text in GDScript, namely the ``String.format()``
   method. It replaces all occurrences of a key in the string with the corresponding
   value. The method can handle arrays or dictionaries for the key/value pairs.

   Arrays can be used as key, index, or mixed style (see below examples). Order only
   matters when the index or mixed style of Array is used.

   A quick example in GDScript:

   ::

       # Define a format string
       var format_string = "We're waiting for {str}"

       # Using the 'format' method, replace the 'str' placeholder
       var actual_string = format_string.format({"str": "Godot"})

       print(actual_string)
       # Output: "We're waiting for Godot"

   There are other `format specifiers`_, but they are only applicable when using
   the ``%`` operator.



































複数のプレースホルダ
----------------------------------------

フォーマット文字列には複数のプレースホルダが含まれる場合がある。
このような場合の値は、プレースホルダごとに1つの値の配列の形式で渡される( ``*`` で書式指定市を使用しない限り `dynamic padding`_ を参照すること )。

::

   var format_string = "%s was reluctant to learn %s, but now he enjoys it."
   var actual_string = format_string % ["Estragon", "GDScript"]

   print(actual_string)
   # 出力結果："Estragon was reluctant to learn GDScript, but now he enjoys it."

値が順番に挿入されることに注意すること。
すべてのプレースホルダを一度に置き換える必要があるため、適切な数の値が必要であることに注意すること。

.. todo::

   リンクが切れているため、つなぐこと。



.. 英語の原文：複数のプレースホルダ
   Multiple placeholders
   ---------------------

   Format strings may contain multiple placeholders. In such a case, the values
   are handed in the form of an array, one value per placeholder (unless using a
   format specifier with ``*``, see `dynamic padding`_):

   ::

       var format_string = "%s was reluctant to learn %s, but now he enjoys it."
       var actual_string = format_string % ["Estragon", "GDScript"]

       print(actual_string)
       # Output: "Estragon was reluctant to learn GDScript, but now he enjoys it."

   Note the values are inserted in order. Remember all placeholders must be
   replaced at once, so there must be an appropriate number of values.

































フォーマット指定子
------------------------------------

プレースホルダで使用できる ``s`` 以外の書式指定子がある。
それらは1つ以上の文字で構成される。
それらの中には ``s`` のように単独で機能したり、他の文字列の前に現れるもの、特定の値または文字でのみ機能するものがある。


.. 英語の原文：フォーマット指定子
   Format specifiers
   -----------------

   There are format specifiers other than ``s`` that can be used in placeholders.
   They consist of one or more characters. Some of them work by themselves like
   ``s``, some appear before other characters, some only work with certain
   values or characters.



































プレースホルダ型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これらの1つだけが、常に書式指定子の最後の文字として表示される必要がある。
``s`` とは別に、これらには特定の型の引数が必要になる。

.. csv-table:: 
   :header: 書式指定子, 説明
   :widths: 1, 5

   ``s``, **Simple** ：暗黙的な文字列変換と同じ方法による文字列変換
   ``c``, 単一の **Unicode文字** ：コードポイントまたは1文字の文字列には、符号なし8ビット整数(0〜255)が必要
   ``d``, **10進数の整数** ：整数または実数を期待する(フローリングされる)
   ``o``, **8進数** ：整数または実数を期待する(フローリングされる)
   ``x``, **小文字** を持つ **16進数の整数** ：整数または実数を期待する(フローリングされる) 訳者：訳合っているか？
   ``X``, **大文字** を持つ **16進数の整数** ：整数または実数を期待する(フローリングされる) 訳者：訳合っているか？
   ``f``, **10進数の実数** ：整数または実数を期待する。


※訳者：表の左側は、書式指定子であっている？



.. 英語の原文：プレースホルダ型
   Placeholder types
   ~~~~~~~~~~~~~~~~~

   One and only one of these must always appear as the last character in a format
   specifier. Apart from ``s``, these require certain types of parameters.

   +-------+---------------------------------------------------------------------+
   | ``s`` | **Simple** conversion to String by the same method as implicit      |
   |       | String conversion.                                                  |
   +-------+---------------------------------------------------------------------+
   | ``c`` | A single **Unicode character**. Expects an unsigned 8-bit integer   |
   |       | (0-255) for a code point or a single-character string.              |
   +-------+---------------------------------------------------------------------+
   | ``d`` | A **decimal integral** number. Expects an integral or real number   |
   |       | (will be floored).                                                  |
   +-------+---------------------------------------------------------------------+
   | ``o`` | An **octal integral** number. Expects an integral or real number    |
   |       | (will be floored).                                                  |
   +-------+---------------------------------------------------------------------+
   | ``x`` | A **hexadecimal integral** number with **lower-case** letters.      |
   |       | Expects an integral or real number (will be floored).               |
   +-------+---------------------------------------------------------------------+
   | ``X`` | A **hexadecimal integral** number with **upper-case** letters.      |
   |       | Expects an integral or real number (will be floored).               |
   +-------+---------------------------------------------------------------------+
   | ``f`` | A **decimal real** number. Expects an integral or real number.      |
   +-------+---------------------------------------------------------------------+


































プレースホルダ修飾子
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これらの文字は、上記の前に表示される。
それらのいくつかは、特定の条件下でのみ機能する。

.. csv-table:: 
   :header: 修飾子, 説明
   :widths: 1, 5

   ``+``, 数値指定子は、正の場合は、 **show + sign** になる。
   Integer, **パディング** あり：整数プレースホルダの整数が ``0`` で始まる場合、スペースまたはゼロで埋められる。 ``.`` は、以下を参照。
   ``.``, ``f`` の前に、 **精度** を小数点以下0桁に設定する。変更する番号をフォローアップできる。ゼロ埋めがなされる。
   ``_``, 左では無く、 **右詰めのパディング**
   ``*``, **動的パディング** 、 ``.`` の後ろにパディングまたは精度を設定する追加の整数引数が必要。 `dynamic padding`_ を参照すること。

※訳者：表の左側は、修飾子であっている？

.. todo::

   リンクの確認。



.. 英語の原文：プレースホルダ修飾子
   Placeholder modifiers
   ~~~~~~~~~~~~~~~~~~~~~

   These characters appear before the above. Some of them work only under certain
   conditions.

   +---------+-------------------------------------------------------------------+
   | ``+``   | In number specifiers, **show + sign** if positive.                |
   +---------+-------------------------------------------------------------------+
   | Integer | Set **padding**. Padded with spaces or with zeroes if integer     |
   |         | starts with ``0`` in an integer placeholder. When used after      |
   |         | ``.``, see ``.``.                                                 |
   +---------+-------------------------------------------------------------------+
   | ``.``   | Before ``f``, set **precision** to 0 decimal places. Can be       |
   |         | followed up with numbers to change. Padded with zeroes.           |
   +---------+-------------------------------------------------------------------+
   | ``-``   | **Pad to the right** rather than the left.                        |
   +---------+-------------------------------------------------------------------+
   | ``*``   | **Dynamic padding**, expect additional integral parameter to set  |
   |         | padding or precision after ``.``, see `dynamic padding`_.         |
   +---------+-------------------------------------------------------------------+



































パディング(詰め物)
------------------------------------

``.`` ( *ドット* )・ ``*`` ( *アスタリスク* )・ ``-`` ( *マイナス記号* )・数字( ``0`` - ``9`` )・文字がパディングに使用される。
これにより、固定幅フォントが使用されている場合、列にあるかのように複数の値を縦に並べて印刷できる。

文字列を最小長にパディングするには、指定子に整数を追加する。

::

   print("%10d" % 12345)
   # 出力結果："     12345"
   # 合計10の長さから先頭5つのスペースがパディング

整数が ``0`` で始まる場合、整数値は空白では無くゼロで埋められる。

::

   print("%010d" % 12345)
   # 出力結果："0000012345"

実数に精度を指定するには、 ``.`` (*dot*) に整数を追加する。
``.`` の後ろに整数がない場合、0の精度が使用され、整数値に丸められる。
パディングに使用する整数は、dotの前に表示する必要がある。

::

   # 10の最小長にパディングし、小数点以下3桁に丸める
   print("%10.3f" % 10000.5555)
   # 出力結果：" 10000.556"
   # 先頭1つのパディング

``-`` 記号は、左では無く、右にパディングを引き起こす(訳者： "引き起こす" が普通の表現なの？)。
これは、テキストの右揃えに最適だ。

::

   print("%-10d" % 12345678)
   # 出力結果："12345678  "
   # 後尾に2つのスペース


.. 英語の原文：パディング(詰め物)
   Padding
   -------

   The ``.`` (*dot*), ``*`` (*asterisk*), ``-`` (*minus sign*) and digit
   (``0``-``9``) characters are used for padding. This allows printing several
   values aligned vertically as if in a column, provided a fixed-width font is
   used.

   To pad a string to a minimum length, add an integer to the specifier:

   ::

       print("%10d" % 12345)
       # output: "     12345"
       # 5 leading spaces for a total length of 10

   If the integer starts with ``0``, integral values are padded with zeroes
   instead of white space:

   ::

       print("%010d" % 12345)
       # output: "0000012345"

   Precision can be specified for real numbers by adding a ``.`` (*dot*) with an
   integer following it. With no integer after ``.``, a precision of 0 is used,
   rounding to integral value. The integer to use for padding must appear before
   the dot.

   ::

       # Pad to minimum length of 10, round to 3 decimal places
       print("%10.3f" % 10000.5555)
       # Output: " 10000.556"
       # 1 leading space

   The ``-`` character will cause padding to the right rather than the left,
   useful for right text alignment:

   ::

       print("%-10d" % 12345678)
       # Output: "12345678  "
       # 2 trailing spaces


































動的パディング
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``*`` ( *アスタリスク* ) 文字を使用することにより、フォーマット文字列を変更せずにパディングまたは精度を設定できる。
書式指定子の整数の代わりに使用される。
次に、フォーマット時にパディングと精度の値が渡される。

::

   var format_string = "%*.*f"
   # 長さ7に埋め込み、小数点以下3桁に丸める。
   print(format_string % [7, 3, 8.8888])
   # 出力結果："  8.889"
   # 先頭2つ目にスペース

``*`` の前に ``0`` を追加することで、整数のプレースホルダにゼロ埋めを行える。

::

   print("%0*d" % [2, 3])
   # 出力結果："03"


.. 英語の原文：動的パディング
   Dynamic padding
   ~~~~~~~~~~~~~~~

   By using the ``*`` (*asterisk*) character, the padding or precision can be set
   without modifying the format string. It is used in place of an integer in the
   format specifier. The values for padding and precision are then passed when
   formatting:

   ::

       var format_string = "%*.*f"
       # Pad to length of 7, round to 3 decimal places:
       print(format_string % [7, 3, 8.8888])
       # Output: "  8.889"
       # 2 leading spaces

   It is still possible to pad with zeroes in integer placeholders by adding ``0``
   before ``*``:

   ::

       print("%0*d" % [2, 3])
       #output: "03"


































エスケープシーケンス
----------------------------------------

リテラル ``%`` 文字をフォーマット文字列に挿入するには、プレースホルダとして読み取らないようにエスケープする必要がある。
これは、同じ文字を続けることで解決できる。

::

   var health = 56
   print("Remaining health: %d%%" % health)
   # 出力結果："Remaining health: 56%"

訳者：見にくい。かなり混乱しそうだ。

.. 英語の原文：エスケープシーケンス
   Escape sequence
   ---------------

   To insert a literal ``%`` character into a format string, it must be escaped to
   avoid reading it as a placeholder. This is done by doubling the character:

   ::

       var health = 56
       print("Remaining health: %d%%" % health)
       # Output: "Remaining health: 56%"


























.. memo

   以下の"フォーマット方法例"では、エスケープシーケンスを使いまくらなければ、CSV形式の表に置き換えられない。
   無理orz

   .. csv-table:: 
      :header: 型, スタイル, 例, 出力結果
      :widths: 5, 5, 5, 5

      Dictionary, key, "``""Hi, {name} v{version}!"".format({""name"":""Godette"", ""version"":""3.0""})``", "Hi, Godette v3.0!"

   delimやquoteなどのオプションを変更することでめんどくささは回避できる？
   上記の私の対応では、デフォルトのescapeを使って対応している。









フォーマット方法例
------------------------------------

以下は ``String.format`` メソッドの様々な呼び出し使用方法の例

+------------+-----------+------------------------------------------------------------------------------+-------------------+
| **Type**   | **Style** | **Example**                                                                  | **Result**        |
+------------+-----------+------------------------------------------------------------------------------+-------------------+
| Dictionary | key       | ``"Hi, {name} v{version}!".format({"name":"Godette", "version":"3.0"})``     | Hi, Godette v3.0! |
+------------+-----------+------------------------------------------------------------------------------+-------------------+
| Dictionary | index     | ``"Hi, {0} v{1}!".format({"0":"Godette", "1":"3.0"})``                       | Hi, Godette v3.0! |
+------------+-----------+------------------------------------------------------------------------------+-------------------+
| Dictionary | mix       | ``"Hi, {0} v{version}!".format({"0":"Godette", "version":"3.0"})``           | Hi, Godette v3.0! |
+------------+-----------+------------------------------------------------------------------------------+-------------------+
| Array      | key       | ``"Hi, {name} v{version}!".format([["version","3.0"], ["name","Godette"]])`` | Hi, Godette v3.0! |
+------------+-----------+------------------------------------------------------------------------------+-------------------+
| Array      | index     | ``"Hi, {0} v{1}!".format(["Godette","3.0"])``                                | Hi, Godette v3.0! |
+------------+-----------+------------------------------------------------------------------------------+-------------------+
| Array      | mix       | ``"Hi, {name} v{0}!".format([3.0, ["name","Godette"]])``                     | Hi, Godette v3.0! |
+------------+-----------+------------------------------------------------------------------------------+-------------------+
| Array      | no index  | ``"Hi, {} v{}!".format(["Godette", 3.0], "{}")``                             | Hi, Godette v3.0! |
+------------+-----------+------------------------------------------------------------------------------+-------------------+

``String.format`` を使用するときにプレースホルダをカスタマイズすることもできる。
その機能例を次に示す。

+-----------------+------------------------------------------------------+------------------+
| **Type**        | **Example**                                          | **Result**       |
+-----------------+------------------------------------------------------+------------------+
| Infix (default) | ``"Hi, {0} v{1}".format(["Godette", "3.0"], "{_}")`` | Hi, Godette v3.0 |
+-----------------+------------------------------------------------------+------------------+
| Postfix         | ``"Hi, 0% v1%".format(["Godette", "3.0"], "_%")``    | Hi, Godette v3.0 |
+-----------------+------------------------------------------------------+------------------+
| Prefix          | ``"Hi, %0 v%1".format(["Godette", "3.0"], "%_")``    | Hi, Godette v3.0 |
+-----------------+------------------------------------------------------+------------------+

``String.format`` には数値の表現を操作する方法が無いため、 ``String.format`` メソッドと ``%`` 演算子の両方を組み合わせると便利になる。

+---------------------------------------------------------------------------+-------------------+
| **Example**                                                               | **Result**        |
+---------------------------------------------------------------------------+-------------------+
| ``"Hi, {0} v{version}".format({0:"Godette", "version":"%0.2f" % 3.114})`` | Hi, Godette v3.11 |
+---------------------------------------------------------------------------+-------------------+


.. 英語の原文：フォーマット方法例
   Format method examples
   ----------------------

   The following are some examples of how to use the various invocations of the
   ``String.format``  method.


   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | **Type**   | **Style** | **Example**                                                                  | **Result**        |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | Dictionary | key       | ``"Hi, {name} v{version}!".format({"name":"Godette", "version":"3.0"})``     | Hi, Godette v3.0! |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | Dictionary | index     | ``"Hi, {0} v{1}!".format({"0":"Godette", "1":"3.0"})``                       | Hi, Godette v3.0! |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | Dictionary | mix       | ``"Hi, {0} v{version}!".format({"0":"Godette", "version":"3.0"})``           | Hi, Godette v3.0! |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | Array      | key       | ``"Hi, {name} v{version}!".format([["version","3.0"], ["name","Godette"]])`` | Hi, Godette v3.0! |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | Array      | index     | ``"Hi, {0} v{1}!".format(["Godette","3.0"])``                                | Hi, Godette v3.0! |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | Array      | mix       | ``"Hi, {name} v{0}!".format([3.0, ["name","Godette"]])``                     | Hi, Godette v3.0! |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+
   | Array      | no index  | ``"Hi, {} v{}!".format(["Godette", 3.0], "{}")``                             | Hi, Godette v3.0! |
   +------------+-----------+------------------------------------------------------------------------------+-------------------+

   Placeholders can also be customized when using ``String.format``, here's some
   examples of that functionality.


   +-----------------+------------------------------------------------------+------------------+
   | **Type**        | **Example**                                          | **Result**       |
   +-----------------+------------------------------------------------------+------------------+
   | Infix (default) | ``"Hi, {0} v{1}".format(["Godette", "3.0"], "{_}")`` | Hi, Godette v3.0 |
   +-----------------+------------------------------------------------------+------------------+
   | Postfix         | ``"Hi, 0% v1%".format(["Godette", "3.0"], "_%")``    | Hi, Godette v3.0 |
   +-----------------+------------------------------------------------------+------------------+
   | Prefix          | ``"Hi, %0 v%1".format(["Godette", "3.0"], "%_")``    | Hi, Godette v3.0 |
   +-----------------+------------------------------------------------------+------------------+

   Combining both the ``String.format`` method and the ``%`` operator could be useful, as
   ``String.format`` does not have a way to manipulate the representation of numbers.

   +---------------------------------------------------------------------------+-------------------+
   | **Example**                                                               | **Result**        |
   +---------------------------------------------------------------------------+-------------------+
   | ``"Hi, {0} v{version}".format({0:"Godette", "version":"%0.2f" % 3.114})`` | Hi, Godette v3.11 |
   +---------------------------------------------------------------------------+-------------------+


.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
