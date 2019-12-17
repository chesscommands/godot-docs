.. _doc_command_line_tutorial_jp:


































コマンドラインについて
======================

.. highlight:: shell

一部の開発者は、コマンドラインを広範囲に使用することを好む。
Godotは使いやすいように設計されているため、コマンドラインから完全に操作が可能であり、それを次に示す。
エンジンが外部ライブラリにほとんど依存しないことを考えれば、初期化時間は非常に早く、このワークフローに適している。

.. 英語の原文：コマンドラインについて
   Command line tutorial
   =====================

   .. highlight:: shell

   Some developers like using the command line extensively. Godot is
   designed to be friendly to them, so here are the steps for working
   entirely from the command line. Given the engine relies on almost no
   external libraries, initialization times are pretty fast, making it
   suitable for this workflow.




































Path
----

GodotバイナリをPath環境変数に含めることを勧める。
これにより、 ``godot`` と入力することで、任意の場所から簡単に実行できる。
Linuxで行うには、Godotバイナリを ``/usr/local/bin`` に配置することにより ``godot`` を呼べるようになる。


.. 英語の原文：Path
   Path
   ----

   It is recommended that your Godot binary be in your PATH environment
   variable, so it can be executed easily from any place by typing
   ``godot``. You can do so on Linux by placing the Godot binary in
   ``/usr/local/bin`` and making sure it is called ``godot``.


































プロジェクトのPath設定
--------------------------------------------

Godotバイナリの場所と現在の作業ディレクトリに応じて、次のコマンドが正しく機能するようにプロジェクトへのPathを設定する必要がある。

これは、次のように、プロジェクトの ``project.godot`` ファイルへのPathを最初の引数として与えることで実行できる。

::

   user@host:~$ godot path_to_your_project/project.godot [other] [commands] [and] [args]

または ``--path`` 引数を使用する。

::

   user@host:~$ godot --path path_to_your_project [other] [commands] [and] [args]

例えば、ゲームをエクスポートするための完全なコマンドは次の通り。

::

   user@host:~$ godot --path path_to_your_project --export my_export_preset_name game.exe



.. 英語の原文：プロジェクトのPath設定
   Setting the project path
   ------------------------

   Depending on where your Godot binary is located and what your current
   working directory is, you may need to set the path to your project
   for any of the following commands to work correctly.

   This can be done by giving the path to the ``project.godot`` file
   of your project as either the first argument, like this:

   ::

       user@host:~$ godot path_to_your_project/project.godot [other] [commands] [and] [args]

   Or by using the ``--path`` argument:

   ::

       user@host:~$ godot --path path_to_your_project [other] [commands] [and] [args]

   For example, the full command for exporting your game (as explained below) might look like this:

   ::

       user@host:~$ godot --path path_to_your_project --export my_export_preset_name game.exe


































プロジェクトの作成
------------------------------------

コマンドラインからプロジェクトを作成するには、シェルを目的の場所に移動し、project.godotファイルを作成する。

::

   user@host:~$ mkdir newgame
   user@host:~$ cd newgame
   user@host:~/newgame$ touch project.godot

これで、プロジェクトをGodotで開くことができる。

.. 英語の原文：プロジェクトの作成
   Creating a project
   ------------------


   Creating a project from the command line can be done by navigating the
   shell to the desired place and making a project.godot file.


   ::

       user@host:~$ mkdir newgame
       user@host:~$ cd newgame
       user@host:~/newgame$ touch project.godot


   The project can now be opened with Godot.


































エディタの実行
----------------------------

エディタの実行には、 ``-e`` フラグを付けてGodotを実行する。
これは、プロジェクトディレクトリまたはサブディレクトリ内から実行する必要がある。
そうでない場合、コマンドは無視され、プロジェクトマネージャが表示される。

::

   user@host:~/newgame$ godot -e

シーンが作成されて保存されている場合、そのシーンを引数として同じコードを実行することで、後で編集できる。

::

   user@host:~/newgame$ godot -e scene.tscn


.. 英語の原文：エディタの実行
   Running the editor
   ------------------

   Running the editor is done by executing Godot with the ``-e`` flag. This
   must be done from within the project directory or a subdirectory,
   otherwise the command is ignored and the project manager appears.

   ::

       user@host:~/newgame$ godot -e

   If a scene has been created and saved, it can be edited later by running
   the same code with that scene as argument.

   ::

       user@host:~/newgame$ godot -e scene.tscn


































シーンの消去
------------------------

Godotは、ファイルシステムと親密な関係であり、追加のメタデータファイルを作成しない。
``rm`` の使用でシーンファイルを消去する。
そのシーンを参照していないことを確認しなければ、プロジェクトを開いたときにエラーが発生する。

::

   user@host:~/newgame$ rm scene.tscn


.. 英語の原文：シーンの消去
   Erasing a scene
   ---------------

   Godot is friends with your filesystem and will not create extra
   metadata files. Use ``rm`` to erase a scene file. Make sure nothing
   references that scene or else an error will be thrown upon opening.

   ::

       user@host:~/newgame$ rm scene.tscn


































ゲームの実行
------------------------

ゲームを実行するには、プロジェクトディレクトリまたはサブディレクトリ内でGodotを実行する。

::

   user@host:~/newgame$ godot

特定のシーンをテストする必要がある場合、そのシーンをコマンドラインに渡す。

::

   user@host:~/newgame$ godot scene.tscn



.. 英語の原文：ゲームの実行
   Running the game
   ----------------

   To run the game, simply execute Godot within the project directory or
   subdirectory.

   ::

       user@host:~/newgame$ godot

   When a specific scene needs to be tested, pass that scene to the command
   line.

   ::

       user@host:~/newgame$ godot scene.tscn


































デバッグ
----------------

コマンドライン上での実行はエラーをも通り過ぎるため、エラー箇所をつかむのは至難の業だろう。
このため、 ``-d`` を追加することで、コマンドラインデバッガが有効になる。
ゲームまたはシンプルなシーンを実行するために機能する。

::

   user@host:~/newgame$ godot -d

::

   user@host:~/newgame$ godot -d scene.tscn

.. _doc_command_line_tutorial_exporting:

.. todo::

   リンクの確認。



.. 英語の原文：デバッグ
   Debugging
   ---------

   Catching errors in the command line can be a difficult task because they
   just fly by. For this, a command line debugger is provided by adding
   ``-d``. It works for running either the game or a simple scene.

   ::

       user@host:~/newgame$ godot -d

   ::

       user@host:~/newgame$ godot -d scene.tscn

   .. _doc_command_line_tutorial_exporting:


































エクスポート
------------------------

コマンドラインからのプロジェクトのエクスポートもサポートされている。
これは、継続的な統合セットアップに特に役立つ。
これには、ヘッドレス(サーバ構築・ビデオなし)のGodotのバージョンが理想的(訳者：何が？)。

::

   user@host:~/newgame$ godot --export "Linux/X11" /var/builds/project
   user@host:~/newgame$ godot --export Android /var/builds/project.apk

``--export`` オプションで認識されるプラットフォーム名は、エディタのエクスポートウィザードに表示されるものと同じ。サポートされているプラットフォームのリストをコマンドラインから取得するには、認識されていないプラットフォームにエクスポートすれば分かるとおり、サポートするプラットフォームの完全なリストが構成表示される。

ゲームのデバッグバージョンをエクスポートするには ``--export`` の代わりに ``--export-debug`` オプションを使用する。
それらのパラメータと使用方法は同じ。


.. 英語の原文：エクスポート
   Exporting
   ---------

   Exporting the project from the command line is also supported. This is
   especially useful for continuous integration setups. The version of Godot
   that is headless (server build, no video) is ideal for this.

   ::

       user@host:~/newgame$ godot --export "Linux/X11" /var/builds/project
       user@host:~/newgame$ godot --export Android /var/builds/project.apk

   The platform names recognized by the ``--export`` switch are the same as
   displayed in the export wizard of the editor. To get a list of supported
   platforms from the command line, try exporting to a non-recognized
   platform and the full listing of platforms your configuration supports
   will be shown.

   To export a debug version of the game, use the ``--export-debug`` switch
   instead of ``--export``. Their parameters and usage are the same.




































スクリプトの実行
--------------------------------

コマンドラインから単純な.gdスクリプトを実行することができる。
この機能は、アセットのバッチ変換やカスタムインポート/エクスポートなどの大規模プロジェクトで特に役立つ。

スクリプトのシーンツリーまたは :ref:`メインループ <jホップステップメインループjump>` から継承する必要がある。

仕組みの簡単な例を次に示す。

.. code:: python

   #sayhello.gd
   extends SceneTree

   func _init():
       print("Hello!")
       quit()

そして、実行する。

::

   user@host:~/newgame$ godot -s sayhello.gd
   Hello!

project.godotがPathに存在しない場合、現在のPath現在の作業ディレクトリであると見なされる( ``-path`` が指定されていない限り)。


.. 英語の原文：スクリプトの実行
   Running a script
   ----------------

   It is possible to run a simple .gd script from the command line. This
   feature is especially useful in large projects, for batch
   conversion of assets or custom import/export.

   The script must inherit from SceneTree or MainLoop.

   Here is a simple example of how it works:

   .. code:: python

       #sayhello.gd
       extends SceneTree

       func _init():
           print("Hello!")
           quit()

   And how to run it:

   ::

       user@host:~/newgame$ godot -s sayhello.gd
       Hello!

   If no project.godot exists at the path, current path is assumed to be the
   current working directory (unless ``-path`` is specified).

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
