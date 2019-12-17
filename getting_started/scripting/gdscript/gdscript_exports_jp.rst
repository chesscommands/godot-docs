.. _doc_gdscript_exports_jp:






























GDScriptエクスポート
========================================

.. 英語の原文：GDScriptエクスポート
   GDScript exports
   ================






























エクスポート入門
--------------------------------

Godotでは、クラスメンバをエクスポートできる。
これは、それらの値がリソース( :ref:`scene <class_PackedScene>` )とともに保存されていることを意味する。
プロパティエディタで編集することもできる。
エクスポートは、 ``export`` キーワードを使う。

.. todo::

   リンクの確認。


::

   extends Button

   export var number = 5 # 値は保存され、プロパティエディタに表示される。

エクスポートされた変数は、定数式に初期化されるか、または ``export`` キーワードへの引数の形式でエクスポートヒントを持たなければならない(以下の *例* セクション参照すること)。

メンバ変数をエクスポートすることの基本的な利点の1つは、エディタで表示及び編集できること。
アーティストやゲームデザイナは、後でプログラムの実行方法に影響を与える値を変更できる。
このための特別なエクスポート構文が提供されている。

.. note::

   プロパティのエクスポートは、C#などの他の言語でも実行できる。
   構文は言語により異なる。



.. 英語の原文：エクスポート入門
   Introduction to exports
   -----------------------

   In Godot, class members can be exported. This means their value gets saved along
   with the resource (such as the :ref:`scene <class_PackedScene>`) they're
   attached to. They will also be available for editing in the property editor.
   Exporting is done by using the ``export`` keyword::

       extends Button

       export var number = 5 # Value will be saved and visible in the property editor.

   An exported variable must be initialized to a constant expression or have an
   export hint in the form of an argument to the ``export`` keyword (see the
   *Examples* section below).

   One of the fundamental benefits of exporting member variables is to have
   them visible and editable in the editor. This way, artists and game designers
   can modify values that later influence how the program runs. For this, a
   special export syntax is provided.

   .. note::

       Exporting properties can also be done in other languages such as C#.
       The syntax varies depending on the language.



































事例
------------

::

   # エクスポートされた値が定数または定数式を割り当てる場合、
   # その型が推測され、エディタで使用可能になる。

   export var number = 5

   # エクスポートは、エディタで使用される基本データ型を引数として使用できる。

   export(int) var number

   # エクスポートは、ヒントとして使用するリソース型を取ることもできる。

   export(Texture) var character_face
   export(PackedScene) var scene_file
   # この方法で使用できるリソース型は多数ある。
   # それらを一覧化するには、次のようにする。
   export(Resource) var resource

   # 整数と文字列は列挙値を示唆する。

   # エディタは0・1・2として列挙する。
   export(int, "Warrior", "Magician", "Thief") var character_class
   # エディタは文字列名で列挙する。
   export(String, "Rebecca", "Mary", "Leah") var character_name

   # 名前付き列挙値

   # エディタはTHING_1・THING_2・ANOTHER_THINGとして列挙する。
   enum NamedEnum {THING_1, THING_2, ANOTHER_THING = -1}
   export (NamedEnum) var x

   # Pathとしての文字列

   # 文字列はファイルへのPathを表している。
   export(String, FILE) var f
   # 文字列はディレクトリへのPathを表している。
   export(String, DIR) var f
   # 文字列は、ファイルへのPathであり、ヒントとして提供されるカスタムフィルタになる。
   export(String, FILE, "*.txt") var f

   # グローバルファイルシステムでPathを使用することも可能だが、
   # "tool" モードのスクリプトでのみ使用できる。

   # 文字列は、グローバルファイルシステム内のPNGファイルへのPathになる。
   export(String, FILE, GLOBAL, "*.png") var tool_image
   # 文字列は、グローバルファイルシステム内のディレクトリへのPathになる。
   export(String, DIR, GLOBAL) var tool_dir

   # MULTILINE 設定は、複数の行に渡って編集するための大きな入力欄を表示するようエディタに指示する。
   export(String, MULTILINE) var text

   # エディタ入力範囲の制限

   # 0〜20の整数値を許可する。
   export(int, 20) var i
   # -10〜20の整数値を許可する。
   export(int, -10, 20) var j
   # 0.2ステップごとに、-10〜20までの浮動小数点数を許可する。
   export(float, -10, 20, 0.2) var k
   # 値 'y = exp(x)' を許可する。
   # ここで 'y' は、100〜1000で変化し、20ステップごとにスナップする。
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

   # シーン内の別ノードもエクスポートできる。

   export(NodePath) var node

エディタでスクリプトが実行されていない場合もエクスポートされたプロパティは編集可能であることに注意する必要がある。
これは、 :ref:`"tool" モードのスクリプト <doc_gdscript_tool_mode>` と組み合わせて使用できる。

.. todo::

   リンクの確認。



.. 英語の原文：事例
   Examples
   --------

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
       # but only in scripts in "tool" mode.

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
   editor, the exported properties are still editable. This can be used
   in conjunction with a :ref:`script in "tool" mode <doc_gdscript_tool_mode>`.

































ビットフラグのエクスポート
----------------------------------------------------

ビットフラグとして使用される整数は、1つのプロパティに複数の ``true``/``false`` (bool値)を格納できる。
エクスポートヒント ``int, FLAGS`` を使用した場合、エディタから設定できる。

::

   # 整数のビットを個別に編集する。
   export(int, FLAGS) var spell_elements = ELEMENT_WIND | ELEMENT_WATER

フラグを特定の数の名前付きフラグに制限することもできる。
構文は列挙構文に似ている。

::

   # エディタから指定されたフラグのいずれかを設定する。
   export(int, FLAGS, "Fire", "Water", "Earth", "Wind") var spell_elements = 0

この例では、 ``Fire`` の値は1、``Water`` の値は2、 ``Earth`` の値は4、 ``Wind`` の値は8に設定される(2の倍数)。
通常、定数はそれに応じて定義する必要がある(例： ``const ELEMENT_WIND = 8`` など)。

ビットフラグを使用するには、ビット単位の操作をある程度理解する必要がある。
疑わしい場合は、代わりにBool変数をエクスポートする必要がある。



.. 英語の原文：ビットフラグのエクスポート
   Exporting bit flags
   -------------------

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
------------------------------------

配列のエクスポートは機能するが、重要な注意事項がある。
通常の配列はすべてのクラスインスタンスに対してローカルに作成されるが、エクスポートされた配列はすべてのインスタンス間で *共有* される。
要は、1つのインスタンスで編集した場合、他のすべてのインスタンスで変更されると言うこと。
エクスポートされた配列は初期化子を持つことはできるが、定数式を使わなければならない。

::

   # すべてのインスタンス間で共有されるエクスポートされた配列。
   # 初期設定の値は、定数式になっている。

   export var a = [1, 2, 3]

   # エクスポートされた配列は、型を指定できる(以前と同じヒントを使用)。

   export(Array, int) var ints = [1,2,3]
   export(Array, int, "Red", "Green", "Blue") var enums = [2, 1, 0]
   export(Array, Array, float) var two_dimensional = [[1.0, 2.0], [3.0, 4.0]]

   # 初期設定値は省略できるが、割り当てられない場合はnullが割り振られる。

   export(Array) var b
   export(Array, PackedScene) var scenes

   # 初期化された空のみ型付き配列も機能する。

   export var vector3s = PoolVector3Array()
   export var strings = PoolStringArray()

   # すべてのインスタンスに対してローカルに作成された通常の配列。
   # 初期設定値にはラインタイム値を含めることはできるが、エクスポートすることはできない。

   var c = [a, 2, 3]


.. 英語の原文：配列のエクスポート
   Exporting arrays
   ----------------

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

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
