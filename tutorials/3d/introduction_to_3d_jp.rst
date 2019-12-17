.. _doc_introduction_to_3d_jp:


































3Dの概要
================

3Dゲームの作成は難しい経験に関わることになるだろう。
Z座標という余分な存在により、2Dゲームを簡素に開発できた一般的な多くの経験を活かせなくなる。
この移行を支援するために、Godotは2Dおよび3Dに同様のAPIを用いたため、新しい経験に関われないまま過去の技術を流用して開発ができてしまう。
ほとんどのノードは同じであり、2D版と3D版の両方に存在する。
実際、3Dプラットフォームチュートリアルまたは3D研磨ティックキャラクタチュートリアルを確認する価値がある。

3Dでは、数学は2Dよりもやや複雑な経験に携われる。
従い、経験からでは無く、wikiの :ref:`doc_vector_math` (数学者はエンジニアでは無く、ゲーム開発者向けに特別に作成されたもの)を勉強したときのみ、3Dゲームを効率的に開発する道が開かれる。



.. 英語の原文：3Dの概要
   Introduction to 3D
   ==================

   Creating a 3D game can be challenging. That extra Z coordinate makes
   many of the common techniques that helped to make 2D games simple no
   longer work. To aid in this transition, it is worth mentioning that
   Godot uses similar APIs for 2D and 3D. Most nodes are the same and
   are present in both 2D and 3D versions. In fact, it is worth checking
   the 3D platformer tutorial, or the 3D kinematic character tutorials,
   which are almost identical to their 2D counterparts.

   In 3D, math is a little more complex than in 2D, so also checking the
   :ref:`doc_vector_math` entry in the wiki (which was especially created for game
   developers, not mathematicians or engineers) will help pave the way for you
   to develop 3D games efficiently.


































空間(Spatial)ノード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Node2D <class_Node2D>` は、2Dのベースノードになる。
:ref:`Control <class_Control>` は、すべてのGUIのベースノードになる。
この推論に従い、3Dエンジンはすべての3Dに対して :ref:`Spatial <class_Spatial>` ノードを使用する。

.. image:: img/tuto_3d1.png

空間ノードには、親ノードに相対的なローカル変換がある(親ノードにも空間(Spatial)タイプから **または継承** している場合)。
この変換は 4x3 :ref:`Transform <class_Transform>` として、または位置・オイラー回転(x、y、z角度)及びスケールを表す3 :ref:`Vector3 <class_Vector3>` メンバとしてアクセスできる。

.. image:: img/tuto_3d2.png

訳者：何を言いたいのか全く分からない。

.. 英語の原文：空間(Spatial)ノード
   Spatial node
   ~~~~~~~~~~~~

   :ref:`Node2D <class_Node2D>` is the base node for 2D.
   :ref:`Control <class_Control>` is the base node for everything GUI.
   Following this reasoning, the 3D engine uses the :ref:`Spatial <class_Spatial>`
   node for everything 3D.

   .. image:: img/tuto_3d1.png

   Spatial nodes have a local transform, which is relative to the parent
   node (as long as the parent node is also of **or inherits** from the type
   Spatial). This transform can be accessed as a 4x3
   :ref:`Transform <class_Transform>`, or as 3 :ref:`Vector3 <class_Vector3>`
   members representing location, Euler rotation (x,y and z angles) and
   scale.

   .. image:: img/tuto_3d2.png


































3Dコンテンツ
~~~~~~~~~~~~~~~~~~~~~~~~

画像コンテンツの読み込みと描画が簡単な2Dとは異なり、3Dはもう少し難しくなる。
コンテンツは、特別な3Dツールで(通常DCCと呼ばれる)作成し、Godotでインポートするために交換ファイル形式にエクスポートする必要がある(3D形式は画像ほど標準化されていない)。

.. 英語の原文：3Dコンテンツ
   3D content
   ~~~~~~~~~~

   Unlike 2D, where loading image content and drawing is straightforward,
   3D is a little more difficult. The content needs to be created with
   special 3D tools (usually referred to as DCCs) and exported to an
   exchange file format in order to be imported in Godot (3D formats are
   not as standardized as images).


































DCCの作成モデル
------------------------------

.. FIXME:

   Godot3.xワークフローを正しく説明するための更新が必要になる。
   （既存の doc_importing_3d_meshes_jp インポータを参照するために使用）

Godotに3Dモデルをインポートするには、2つのパイプラインがある。
最初の最も一般的な物は :ref:`doc_importing_3d_scenes` によるもので、アニメーション・スケルタルリグ・ブレンドシェイプなどを含むシーン全体(DCCで確認済み)をインポートできる。

訳者：カタカナの用語ばかりで全く理解できない。

2番目のパイプラインは、単純な.OBJファイルをメッシュリソースとしてインポートし、表示用に :ref:`MeshInstance <class_MeshInstance>` ノード内に配置できる。


.. 英語の原文：DCCの作成モデル
   DCC-created models
   ------------------

   .. FIXME: Needs update to properly description Godot 3.x workflow
      (used to reference a non existing doc_importing_3d_meshes importer).

   There are two pipelines to import 3D models in Godot. The first and most
   common one is by :ref:`doc_importing_3d_scenes`, which allows you to import
   entire scenes (just as they look in the DCC), including animation,
   skeletal rigs, blend shapes, etc.

   The second pipeline is by importing simple .OBJ files as mesh resources,
   which can be then put inside a :ref:`MeshInstance <class_MeshInstance>`
   node for display.



































生成されたジオメトリ
----------------------------------------

:ref:`ArrayMesh <class_ArrayMesh>` リソースを直接使用して、カスタムジオメトリを作成することができる(訳者：そもそもそれって何？)。
単純に配列を作成し、 :ref:`ArrayMesh.add_surface_from_arrays() <class_ArrayMesh_method_add_surface_from_arrays>` 関数を使用する。
:ref:`SurfaceTool <class_SurfaceTool>` と言うヘルパークラスも利用できる。
これは、インデックス作成・法線・タンジェントなどのより簡単なAPIとヘルパーを提供する。

いずれの場合でも頂点配列を作成して3D APIに送信したときパフォーマンスが大幅に低下するため、このメソッドは静的ジオメトリ(頻繁に更新されないモデル)を生成するためのもの。


.. 英語の原文：生成されたジオメトリ
   Generated geometry
   ------------------

   It is possible to create custom geometry by using the
   :ref:`ArrayMesh <class_ArrayMesh>` resource directly. Simply create your arrays
   and use the :ref:`ArrayMesh.add_surface_from_arrays() <class_ArrayMesh_method_add_surface_from_arrays>`
   function. A helper class is also available, :ref:`SurfaceTool <class_SurfaceTool>`,
   which provides a more straightforward API and helpers for indexing,
   generating normals, tangents, etc.

   In any case, this method is meant for generating static geometry (models
   that will not be updated often), as creating vertex arrays and
   submitting them to the 3D API has a significant performance cost.




































即時ジオメトリ
----------------------------

代わりに、頻繁に更新される単純なジオメトリを生成する必要がある場合、Godotはポイントを作成するOpenGL 1.xスタイルのイミディエイトモードAPIを提供する特別なノード :ref:`ImmediateGeometry <class_ImmediateGeometry>` を提供する。
線・三角形など。

.. 英語の原文：即時ジオメトリ
   Immediate geometry
   ------------------

   If, instead, there is a requirement to generate simple geometry that
   will be updated often, Godot provides a special node,
   :ref:`ImmediateGeometry <class_ImmediateGeometry>`,
   which provides an OpenGL 1.x style immediate-mode API to create points,
   lines, triangles, etc.

































2D in 3D
----------------

Godotは強力な2Dエンジンを搭載しているが、多くのタイプのゲームは3D環境で2Dを使用している(訳者：Godotは違うってことが言いたい？)。
回転しない固定カメラ(直交または遠近法)を使用することで、 :ref:`Sprite3D <class_Sprite3D>` や :ref:`AnimatedSprite3D <class_AnimatedSprite3D>` などのノードを使用して、ミキシングを活用する2Dゲームを作成できる。
3D背景・より現実的な視差・照明/影など。

欠点は、もちろん素の2Dと比較して複雑さが増し、パフォーマンスが低下することとピクセル単位での作業の参照が無いことがあげられる。


.. 英語の原文：2D in 3D
   2D in 3D
   --------

   While Godot packs a powerful 2D engine, many types of games use 2D in a
   3D environment. By using a fixed camera (either orthogonal or
   perspective) that does not rotate, nodes such as
   :ref:`Sprite3D <class_Sprite3D>` and
   :ref:`AnimatedSprite3D <class_AnimatedSprite3D>`
   can be used to create 2D games that take advantage of mixing with 3D
   backgrounds, more realistic parallax, lighting/shadow effects, etc.

   The disadvantage is, of course, that added complexity and reduced
   performance in comparison to plain 2D, as well as the lack of reference
   of working in pixels.



































環境
~~~~~~~~~~~~

シーンを編集する以外に、環境を編集することが頻繁に発生する。
Godotは :ref:`WorldEnvironment <class_WorldEnvironment>` ノードを提供する。
これにより、背景色・モード(スカイボックスを置くなど)を変更し、いくつかのタイプの組み込み後処理効果を適用できる。
環境はカメラでも上書きできる。

訳者：全く理解できない説明だ。


.. 英語の原文：環境
   Environment
   ~~~~~~~~~~~

   Besides editing a scene, it is often common to edit the environment.
   Godot provides a :ref:`WorldEnvironment <class_WorldEnvironment>`
   node that allows changing the background color, mode (as in, put a
   skybox), and applying several types of built-in post-processing effects.
   Environments can also be overridden in the Camera.



































3Dビューポート
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3Dシーンの編集は、3Dタブで行う。
このタブは手動で選択できるが、空間ノードを選択することで自動的に有効になる。

.. image:: img/tuto_3d3.png


初期設定の3DシーンナビゲーションコントロールはBlenderに似ている(フリーソフトウェアパイプラインに何らかの一貫性を持たせることを目的としている)が、エディタの設定と他のツールと同様にマウスボタンと動作をカスタマイズするオプションが含まれている。


.. image:: img/tuto_3d4.png


.. 英語の原文：3Dビューポート
   3D viewport
   ~~~~~~~~~~~

   Editing 3D scenes is done in the 3D tab. This tab can be selected
   manually, but it will be automatically enabled when a Spatial node is
   selected.

   .. image:: img/tuto_3d3.png

   Default 3D scene navigation controls are similar to Blender (aiming to
   have some sort of consistency in the free software pipeline..), but
   options are included to customize mouse buttons and behavior to be
   similar to other tools in the Editor Settings:

   .. image:: img/tuto_3d4.png




































座標系
------------

Godotはすべてに `metric <https://en.wikipedia.org/wiki/Metric_system>`__ システムを使用する。
3D Physics 及びその他の領域はこのために調整されているため、通常異なるスケールを使用するのは得策とは言えない(何をしているのか分からない場合)。

3Dアセットを使用する場合は、常に正しいスケールで作業することが最善になる(DCCをメトリックに設定する)。
Godotはインポート後のスケーリングを可能にするが、ほとんどの場合これは機能するが、まれに、レンダリングや物理学などのデリケートな領域で浮動小数点精度の問題(グリッチまたはアーティファクト)を引き起こす可能性があるため、アーティストが常に機能するようにすること。
適切な規模で！！

Y座標は "上" に使用されるが、位置合わせが必要なほとんどのオブジェクト(ライト・カメラ・カプセルコライダー・車両など)では、Z軸は "方向" を指す方向として使用される。
この規模は大体次のことを意味する。

-  **X** ：側面
-  **Y** ：アップ/ダウン
-  **Z** ：前面/背面



.. 英語の原文：座標系
   Coordinate system
   -----------------

   Godot uses the `metric <https://en.wikipedia.org/wiki/Metric_system>`__
   system for everything. 3D Physics and other areas are tuned for this, so
   attempting to use a different scale is usually a bad idea (unless you
   know what you are doing).

   When working with 3D assets, it's always best to work in the correct
   scale (set your DCC to metric). Godot allows scaling post-import and,
   while this works in most cases, in rare situations it may introduce
   floating point precision issues (and thus, glitches or artifacts) in
   delicate areas, such as rendering or physics, so make sure your artists
   always work in the right scale!

   The Y coordinate is used for "up", though for most objects that need
   alignment (like lights, cameras, capsule collider, vehicle, etc.), the Z
   axis is used as a "pointing towards" direction. This convention roughly
   means that:

   -  **X** is sides
   -  **Y** is up/down
   -  **Z** is front/back



































スペースと操作のギズモ
--------------------------------------------

3Dビューでのオブジェクト移動は、マニピュレータギズモを介して行われる。
各軸は色で表される
⇒
赤(X)・緑(Y)・青(Z)。
この規則は、グリッドやその他のギズモにも適用される(また、シェーダ言語・Vector3・Colorなどのコンポーネントの順序にも適用される)。

.. image:: img/tuto_3d5.png

いくつかの便利なキーバインド：

- 配置または回転をスナップするには、移動・スケーリング・回転中に "Ctrl" キーを押す。
- ビューを選択したオブジェクトの中央に配置するには、 "f" キーを押す。


.. 英語の原文：スペースと操作のギズモ
   Space and manipulation gizmos
   -----------------------------

   Moving objects in the 3D view is done through the manipulator gizmos.
   Each axis is represented by a color: Red, Green, Blue represent X,Y,Z
   respectively. This convention applies to the grid and other gizmos too
   (and also to the shader language, ordering of components for
   Vector3,Color,etc.).

   .. image:: img/tuto_3d5.png

   Some useful keybindings:

   -  To snap placement or rotation, press the "Ctrl" key while moving, scaling
      or rotating.
   -  To center the view on the selected object, press the "f" key.
































表示メニュー
------------------------

表示オプションは、ビューポートのツールバーの "表示" メニューで制御される。

.. image:: img/tuto_3d6.png

このメニューを使用し、エディタの3Dビューでギズモを非表示にできる。

.. image:: img/tuto_3d6_1.png

特定の種類のギズモを非表示にするには、 "表示" メニューでオフに切り替える。

.. image:: img/tuto_3d6_2.png




.. 英語の原文：表示メニュー
   View menu
   ---------

   The view options are controlled by the "View" menu in the viewport's toolbar.

   .. image:: img/tuto_3d6.png

   You can hide the gizmos in the 3D view of the editor through this menu:

   .. image:: img/tuto_3d6_1.png

   To hide a specific type of gizmos, you can toggle them off in the "View" menu.

   .. image:: img/tuto_3d6_2.png

































デフォルト環境
----------------------------

プロジェクトマネージャから作成した場合、3D環境にはデフォルトの空がある。

.. image:: img/tuto_3d8.png

物理ベースのレンダリングがどのように機能するかを考えた場合、オブジェクトに間接光と反射光を提供するために、常にデフォルト環境で作業することを勧める。

.. 英語の原文：デフォルト環境
   Default environment
   -------------------

   When created from the Project Manager, the 3D environment has a default sky.

   .. image:: img/tuto_3d8.png

   Given how physically based rendering works, it is advised to always try to
   work with a default environment in order to provide indirect and reflected
   light to your objects.


































カメラ
------------

3D空間にいくつかのオブジェクトを配置したとして、シーンに :ref:`Camera <class_Camera>` が追加されない限り、何も表示されない。
カメラは、正投影または透視投影のいずれかで動作する。

.. image:: img/tuto_3d10.png

カメラは、親または祖父母のビューポートに関連付けられている(表示のみ)。
シーンツリーのルートはビューポートであるため、カメラはデフォルトでその上に表示されるが、サブビューポート(レンダーターゲットまたはピクチャーインピクチャとして)が必要な場合、表示するには独自の子カメラが必要になる。

.. image:: img/tuto_3d11.png

複数のカメラを扱う場合、ビューポートごとに次のルールが適用される。

- シーンツリーにカメラが存在しない場合、最初に入力したカメラがアクティブなカメラになる。
  シーンに入ってくるカメラは無視される( *current* として設定されていない限り)
- カメラに "*current*" プロパティが設定されている場合、シーン内の他のカメラに関係なく使用される。
  プロパティが設定されている場合、以前のカメラを置き換えてアクティブになる。
- アクティブなカメラがシーンツリーを離れた場合、ツリー順の最初のカメラが代わりに動く。

.. 英語の原文：カメラ
   Cameras
   -------

   No matter how many objects are placed in the 3D space, nothing will be
   displayed unless a :ref:`Camera <class_Camera>` is
   also added to the scene. Cameras can work in either orthogonal or
   perspective projections:

   .. image:: img/tuto_3d10.png

   Cameras are associated with (and only display to) a parent or grandparent
   viewport. Since the root of the scene tree is a viewport, cameras will
   display on it by default, but if sub-viewports (either as render target
   or picture-in-picture) are desired, they need their own children cameras
   to display.

   .. image:: img/tuto_3d11.png

   When dealing with multiple cameras, the following rules are enforced for
   each viewport:

   -  If no cameras are present in the scene tree, the first one that
      enters it will become the active camera. Further cameras entering the
      scene will be ignored (unless they are set as *current*).
   -  If a camera has the "*current*" property set, it will be used
      regardless of any other camera in the scene. If the property is set,
      it will become active, replacing the previous camera.
   -  If an active camera leaves the scene tree, the first camera in
      tree-order will take its place.
































ライト
------------

Godotのライトの数やライトのタイプに制限はない。
必要な数を追加できる(パフォーマンスが許す限り)。

.. 英語の原文：ライト
   Lights
   ------

   There is no limitation on the number of lights, nor of types of lights, in
   Godot. As many as desired can be added (as long as performance allows).


.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
