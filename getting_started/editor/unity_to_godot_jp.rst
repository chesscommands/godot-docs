.. _unity_to_godot_jp:

..    references :
..    https://wiki.unrealengine.com/Unity3D_Developer's_Guide_to_Unreal_Engine_4
..    https://docs.unrealengine.com/latest/INT/GettingStarted/FromUnity/




































UnityからGodotEngineへ
============================================

今回は、Unityユーザの視点からGodot Engineの概要を説明し、既存のUnityエクスペリエンスをGodotの世界に移行を支援する目的がある。

.. note::

   この記事では、Unityの古いバージョンについて説明する。ネスト可能なプレハブ( 'Nested prefabs' )がUnity 2018.3に追加された。
   NestableプレハブはGodotのシーンに似ており、シーンの編集によりGodotのようなアプローチを可能にする。





.. 英語の原文：UnityからGodotEngineへ
   From Unity to Godot Engine
   ==========================

   This guide provides an overview of Godot Engine from the viewpoint of a Unity user,
   and aims to help you migrate your existing Unity experience into the world of Godot.

   .. note::

      This article talks about older versions of Unity. Nestable prefabs ('Nested prefabs') were added to Unity 2018.3. Nestable prefabs are analogous to Godot's scenes, and allow a more Godot-like approach to scene organisation.


































相違
------------

.. list-table:: 
   :header-rows: 1
   :widths: 5, 10, 10

   * - 
     - Unity
     - Godot
   * - ライセンス
     - 収益上限と使用制限付きの独自のクローズド無料ライセンス
     - MITライセンス、制限なしの無料の完全オープンソース
   * - OS (エディタ)
     - Windows, macOS, Linux (非公式及び非サポート)
     - Windows, macOS, X11 (Linux, \*BSD)
   * - OS (エクスポート)
     - | * **デスクトップ** Windows, macOS, Linux
       | * **モバイル** Android, iOS, Windows Phone, Tizen
       | * **Web** WebAssembly or asm.js
       | * **コンシューマ** PS4, PS Vita, Xbox One, Xbox 360, Wii U, Nintendo 3DS
       | * **VR** Oculus Rift, SteamVR, Google Cardboard, Playstation VR, Gear VR, HoloLens
       | * **TV** Android TV, Samsung SMART TV, tvOS
     - | * **デスクトップ** Windows, macOS, X11
       | * **モバイル** Android, iOS
       | * **Web** WebAssembly
       | * **コンソール** Seedoc_consoles
       | * **VR** Oculus Rift, SteamVR
   * - シーンシステム
     - | * コンポーネント/シーン (GameObject > Component)
       | * プレハブ
     - :ref:`シーンツリーのノード <doc_scenes_and_nodes_jp>` (シーンのネストや他のシーンを継承可能)
   * - サードパーティツール
     - | * Visual Studio
       | * VS Code
     - | * :ref:`External editors are possible <doc_external_editor>`
       | * :ref:`Android SDK for Android export <doc_exporting_for_android>`
   * - 顕著な利点
     - | * 巨大なコミュニティ
       | * 大規模資産ストア
     - | * シーンシステム
       | * :ref:`アニメーションパイプライン <doc_animations>`
       | * :ref:`書きやすいシェーダ <doc_shading_language>`
       | * デバイス上でのデバッグ

.. todo::

   リンクの確認。


.. 英語の原文：相違
   Differences
   -----------

   +-------------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   |                   | Unity                                                                              | Godot                                                                                                          |
   +===================+====================================================================================+================================================================================================================+
   | License           | Proprietary, closed, free license with revenue caps and usage restrictions         | MIT license, free and fully open source without any restriction                                                |
   +-------------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | OS (editor)       | Windows, macOS, Linux (unofficial and unsupported)                                 | Windows, macOS, X11 (Linux, \*BSD)                                                                             |
   +-------------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | OS (export)       | * **Desktop:** Windows, macOS, Linux                                               | * **Desktop:** Windows, macOS, X11                                                                             |
   |                   | * **Mobile:** Android, iOS, Windows Phone, Tizen                                   | * **Mobile:** Android, iOS                                                                                     |
   |                   | * **Web:** WebAssembly or asm.js                                                   | * **Web:** WebAssembly                                                                                         |
   |                   | * **Consoles:** PS4, PS Vita, Xbox One, Xbox 360, Wii U, Nintendo 3DS              | * **Console:** See :ref:`doc_consoles`                                                                         |
   |                   | * **VR:** Oculus Rift, SteamVR, Google Cardboard, Playstation VR, Gear VR, HoloLens| * **VR:** Oculus Rift, SteamVR                                                                                 |
   |                   | * **TV:** Android TV, Samsung SMART TV, tvOS                                       |                                                                                                                |
   +-------------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | Scene system      | * Component/Scene (GameObject > Component)                                         | :ref:`Scene tree and nodes <doc_scenes_and_nodes>`, allowing scenes to be nested and/or inherit other scenes   |
   |                   | * Prefabs                                                                          |                                                                                                                |
   +-------------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | Third-party tools | Visual Studio or VS Code                                                           | * :ref:`External editors are possible <doc_external_editor>`                                                   |
   |                   |                                                                                    | * :ref:`Android SDK for Android export <doc_exporting_for_android>`                                            |
   +-------------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | Notable advantages| * Huge community                                                                   | * Scene System                                                                                                 |
   |                   | * Large assets store                                                               | * :ref:`Animation Pipeline <doc_animations>`                                                                   |
   |                   |                                                                                    | * :ref:`Easy to write Shaders <doc_shading_language>`                                                          |
   |                   |                                                                                    | * Debug on Device                                                                                              |
   |                   |                                                                                    |                                                                                                                |
   |                   |                                                                                    |                                                                                                                |
   +-------------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+


































エディタ
----------------

Godot Engineは、ゲームを構築できる豊富な機能を備えたエディタを提供する。
以下の図は、両方のエディタのデフォルトのレイアウトを色つきのブロックで表示し、一般的な機能を示している。

.. image:: img/unity-gui-overlay.png
.. image:: img/godot-gui-overlay.png

どちらのエディタも似ているように見えるかもしれないが、潜在的には多くの違いがある。
どちらもファイルシステムを使用してプロジェクトを整理できるが、Godotの活動は、単一の構成ファイル・最小限のテキスト形式・メタデータなしでより簡単になっている。
これにより、Git・Subversion・MercurialなどのVCSシステムに対してGodotがより使いやすくなる。

Godotのシーンドックは、UnityのHierarchyパネルに似ているが、各ノードには特定の機能があるため、Godotで使用される機能が視覚的に分かりやすくなっている。
そのため、シーンが一目で何をするかを理解するのが簡単だ。

Godotのインスペクタは最小限であり、プロパティのみを表示する。
これにより、オブジェクトは、API言語の機能を隠すこと無く、より有用なパラメータをユーザに公開できる。
さらに、Godotではこれらのプロパティを視覚的にアニメーション化できる。
コードを記述する必要なく、色・テクスチャ・列挙・リソースへのリンクをリアルタイムで変更できる。

画面上部のツールバーは、両方のエディタで似ており、プロジェクトの再生を制御できる。
Godotのプロジェクトは、エディタ内では無く、別のウィンドウで実行される。
（ただし、ツリーとオブジェクトは、デバッガウィンドウで引き続き探索できる）

このアプローチ(訳者：どのアプローチ？)には、Godotで実行中のゲームを様々な角度から探索できないという欠点がある(しかし、将来サポートされる可能性があり、実行中のゲームでの衝突ギズモの表示は既にサポート対象だ)が、引き換えにいくつかの利点がある。

- プロジェクトの実行と終了は高速(Unityは保存し、プロジェクトを実行し、プロジェクトを閉じてから前の状態をリロードする必要がある)。
- エディタに加えられた変更はゲームですぐに有効になり、ゲームが閉じられても失われない(同期不要)であり、ライブ編集ははるかに便利になっている。
  これにより、プレイ中にレベルを作成するなどの素晴らしいワークフローが可能になる。
- ゲームは別のプロセスで実行されるため、エディタはより安定している。

最後に、Godotの上部のツールバーには、リモートでバッグ用のメニューが含まれている。
これらのオプションを使用した場合、デバイス(HTML5を介して接続されたスマートフォン・タブレット・ブラウザ)に展開し、ゲームのエクスポート後に、デバッグ/ライブ編集できる。



.. 英語の原文：エディタ
   The editor
   ----------

   Godot Engine provides a rich-featured editor that allows you to build your games.
   The pictures below display the default layouts of both editors with colored blocks to indicate common functionalities.

   .. image:: img/unity-gui-overlay.png
   .. image:: img/godot-gui-overlay.png

   While both editors may seem similar, there are many differences below the surface.
   Both let you organize the project using the filesystem,
   but Godot's approach is simpler with a single configuration file, minimalist text format,
   and no metadata. This makes Godot more friendly to VCS systems, such as Git, Subversion, or Mercurial.

   Godot's Scene panel is similar to Unity's Hierarchy panel but, as each node has a specific function,
   the approach used by Godot is more visually descriptive. It's easier to understand
   what a scene does at a glance.

   The Inspector in Godot is more minimal, it shows only properties.
   Thanks to this, objects can expose more useful parameters to the user
   without having to hide functionality in language APIs. As a plus, Godot allows animating any of those properties visually.
   Changing colors, textures, enumerations, or even links to resources in real-time is possible without needing to write code.

   The Toolbar at the top of the screen is similar in both editors, offering control over project playback.
   Projects in Godot run in a separate window, rather than inside the editor
   (but the tree and objects can still be explored in the debugger window).

   This approach has the disadvantage that in Godot the running game can't be explored from different angles
   (though this may be supported in the future and displaying collision gizmos in the running game is already possible),
   but in exchange has several advantages:

   - Running the project and closing it is fast (Unity has to save, run the project, close the project, and then reload the previous state).
   - Live editing is a lot more useful because changes done to the editor take effect immediately in the game and are not lost (nor have to be synced) when the game is closed. This allows fantastic workflows, like creating levels while you play them.
   - The editor is more stable because the game runs in a separate process.

   Finally, Godot's top toolbar includes a menu for remote debugging.
   These options allow deployment to a device (connected phone, tablet, or browser via HTML5),
   and debugging/live editing on it after the game is exported.

































シーンシステム
----------------------------

これは、UnityとGodotの最も重要な違いであり、ほとんどのGodotユーザのお気に入りの機能と言っても過言ではない。

Godotのシーンシステムは、表面上はUnityに似ている。
'level' はノードのコレクションで構成され、各ノードには独自の目的がある。
スプライト(Sprite)・メッシュ(Mesh)・ライト(Light)など。
ただし、Godotでは、ノードはツリー配置の構成になる。
各ノードは複数の子を持ち、それぞれがメインシーンのサブシーンに割り当てられる。
これは、異なるファイルに保存された異なるシーンでシーン全体の構築が可能であることを意味する。

例えば、プラットフォームの提供を考えることにする。
複数の要素で構成する。

- レンガ
- コイン
- プレイヤー
- 敵

Unityでは、すべてのゲームオブジェクトをシーンに配置する。
プレイヤー・複数の敵のインスタンス・レンガを至る所に配置して、起伏のある地面を形成し、次にゲーム全体にコインの複数のインスタンスを配置する。

.. memo

   レベルの意図が全く分からない。そのため、全く異なる言葉に置き換えた。あっているか保証できない。

Godotでは、シーン全体を3つの独立した小さなシーンに分割し、メインシーンにインスタンス化する。

1. **プレイヤーだけのシーン**

プレイヤーを様々な親シーン(例えば 'レベル' シーン)で使用する要素として考える。
この場合、プレイヤー要素には少なくともAnimatedSpriteノードが必要になる。
このノードには、さまざまなアニメーション(歩行などのアニメーション)に必要なスプライトテクスチャが含まれている。

2. **敵のシーン**

敵は、いくつかのシーンで使用したい要素でもある。
プレイヤーノードとほぼ同じ扱い。
唯一の違いは、スクリプト(敵の行動を生成するために 'AI' 処理が必要)とAnimatedSpriteノードで使用されるスプライトテクスチャが必要になる。

3. **レベルシーン**

レベルシーンは、ブリック(プラットフォーム用)・コイン(プレイヤーによる収集用)・敵シーンのいくつかのインスタンスで構成される。
各インスタンスは、レベルシーンツリーのノードになる。
これらのインスタンスは別々の敵であり、最初は敵のシーンで定義されている動作と外観を共有している。
Enemyノードごとに異なるプロパティを設定できる(例えば、色の変更など)。

4. **メインシーン**

メインシーンは、プレイヤーインスタンスノードとレベルインスタンスノードの2つの子を持つ1つのルートノードで構成される。
ルートノードはどのような種類でも構わない。
一般に、最も汎用性のある "Node" ノードなどの "root" 型や "Node2D" (すべての2D関連ノードのルート型)・ "Spatial" (すべての3D関連ノード)・ "Control" (すべてのGUI関連ノードのルート型)。

今までの説明からすべてのシーンはツリーとして構成される。
ノードのプロパティについても同様の扱いだ。
Unityのようにノードに衝突コンポーネントを *追加* して衝突可能にしないこと。
その代わりに、このノードを衝突プロパティを持つ新しい特定のノードの *子* に割り当てる。
Godotは、使用法に応じてさまざまな衝突型のノードを備えている( :ref:`Physics introduction <doc_physics_introduction>` を参照すること )


.. todo::

   日本語の言い回しを考える。
   そしてリンクの確認。

- このシステムの利点として、

  - Godotoのシステムは、周知されたオブジェクト指向のパラダイムに近い：
    Godotは、明確に "ゲームオブジェクト" ではない多くのノードを提供するが、子には独自機能を提供する。
    継承として。

- シーンツリーの深さを潜在的に増加させることへの懸念として、(Unityでは、空のゲームオブジェクト内にゲームオブジェクトを配置することで、ゲームオブジェクトの整理が許可されているはずだが？)

  - Godotでは、シーンのサブツリーを抽出し、それを独自シーンにすることができる。
    そのため、シーンツリーが深くなる場合、より小さなサブツリーに分割し、深くなることを回避できる。
    これは、任意のノードの子として任意のサブツリーを含めることができるため、再利用性にとって優れている。
    Unityの空のゲームオブジェクトに複数のゲームオブジェクトを配置した場合、同じ機能は提供されない。


.. 英語の原文：シーンシステム
   The scene system
   ----------------

   This is the most important difference between Unity and Godot and the favourite feature of most Godot users.

   Working on a 'level' in Unity usually means embedding all the required assets in a scene
   and linking them together with components and scripts.

   Godot's scene system is superficially similar to Unity. A 'level' consists of a collection of nodes, each with its own purpose: Sprite, Mesh, Light, etc. However, in Godot the nodes are arranged in a tree. Each node can have multiple children, which makes each a subscene of the main scene.
   This means you can compose a whole scene with different scenes stored in different files.

   For example, think of a platformer level. You would compose it with multiple elements:

   - Bricks
   - Coins
   - The player
   - The enemies

   In Unity, you would put all the GameObjects in the scene: the player, multiple instances of enemies,
   bricks everywhere to form the ground of the level and then multiple instances of coins all over the level.
   You would then add various components to each element to link them and add logic in the level: For example,
   you'd add a BoxCollider2D to all the elements of the scene so that they can collide. This principle is different in Godot.

   In Godot, you would split your whole scene into three separate, smaller scenes, and instance them in the main scene.

   1. **A scene for the Player alone.**

   Consider the player as an element we'd like to use in different parent scenes (for instance 'level' scenes). In our case, the player element needs at least an AnimatedSprite node. This node contains the sprite textures necessary for various animations (for example, a walking animation).

   2. **A scene for the Enemy.**

   An enemy is also an element we'd like to use in several scenes. It's almost the same
   as the Player node. The only differences are the script (it needs 'AI' routines to generate the enemy's behaviour)
   and the sprite textures used by the AnimatedSprite node.

   3. **A Level scene.**

   A Level scene is composed of Bricks (for platforms), Coins (for the player to collect) and a
   number of instances of the Enemy scene. Each instance is a node in the Level scene tree. These instances are separate enemies,
   which initially have shared behaviour and appearance as defined in the Enemy scene. You can set different properties for each Enemy node (to change its color, for example).

   4. **A Main scene.**
   The Main scene would be composed of one root node with 2 children: a Player instance node, and a Level instance node.
   The root node can be anything, generally a "root" type such as "Node" which is the most global type,
   or "Node2D" (root type of all 2D-related nodes), "Spatial" (root type of all 3D-related nodes) or
   "Control" (root type of all GUI-related nodes).

   As you can see, every scene is organized as a tree. The same goes for nodes' properties: you don't *add* a
   collision component to a node to make it collidable like Unity does. Instead, you make this node a *child* of a
   new specific node that has collision properties. Godot features various collision types nodes, depending on the usage
   (see the :ref:`Physics introduction <doc_physics_introduction>`).

   - What are the advantages of this system? Wouldn't this system potentially increase the depth of the scene tree? And doesn't Unity already allow you to organize GameObjects by putting them inside empty GameObjects?

       - Godot's system is closer to the well-known object-oriented paradigm: Godot provides a number of nodes which are not clearly "Game Objects", but they provide their children with their own capabilities: this is inheritance.
       - Godot allows the extraction of a subtree of a scene to make it a scene of its own. So if a scene tree gets too deep, it can be split into smaller subtrees. This is better for reusability, as you can include any subtree as a child of any node. Putting multiple GameObjects in an empty GameObject in Unity does not provide the same functionality.

































プロジェクト組織
--------------------------------

.. image:: img/unity-project-organization-example.png

完璧なプロジェクトアーキテクチャはない。
UnityおよびGodotで動作するように、任意のアーキテクチャを作成できる。

ただし、Unityプロジェクトの一般的なアーキテクチャでは、ルートディレクトリにAssetsフォルダが1つある。
このフォルダには、オーディオ・グラフィック・モデル・マテリアル・スクリプト・シーンなどのアセットの種類ごとにさまざまなフォルダを内包している。

Godotでは、シーンをより小さなシーンに分割できるため、各シーンとサブシーンはプロジェクト内のファイルとして存在するため、プロジェクトを少し異なる方法で整理することを推奨する。
:ref:`doc_project_organization` を参照すること。

.. todo::

   リンクの確認。


.. 英語の原文：プロジェクト組織
   Project organization
   --------------------

   .. image:: img/unity-project-organization-example.png

   There is no perfect project architecture.
   Any architecture can be made to work in either Unity and Godot.

   However, a common architecture for Unity projects is to have one Assets folder in the root directory
   that contains various folders, one per type of asset: Audio, Graphics, Models, Materials, Scripts, Scenes, and so on.

   Since Godot allows splitting scenes into smaller scenes, each scene and subscene existing as a file in the project, we recommend organizing your project a bit differently.
   This wiki provides a page for this: :ref:`doc_project_organization`.


































Unityで言うプレハブはどこにある？
------------------------------------------------------------------

Unityが提供するプレハブは、シーンの 'template' 要素に当たる。
再利用可能であり、シーン内に存在するプレハブの各インスタンスには独自の存在があり、しかしそれらはすべてプレハブで定義されてたプロパティを持っている。

Godotはプレハブ自体を提供していないが、同じ機能がシーンシステムによって提供されている。
シーンシステムはツリーとして構成されている。
Godotを使う場合、シーンのサブツリーをシーンファイルとして保存できる。
この保存されたシーンは、任意のノードの子として、何度でもインスタンスで呼び出せる。
しかも、保存したシーンに加えた変更がインスタンスで呼び出したシーンにも反映される。
ただし、インスタンスに加えた変更は、元の '保存したシーン' には影響しない。

.. image:: img/save-branch-as-scene.png

正確には、インスペクタパネルのインスタンスのパラメータを変更する。
このインスタンスを構成するノードは、最初はロックされている。
必要に応じてロックを解除する。
シーンツリーでインスタンスを右クリックし、メニューで "編集可能な子" にする必要がある。
このノードに "新しい" 子ノードを追加するためには不要な作業になる。
新しい子は、保存ファイルの '保存したシーン' ではなく、インスタンスに属することに注意すること。
'保存したシーン' のすべてのインスタンスに新しい子を追加する場合は、 '保存したシーン' そのものに新しい子を追加すべきだろう。

.. image:: img/editable-children.png
















.. 英語の原文：Unityで言うプレハブはどこにある？
   Where are my prefabs?
   ---------------------

   A prefab as provided by Unity is a 'template' element of the scene.
   It is reusable, and each instance of the prefab that exists in the scene has an existence of its own,
   but all of them have the same properties as defined by the prefab.

   Godot does not provide prefabs as such, but the same functionality is provided by its scene system:
   The scene system is organized as a tree. Godot allows you to save any subtree of a scene as a scene file. This new scene can then be instanced as many times as you want, as a child of any node.
   Any change you make to this new, separate scene will be applied to its instances.
   However, any change you make to the instance will not have any impact on the 'template' scene.

   .. image:: img/save-branch-as-scene.png

   To be precise, you can modify the parameters of an instance in the Inspector panel.
   The nodes that compose this instance are initially locked. You can unlock them if you need to by
   right-clicking the instance in the Scene tree and selecting "Editable children" in the menu.
   You don't need to do this to add *new* child nodes to this node.
   Remember that any new children will belong to the instance, not to the 'template' scene on disk.
   If you want to add new children to every instance of your 'template' scene, then you should add them in the 'template' scene.

   .. image:: img/editable-children.png

































用語集対応
--------------------

- ゲームオブジェクト ⇒ ノード
- コンポーネントを追加 ⇒ 継承
- プレハブ ⇒ 再利用可能なシーンファイル


.. 英語の原文：用語集対応
   Glossary correspondence
   -----------------------

   - GameObject -> Node
   - Add a component -> Inheriting
   - Prefab -> Reusable Scene file





































スクリプト：GDScript・C#・Visual Script
------------------------------------------------------------------------------

.. 英語の原文：スクリプト：GDScript・C#・Visual Script
   Scripting: GDScript, C# and Visual Script
   -----------------------------------------




































設計
^^^^^^^^^^^^

UnityはC#をサポートしている。
C#はVisual Studioとの統合から恩恵を受け、静的型付けなどの望ましい機能を備えている。

Godotは独自のスクリプト言語( :ref:`GDScript <doc_scripting>` )を提供し、 :ref:`Visual Script <toc-learn-scripting-visual_script>` および :ref:`C# <doc_c_sharp>` をサポートする。
GDScriptはその構文をPythonから拝借しているが、Pythonとの関係はない。
独自スクリプト言語の理由について疑問がある場合は、 :ref:`doc_gdscript_jp` および :ref:`doc_faq` を参照すること。
GDScriptはGodotAPIに強く結びついており、習得にそれほど時間は掛からない。
経験豊富なプログラマのある夜から完全な初心者の1週間まで(訳者：どういう意味？)。

.. todo::

   リンクの確認。

Unityでは、必要な数のスクリプトをゲームオブジェクトに添付できる。
各スクリプトは、挙動をゲームオブジェクトに追加する(訳者：挙動？)。
例えば、プレイヤーのコントロールと特定のゲーム論理を制御する別のスクリプトに反応するようにスクリプトを添付できる。

- ターゲットノードとその現在の親の間に新しいノードを追加後、この新しいノードにスクリプトを追加する。
- または、ターゲットノードを複数の子に分割し、それぞれに1つのスクリプトを添付できる。

瞬く間に複雑なシーンツリーを構築できるため、混乱するのは簡単だろう。
そのため、複雑なシーンを複数の小さなシーンに分割することを検討すべきだろう。


.. 英語の原文：設計
   Design
   ^^^^^^

   Unity supports C#. C# benefits from its integration with Visual Studio and has desirable features such as static typing.

   Godot provides its own scripting language, :ref:`GDScript <doc_scripting>` as well as support
   for :ref:`Visual Script <toc-learn-scripting-visual_script>` and :ref:`C# <doc_c_sharp>`.
   GDScript borrows its syntax from Python, but is not related to it. If you wonder about the reasoning for a custom scripting language,
   please read the :ref:`doc_gdscript` and :ref:`doc_faq` pages. GDScript is strongly attached to the Godot API
   and doesn't take long to learn: Between one evening for an experienced programmer and a week for a complete beginner.

   Unity allows you to attach as many scripts as you want to a GameObject.
   Each script adds a behaviour to the GameObject: For example, you can attach a script so that it reacts to the player's controls,
   and another that controls its specific game logic.

   In Godot, you can only attach one script per node. You can use either an external GDScript file
   or include the script directly in the node. If you need to attach more scripts to one node, then you may consider two solutions,
   depending on your scene and on what you want to achieve:

   - either add a new node between your target node and its current parent, then add a script to this new node.
   - or, you can split your target node into multiple children and attach one script to each of them.

   As you can see, it can be easy to turn a scene tree to a mess. Consider splitting any complicated scene into multiple, smaller branches.



































接続：グループとシグナル
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

スクリプトを介してノードに接続し、それらに組み込まれた関数またはユーザ定義関数を呼び出すことで、ノードを制御できる。
グループにノードを配置し、このグループのすべてのノードで関数を呼び出すこともできる。
詳細は :ref:`scripting documentation <doc_scripting_continued>` を参照すること。

ノードは、指定された挙動発生時に信号を送信する。
任意の関数を呼び出すように信号を設定できる。
カスタムシグナルを定義し、きっかけとなる見計らいの指定もできる。
詳細は :ref:`シグナルドクメンテーション <doc_gdscript_signals_jp>` を参照すること。

.. todo::

   リンクの確認。


.. 英語の原文：接続：グループとシグナル
   Connections: groups and signals
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   You can control nodes by accessing them via script and calling built-in
   or user-defined functions on them. You can also place nodes in a group
   and call functions on all nodes in this group. See more in the 
   :ref:`scripting documentation <doc_scripting_continued>`.

   Nodes can send a signal when a specified action occurs. A signal can
   be set to call any function. You can define custom signals and specify
   when they are triggered. See more in the :ref:`signals documentation <doc_gdscript_signals>`.




































スクリプトのシリアル化
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unityは、次の二つの方法でスクリプトのシリアル化を処理する。

- 暗黙的：型がシリアル化可能な型である場合、クラス内のすべてのパブリックフィールドは自動的にシリアル化される(  ``辞書`` は例外できにできない)。
- 明示的：非公開フィールドは ``[SerializeField]`` 属性を使用してシリアル化する。

Godotにはスクリプトシリアル化システムも組み込まれているが、明示的にのみ機能する。
``export`` キーワードを使用して、任意のシリアル化可能な型( :ref:`built-in and various engine types <doc_binary_serialization_api>` ・ :ref:`class_Array` ・ :ref:`class_Dictionary` を含む)をシリアル化できる。
:ref:`エクスポートドクメンテーション <doc_gdscript_exports_jp>` を参照すること。

Unityには、カスタムAssetオブジェクトのシリアル化に使用される ``ScriptableObject`` と呼ばれるデータ型もある。
Godotに同等するオブジェクトは、すべてのリソースの基本クラス :ref:`class_Resource` がそれに当たる。
:ref:`class_Resource` を継承するスクリプトを作成した場合、カスタムのシリアライズ可能なオブジェクトを作成できる。
リソースの詳細は、 :ref:`here <doc_resources>` を参照すること。

.. todo::

   リンクの確認。


.. 英語の原文：スクリプトのシリアル化
   Script serialization
   ^^^^^^^^^^^^^^^^^^^^

   Unity can handle script serialization in two ways:

   - Implicit: All public fields in a class are automatically serialized if the type is a serializable type (``Dictionary`` is not serializable).
   - Explicit: Non-public fields can be serialized using the ``[SerializeField]`` attribute.

   Godot also has a built-in script serialization system, but it works only explicitly.
   You can serialize any serializable type (:ref:`built-in and various engine types <doc_binary_serialization_api>`,
   including :ref:`class_Array` and :ref:`class_Dictionary`) using the ``export`` keyword.
   See the :ref:`exports documentation <doc_gdscript_exports>` for details.

   Unity also has a data type called ``ScriptableObject`` used to serialize custom asset objects.
   Its equivalent in Godot is the base class for all resources: :ref:`class_Resource`.
   Creating a script that inherits :ref:`class_Resource` will allow you to create custom serializable objects. More information about resources can be found :ref:`here <doc_resources>`.


































GodotでのC++使用
--------------------------------

Godotでは、APIを使用してC++でプロジェクトを直接開発できるが、現時点のUnityでは不可能だ。
例えば、Godotエンジンのエディタは、GodotAPIを使用してC++で記述された "game" と見なすことができる。

C++でGodotを使用することに興味がある場合は、 :ref:`Developing in C++ <doc_introduction_to_godot_development>` を参照すること。

.. todo::

   リンクの確認。


.. 英語の原文：GodotでのC++使用
   Using Godot in C++
   ------------------

   Godot allows you to develop your project directly in C++ by using its API, which is not possible with Unity at the moment. 
   As an example, you can consider Godot Engine's editor as a "game" written in C++ using the Godot API.

   If you are interested in using Godot in C++, you may want to start reading the :ref:`Developing in
   C++ <doc_introduction_to_godot_development>` page.

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
