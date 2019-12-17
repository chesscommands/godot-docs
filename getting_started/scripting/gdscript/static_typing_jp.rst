.. _doc_gdscript_static_typing_jp:

































GDScriptでの静的型付け
============================================

今回は、次のことを説明する。

- **GDScriptで型を使用する方法**
- **静的型はバグ回避に役立つ**

この新しい言語機能をどこでどのように使用するかは完全に利用者(開発者)次第だ。
一部の機密性の高い部分は、GDScriptでのみ使える。

静的型は、変数・定数・関数・引数・戻り値型に使用できる。

.. note::

   型付きGDScriptはGodot 3.1以降で使用可能になっている。


.. 英語の原文：GDScriptでの静的型付け
   Static typing in GDScript
   =========================

   In this guide, you will learn:

   -  **How to use types in GDScript**
   -  That **static types can help you avoid bugs**

   Where and how you use this new language feature is entirely up to you:
   you can use it only in some sensitive GDScript files, use it everywhere,
   or write code like you always did!

   Static types can be used on variables, constants, functions, parameters,
   and return types.

   .. note::

       Typed GDScript is available since Godot 3.1.


































静的型付けの概要
--------------------------------

型付きGDScriptを使う場合、Godotはコードの記述時に、さらに多くのエラーを検出する。
メソッドを呼び出すときの引数型が表示されるなど、作業中に作業者への情報提供がなされる。

在庫システムをプログラミングしていると仮定しよう。
``Item`` ノードをコーディング後に、 ``Inventory`` のコーディングに着手する。
そして、インベントリにアイテムを追加するには、コーディング作業者は、常に ``Item`` を ``Inventory.add`` メソッドに渡す必要がある。
型指定を行えば、これを強制できる。

::

   # Item.gd内作業
   class_name Item

   # Inventory.gd内作業
   class_name Inventory

   func add(reference: Item, amount: int = 1):
       var item = find_item(reference)
       if not item:
           item = _instance_item_from_db(reference)
           item.amount += amount

型付きGDScriptのもう1つの重要な利点は、新しい **警告システム** がある。
バージョン3.1以降、Godotはコードの記述時に警告を表示するようになった。
エンジンは、実行時に問題を引き起こす可能性のあるコードのセクションを識別するが、コードをそのまま残すかどうかを決定できる(訳者：誰が？作業者？警告システムが？)。
詳細は後ほど。。。

静的型は、より優れたコード補完オプションを提供する。
以下では、 ``PlayerController`` と言うクラスの動的型と静的型の補完オプションの違いを確認できる。

以前の作業で、ノード変数に保存し、自動補完の候補を残さないように、ドットを入力したことがある(訳者：無いけど？)。

.. figure:: ./img/typed_gdscript_code_completion_dynamic.png
   :alt: 動的なコード補完オプション

これは動的コードの結果。
Godotは、関数に渡すノードまたは値の型を知ることができない。
ただし、型を明示的に記述した場合、ノードからすべてのパブリックメソッドと変数を取得できるようになる。

.. figure:: ./img/typed_gdscript_code_completion_typed.png
   :alt: 型付きのコード補完オプション

将来的には、型指定されたGDScriptにより、コード性能が向上する。
実行時コンパイラ(ソフトウェア実行時にコンパイルを行う技法)およびその他のコンパイラの改善は既にロードマップにある！

全体的に、型付きプログラミングは、より構造化体験を提供する。
エラーを防ぎ、スクリプトの自己文書化の側面を改善する。
これは、チームや長期プロジェクトで作業している場合に特に役立つ。
今までのプログラミング経験上、開発者はほとんどの時間を他の人のコード読解や過去に書いて忘れてしまったコード読解をしている。
コードがより明確で構造化されているほど、理解が早くなり、より開発の進捗が上がりやすくなる。


.. 英語の原文：静的型付けの概要
   A brief look at static typing
   -----------------------------

   With typed GDScript, Godot can detect even more errors as you write
   code! It gives you and your teammates more information as you’re
   working, as the arguments’ types show up when you call a method.

   Imagine you’re programming an inventory system. You code an ``Item``
   node, then an ``Inventory``. To add items to the inventory, the people
   who work with your code should always pass an ``Item`` to the
   ``Inventory.add`` method. With types, you can enforce this:

   ::

       # In Item.gd
       class_name Item

       # In Inventory.gd
       class_name Inventory

       func add(reference: Item, amount: int = 1):
           var item = find_item(reference)
           if not item:
               item = _instance_item_from_db(reference)
           item.amount += amount

   Another significant advantage of typed GDScript is the new **warning
   system**. From version 3.1, Godot gives you warnings about your code as
   you write it: the engine identifies sections of your code that may lead
   to issues at runtime, but lets you decide whether or not you want to
   leave the code as it is. More on that in a moment.

   Static types also give you better code completion options. Below, you
   can see the difference between a dynamic and a static typed completion
   options for a class called ``PlayerController``.

   You’ve probably stored a node in a variable before, and typed a dot to
   be left with no autocomplete suggestions:

   .. figure:: ./img/typed_gdscript_code_completion_dynamic.png
      :alt: code completion options for dynamic

   This is due to dynamic code. Godot cannot know what node or value type
   you’re passing to the function. If you write the type explicitly
   however, you will get all public methods and variables from the node:

   .. figure:: ./img/typed_gdscript_code_completion_typed.png
      :alt: code completion options for typed

   In the future, typed GDScript will also increase code performance:
   Just-In-Time compilation and other compiler improvements are already
   on the roadmap!

   Overall, typed programming gives you a more structured experience. It
   helps prevent errors and improves the self-documenting aspect of your
   scripts. This is especially helpful when you’re working in a team or on
   a long-term project: studies have shown that developers spend most of
   their time reading other people’s code, or scripts they wrote in the
   past and forgot about. The clearer and the more structured the code, the
   faster it is to understand, the faster you can move forward.


































静的型付けの使用方法
----------------------------------------

変数または定数の型を定義するには、変数の名前の後ろにコロンを記述し、その後ろに型を打ち込む。
例えば、 ``var health: int`` などのように記述する。
これにより、変数の型は常に保てる。

::

   var damage: float = 10.5
   const MOVE_SPEED: float = 50.0

Godotは、コロンを記述したとき、型を推測するため、型を省略できる。

::

   var life_points := 4
   var damage := 10.5
   var motion := Vector2()

現在、次の3つの型を使用できる。

1. :ref:`Built-in <doc_gdscript_builtin_types>`
2. コアクラスとノード(``Object`` ・ ``Node`` ・ ``Area2D`` ・ ``Camera2D`` など)
3. 独自のカスタムクラス。
   :ref:`class_name <doc_scripting_continued_class_name>` 機能を確認し、エディタに型を作る。

.. note::

   Godotは割り当てられた値から自動的に設定するため、定数の型ヒントを記述する必要は無い。
   ただし、コードの意図をより明確にするために、引き続き行うことができる。

   訳者：ちょいちょい出現する "ヒント" とは何？
   そして、何を継続できるの？

.. todo::

   リンクの確認。


.. 英語の原文：静的型付けの使用方法
   How to use static typing
   ------------------------

   To define the type of a variable or a constant, write a colon after the
   variable’s name, followed by its type. E.g. ``var health: int``. This
   forces the variable's type to always stay the same:

   ::

       var damage: float = 10.5
       const MOVE_SPEED: float = 50.0

   Godot will try to infer types if you write a colon, but you omit the
   type:

   ::

       var life_points := 4
       var damage := 10.5
       var motion := Vector2()

   Currently you can use three types of… types:

   1. :ref:`Built-in <doc_gdscript_builtin_types>`
   2. Core classes and nodes (``Object``, ``Node``, ``Area2D``,
      ``Camera2D``, etc.)
   3. Your own, custom classes. Look at the new :ref:`class_name <doc_scripting_continued_class_name>`
      feature to register types in the editor.

   .. note::

       You don't need to write type hints for constants, as Godot sets it automatically from the assigned value. But you can still do so to make the intent of your code clearer.


































カスタム変数型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

カスタムクラスを含む任意のクラスを型として使用できる。
スクリプトでそれらを使用するには2つの方法が用意されている。
一つ目は、定数の型として使用するスクリプトをプリロードすること。

::

   const Rifle = preload('res://player/weapons/Rifle.gd')
   var my_rifle: Rifle

二つ目は、作成時に ``class_name`` キーワードを使用すること。
上記の例で言えば、Rifle.gdは次のようになる。

::

   extends Node2D
   class_name Rifle

``class_name`` を使用した場合、GodotはRifle型をエディタにグローバル登録し、定数にプリロードすること無く、どこでも使えるようになる。

::

   var my_rifle: Rifle



.. 英語の原文：カスタム変数型
   Custom variable types
   ~~~~~~~~~~~~~~~~~~~~~

   You can use any class, including your custom classes, as types. There
   are two ways to use them in scripts. The first method is to preload the
   script you want to use as a type in a constant:

   ::

       const Rifle = preload('res://player/weapons/Rifle.gd')
       var my_rifle: Rifle

   The second method is to use the ``class_name`` keyword when you create.
   For the example above, your Rifle.gd would look like this:

   ::

       extends Node2D
       class_name Rifle

   If you use ``class_name``, Godot registers the Rifle type globally in
   the editor, and you can use it anywhere, without having to preload it
   into a constant:

   ::

       var my_rifle: Rifle

































可変キャスト
~~~~~~~~~~~~~~~~~~~~~~~~

型キャストは、型付き言語の重要な概念になる。
キャストとは、ある型から別の型に変換すること(当然、型によって値も変わる)。

では、これを読んでいる読者は、ゲームから ``extends Area2D`` の敵を想像すること。
Playerに衝突し、 ``KinematicBody2D`` に ``PlayerController`` と呼ばれるスクリプトを添付する。
衝突を検出するには、 ``on_body_entered`` シグナルを使用する。
型付きコードでは、検出する本文は汎用の ``PhysicsBody2D`` であり、 ``_on_body_entered`` コールバックの ``PlayerController`` ではない。

訳者：結局何が言いたいの？

この ``PhysicsBody2D`` が ``as`` キャスティングキーワードを使用しているプレイヤーであり、コロン ``:`` を再度使用して変数にこの型を使用させるかどうかを確認できる。
これにより、変数は ``PlayerController`` 型に固定される。

::

   func _on_body_entered(body: PhysicsBody2D) -> void:
       var player := body as PlayerController
       if not player:
           return
       player.damage()

カスタム型を扱うため、 ``body`` が ``PlayerController`` を拡張しない場合、 ``player`` 変数は ``null`` に設定される。
これを利用し、bodyがplayerかどうかを確認できる。
そのキャストのおかげで、player変数の完全な自動補完も取得できる。

.. note::

   組み込み型でキャストしようとして失敗した場合、Godotはエラーをthrowする。



.. 英語の原文：可変キャスト
   Variable casting
   ~~~~~~~~~~~~~~~~

   Type casting is a key concept in typed languages.
   Casting is the conversion of a value from one type to another.

   Imagine an Enemy in your game, that ``extends Area2D``. You want it to
   collide with the Player, a ``KinematicBody2D`` with a script called
   ``PlayerController`` attached to it. You use the ``on_body_entered``
   signal to detect the collision. With typed code, the body you detect is
   going to be a generic ``PhysicsBody2D``, and not your
   ``PlayerController`` on the ``_on_body_entered`` callback.

   You can check if this ``PhysicsBody2D`` is your Player with the ``as``
   casting keyword, and using the colon ``:`` again to force the variable
   to use this type. This forces the variable to stick to the
   ``PlayerController`` type:

   ::

       func _on_body_entered(body: PhysicsBody2D) -> void:
           var player := body as PlayerController
           if not player:
               return
           player.damage()

   As we’re dealing with a custom type, if the ``body`` doesn’t extend
   ``PlayerController``, the ``player``\ variable will be set to ``null``.
   We can use this to check if the body is the player or not. We will also
   get full autocompletion on the player variable thanks to that cast.

   .. note::

       If you try to cast with a built-in type and it fails, Godot will throw an error.

































安全圏
^^^^^^^^^^^^

キャストを使用し、安全処理を確保することもできる(安全圏)。
安全処理はGodot 3.1の新しいツールで、曖昧なコード行が型安全(タイプセーフ・type-safe)であることを通知する。
型付きコードと動的コードを組み合わせて使用できるため、Godotには命令が実行時にエラーをトリガーするかどうかを知るのに十分な情報が無い場合がある。

訳者：日本語の言い回しが複雑で理解できない。

これは、子ノードを取得したときに発生する。
例えば、タイマ例で説明する。
動的コードを使用した場合、 ``$Timer`` でノードを取得できる。
GDScriptは `duck-typing <https://stackoverflow.com/a/4205163/8125343>`__ をサポートしているため、タイマ型が ``Timer`` の場合、 ``Node`` と ``Object`` を拡張する2つのクラスに影響するのかな(訳者：全く日本語訳を読解できない)。
動的GDScriptでは、呼び出す必要のあるメソッドがある場合、ノードの型も気にしない。

キャストを使用し、ノードを取得するときに期待する型をGodotに伝えることができる( ``($Timer as Timer)`` ・ ``($Player as KinematicBody2D)`` など)。
Godotは型が機能することを保証する。
スクリプトエディタの左側に表示される行番号が緑色に変わる。

.. figure:: ./img/typed_gdscript_safe_unsafe_line.png
   :alt: 安全処理と非安全処理

   安全処理と非安全処理

.. note::

   エディタ設定で安全処理をオフにすることや色を変更できる。


.. 英語の原文：安全圏
   Safe lines
   ^^^^^^^^^^

   You can also use casting to ensure safe lines. Safe lines are a new
   tool in Godot 3.1 to tell you when ambiguous lines of code are
   type-safe. As you can mix and match typed and dynamic code, at times,
   Godot doesn’t have enough information to know if an instruction will trigger
   an error or not at runtime.

   This happens when you get a child node. Let’s take a timer for example:
   with dynamic code, you can get the node with ``$Timer``. GDScript
   supports `duck-typing <https://stackoverflow.com/a/4205163/8125343>`__,
   so even if your timer is of type ``Timer``, it is also a ``Node`` and an
   ``Object``, two classes it extends. With dynamic GDScript, you also
   don’t care about the node’s type as long as it has the methods you need
   to call.

   You can use casting to tell Godot the type you expect when you get a
   node: ``($Timer as Timer)``, ``($Player as KinematicBody2D)``, etc.
   Godot will ensure the type works and if so, the line number will turn
   green at the left of the script editor.

   .. figure:: ./img/typed_gdscript_safe_unsafe_line.png
      :alt: Safe vs Unsafe Line

      Safe vs Unsafe Line

   .. note::

       You can turn off safe lines or change their color in the editor settings.

































矢印で関数の戻り値の型を定義 ->
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関数の戻り値の型を定義するには、宣言の後ろにハイフンと山形右括弧 ``->`` を書き、その後ろに戻り値の型を続ける。
::

   func _process(delta: float) -> void:
       pass

``void`` 型は、関数が何も返さないことを意味する。
変数と同様に、任意の型を使用できる。

::

   func hit(damage: float) -> bool:
       health_points -= damage
       return health_points <= 0

戻り型として独自のノードを使用することもできる。

::

   # Inventory.gd

   # インベントリにアイテムを追加して返却。
   func add(reference: Item, amount: int) -> Item:
       var item: Item = find_item(reference)
       if not item:
           item = ItemDatabase.get_instance(reference)
       item.amount += amount
       return item



.. 英語の原文：矢印で関数の戻り値の型を定義 ->
   Define the return type of a function with the arrow ->
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   To define the return type of a function, write a dash and a right angle
   bracket ``->`` after its declaration, followed by the return type:

   ::

       func _process(delta: float) -> void:
           pass

   The type ``void`` means the function does not return anything. You can
   use any type, as with variables:

   ::

       func hit(damage: float) -> bool:
           health_points -= damage
           return health_points <= 0

   You can also use your own nodes as return types:

   ::

       # Inventory.gd

       # Adds an item to the inventory and returns it.
       func add(reference: Item, amount: int) -> Item:
           var item: Item = find_item(reference)
           if not item:
               item = ItemDatabase.get_instance(reference)
           item.amount += amount
           return item

































型付きまたは動的：1つのスタイルに固着する
----------------------------------------------------------------------------------

型指定されたGDScriptと動的GDScriptは、同じプロジェクト内で共存できる。
ただし、コードベースと対を一貫しているため、どちらのスタイルにも固着することを勧める。
同じガイドラインに従うならば、全員が協力しやすくなり、他の人のコードを素早く読解できる。

型付きコードはもう少し記述量は増えるが、上記で説明した利点が得られる。
動的スタイルの同じ空のスクリプトを例を次に示す。

::

   extends Node
      func _ready():
          pass
      func _process(delta):
          pass

そして、静的型付けを以下に示す。

::

   extends Node
      func _ready() -> void:
          pass
      func _process(delta: float) -> void:
          pass

上記通り、エンジンの仮想メソッドで型を使用することができる。
他のメソッドと同様に、シグナルコールバックも型を使用できる。
動的スタイルの ``body_entered`` シグナルは次の通り。

::

   func _on_Area2D_body_entered(body):
       pass

そして、同じコールバックで、型のヒントがある。

::

   func _on_area_entered(area: CollisionObject2D) -> void:
       pass

交換の手間暇掛からない(訳者：何の交換？)。
例：独自型の ``CollisionObject2D`` を使用して、引数を自動的にキャストする。

::

   func _on_area_entered(bullet: Bullet) -> void:
       if not bullet:
          return
       take_damage(bullet.damage)

``bullet`` 変数は、ここで ``CollisionObject2D`` を保持できるが、プロジェクト用に作成したノードである ``Bullet`` であることを確認する。
``Area2D`` や ``Bullet`` を拡張しないノードなど、他の何かである場合、 ``bullet`` 変数は ``null`` になる。


.. 英語の原文：型付きまたは動的：1つのスタイルに固着する
   Typed or dynamic: stick to one style
   ------------------------------------

   Typed GDScript and dynamic GDScript can coexist in the same project. But
   I recommended to stick to either style for consistency in your codebase,
   and for your peers. It’s easier for everyone to work together if you
   follow the same guidelines, and faster to read and understand other
   people’s code.

   Typed code takes a little more writing, but you get the benefits we
   discussed above. Here’s an example of the same, empty script, in a
   dynamic style:

   ::

       extends Node
           func _ready():
               pass
           func _process(delta):
               pass

   And with static typing:

   ::

       extends Node
           func _ready() -> void:
               pass
           func _process(delta: float) -> void:
               pass

   As you can see, you can also use types with the engine’s virtual
   methods. Signal callbacks, like any methods, can also use types. Here’s
   a ``body_entered`` signal in a dynamic style:

   ::

       func _on_Area2D_body_entered(body):
           pass

   And the same callback, with type hints:

   ::

       func _on_area_entered(area: CollisionObject2D) -> void:
           pass

   You’re free to replace, e.g. the ``CollisionObject2D``, with your own type,
   to cast parameters automatically:

   ::

       func _on_area_entered(bullet: Bullet) -> void:
           if not bullet:
               return
           take_damage(bullet.damage)

   The ``bullet`` variable could hold any ``CollisionObject2D`` here, but
   we make sure it is our ``Bullet``, a node we created for our project. If
   it’s anything else, like an ``Area2D``, or any node that doesn’t extend
   ``Bullet``, the ``bullet`` variable will be ``null``.


































警告システム
------------------------

警告システムは、型付きGDScriptを補完する。
開発時に発見ができず、実行時にエラー発生につながる可能性のある失敗を回避するのに役立つ。

``GDScript`` と言う新しいセクションの下のプロジェクト設定で警告を設定できる。

.. figure:: ./img/typed_gdscript_warning_system_settings.png
   :alt: 警告システムのプロジェクト設定

   警告システムのプロジェクト設定

アクティブなGDScriptファイルの警告の一覧は、スクリプトエディタのステータスバーで確認できる。
次の例には3つの警告がある。

.. figure:: ./img/typed_gdscript_warning_example.png
   :alt: 警告システムの例

   警告システムの例

1つのファイル内の特定の警告を無視するには、 ``#warning-ignore:warning-id`` と言う形式の特別なコメントを挿入するか、警告の説明の右側にある無視リンクをクリックする。
Godotは対応する行の上にコメントを追加し、コードは対応する警告をトリガーしなくなる。

.. figure:: ./img/typed_gdscript_warning_system_ignore.png
   :alt: 警告システム無視の例

   警告システム無視の例

警告はゲームの実行を妨げないが、必要に応じてエラーに変えることができる。
この方法では、すべての警告を修正しない限り、ゲームはコンパイルされない。
このオプションをオンにするには、プロジェクト設定の ``GDScript`` セクションを開く。
エラーがオンになるときに警告が表示される前の例と同じファイルを次に示す(訳者：また日本語の言い回しが難しいぞ)。
.. figure:: ./img/typed_gdscript_warning_system_errors.png
   :alt: エラーとしての警告

   エラーとしての警告


.. 英語の原文：警告システム
   Warning system
   --------------

   The warning system complements typed GDScript. It’s here to help you
   avoid mistakes that are hard to spot during development, and that may
   lead to runtime errors.

   You can configure warnings in the Project Settings under a new section
   called ``GDScript``:

   .. figure:: ./img/typed_gdscript_warning_system_settings.png
      :alt: warning system project settings

      warning system project settings

   You can find a list of warnings for the active GDScript file in the
   script editor’s status bar. The example below has 3 warnings:

   .. figure:: ./img/typed_gdscript_warning_example.png
      :alt: warning system example

      warning system example

   To ignore specific warnings in one file, insert a special comment of the
   form ``#warning-ignore:warning-id``, or click on the ignore link to the
   right of the warning’s description. Godot will add a comment above the
   corresponding line and the code won’t trigger the corresponding warning
   anymore:

   .. figure:: ./img/typed_gdscript_warning_system_ignore.png
      :alt: warning system ignore example

      warning system ignore example

   Warnings won’t prevent the game from running, but you can turn them into
   errors if you’d like. This way your game won’t compile unless you fix
   all warnings. Head to the ``GDScript`` section of the Project Settings to
   turn on this option. Here’s the same file as the previous example with
   warnings as errors turned on:

   .. figure:: ./img/typed_gdscript_warning_system_errors.png
      :alt: warnings as errors

      warnings as errors

































型を指定できない場合
----------------------------------------

今回の説明の締めくくりとして、型ヒントを使用できない事例を補うことにする。
以下のすべての例は **エラーをトリガーする** 。

Enumsを型として使用することはできない。

::

   enum MoveDirection {UP, DOWN, LEFT, RIGHT}
   var current_direction: MoveDirection

配列内の個々のメンバの型を指定することはできない。
これにより、エラーが発生する。

::

   var enemies: Array = [$Goblin: Enemy, $Zombie: Enemy]

``for`` キーワードがループする各要素には既に異なる型があるため、 ``for`` ループ型での割り当てを強制することはできない。
ゆえに、開発者はそれを **記述できない** 。

::

   var names = ['John', 'Marta', 'Samantha', 'Jimmy']
   for name: String in names:
       pass

2つのスクリプトは、循環的に相互に依存することができない。

::

   # Player.gd
   extends Area2D
   class_name Player

   var rifle: Rifle

::

   # Rifle.gd
   extends Area2D
   class_name Rifle

   var player: Player


.. 英語の原文：型を指定できない場合
   Cases where you can’t specify types
   -----------------------------------

   To wrap up this introduction, let’s cover a few cases where you can’t
   use type hints. All the examples below **will trigger errors**.

   You can’t use Enums as types:

   ::

       enum MoveDirection {UP, DOWN, LEFT, RIGHT}
       var current_direction: MoveDirection

   You can’t specify the type of individual members in an array. This will
   give you an error:

   ::

       var enemies: Array = [$Goblin: Enemy, $Zombie: Enemy]

   You can’t force the assignment of types in a ``for`` loop, as each
   element the ``for`` keyword loops over already has a different type. So you
   **cannot** write:

   ::

       var names = ['John', 'Marta', 'Samantha', 'Jimmy']
       for name: String in names:
           pass

   Two scripts can’t depend on each other in a cyclic fashion:

   ::

       # Player.gd
       extends Area2D
       class_name Player

       var rifle: Rifle

   ::

       # Rifle.gd
       extends Area2D
       class_name Rifle

       var player: Player


































概要
------------

型付きGDScriptは強力な道具だ。
GDScriptのバージョン3.1から利用可能になり、より構造化されたコードの記述・一般的なエラーの回避・スケーラ部UR菜システム作成を支援する。
将来的には、静的型は、今後のコンパイラの最適化のおかげで、素晴らしい性能向上をもたらす。


.. 英語の原文：概要
   Summary
   -------

   Typed GDScript is a powerful tool. Available as of version 3.1 of Godot, it
   helps you write more structured code, avoid common errors, and
   create scalable systems. In the future, static types will also bring you
   a nice performance boost thanks to upcoming compiler optimizations.

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
