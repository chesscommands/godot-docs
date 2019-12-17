.. _doc_scene_tree_jp:

































シーンツリー
============

.. 英語の原文：シーンツリー
   SceneTree
   =========


































概論
------------

以前の説明では、ノードの概念を中心に話を進めていた。
シーンはノードのコレクションの一つにしか過ぎない。
それらは、 *scene tree* に編入したとき、アクティブになる。


.. 英語の原文：概論
   Introduction
   ------------

   In previous tutorials, everything revolved around the concept of
   nodes. Scenes are collections of nodes. They become active once
   they enter the *scene tree*.
































.. _jホップステップメインループjump:

メインループ
------------------------

Godotが内部的に機能する方法は次の通り。
:ref:`OS <class_OS>` クラスは、最初に実行される唯一のインスタンスになっている。
その後、すべてのドライバ・サーバ・スクリプト言語・シーンシステムなどが読み込まれる。

初期化完了後、 :ref:`OS <class_OS>` に :ref:`MainLoop <class_MainLoop>` を指定して実行する必要がある。
これまでは、すべて内部で動作していた( 詳細は ソースコードの main/main.cpp ファイルを参照すること)。

ユーザプログラムまたはゲームは、MainLoopで起動する。
このクラスには、初期化・アイドル(フレーム同期コールバック)・固定(物理同期コールバック)・入力のためのいくつかのメソッドがある。
繰り返しの説明になるが、これは低レベルであり、Godotでゲームを作成する場合、独自のMainLoopを記述することはほとんど意味が無い。

.. todo::

   リンクの確認。


.. 英語の原文：メインループ
   MainLoop
   --------

   The way Godot works internally is as follows. There is the
   :ref:`OS <class_OS>` class,
   which is the only instance that runs at the beginning. Afterwards, all
   drivers, servers, scripting languages, scene system, etc are loaded.

   When initialization is complete, :ref:`OS <class_OS>` needs to be
   supplied a :ref:`MainLoop <class_MainLoop>`
   to run. Up to this point, all this is internals working (you can check
   main/main.cpp file in the source code if you are ever interested to
   see how this works internally).

   The user program, or game, starts in the MainLoop. This class has a few
   methods, for initialization, idle (frame-synchronized callback), fixed
   (physics-synchronized callback), and input. Again, this is low
   level and when making games in Godot, writing your own MainLoop seldom makes sense.
































シーンツリー
------------------------

Godotの仕組みを説明する方法の1つとして、Godotが低レベルのミドルウェアよりも高レベルのゲームエンジンであることがあげられる。

訳者：どういう意味？

シーンシステムはゲームエンジンであり、 :ref:`OS <class_OS>` とサーバは低レベルAPIになる。

シーンシステムは独自のメインループをOSの :ref:`SceneTree <class_SceneTree>` を提供する。

訳者：意味が通じないよな・・・。

このクラスにはいくつかの重要な用途があるため、このクラスの存在を知っておくことが重要になる。

- これにはルート :ref:`Viewport <class_Viewport>` が含まれ、 *Scene Tree* の一部になるために最初に開かれたときにシーンが子として追加される(詳細は次)

- グループに関する情報が含まれており、グループ内のすべてのノードを呼び出すか、それらのリストを取得する手段がある。

- 一時停止モードの設定やプロセスの終了など、いくつかのグローバル状態機能が含まれている。

ノードがシーンツリーの一部である場合、 :ref:`SceneTree <class_SceneTree>` を呼び出すことで、 :ref:`Node.get_tree() <class_Node_method_get_tree>` シングルトンを取得する。



.. todo::

   リンクの確認。



.. 英語の原文：シーンツリー
   SceneTree
   ---------

   One of the ways to explain how Godot works is that it's a high level
   game engine over a low level middleware.

   The scene system is the game engine, while the :ref:`OS <class_OS>`
   and servers are the low level API.

   The scene system provides its own main loop to OS,
   :ref:`SceneTree <class_SceneTree>`.
   This is automatically instanced and set when running a scene, no need
   to do any extra work.

   It's important to know that this class exists because it has a few
   important uses:

   -  It contains the root :ref:`Viewport <class_Viewport>`, to which a
      scene is added as a child when it's first opened to become
      part of the *Scene Tree* (more on that next)
   -  It contains information about the groups and has the means to call all
      nodes in a group or get a list of them.
   -  It contains some global state functionality, such as setting pause
      mode or quitting the process.

   When a node is part of the Scene Tree, the
   :ref:`SceneTree <class_SceneTree>`
   singleton can be obtained by calling
   :ref:`Node.get_tree() <class_Node_method_get_tree>`.

































ルートビューポート
------------------------------------

ルート :ref:`Viewport <class_Viewport>` は常にシーンの最上部にある。
ノードからは、2つの異なる方法で取得できる。

.. tabs::
   .. code-tab:: gdscript GDScript

      get_tree().get_root() # シーンのメインループを介してアクセスする。
      get_node("/root")     # 絶対Path経由でアクセスする。

   .. code-tab:: csharp

      GetTree().GetRoot(); // Access via scene main loop.
      GetNode("/root");    // Access via absolute path.

このノードにはメインビューポートが含まれる。
:ref:`Viewport <class_Viewport>` の子である物はすべて初期設定でその中に描画されるため、すべてのノードの最上部は常にこのタイプのノードであり、そうでない場合は何も表示されない。

シーンには他のビューポートを作成できるが(画面分割効果など)、これはユーザによって作成されることのない唯一のビューポートになる。
シーンツリー内で自動的に作成される。



.. 英語の原文：ルートビューポート
   Root viewport
   -------------

   The root :ref:`Viewport <class_Viewport>`
   is always at the top of the scene. From a node, it can be obtained in
   two different ways:

   .. tabs::
    .. code-tab:: gdscript GDScript

           get_tree().get_root() # Access via scene main loop.
           get_node("/root") # Access via absolute path.

    .. code-tab:: csharp

           GetTree().GetRoot(); // Access via scene main loop.
           GetNode("/root"); // Access via absolute path.

   This node contains the main viewport. Anything that is a child of a
   :ref:`Viewport <class_Viewport>`
   is drawn inside of it by default, so it makes sense that the top of all
   nodes is always a node of this type otherwise nothing would be seen.

   While other viewports can be created in the scene (for split-screen
   effects and such), this one is the only one that is never created by the
   user. It's created automatically inside SceneTree.

































シーンツリー
------------------------

ノードが直接または間接的にルートビューポートに接続された場合、ノードは *scene tree* の一部になる。

これは、前の説明通り、_enter_tree()・_ready()・_exit_tree()コールバックを取得することを意味する。

.. image:: img/activescene.png

ノードが *Scene Tree* に入る場合、アクティブになる。
処理・入力の取得・2D・3Dビジュアルの表示・通知の送受信・サウンドの再生などに必要なすべてにアクセスできる。
*scene tree* から削除された時に、これらの機能が失われる。



.. 英語の原文：シーンツリー
   Scene tree
   ----------

   When a node is connected, directly or indirectly, to the root
   viewport, it becomes part of the *scene tree*.

   This means that as explained in previous tutorials, it will get the
   _enter_tree() and _ready() callbacks (as well as _exit_tree()).

   .. image:: img/activescene.png

   When nodes enter the *Scene Tree*, they become active. They get access
   to everything they need to process, get input, display 2D and 3D visuals,
   receive and send notifications, play sounds, etc. When they are removed from the
   *scene tree*, they lose these abilities.

































ツリー順序
--------------------

2Dの描画・処理・通知の取得など、Godotのほとんどのノード操作は、ツリー順に実行される。
これは、ツリー順序の低いランクを持つ親と兄弟が現在のノードの前に通知されることを意味する。

.. image:: img/toptobottom.png



.. 英語の原文：ツリー順序
   Tree order
   ----------

   Most node operations in Godot, such as drawing 2D, processing, or getting
   notifications are done in tree order. This means that parents and
   siblings with a lower rank in the tree order will get notified before
   the current node.

   .. image:: img/toptobottom.png

































*シーンツリー* を入力して "アクティブになる"
----------------------------------------------------------------------------------------

#. シーンがディスクから読み込まれるが、スクリプトによって作成される。
#. そのシーンのルートノード(1つのルートのみを説明済みだが、記憶障害ではないよね)は、 "root" ビューポートの子として(シーンツリーから)、またはその子または孫に追加される。
#. 新規追加されたシーンのすべてのノードは、 "enter_tree" 通知(GDScriptの _enter_tree() コールバック)を上から下の順に受け取る。
#. ノードとそのすべての子がアクティブシーン内にある場合、便宜上、追加の通知 "ready" (GDScriptの _ready() コールバック)が提供される。
#. シーン(またはその一部)が削除された場合、 "exit scene" の通知(GDScriptの_exit_tree()コールバック)を下から上に受け取る。




.. 英語の原文：*シーンツリー* を入力して "アクティブになる"
   "Becoming active" by entering the *Scene Tree*
   ----------------------------------------------

   #. A scene is loaded from disk or created by scripting.
   #. The root node of that scene (only one root, remember?) is added as
      either a child of the "root" Viewport (from SceneTree), or to any
      child or grandchild of it.
   #. Every node of the newly added scene, will receive the "enter_tree"
      notification ( _enter_tree() callback in GDScript) in top-to-bottom
      order.
   #. An extra notification, "ready" ( _ready() callback in GDScript) is
      provided for convenience, when a node and all its children are
      inside the active scene.
   #. When a scene (or part of it) is removed, they receive the "exit
      scene" notification ( _exit_tree() callback in GDScript) in
      bottom-to-top order

































現在のシーン変更
--------------------------------

シーンが読み込まれた後、このシーンを別のシーンに変更することがしばしば望まれる。
これを行う簡単な方法は、 :ref:`SceneTree.change_scene() <class_SceneTree_method_change_scene>` 関数を使用することで対応可能になる。

.. tabs::
   .. code-tab:: gdscript GDScript

      func _my_level_was_completed():
          get_tree().change_scene("res://levels/level2.tscn")

   .. code-tab:: csharp

      public void _MyLevelWasCompleted()
      {
          GetTree().ChangeScene("res://levels/level2.tscn");
      }

ファイルPathを使用する代わりに、同等の関数 :ref:`SceneTree.change_scene_to(PackedScene scene) <class_SceneTree_method_change_scene_to>` を使用して、既製の :ref:`PackedScene <class_PackedScene>` リソースを使用することもできる。

.. tabs::
   .. code-tab:: gdscript GDScript

      var next_scene = preload("res://levels/level2.tscn")

      func _my_level_was_completed():
          get_tree().change_scene_to(next_scene)

   .. code-tab:: csharp

      public void _MyLevelWasCompleted()
      {
          var nextScene = (PackedScene)ResourceLoader.Load("res://levels/level2.tscn");
          GetTree().ChangeSceneTo(nextScene);
      }

これらは、シーンを切り替えるための迅速で便利な方法だが、新しいシーンが読み込まれて実行されるまでゲームが停止するという欠点がある。
ゲーム開発のとある時点で、プログレスバー・アニメーションインジケータ・スレッド(バックグランド)の読み込みを備えた適切な読み込み画像を作成することを勧める。
これは、オートロード(次の章)と :ref:`doc_background_loading` を使用して手動で行う必要がある。

.. todo::

   リンクの確認。

.. 英語の原文：現在のシーン変更
   Changing current scene
   ----------------------

   After a scene is loaded, it is often desired to change this scene for
   another one. The simple way to do this is to use the
   :ref:`SceneTree.change_scene() <class_SceneTree_method_change_scene>`
   function:

   .. tabs::
    .. code-tab:: gdscript GDScript

       func _my_level_was_completed():
           get_tree().change_scene("res://levels/level2.tscn")

    .. code-tab:: csharp

       public void _MyLevelWasCompleted()
       {
           GetTree().ChangeScene("res://levels/level2.tscn");
       }

   Rather than using file paths, one can also use ready-made
   :ref:`PackedScene <class_PackedScene>` resources using the equivalent
   function
   :ref:`SceneTree.change_scene_to(PackedScene scene) <class_SceneTree_method_change_scene_to>`:

   .. tabs::
    .. code-tab:: gdscript GDScript

       var next_scene = preload("res://levels/level2.tscn")

       func _my_level_was_completed():
         get_tree().change_scene_to(next_scene)

    .. code-tab:: csharp

       public void _MyLevelWasCompleted()
       {
           var nextScene = (PackedScene)ResourceLoader.Load("res://levels/level2.tscn");
           GetTree().ChangeSceneTo(nextScene);
       }

   These are quick and useful ways to switch scenes but have the drawback
   that the game will stall until the new scene is loaded and running. At
   some point in the development of your game, it may be preferable to create proper loading
   screens with progress bar, animated indicators or thread (background)
   loading. This must be done manually using autoloads (see next chapter)
   and :ref:`doc_background_loading`.

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
