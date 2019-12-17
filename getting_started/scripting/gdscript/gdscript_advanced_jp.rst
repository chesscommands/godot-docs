.. _doc_gdscript_more_efficiently_jp:


GDScript：動的言語の紹介
================================================

.. 英語の原文：GDScript：動的言語の紹介
   GDScript: An introduction to dynamic languages
   ==============================================

































概要
--------

今回の説明では、GDScriptをより効率的に使用する方法のクイックリファレンスを目的としている。
言語固有の一般的な事例に焦点を当てているが、動的に型指定された言語に関する多くの情報も補っている。

これは、動的型付け言語の経験がほとんど無いか全くないプログラマーに、特に役立つことを意図している。

.. 英語の原文：概要
   About
   -----

   This tutorial aims to be a quick reference for how to use GDScript more
   efficiently. It focuses on common cases specific to the language, but
   also covers a lot of information on dynamically typed languages.

   It's meant to be especially useful for programmers with little or no previous
   experience with dynamically typed languages.




































動的な性質
--------------------

.. 英語の原文：動的な性質
   Dynamic nature
   --------------



































動的型付けの長所と短所
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GDScriptは、動的に型指定された言語だ。
そのため、その主な長所は次の通り。

- 言語は簡素で習得しやすい。
- ほとんどのコードは、手間をかけずに素早く作成及び変更できる。
- 記述されたコードを短く(簡素に)できるため、エラーとミスを最小限に抑えられる。
- コードが読みやすい(混乱が少ない)。
- テストにコンパイルは必要ない。
- ランタイムが小さい。
- 型付けの作法用ポリモーフィズムを備えている。

主な短所は次の通り。

- 静的に型付けされた言語よりもパフォーマンスが低下する。
- リファクタリングがより困難(記号追跡ができない)
- 通常、静的に型指定された言語でコンパイル時に検出されるいくつかのエラーは、コードの実行中にのみ表示される
  （式の解析がより厳密であるため）。
- コード補完の柔軟性が低い
  (一部の変数タイプは実行時にのみ認識される)。

これを現実に変換した場合、Godot+GDScriptは、ゲームを迅速かつ効率的に作成するために設計された組み合わせの結論が導き出される。
計算量が非常に多く、エンジンの組み込みツール(ベクター型・物理エンジン・数学ライブラリなど)の恩恵を受けられないゲームでは、C++言語を使用する可能性もある。
これにより、GDScriptでゲームのほとんどを作成し、性能向上が必要な領域に小さなC++を追加できる。



.. 英語の原文：動的型付けの長所と短所
   Pros & cons of dynamic typing
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   GDScript is a Dynamically Typed language. As such, its main advantages
   are that:

   -  The language is simple and easy to learn.
   -  Most code can be written and changed quickly and without hassle.
   -  Less code written means less errors & mistakes to fix.
   -  Easier to read the code (less clutter).
   -  No compilation is required to test.
   -  Runtime is tiny.
   -  Duck-typing and polymorphism by nature.

   While the main disadvantages are:

   -  Less performance than statically typed languages.
   -  More difficult to refactor (symbols can't be traced)
   -  Some errors that would typically be detected at compile time in
    statically typed languages only appear while running the code
    (because expression parsing is more strict).
   -  Less flexibility for code-completion (some variable types are only
    known at run-time).

   This, translated to reality, means that Godot+GDScript are a combination
   designed to create games quickly and efficiently. For games that are very
   computationally intensive and can't benefit from the engine built-in
   tools (such as the Vector types, Physics Engine, Math library, etc), the
   possibility of using C++ is present too. This allows you to still create most of the
   game in GDScript and add small bits of C++ in the areas that need
   a performance boost.



































変数と割り当て
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

動的に型付けされた言語のすべての変数は、 "variant" のようなもの。
これは、その型が固定されておらず、割り当てによってのみ変更されることを意味する。
以下、例。

Static:

.. code:: cpp

   int a; // 初期化されていない値
   a = 5; // 有効代入
   a = "Hi!"; // 無効代入

Dynamic:

::

   var a # 初期設定：null
   a = 5 # 有効代入：変数aは、整数値。
   a = "Hi!" # 有効代入：変数aは、文字列型に代わる。


.. 英語の原文：変数と割り当て
   Variables & assignment
   ~~~~~~~~~~~~~~~~~~~~~~

   All variables in a dynamically typed language are "variant"-like. This
   means that their type is not fixed, and is only modified through
   assignment. Example:

   Static:

   .. code:: cpp

     int a; // Value uninitialized
     a = 5; // This is valid
     a = "Hi!"; // This is invalid

   Dynamic:

   ::

     var a # null by default
     a = 5 # Valid, 'a' becomes an integer
     a = "Hi!" # Valid, 'a' changed to a string




































関数の引数
~~~~~~~~~~~~~~~~~~~~

関数も動的な性質を持っている。
要は、次のように、異なる引数で呼び出すことができる。

Static:

.. code:: cpp

   void print_value(int value) {

       printf("value is %i\n", value);
       }

       [..]

       print_value(55); // 有効な関数呼び出し。
       print_value("Hello"); // 無効なな関数呼び出し。

Dynamic:

::

   func print_value(value):
       print(value)

       [..]

       print_value(55) # 有効
       print_value("Hello") # 有効



.. 英語の原文：関数の引数
   As function arguments:
   ~~~~~~~~~~~~~~~~~~~~~~

   Functions are of dynamic nature too, which means they can be called with
   different arguments, for example:

   Static:

   .. code:: cpp

     void print_value(int value) {

         printf("value is %i\n", value);
     }

     [..]

     print_value(55); // Valid
     print_value("Hello"); // Invalid

   Dynamic:

   ::

     func print_value(value):
         print(value)

     [..]

     print_value(55) # Valid
     print_value("Hello") # Valid




































ポインタと参照
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CやC++(およびある程度のJavaやC#)などの静的言語では、変数と変数へのポインタ/参照との間には区別がある。
後者は、元の関数への参照を渡すことにより、オブジェクトを他の関数で変更できる。

C#またはJavaでは、組み込み型(int・float・場合によりString)ではないものは、すべてポインタまたは参照にあたる。
参照も自動的にガーベージコレクションされる。
要は、参照が使用されなくなると削除される。
動的に型付けされた言語もこのメモリモデルを使用する傾向がある。
以下、例。

-  C++:

.. code:: cpp

   void use_class(SomeClass *instance) {

   instance->use();
   }

   void do_something() {

       SomeClass *instance = new SomeClass; // ポインタとして作成
       use_class(instance); // ポインタとして渡す。
       delete instance; // 削除しなければメモリリークが発生する(訳者：訳合ってる？)。
   }

-  Java:

.. code:: java

   @Override
   public final void use_class(SomeClass instance) {

   instance.use();
   }

   public final void do_something() {

       SomeClass instance = new SomeClass(); // 参照として作成
       use_class(instance); // 参照として渡す。
       // ガーベージコレクタは、使用していないときにそれを取り除き、
       // ゲームを1秒間ランダムにフリーズする。
   }

-  GDScript:

::

   func use_class(instance); # クラスの種類を気にしない。
   instance.use() # ".use()" メソッドを持つクラスで動作する。

   func do_something():
       var instance = SomeClass.new() # 参照として作成
       use_class(instance) # 参照として渡す。
       # 参照されないため削除(ガーベージコレクタ対象に)された。

GDScriptでは、基本型(int・float・String・vector)のみが値によって関数に渡される(値がコピーされて渡される)。
（訳者：要は、値渡しってこと？）
他のすべての(インスタンス・配列・辞書など)は参照として渡される。
:ref:`class_Reference` を継承するクラス(何も指定しない場合の初期設定)は、使用しない場合は解放されるが、 :ref:`class_Object` から手動で継承する場合は、手動のメモリ管理も許可される。

.. todo::

   リンクの確認。


.. 英語の原文：ポインタと参照
   Pointers & referencing:
   ~~~~~~~~~~~~~~~~~~~~~~~

   In static languages, such as C or C++ (and to some extent Java and C#),
   there is a distinction between a variable and a pointer/reference to a
   variable. The latter allows the object to be modified by other functions
   by passing a reference to the original one.

   In C# or Java, everything not a built-in type (int, float, sometimes
   String) is always a pointer or a reference. References are also
   garbage-collected automatically, which means they are erased when no
   longer used. Dynamically typed languages tend to use this memory model,
   too. Some Examples:

   -  C++:

   .. code:: cpp

     void use_class(SomeClass *instance) {

         instance->use();
     }

     void do_something() {

         SomeClass *instance = new SomeClass; // Created as pointer
         use_class(instance); // Passed as pointer
         delete instance; // Otherwise it will leak memory
     }

   -  Java:

   .. code:: java

     @Override
     public final void use_class(SomeClass instance) {

         instance.use();
     }

     public final void do_something() {

         SomeClass instance = new SomeClass(); // Created as reference
         use_class(instance); // Passed as reference
         // Garbage collector will get rid of it when not in
         // use and freeze your game randomly for a second
     }

   -  GDScript:

   ::

     func use_class(instance); # Does not care about class type
         instance.use() # Will work with any class that has a ".use()" method.

     func do_something():
         var instance = SomeClass.new() # Created as reference
         use_class(instance) # Passed as reference
         # Will be unreferenced and deleted

   In GDScript, only base types (int, float, string and the vector types)
   are passed by value to functions (value is copied). Everything else
   (instances, arrays, dictionaries, etc) is passed as reference. Classes
   that inherit :ref:`class_Reference` (the default if nothing is specified)
   will be freed when not used, but manual memory management is allowed too
   if inheriting manually from :ref:`class_Object`.





































配列
------------

動的に型付けされた言語の配列は、内部に様々な混合データ型を含むことができ、常に動的扱いする(いつでも大きさを変更できる)。
以下、静的に型付けされた言語の配列の例を比較する。

.. code:: cpp

   int *array = new int[4]; // 配列の作成
   array[0] = 10; // 手動初期化
   array[1] = 20; // 型の混在はできない(今回で言えば、すべて整数のみを代入する)
   array[2] = 40;
   array[3] = 60;
   // 配列の大きさ変更不可
   use_array(array); // ポインタとして渡す。
   delete[] array; // 手動開放必須

   // もしくは、

   std::vector<int> array;
   array.resize(4);
   array[0] = 10; // 手動で初期化
   array[1] = 20; // 型の混在はできない
   array[2] = 40;
   array[3] = 60;
   array.resize(3); // 配列と異なり、大きさの変更はできる。
   use_array(array); // 渡された参照または値(訳者：どういう意味？)
   // スタックが終了されれば解放される(訳者：スタックとは？)。

GDScript:

::

   var array = [10, "hello", 40, 60] # 簡素な記述で、かつ型の混在が可能
   array.resize(3) # 配列の大きさも変更可能
   use_array(array) # 参照として渡す。
   # 使用されない場合、解放される。

動的に型付けされた言語では、配列は他のデータ型(リストなど)としても機能する。

::

   var array = []
   array.append(4)
   array.append(5)
   array.pop_front()

順序なしの場合：

::

   var a = 20
   if a in [10, 20, 30]:
       print("勝者がいる！")



.. 英語の原文：配列
   Arrays
   ------

   Arrays in dynamically typed languages can contain many different mixed
   datatypes inside and are always dynamic (can be resized at any time).
   Compare for example arrays in statically typed languages:

   .. code:: cpp

     int *array = new int[4]; // Create array
     array[0] = 10; // Initialize manually
     array[1] = 20; // Can't mix types
     array[2] = 40;
     array[3] = 60;
     // Can't resize
     use_array(array); // Passed as pointer
     delete[] array; // Must be freed

     // or

     std::vector<int> array;
     array.resize(4);
     array[0] = 10; // Initialize manually
     array[1] = 20; // Can't mix types
     array[2] = 40;
     array[3] = 60;
     array.resize(3); // Can be resized
     use_array(array); // Passed reference or value
     // Freed when stack ends

   And in GDScript:

   ::

     var array = [10, "hello", 40, 60] # Simple, and can mix types
     array.resize(3) # Can be resized
     use_array(array) # Passed as reference
     # Freed when no longer in use

   In dynamically typed languages, arrays can also double as other
   datatypes, such as lists:

   ::

     var array = []
     array.append(4)
     array.append(5)
     array.pop_front()

   Or unordered sets:

   ::

     var a = 20
     if a in [10, 20, 30]:
         print("We have a winner!")





































辞書
------------

辞書は、動的に型付けされた言語の強力なツール。
静的に型付けされた言語(C++やC#など)のプログラマのほとんどは、その存在を無視し、生活を不必要に難しくしている。
通常、このデータ型はそのような言語には存在しない(または限定された形式でのみ)。

辞書は、キーまたは値として使用されるデータ型を完全に無視して、任意の値を他の値にマッピングできる。
一般的な考えに反して、ハッシュテーブルを使用して実装できるため、効率的になる。
実際、これらは非常に効率的であるため、一部の言語では配列を辞書として実装することができる。
以下、例。

::

   var d = {"name": "John", "age": 22} # 簡単な構文
   print("Name: ", d["name"], " Age: ", d["age"])

辞書も動的であり、キーはいつでも追加または削除できる。
労力は皆無に近い。

::

   d["mother"] = "Rebecca" # Addition(訳者：追加したってこと？)
   d["age"] = 11 # 値の変更
   d.erase("name") # 削除

ほとんどの場合、2次元配列は、多くの場合辞書を使用してより簡単に実装できる。
簡単な戦艦ゲームの例を次に示す。

::

   # 戦艦ゲーム

   const SHIP = 0
   const SHIP_HIT = 1
   const WATER_HIT = 2

   var board = {}

   func initialize():
       board[Vector2(1, 1)] = SHIP
       board[Vector2(1, 2)] = SHIP
       board[Vector2(1, 3)] = SHIP

   func missile(pos):
       if pos in board: # 渡された引数の場所を基準に処理をする。
           if board[pos] == SHIP: # 戦艦を発見したため、射撃開始
              board[pos] = SHIP_HIT
           else:
              print("攻撃が当たった！") # この場所で、球を当てた。
       else: # 水があるだけ。それ以外は何も。
           board[pos] = WATER_HIT

   func game():
       initialize()
       missile(Vector2(1, 1))
       missile(Vector2(5, 8))
       missile(Vector2(2, 3))

辞書は、データマークアップまたはクイック構造としても使用できる。
GDScriptの辞書はPython辞書に似ているが、Lua文体の構文とインデックス付けも支援しているため、初期状態と簡単な構造体の記述に役立つ。

::

   # 同様例。Lua文体の手助け
   # この構文は、遙かに読みやすく使いやすい。
   # 他のGDScript識別子と同様に、この形式で記述されたキーは数字で始めることはできない。

   var d = {
       name = "John",
       age = 22
   }

   print("Name: ", d.name, " Age: ", d.age) # "." によるインデックス付け。

   # 索引付け

   d["mother"] = "Rebecca"
   d.mother = "Caroline" # これは、新しいキーを作成するためにも機能する。



.. 英語の原文：辞書
   Dictionaries
   ------------

   Dictionaries are a powerful tool in dynamically typed languages.
   Most programmers that come from statically typed languages (such as C++
   or C#) ignore their existence and make their life unnecessarily more
   difficult. This datatype is generally not present in such languages (or
   only in limited form).

   Dictionaries can map any value to any other value with complete
   disregard for the datatype used as either key or value. Contrary to
   popular belief, they are efficient because they can be implemented
   with hash tables. They are, in fact, so efficient that some languages
   will go as far as implementing arrays as dictionaries.

   Example of Dictionary:

   ::

     var d = {"name": "John", "age": 22} # Simple syntax
     print("Name: ", d["name"], " Age: ", d["age"])

   Dictionaries are also dynamic, keys can be added or removed at any point
   at little cost:

   ::

     d["mother"] = "Rebecca" # Addition
     d["age"] = 11 # Modification
     d.erase("name") # Removal

   In most cases, two-dimensional arrays can often be implemented more
   easily with dictionaries. Here's a simple battleship game example:

   ::

     # Battleship game

     const SHIP = 0
     const SHIP_HIT = 1
     const WATER_HIT = 2

     var board = {}

     func initialize():
         board[Vector2(1, 1)] = SHIP
         board[Vector2(1, 2)] = SHIP
         board[Vector2(1, 3)] = SHIP

     func missile(pos):
         if pos in board: # Something at that pos
             if board[pos] == SHIP: # There was a ship! hit it
                 board[pos] = SHIP_HIT
             else:
                 print("Already hit here!") # Hey dude you already hit here
         else: # Nothing, mark as water
             board[pos] = WATER_HIT

     func game():
         initialize()
         missile(Vector2(1, 1))
         missile(Vector2(5, 8))
         missile(Vector2(2, 3))

   Dictionaries can also be used as data markup or quick structures. While
   GDScript's dictionaries resemble python dictionaries, it also supports Lua
   style syntax and indexing, which makes it useful for writing initial
   states and quick structs:

   ::

     # Same example, lua-style support.
     # This syntax is a lot more readable and usable
     # Like any GDScript identifier, keys written in this form cannot start with a digit.

     var d = {
         name = "John",
         age = 22
     }

     print("Name: ", d.name, " Age: ", d.age) # Used "." based indexing

     # Indexing

     d["mother"] = "Rebecca"
     d.mother = "Caroline" # This would work too to create a new key




































For & while
----------------------

一部の静的に型付けされた言語での反復は、非常に複雑になる可能性がある。

.. code:: cpp

   const char* strings = new const char*[50];

   [..]

   for (int i = 0; i < 50; i++)
   {

   printf("Value: %s\n", i, strings[i]);
   }

   // Even in STL:

   for (std::list<std::string>::const_iterator it = strings.begin(); it != strings.end(); it++) {

   std::cout << *it << std::endl;
   }

これは、動的に型付けされた言語で大幅に簡素化される。

::

   for s in strings:
       print(s)

コンテナのデータ型(配列と辞書)は反復可能になっている。
辞書はキーの反復を許可する。

::

   for key in dict:
       print(key, " -> ", dict[key])

インデックスを使用した反復にも使える。

::

   for i in range(strings.size()):
       print(strings[i])

range()関数は3つまでの引数を取る。

::

   range(n) # 0 から n-1 になる。
   range(b, n) # b から n-1 になる。
   range(b, n, s) # s のステップごとに b から n-1 に移動する。

以下、静的に型付けされたプログラミング言語の例

.. code:: cpp

   for (int i = 0; i < 10; i++) {}

   for (int i = 5; i < 10; i++) {}

   for (int i = 5; i < 10; i += 2) {}

プログラムを以下に書き換え。

::

   for i in range(10):
       pass

   for i in range(5, 10):
       pass

   for i in range(5, 10, 2):
       pass

そして、逆方向の反復は、負のカウンタを通して行われる。

::

   for (int i = 10; i > 0; i--) {}

以下に置き換え。

::

   for i in range(10, 0, -1):
       pass


.. 英語の原文：For & while
   For & while
   -----------

   Iterating in some statically typed languages can be quite complex:

   .. code:: cpp

     const char* strings = new const char*[50];

     [..]

     for (int i = 0; i < 50; i++)
     {

         printf("Value: %s\n", i, strings[i]);
     }

     // Even in STL:

     for (std::list<std::string>::const_iterator it = strings.begin(); it != strings.end(); it++) {

         std::cout << *it << std::endl;
     }

   This is usually greatly simplified in dynamically typed languages:

   ::

     for s in strings:
         print(s)

   Container datatypes (arrays and dictionaries) are iterable. Dictionaries
   allow iterating the keys:

   ::

     for key in dict:
         print(key, " -> ", dict[key])

   Iterating with indices is also possible:

   ::

     for i in range(strings.size()):
         print(strings[i])

   The range() function can take 3 arguments:

   ::

     range(n) # Will go from 0 to n-1
     range(b, n) # Will go from b to n-1
     range(b, n, s) # Will go from b to n-1, in steps of s

   Some statically typed programming language examples:

   .. code:: cpp

     for (int i = 0; i < 10; i++) {}

     for (int i = 5; i < 10; i++) {}

     for (int i = 5; i < 10; i += 2) {}

   Translate to:

   ::

     for i in range(10):
         pass

     for i in range(5, 10):
         pass

     for i in range(5, 10, 2):
         pass

   And backwards looping is done through a negative counter:

   ::

     for (int i = 10; i > 0; i--) {}

   Becomes:

   ::

     for i in range(10, 0, -1):
         pass




































While
----------

while()ループはどこでも同じ。

::

   var i = 0

   while i < strings.size():
       print(strings[i])
       i += 1


.. 英語の原文：While
   While
   -----

   while() loops are the same everywhere:

   ::

     var i = 0

     while i < strings.size():
         print(strings[i])
         i += 1




































カスタムイテレータ
------------------------------------

スクリプトでVariantクラスの ``_iter_init`` ・ ``_iter_next`` ・ ``_iter_get`` 関数をオーバライドすることで、デフォルトのイテレータがニーズを十分に満たしていない場合にカスタムイテレータを作成できる。
前方反復子の実装例は次の通り。

::

   class ForwardIterator:
       var start
       var current
       var end
       var increment

       func _init(start, stop, increment):
           self.start = start
           self.current = start
           self.end = stop
           self.increment = increment

       func should_continue():
           return (current < end)

       func _iter_init(arg):
           current = start
           return should_continue()

       func _iter_next(arg):
           current += increment
           return should_continue()

       func _iter_get(arg):
           return current

当然のように、他のイテレータと同様に使用できる。

::

   var itr = ForwardIterator.new(0, 6, 2)
   for i in itr:
       print(i) # 0・2・4を出力

必ず ``_iter_init`` でイテレータの状態をリセットすること。
しなければ、カスタムイテレータを使用するネストされたforループが期待通りに動作しない。


















.. 英語の原文：カスタムイテレータ
   Custom iterators
   ----------------
   You can create custom iterators in case the default ones don't quite meet your
   needs by overriding the Variant class's ``_iter_init``, ``_iter_next``, and ``_iter_get``
   functions in your script. An example implementation of a forward iterator follows:

   ::

     class ForwardIterator:
         var start
         var current
         var end
         var increment

         func _init(start, stop, increment):
             self.start = start
             self.current = start
             self.end = stop
             self.increment = increment

         func should_continue():
             return (current < end)

         func _iter_init(arg):
             current = start
             return should_continue()

         func _iter_next(arg):
             current += increment
             return should_continue()

         func _iter_get(arg):
             return current

   And it can be used like any other iterator:

   ::

     var itr = ForwardIterator.new(0, 6, 2)
     for i in itr:
         print(i) # Will print 0, 2, and 4

   Make sure to reset the state of the iterator in ``_iter_init``, otherwise nested
   for-loops that use custom iterators will not work as expected.


































ダックタイピング
--------------------------------

静的に型付けされた言語から動的な型に移行するときに把握するのが最も難しい概念の1つは、ダックタイピングのなる。
ダックタイピングにより、全体的なコード設計が非常に簡単かつ簡単に記述できるが、どのように機能するかは明らかではない。

例として、大きな岩がトンネルに落ちて、途中ですべてを壊している状況を想像すること。
静的に型付けされた言語での岩のコードは次のようになる。

.. code:: cpp

   void BigRollingRock::on_object_hit(Smashable *entity) {

       entity->smash();
   }

この方法では、岩によって破壊される可能性のあるすべての物がSmashableを継承する必要がある。
キャラクタ・敵・家具・小さな岩がすべて破壊可能である場合、それらは複数の継承を必要とする可能性のあるクラスSmashableから継承する必要があります。
多重継承が望ましくない場合は、Entityなどの共通クラスを継承する必要がある。
しかし、仮想メソッド ``smash()`` をEntityに追加するのは、そのうちのいくつかをsmashできる場合に限り、それほどエレガントではない。

動的に型付けされた言語では、これは問題ではない。
ダックタイピングにより、必要な場合で ``smash()`` 関数を定義するだけでよくなる。
継承、基本クラスなどを考慮する必要は無い。

::

   func _on_object_hit(object):
       object.smash()

以上の処理がすべてだ。
大きな岩にぶつかったオブジェクトに smash() メソッドがある場合、呼び出される。
継承またはポリモーフィズムの必要は無い。
動的に型付けされた言語は、目的のメソッドまたはメンバを持つインスタンスのみを対象とし、継承する物やクラス型は対象としない。
ダックタイピング(Duck Typing)の定義により、これがより明確になる。

*"アヒル用のように歩き、アヒルのような泳ぎ、アヒルのように鳴く鳥を見るとき、私はその鳥をアヒルと呼ぶ"*

この場合、次のように変換される。

*"オブジェクトを破壊できる場合は、それが何であるかを気にせず、単に破壊すること。"*

破壊の名称は、Hulk typingと呼ぶ。

ヒットしているオブジェクトにsmash()関数がない可能性がある。
一部の動的型付け言語が存在しない場合(Objective Cなどに)メソッド呼び出しを単に無視するが、GDScriptはより厳密なので、関数が存在するかどうかを確認することが望ましい。

::

   func _on_object_hit(object):
       if object.has_method("smash"):
           object.smash()

次に、その方法を定義するだけで、岩に触れることで壊すことができる。

（訳者：本当に訳が合っているのか？）



.. 英語の原文：ダックタイピング
   Duck typing
   -----------

   One of the most difficult concepts to grasp when moving from a
   statically typed language to a dynamic one is duck typing. Duck typing
   makes overall code design much simpler and straightforward to write, but
   it's not obvious how it works.

   As an example, imagine a situation where a big rock is falling down a
   tunnel, smashing everything on its way. The code for the rock, in a
   statically typed language would be something like:

   .. code:: cpp

     void BigRollingRock::on_object_hit(Smashable *entity) {

         entity->smash();
     }

   This way, everything that can be smashed by a rock would have to
   inherit Smashable. If a character, enemy, piece of furniture, small rock
   were all smashable, they would need to inherit from the class Smashable,
   possibly requiring multiple inheritance. If multiple inheritance was
   undesired, then they would have to inherit a common class like Entity.
   Yet, it would not be very elegant to add a virtual method ``smash()`` to
   Entity only if a few of them can be smashed.

   With dynamically typed languages, this is not a problem. Duck typing
   makes sure you only have to define a ``smash()`` function where required
   and that's it. No need to consider inheritance, base classes, etc.

   ::

     func _on_object_hit(object):
         object.smash()

   And that's it. If the object that hit the big rock has a smash() method,
   it will be called. No need for inheritance or polymorphism. Dynamically
   typed languages only care about the instance having the desired method
   or member, not what it inherits or the class type. The definition of
   Duck Typing should make this clearer:

   *"When I see a bird that walks like a duck and swims like a duck and
   quacks like a duck, I call that bird a duck"*

   In this case, it translates to:

   *"If the object can be smashed, don't care what it is, just smash it."*

   Yes, we should call it Hulk typing instead.

   It's possible that the object being hit doesn't have a smash() function.
   Some dynamically typed languages simply ignore a method call when it
   doesn't exist (like Objective C), but GDScript is stricter, so
   checking if the function exists is desirable:

   ::

     func _on_object_hit(object):
         if object.has_method("smash"):
             object.smash()

   Then, simply define that method and anything the rock touches can be
   smashed.


.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
