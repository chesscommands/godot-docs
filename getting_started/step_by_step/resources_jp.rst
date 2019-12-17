.. _doc_resources_jp:

































資源(リソース)
============================

.. 英語の原文：資源(リソース)
   Resources
   =========
































ノードとリソース
--------------------------------

この説明までは、Godotの :ref:`Node <class_Node>` クラスに注目してきた。
これは、動作をコーディングするために使用するクラスであり、エンジンのほとんどの機能がこれに依存する。
同様に重要な別のデータ型が存在する。
それが
:ref:`Resource <class_Resource>`
だ。

*Nodes* は機能を提供する。
スプライト・3Dモデルの描画・物理シミュレート・ユーザインタフェイスの配置など。
**リソース** は **データコンテナ** であり、自身では何もできない。
その代わりに、Nodesはリソースに含まれるデータを使用する。

Godotはディスクから保存または読み込む物すべてをリソース扱いする。
シーン( 〜.tscn または 〜.scn )・画像・スクリプトなど。
``Resource`` の例として、
:ref:`Texture <class_Texture>` ・
:ref:`Script <class_Script>` ・
:ref:`Mesh<class_Mesh>` ・
:ref:`Animation <class_Animation>` ・
:ref:`AudioStream<class_AudioStream>` ・
:ref:`Font <class_Font>` ・
:ref:`Translation<class_Translation>`
などがある。

.. todo::

   リンクの確認。

エンジンがディスクからリソースを読み込むときは、 **一度のみの読み込み** 。
そのリソースのコピーが既にメモリにある場合、リソースの再ロード時に、毎回同じコピーが使い回される。
リソースにはデータしか含まれていないため、リソースを複製する必要は無い。

すべてのオブジェクトは、ノードであればリソースであれ、プロパティをエクスポートできる。
String・integer・Vector2など多くのタイプのプロパティがあり、これらのタイプはいずれもリソースになることができる。
つまり、ノードとリソースの両方にリソースをプロパティとして含めることができる。

.. image:: img/nodes_resources.png



.. 英語の原文：ノードとリソース
   Nodes and resources
   -------------------

   Up to this tutorial, we focused on the :ref:`Node <class_Node>`
   class in Godot as that's the one you use to code behavior and
   most of the engine's features rely on it. There is
   another datatype that is just as important:
   :ref:`Resource <class_Resource>`.

   *Nodes* give you functionality: they draw sprites, 3D models, simulate physics,
   arrange user interfaces, etc. **Resources** are **data containers**. They don't
   do anything on their own: instead, nodes use the data contained in resources.

   Anything Godot saves or loads from disk is a resource. Be it a scene (a .tscn or
   an .scn file), an image, a script... Here are some ``Resource`` examples:
   :ref:`Texture <class_Texture>`, :ref:`Script <class_Script>`, :ref:`Mesh
   <class_Mesh>`, :ref:`Animation <class_Animation>`, :ref:`AudioStream
   <class_AudioStream>`, :ref:`Font <class_Font>`, :ref:`Translation
   <class_Translation>`.

   When the engine loads a resource from disk, **it only loads it once**. If a copy
   of that resource is already in memory, trying to load the resource again will
   return the same copy every time. As resources only contain data, there is no need
   to duplicate them.

   Every object, be it a Node or a Resource, can export properties. There are many
   types of Properties, like String, integer, Vector2, etc., and any of these types
   can become a resource. This means that both nodes and resources can contain
   resources as properties:

   .. image:: img/nodes_resources.png

































外部VS組み込み
----------------------------

リソースを節約するには、以下の2種類がある。

1. **External(外部)** ：シーンに個別のファイルとしてディスクに保存する。
2. **Built-in(組み込み)** ：それらが添付されている \*.tscn または \*.scn ファイル内に保存する。

具体的には、 :ref:`Texture <class_Texture>` を :ref:`Sprite <class_Sprite>` ノードに追加する。

.. image:: img/spriteprop.png

リソースのプレビュをクリックしたとき、リソースのプロパティを表示及び編集できる。

.. image:: img/resourcerobi.png

.. todo::

   これらの画像を用意できるならば、作成したい。
   それとリンクの確認。

Pathプロパティは、リソースがどこから来たかを教えてくれる。
この場合、それは ``robi.png`` と呼ばれるPNG画像から来ている。
リソースがこのようなファイルに依存する場合、それは外部リソース扱いになる。
Pathを消去するか、このPathが空の場合、それは組み込みリソースになる(訳者：どういう意味？)。

シーンの保存後、組み込みリソースと外部リソースの切り替えが発生する。
上記の例では、Path `"res://robi.png"` を消去後に保存した場合、Godotは.tscnシーンファイル内に画像を保存する。

.. note::

   組み込みリソースを保存した場合、シーンを複数回インスタンス化することで、エンジンはそのコピーを1つだけ読み込む。



.. 英語の原文：外部VS組み込み
   External vs built-in
   --------------------

   There are two ways to save resources. They can be:

   1. **External** to a scene, saved on the disk as individual files.
   2. **Built-in**, saved inside the \*.tscn or the \*.scn file they're attached to.

   To be more specific, here's a :ref:`Texture <class_Texture>`
   in a :ref:`Sprite <class_Sprite>` node:

   .. image:: img/spriteprop.png

   Clicking the resource preview allows us to view and edit the resource's properties.

   .. image:: img/resourcerobi.png

   The path property tells us where the resource comes from. In this case, it comes
   from a PNG image called ``robi.png``. When the resource comes from a file like
   this, it is an external resource. If you erase the path or this path is empty,
   it becomes a built-in resource.

   The switch between built-in and external resources happens when you save the
   scene. In the example above, if you erase the path \`"res://robi.png"\` and
   save, Godot will save the image inside the .tscn scene file.

   .. note::

       Even if you save a built-in resource, when you instance a scene multiple
       times, the engine will only load one copy of it.


































コードからリソースを読み込む
--------------------------------------------------------

コードからリソースを読み込むには、2つの方法がある。
まず、いつでも ``load()`` 関数を使用できること。

.. tabs::
   .. code-tab:: gdscript GDScript

      func _ready():
          var res = load("res://robi.png") # load関数処理時にリソースを読み込む。
          get_node("sprite").texture = res

   .. code-tab:: csharp

      public override void _Ready()
      {
          var texture = (Texture)GD.Load("res://robi.png"); // Godot loads the Resource when it reads the line.
          var sprite = (Sprite)GetNode("sprite");
          sprite.Texture = texture;
      }

リソースを ``preload`` することもできる。
``load`` と異なり、この関数は、ディスクからファイルを読み取り、コンパイル時に取り込む。
そのため、変数Pathを使用してpreloadを呼び出すことはできない(訳者：どういう意味？)。
定数文字列を使用する必要がある。

.. tabs::
   .. code-tab:: gdscript GDScript

      func _ready():
          var res = preload("res://robi.png") # コンパイル時にリソースを読み込む。
          get_node("sprite").texture = res

   .. code-tab:: csharp

      // 'preload()' is unavailable in C Sharp.



.. 英語の原文：コードからリソースを読み込む
   Loading resources from code
   ---------------------------

   There are two ways to load resources from code. First, you can use the ``load()`` function anytime:

   .. tabs::
    .. code-tab:: gdscript GDScript

       func _ready():
               var res = load("res://robi.png") # Godot loads the Resource when it reads the line.
               get_node("sprite").texture = res

    .. code-tab:: csharp

       public override void _Ready()
       {
           var texture = (Texture)GD.Load("res://robi.png"); // Godot loads the Resource when it reads the line.
           var sprite = (Sprite)GetNode("sprite");
           sprite.Texture = texture;
       }

   You can also ``preload`` resources. Unlike ``load``, this function will read the
   file from disk and load it at compile-time. As a result, you cannot call preload
   with a variable path: you need to use a constant string.

   .. tabs::
    .. code-tab:: gdscript GDScript

       func _ready():
               var res = preload("res://robi.png") # Godot loads the resource at compile-time
               get_node("sprite").texture = res

    .. code-tab:: csharp

       // 'preload()' is unavailable in C Sharp.
































シーンの読み込み
--------------------------------

シーンもリソースだが、キャッチがある。
ディスクに保存されるシーンの属性は、 :ref:`PackedScene <class_PackedScene>` のリソースになる。
シーンはリソース内に詰め込まれている。

.. todo::

   キャッチって何？

シーンのインスタンスを取得するには、 :ref:`PackedScene.instance() <class_PackedScene_method_instance>` メソッドを使用する必要がある。

.. tabs::
   .. code-tab:: gdscript GDScript

      func _on_shoot():
          var bullet = preload("res://bullet.tscn").instance()
          add_child(bullet)

   .. code-tab:: csharp

      private PackedScene _bulletScene = (PackedScene)GD.Load("res://bullet.tscn");

      public void OnShoot()
      {
          Node bullet = _bulletScene.Instance();
          AddChild(bullet);
      }

このメソッドは、シーンの階層にノードを作成して構成し、シーンのルートノードを返却する。
その後、他のノードの子として追加できる。

このアプローチにはいくつかの利点がある。
:ref:`PackedScene.instance() <class_PackedScene_method_instance>`
メソッドは高速なので、ディスクからそれらを再ロード不要で、新規の敵・弾丸・エフェクトなどを作成できる(訳者：高速なのとどのような関係がある？)。
いつものように、画像・メッシュなどはすべてシーンインスタンス間で共有されることに注意すること。

.. todo::

   リンクの確認。

.. 英語の原文：シーンの読み込み
   Loading scenes
   --------------

   Scenes are also resources, but there is a catch. Scenes saved to disk are
   resources of type :ref:`PackedScene <class_PackedScene>`. The
   scene is packed inside a resource.

   To get an instance of the scene, you have to use the
   :ref:`PackedScene.instance() <class_PackedScene_method_instance>` method.

   .. tabs::
    .. code-tab:: gdscript GDScript

       func _on_shoot():
               var bullet = preload("res://bullet.tscn").instance()
               add_child(bullet)


    .. code-tab:: csharp

       private PackedScene _bulletScene = (PackedScene)GD.Load("res://bullet.tscn");

       public void OnShoot()
       {
           Node bullet = _bulletScene.Instance();
           AddChild(bullet);
       }

   This method creates the nodes in the scene's hierarchy, configures them, and
   returns the root node of the scene. You can then add it as a child of any other
   node.

   The approach has several advantages. As the :ref:`PackedScene.instance()
   <class_PackedScene_method_instance>` function is fast, you can create new
   enemies, bullets, effects, etc. without having to load them again from disk each
   time. Remember that, as always, images, meshes, etc. are all shared between the
   scene instances.


































リソース解放
------------------------

``Resource`` が不要になった場合、自動解放される。
ほとんどの場合、リソースはノードに含まれているため、ノードの解放後、それに引きづられ、所有するすべてのリソースも解放される。
















.. 英語の原文：リソース解放
   Freeing resources
   -----------------

   When a ``Resource`` is no longer in use, it will automatically free itself.
   Since, in most cases, Resources are contained in Nodes, when you free a node,
   the engine frees all the resources it owns as well if no other node uses them.



































独自のリソース作成
------------------------------------

Godotのオブジェクトと同様に、ユーザはリソースをスクリプト化することもできる。
リソーススクリプトは、オブジェクトプロパティとシリアル化されたテキストまたはバイナリデータ (*.tres・*.res) の間を自由に変換する機能を継承する。
また、参照型から参照カウントメモリ管理を継承する。

これには、JSON・CSV・カスタムTXTファイルなどの代替データ構造を超える多くの明確な利点がある。
ユーザはこれらのアセットを :ref:`Dictionary <class_Dictionary>` (JSON) または、 :ref:`File <class_File>` としてインポートして解析できる。
リソースを際立たせるのは、 :ref:`Object <class_Object>` ・ :ref:`Reference <class_Reference>` ・ :ref:`Resource <class_Resource>` の継承だろう。

- 定数を定義できるため、他のデータフィールドまたはオブジェクトの定数は不要

- プロパティのsetter/getterメソッドを含むメソッドを定義できる。
  これにより、基になるデータの抽象化とカプセル化が可能になる。
  リソーススクリプトの構造を変更する必要がある場合、リソースを使用するゲームに変更は不要

- シグナルを定義できるため、リソースは管理するデータの変更に対する応答をトリガー可能

- プロパティが定義されているため、ユーザは自分のデータが存在することを100%知っている。

- リソースの自動シリアル化と逆シリアル化は、組み込みGodotエンジン機能になっている。
  リソースファイルのデータをimport/exportするためのカスタムロジックが不要

- リソースはサブリソースを再帰的にシリアル化できるため、ユーザはさらに高度なデータ構造を設計可能

- ユーザは、リソースをバージョン管理に適したテキストファイル (\*.tres) として保存できる。
  ゲームをエクスポートした場合、Godotはリソースファイルをバイナリファイル (\*.res) としてシリアル化し、速度と圧縮を向上させる。

- Godotエンジンのインスペクタは、すぐに使用できるリソースファイルをレンダリング及び編集する。
  そのため、データを視覚化または編集するためにカスタムロジックの実装を不要にする。
  その方法は、ファイルシステムドックでリソースファイルをダブルクリックするか、インスペクタドックからフォルダアイコンをクリックしてダイアログでファイルを開く。

- 基本リソースだけで無く、 **other** リソースタイプを拡張できる。

.. warning::

   リソースとディクショナリは両方とも参照で渡されるが、参照カウントされるのはリソースのみになる。
   要は、ディクショナリがオブジェクト間で渡され、最初のオブジェクトが削除された場合、他のすべてのオブジェクトのディクショナリへの参照が無効になる。
   逆に、すべてのオブジェクトが削除されるまで、リソースはメモリから解放されない。

.. tabs::
   .. code-tab:: gdscript GDScript

      extends Node

      class MyObject:
      extends Object
      var dict = {}

      func _ready():
          var obj1 = MyObject.new()
          var obj2 = MyObject.new()
          obj1.dict.greeting = "hello"
          obj2.dict = obj1.dict         # 'obj2.dict' は 'obj1' のディクショナリを参照可能になった。
          obj1.free()                   # 'obj1' はディクショナリとともに解放された。
          print(obj2.dict.greeting)     # Error! 'greeting' インデックスはnullインスタンスでアクセスされる。

      # これを回避するには、ディクショナリを手動で複製する必要がある。
      obj1 = MyObject.new()
      obj1.dict.greeting = "hello"      # ←ここまでは同じ。
      obj2.dict = obj1.dict.duplicate() # 今回、参照では無く、コピーを渡す。
      obj1.free()                       # obj2のディクショナリは、まだ存在していない。
      print(obj2.dict.greeting)         # 'hello' を表示する。

Godotを使う場合、インスペクタでカスタムリソースを簡単に作成できる。

1. インスペクタでプレーンリソースオブジェクトを作成する。
   スクリプトがその属性を拡張している限り、これはリソース派生属性でも構わない。
2. インスペクタで ``script`` プロパティをスクリプトに設定する。

これで、インスペクタにリソーススクリプトのカスタムプロパティが表示される。
これらの値を編集後にリソースを保存した場合、インスペクタはカスタムプロパティもシリアル化する。
インスペクタからリソースを保存するには、インスペクタのツリーメニュー(右上)をクリックし、 "保存" または "名前を付けて保存..." を選択する。

スクリプト言語が :ref:`script classes <doc_scripting_continued_class_name>` に対応している場合、プロセスが合理化される(訳者：合理化とは？)。
スクリプトの名前を単独定義した場合、その名前がインスペクタの作成ダイアログに追加される。
これにより、作成したリソースオブジェクトにスクリプトが自動追加される。

いくつかの例で確認する。

.. tabs::
   .. code-tab:: gdscript GDScript

      # bot_stats.gd
      extends Resource
      export(int) var health
      export(Resource) var sub_resource
      export(Array, String) var strings

      func _init(p_health = 0, p_sub_resource = null, p_strings = []):
          health = p_health
          sub_resource = p_sub_resource
          strings = p_strings

      # bot.gd
      extends KinematicBody

      export(Resource) var stats

      func _ready():
          # 'health' と互換性のあるリソースには、暗黙のduck-typedインタフェイスを使用する。
          if stats:
              print(stats.health) # Prints '10'.

   .. code-tab:: csharp

      // BotStats.cs
      using System;
      using Godot;

      namespace ExampleProject {
          public class BotStats : Resource
          {
              [Export]
              public int Health { get; set; }

              [Export]
              public Resource SubResource { get; set; }

              [Export]
              public String[] Strings { get; set; }

              public BotStats(int health = 0, Resource subResource = null, String[] strings = null)
              {
                  Health = health;
                  SubResource = subResource;
                  Strings = strings ?? new String[0];
              }
          }
      }

      // Bot.cs
      using System;
      using Godot;

      namespace ExampleProject {
          public class Bot : KinematicBody
          {
              [Export]
              public Resource Stats;

              public override void _Ready()
              {
                  if (Stats != null && Stats is BotStats botStats) {
                      GD.Print(botStats.Health); // Prints '10'.
                  }
              }
           }
      }

.. todo::

   もう一度見返す。何をやっているプログラムなのか全く分からない。
   それとリンクの確認。


.. 英語の原文：独自のリソース作成
   Creating your own resources
   ---------------------------

   Like any Object in Godot, users can also script Resources. Resource scripts
   inherit the ability to freely translate between object properties and serialized
   text or binary data (/*.tres, /*.res). They also inherit the reference-counting
   memory management from the Reference type.

   This comes with many distinct advantages over alternative data
   structures, such as JSON, CSV, or custom TXT files. Users can only import these
   assets as a :ref:`Dictionary <class_Dictionary>` (JSON) or as a
   :ref:`File <class_File>` to parse. What sets Resources apart is their
   inheritance of :ref:`Object <class_Object>`, :ref:`Reference <class_Reference>`,
   and :ref:`Resource <class_Resource>` features:

   - They can define constants, so constants from other data fields or objects are not needed.

   - They can define methods, including setter/getter methods for properties. This allows for abstraction and encapsulation of the underlying data. If the Resource script's structure needs to change, the game using the Resource need not also change.

   - They can define signals, so Resources can trigger responses to changes in the data they manage.

   - They have defined properties, so users know 100% that their data will exist.

   - Resource auto-serialization and deserialization is a built-in Godot Engine feature. Users do not need to implement custom logic to import/export a resource file's data.

   - Resources can even serialize sub-Resources recursively, meaning users can design even more sophisticated data structures.

   - Users can save Resources as version-control-friendly text files (\*.tres). Upon exporting a game, Godot serializes resource files as binary files (\*.res) for increased speed and compression.

   - Godot Engine's Inspector renders and edits Resource files out-of-the-box. As such, users often do not need to implement custom logic to visualize or edit their data. To do so, double-click the resource file in the FileSystem dock or click the folder icon in the Inspector and open the file in the dialog.

   - They can extend **other** resource types besides just the base Resource.

   .. warning::

       Resources and Dictionaries are both passed by reference, but only Resources are
       reference-counted. This means that if a Dictionary is passed between objects and
       the first object is deleted, all other objects' references to the Dictionary will
       be invalidated. Conversely, Resources will not be freed from memory until *all* the 
       objects are deleted.

       .. tabs::
         .. code-tab:: gdscript GDScript

           extends Node

           class MyObject:
               extends Object
               var dict = {}

           func _ready():
               var obj1 = MyObject.new()
               var obj2 = MyObject.new()
               obj1.dict.greeting = "hello"
               obj2.dict = obj1.dict             # 'obj2.dict' now references 'obj1's Dictionary.
               obj1.free()                       # 'obj1' is freed and the Dictionary too!
               print(obj2.dict.greeting)         # Error! 'greeting' index accessed on null instance!

               # To avoid this, we must manually duplicate the Dictionary.
               obj1 = MyObject.new()
               obj1.dict.greeting = "hello"
               obj2.dict = obj1.dict.duplicate() # Now we are passing a copy, not a reference.
               obj1.free()                       # obj2's Dictionary still exists.
               print(obj2.dict.greeting)         # Prints 'hello'.

   Godot makes it easy to create custom Resources in the Inspector.

   1. Create a plain Resource object in the Inspector. This can even be a type that derives Resource, so long as your script is extending that type.
   2. Set the ``script`` property in the Inspector to be your script.

   The Inspector will now display your Resource script's custom properties. If one edits
   those values and saves the resource, the Inspector serializes the custom properties
   too! To save a resource from the Inspector, click the Inspector's tools menu (top right),
   and select "Save" or "Save As...".

   If the script's language supports :ref:`script classes <doc_scripting_continued_class_name>`,
   then it streamlines the process. Defining a name for your script alone will add it to
   the Inspector's creation dialog. This will auto-add your script to the Resource
   object you create.

   Let's see some examples.

   .. tabs::
     .. code-tab:: gdscript GDScript

       # bot_stats.gd
       extends Resource
       export(int) var health
       export(Resource) var sub_resource
       export(Array, String) var strings

       func _init(p_health = 0, p_sub_resource = null, p_strings = []):
           health = p_health
           sub_resource = p_sub_resource
           strings = p_strings

       # bot.gd
       extends KinematicBody

       export(Resource) var stats

       func _ready():
           # Uses an implicit, duck-typed interface for any 'health'-compatible resources.
           if stats:
               print(stats.health) # Prints '10'.
     .. code-tab:: csharp

           // BotStats.cs
           using System;
           using Godot;

           namespace ExampleProject {
               public class BotStats : Resource
               {
                   [Export]
                   public int Health { get; set; }

                   [Export]
                   public Resource SubResource { get; set; }

                   [Export]
                   public String[] Strings { get; set; }

                   public BotStats(int health = 0, Resource subResource = null, String[] strings = null)
                   {
                       Health = health;
                       SubResource = subResource;
                       Strings = strings ?? new String[0];
                   }
               }
           }

           // Bot.cs
           using System;
           using Godot;

           namespace ExampleProject {
               public class Bot : KinematicBody
               {
                   [Export]
                   public Resource Stats;

                   public override void _Ready()
                   {
                       if (Stats != null && Stats is BotStats botStats) {
                           GD.Print(botStats.Health); // Prints '10'.
                       }
                   }
               }
           }

   .. note::

       Resource scripts are similar to Unity's ScriptableObjects. The Inspector
       provides built-in support for custom resources. If desired though, users
       can even design their own Control-based tool scripts and combine them
       with an :ref:`EditorPlugin <class_EditorPlugin>` to create custom
       visualizations and editors for their data.

       Unreal Engine 4's DataTables and CurveTables are also easy to recreate with
       Resource scripts. DataTables are a String mapped to a custom struct, similar
       to a Dictionary mapping a String to a secondary custom Resource script.

       .. tabs::
         .. code-tab:: gdscript GDScript

           # bot_stats_table.gd
           extends Resource

           const BotStats = preload("bot_stats.gd")

           var data = {
               "GodotBot": BotStats.new(10), # Creates instance with 10 health.
               "DifferentBot": BotStats.new(20) # A different one with 20 health.
           }

           func _init():
               print(data)
         .. code-tab:: csharp

           using System;
           using Godot;

           public class BotStatsTable : Resource
           {
               private Godot.Dictionary<String, BotStats> _stats = new Godot.Dictionary<String, BotStats>();

               public BotStatsTable()
               {
                   _stats["GodotBot"] = new BotStats(10); // Creates instance with 10 health.
                   _stats["DifferentBot"] = new BotStats(20); // A different one with 20 health.
                   GD.Print(_stats);
               }
           }

       Instead of just inlining the Dictionary values, one could also, alternatively...

       1. Import a table of values from a spreadsheet and generate these key-value pairs, or...

       2. Design a visualization within the editor and create a simple plugin that adds it
          to the Inspector when you open these types of Resources.

       CurveTables are the same thing, except mapped to an Array of float values
       or a :ref:`Curve <class_Curve>`/:ref:`Curve2D <class_Curve2D>` resource object.

   .. warning::

       Beware that resource files (\*.tres/\*.res) will store the path of the script
       they use in the file. When loaded, they will fetch and load this script as an
       extension of their type. This means that trying to assign a subclass, i.e. an
       inner class of a script (such as using the ``class`` keyword in GDScript) won't
       work. Godot will not serialize the custom properties on the script subclass properly.

       In the example below, Godot would load the ``Node`` script, see that it doesn't
       extend ``Resource``, and then determine that the script failed to load for the
       Resource object since the types are incompatible.

       .. tabs::
         .. code-tab:: gdscript GDScript

           extends Node

           class MyResource:
               extends Resource
               export var value = 5

           func _ready():
               var my_res = MyResource.new()

               # This will NOT serialize the 'value' property.
               ResourceSaver.save("res://my_res.tres", my_res)
         .. code-tab:: csharp
           using System;
           using Godot;

           public class MyNode : Node
           {
               public class MyResource : Resource
               {
                   [Export]
                   public int Value { get; set; } = 5;
               }

               public override void _Ready()
               {
                   var res = new MyResource();

                   // This will NOT serialize the 'Value' property.
                   ResourceSaver.Save("res://MyRes.tres", res);
               }
           }

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
