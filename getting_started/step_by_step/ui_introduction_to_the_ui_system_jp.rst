.. _doc_design_interfaces_with_the_control_nodes_jp:


































コントロールノードとのインタフェイスを設計する
============================================================================================

コンピュータのディスプレイ・携帯電話・テレビ画面には、あらゆる形と大きさがある。
ゲームを出荷するには、様々な画面比率と解像度に対応する必要がある。
すべての利用端末にレスポンシブインタフェイス(上記の説明通り、多様な形状と大きさ)に適応させるのは難しい場合がある。
ありがたいことに、Godotには、レスポンシブインタフェイスを設計及び管理するための堅牢なツールが付属している。

.. figure:: img/godot_editor_ui.png

   Godotのエディタは、エンジンのUIフレームワークで作成される。

ここでのあなたが学ぶことは、UI設計についてだ。

- ゲームのインタフェイスを構築するための最も便利な5つのコントロールノード
- UI要素のアンカーの使用方法
- コンテナを使用してユーザインタフェイスを効率的に配置及び配置する方法
- 最も一般的な5つのコンテナ( :ref:`GUIコンテナ <doc_gui_containers>` ドキュメントで詳細確認可能)

インタフェイスを制御し、他のスクリプトに接続する方法を学ぶには、
:ref:`Godotで最初のゲームUIを構築する<doc_ui_game_user_interface>`
ドキュメントを確認すること。

UIを設計するには、コントロールノードを使用する。
これらは、エディタ内に緑色のアイコンが付いたノードになる。
ライブゲージから複雑なアプリケーションまで作成するために、数十個用意している。
Godotエディタ自体は、コントロールノードを使用して構築される。

コントロールノードには、相互に機能するための固有のプロパティがある。
Node2DやSpriteなどの他のビジュアルノードには、これらの機能は無い。
従って、UIを構築するときは、できるだけ簡素なコントロールノードの使い方をしなければならない。

すべてのコントロールノードには同じメインプロパティを共有する。

#. アンカー
#. 境界矩形
#. フォーカスとその周辺
#. サイズフラグ ←訳者：どういう意味？
#. 余白
#. オプションのUIテーマ

制御ノードの基本を理解したとき、そこから派生するすべてのノードを学習する時間が短縮される。




.. 英語の原文：コントロールノードとのインタフェイスを設計する
    Design interfaces with the Control nodes
    ========================================

    Computer displays, mobile phones, and TV screens come in all shapes and
    sizes. To ship a game, you'll need to support different screen ratios
    and resolutions. It can be hard to build responsive interfaces that
    adapt to all platforms. Thankfully, Godot comes with robust tools to
    design and manage a responsive User Interface.

    .. figure:: img/godot_editor_ui.png

       Godot's editor is made with the engine's UI framework

    This guide will get you started with UI design. You will learn:

    -  The five most useful control nodes to build your games' interface
    -  How to work with the anchor of UI elements
    -  How to efficiently place and arrange your user interface using
       containers
    -  The five most common containers (at a later time, you can learn more about containers in
       the :ref:`GUI Containers <doc_gui_containers>` documentation page).

    To learn how to control the interface and connect it to other scripts,
    read :ref:`Build your first game UI in Godot <doc_ui_game_user_interface>`.

    To design your UI, you'll use the Control nodes. These are the nodes with green icons in the
    editor. There are dozens of them, for creating anything from life bars to
    complex applications. Godot's editor itself is built using Control nodes.

    Control nodes have unique properties that allow them to work well with one another.
    Other visual nodes, like Node2D and Sprite don't have these capabilities. So to
    make your life easier use Control nodes wherever possible when building your UIs.

    All control nodes share the same main properties:

    1. Anchor
    2. Bounding rectangle
    3. Focus and focus neighbor
    4. Size flags
    5. Margin
    6. The optional UI theme

    Once you understand the basics of the Control node, it will take you less time to learn all the
    nodes that derive from it.



































最も一般的な5つのUI要素
----------------------------------------------

Godotには、多数のコントロールノードが付属している。
それらの多くは、エディタプラグインとアプリケーションの構築を支援するのが今回説明するUI要素だ。

ほとんどのゲームでは、5種類のUI要素といくつかのコンテナを必要とする。
これらの5つのコントロールノードは次の通り。

#. Label：テキストの表示
#. TextureRect：主に背景に使用する。もしくは、静的画像を要求する場面で使用する。
#. TextureProgress：ライフゲージ・ゲームの読み込みバー・水平・垂直・放射状に用いる。
#. NinePatchRect：スケーラブルパネル(訳者：拡張情報表示？)に用いる。
#. TextureButton：ボタン

.. figure:: img/five_most_common_nodes.png

  UI設計のための5つの最も一般的なコントロールノード






.. 英語の原文：最も一般的な5つのUI要素
   The 5 most common UI elements
   -----------------------------

   Godot ships with dozens of Control nodes. A lot of them are here to help
   you build editor plugins and applications.

   For most games, you'll only need five types of UI elements, and a few
   Containers. These five Control nodes are:

   1. Label: for displaying text
   2. TextureRect: used mostly for backgrounds, or everything that should
      be a static image
   3. TextureProgress: for lifebars, loading bars, horizontal, vertical or
      radial
   4. NinePatchRect: for scalable panels
   5. TextureButton: to create buttons

   .. figure:: img/five_most_common_nodes.png

      The 5 most common Control nodes for UI design







































TextureRect
~~~~~~~~~~~

**TextureRect** は、UI内にテクスチャまたは画像を表示する。
Spriteノードに似ているが、複数のスケーリングモードの提供できる箇所が異なる。

- ``Scale On Expand (compat)`` は、 ``expand`` プロパティが ``true`` である場合にのみ、ノードの境界矩形に合うようにテクスチャをスケーリングする。
  それ以外の場合は、 ``Keep`` モードのように動作する。
  後方互換性のために、通常は有効化されている。
- ``Scale`` は、ノードの境界矩形に合うように、テクスチャをスケーリングする。
- ``Tile`` は、テクスチャを繰り返すが、スケーリングはしない。
- ``Keep`` および ``Keep Centered`` は、それぞれ左上隅またはフレームの中央で、テクスチャの大きさを維持するように強制する。
- ``Keep Aspect`` および ``Keep Aspect Centered`` は、テクスチャをスケーリングするが、それぞれ元のアスペクト比を維持する。
- ``Keep Aspect Covered`` は、 ``Keep Aspect Centered`` と同じように機能するが、短辺はは境界矩形に収まり、他の1つはノードの制限に合わせてクリップする。

（訳者：何の話をしているの全く分からない。専門用語が多い割に、用語集も無いため、分からないままになっている）

Spriteノードと同様に、TextureRectの色を調整できる。
``Modulate`` プロパティをクリックして、カラーピッカーを使用する。

.. figure:: img/five_common_nodes_textureframe.png

   赤色で変調されたTextureRect




.. 英語の原文：TextureRect
   TextureRect
   ~~~~~~~~~~~

   **TextureRect** displays a texture or image inside a UI.
   It seems similar to the Sprite node, but it offers multiple scaling modes.
   Set the Stretch Mode property to change its behavior:

   - ``Scale On Expand (compat)`` scales the texture to fit the node's bounding rectangle,
     only if ``expand`` property is ``true``; otherwise, it behaves like ``Keep`` mode.
     Default mode for backwards compatibility.
   - ``Scale`` scales the texture to fit the node's bounding rectangle.
   - ``Tile`` makes the texture repeat, but it won't scale.
   -  ``Keep`` and ``Keep Centered`` force the texture to remain at its
      original size, in the top left corner or the center of the frame
      respectively.
   - ``Keep Aspect`` and ``Keep Aspect Centered`` scales the texture but force it to remain
     its original aspect ratio, in the top left corner or the center of the frame respectively.
   - ``Keep Aspect Covered`` works just like ``Keep Aspect Centered`` but the shorter side
     fits the bounding rectangle and the other one clips to the node's limits.

   As with Sprite nodes, you can modulate the TextureRect's color. Click
   the ``Modulate`` property and use the color picker.

   .. figure:: img/five_common_nodes_textureframe.png

      TextureRect modulated with a red color







































TextureButton
~~~~~~~~~~~~~~~~~~~~~~~~~~

**TextureButton** は、TextureRectに似ているが、5つのテクスチャスロットが付いているところが異なる点だ(ボタンの状態ごとに1つ)。
ほとんどの場合、Normal・Pressed・Hoverの各テクスチャを使用する。
Focusedは、インタフェイスがキーボードの入力を検知する場合に役立つ。
6番目のクリックマスクでは、2ビットの純粋な白黒画像を使用して、クリック可能な領域を定義できる。

ベースボタンセクションには、ボタンの動作を変更するいくつかのチェックボックスがある。
``Toggle Mode`` がオンの時は、ボタンの押下有無で切り替わる(トグルそのものの機能)。
``Disabled`` がオンの時は、通常オフになったボタンがUIに備わる( ``Disabled`` テクスチャが使われる)。
TextureButtonは、テクスチャフレームといくつかのプロパティを共有する。
色の変更用に、 ``modulate`` プロパティがあり、スケール動作の変更用に、 ``Resize`` および ``Stretch`` モードがある。

.. figure:: img/five_common_nodes_texturebutton.png

   TextureButtonとその5つのテクスチャスロット


.. 英語の原文：TextureButton
   TextureButton
   ~~~~~~~~~~~~~

   **TextureButton** is like TextureRect, except it has 5 texture slots:
   one for each of the button's states. Most of the time, you'll use the
   Normal, Pressed, and Hover textures. Focused is useful if your interface
   listens to the keyboard's input. The sixth image slot, the Click Mask,
   lets you define the clickable area using a 2-bit, pure black and white
   image.

   In the Base Button section, you'll find a few checkboxes that change how
   the button behaves. When ``Toggle Mode`` is on, the button will toggle
   between active and normal states when you press it. ``Disabled`` makes it
   disabled by default, in which case it will use the ``Disabled`` texture.
   TextureButton shares a few properties with the texture frame: it has a
   ``modulate`` property, to change its color, and ``Resize`` and ``Stretch`` modes to
   change its scale behavior.

   .. figure:: img/five_common_nodes_texturebutton.png

      TextureButton and its 5 texture slots







































TextureProgress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TextureProgress** は、プログレスバーを作成するために、最大3つのスプライトをレイヤー化する。
アンダーとオーバーのテクスチャはプレグレスを挟み、バーの値を表示する。

``Mode`` プロパティは、バーが進む方向を制御する。
水平・垂直・放射状。
放射状に設定した場合、 ``Initial Angle`` および ``Fill Degrees`` プロパティを使用して、ゲージの範囲を制御する。

バーをアニメーション化するには、範囲セクションを確認する。
``Min`` および ``Max`` プロパティを設定し、ゲージの範囲を定義する。
例えば、プレイヤーの寿命を表すには、 ``Min`` を ``0`` そして ``Max`` に最大寿命を設定する。
``Value`` プロパティを変更して、バーを更新する。
``Min`` と ``Max`` の値を初期値の ``0`` と ``100`` のままにして、 ``Value`` プロパティを ``40`` に設定した場合は、 ``Progress`` のテクスチャが40%表示になり、残りの60%は非表示になる。

.. figure:: img/five_common_nodes_textureprogress.png

   TextureProgressバーを3分の2塗りつぶした状態





.. 英語の原文：TextureProgress
   TextureProgress
   ~~~~~~~~~~~~~~~

   **TextureProgress** layers up to 3 sprites to create a progress bar. The
   Under and Over textures sandwich the Progress one, which displays the
   bar's value.

   The ``Mode`` property controls the direction in which the bar grows:
   horizontally, vertically, or radially. If you set it to radial, the
   ``Initial Angle`` and ``Fill Degrees`` properties let you limit the range of the
   gauge.

   To animate the bar, you'll want to look at the Range section. Set the
   ``Min`` and ``Max`` properties to define the range of the gauge. For instance,
   to represent a character's life, you'll want to set ``Min`` to ``0,`` and ``Max`` to
   the character's maximum life. Change the ``Value`` property to update the
   bar. If you leave the ``Min`` and ``Max`` values to the default of ``0`` and ``100,``
   and set the ``Value`` property to ``40``, 40% of the ``Progress`` texture will show
   up, and 60% of it will stay hidden.

   .. figure:: img/five_common_nodes_textureprogress.png

      TextureProgress bar, two thirds filled








































Label
~~~~~~~~~~

**Label** は、画面にテキストを表示する。
すべてのプロパティは、インスペクタドックのLabelセクションにある。
``Text`` プロパティにテキストを書き込み、テキストボックスの大きさを尊重したい場合は、Autowrapにチェックを入れる。
自動折り返しがオフの場合、ノードを拡大縮小することはできない。
Align および Valign を使用して、テキストをそれぞれ水平及び垂直に整列できる。

.. figure:: img/five_common_nodes_label.png

   ラベル画像


.. 英語の原文：Label
   Label
   ~~~~~

   **Label** prints text to the screen. You'll find all its properties in
   the Label section, in the Inspector. Write the text in the ``Text``
   property, and check Autowrap if you want it to respect the textbox's
   size. If Autowrap is off, you won't be able to scale the node. You can
   align the text horizontally and vertically with Align and Valign,
   respectively.

   .. figure:: img/five_common_nodes_label.png

      Picture of a Label








































NinePatchRect
~~~~~~~~~~~~~~~~~~~~~~~~~~

**NinePatchRect** は、3行3列に分割されたテクスチャを用意している。
テクスチャを拡大縮小したとき、中央と側面がタイル状になるが、角は拡大縮小されない。
UIのパネル・ダイアログボックス・スケーラブルな背景を作成するときに便利だ。

.. figure:: img/five_common_nodes_ninepatchrect.png

   min_sizeプロパティを基準に描画したNinePatchRect


.. 英語の原文：NinePatchRect
   NinePatchRect
   ~~~~~~~~~~~~~

   **NinePatchRect** takes a texture split in 3 rows and 3 columns. The
   center and the sides tile when you scale the texture, but it never
   scales the corners. It is useful to build panels, dialog boxes
   and scalable backgrounds for your UI.

   .. figure:: img/five_common_nodes_ninepatchrect.png

      NinePatchRect scaled with the min\_size property




































レスポンシブUIを構築するには、2つの手順が必要
------------------------------------------------------------------------------------------

Godotでスケーラブルで柔軟なインタフェイスを構築するには、2つのワークフローがある。

#. UI要素を拡大縮小して配置できるコンテナノードを自由に使用する。
   それらは、子を管理する。
#. 反対側には、レイアウトメニューがある。
   親内でUI要素をアンカー・配置・サイズ変更するのに役立つ。

2つのアプローチは互換性を維持しない。
コンテナは子を制御するため、子でレイアウトメニューを使用できない。
各コンテナには特定の効果があるため、機能するインタフェイスを取得するには、いくつかのコンテナをネストする必要がある。
レイアウトアプローチを使用した場合、子プロセスでボトムアップ作業が必要になる。
シーンに余分なコンテナを挿入しないため、階層をきれいに保てるが、行・列・グリッドなどにアイテムを配置するのは困難になる。

ゲームやツールのUIを作成するとき、それぞれの状況に最適な感覚を養うだろう。






.. 英語の原文：レスポンシブUIを構築するには、2つの手順が必要
   There are two workflows to build responsive UIs
   -----------------------------------------------

   There are two workflows to build scalable and flexible interfaces in Godot:

   1. You have many container nodes at your disposal that scale and place UI elements for you. They take control over their children.
   2. On the other side, you have the layout menu. It helps you to anchor, place and resize a UI element within its parent.

   The two approaches are not always compatible. Because a container controls its children, you cannot use the layout menu on them. Each container has a specific effect, so you may need to nest several of them to get a working interface. With the layout approach you work from the bottom up, on the children. As you don't insert extra containers in the scene it can make for cleaner hierarchies, but it's harder to arrange items in a row, column, grid, etc.

   As you create UIs for your games and tools, you'll develop a sense for what fits best in each situation.





































アンカーを使用してUI要素を正確に配置する
--------------------------------------------------------------------------------

コントロールノードには位置と大きさがあり、アンカーとマージンもある。
アンカーは、ノードの左・上・右・下の角の原点または基準点を定義する。
4つのアンカーのいずれかを変更して、マージンの基準点を変更する。

.. figure:: img/anchor_property.png

   アンカープロパティ


.. 英語の原文：アンカーを使用してUI要素を正確に配置する
   Place UI elements precisely with anchors
   ----------------------------------------

   Control nodes have a position and size, but they also have anchors and
   margins. Anchors define the origin, or the reference point, for the
   Left, Top, Right and Bottom edges of the node. Change any of the 4
   anchors to change the reference point of the margins.

   .. figure:: img/anchor_property.png

      The anchor property





































アンカーの変更方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

他のプロパティと同様に、インスペクタドックで4つのアンカーポイントを編集できるが、これは最適解ではない。
コントロールノードを選択したとき、ツールバーのビューポートの上にレイアウトメニューが表示される。
インスペクタの4つのプロパティを使用する代わりに、1回のクリックで4つのアンカーすべてを設定するアイコンのリストが表示される。
レイアウトメニューは、コントロールノードを選択したときのみに表示される。

.. figure:: img/layout_menu.png

   ビューポートのレイアウトメニュー

訳者：レイアウトとアンカーのみの違いが分からない。




.. 英語の原文：アンカーの変更方法
   How to change the anchor
   ~~~~~~~~~~~~~~~~~~~~~~~~

   Like any properties, you can edit the 4 anchor points in the Inspector,
   but this is not the most convenient way. When you select a control node,
   the layout menu appears above the viewport, in the toolbar. It gives you
   a list of icons to set all 4 anchors with a single click, instead of
   using the inspector's 4 properties. The layout menu will only show up
   when you select a control node.

   .. figure:: img/layout_menu.png

      The layout menu in the viewport



































アンカーは親コンテナに関連している
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

各アンカーは0〜1の値を保持する。
左と上のアンカーの場合、値0は、マージンなしで、ノードの角(エッジ)がその親の左と上端に揃えられることを意味する。
右端と下端の値が1の場合、親コンテナの右端と下端に揃えられる。
一方、マージンはアンカー位置までの距離をピクセル単位で表し、アンカーは親コンテナの大きさに相対的になっている。

.. figure:: ./img/ui_anchor_and_margins.png

   マージンは、アンカーに相対的なアンカー位置に相対的になっている。
   実際には、コンテナにマージンを更新させることがよくある。



.. 英語の原文：アンカーは親コンテナに関連している
   Anchors are relative to the parent container
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Each anchor is a value between 0 and 1. For the left and top anchors, a
   value of 0 means that without any margin, the node's edges will align
   with the left and top edges of its parent. For the right and bottom
   edges, a value of 1 means they'll align with the parent container's
   right and bottom edges. On the other hand, margins represent a distance
   to the anchor position in pixels, while anchors are relative to the
   parent container's size.

   .. figure:: ./img/ui_anchor_and_margins.png

      Margins are relative to the anchor position, which is relative to the
      anchors. In practice, you'll often let the container update margins
      for you





































アンカーによってマージンが変わる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コントロールノードを移動またはサイズ変更したとき、マージンは自動的に更新される。
これらは、コントロールノードのエッジからアンカーまでの距離を表す。
アンカーは、親コントロールノードまたはコンテナに相対的だ。
すぐに分かるように、コントロールノードは常にコンテナ内に必要だ。
親がいない場合、マージンは、インスペクタのRectセクションで設定されたノード自身の境界Rectangleに相対的になる。

.. figure:: img/control_node_margin.png

   "Full Rect" アンカーに設定したCenterContainerのマージン

アンカーを変更するか、コンテ七位にコントロールノードをネストして試すこと。
マージンが更新されることがわかる。
マージンを手動で編集する必要はほぼ無い。
最初に役立つコンテナを常に探すこと。
Godotには、すべての一般的な課題を解決するノードが付属している。

ライフゲージと画面の境界としてスペースを追加する必要があるか？
そのときは、MarginContainerを使うべし。

垂直メニューを作りたいか？
そのときは、VBoxContainerを使うべし。

詳細は、以下を確認すること。


.. 英語の原文：アンカーによってマージンが変わる
   Margins change with the anchor
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Margins update automatically when you move or resize a control node.
   They represent the distance from the control node's edges to its anchor,
   which is relative to the parent control node or container. That's why
   your control nodes should always be inside a container, as we'll see in
   a moment. If there's no parent, the margins will be relative to the
   node's own bounding Rectangle, set in the Rect section, in the
   inspector.

   .. figure:: img/control_node_margin.png

      Margins on a CenterContainer set to the "Full Rect" anchor

   Try to change the anchors or nest your Control nodes inside Containers:
   the margins will update. You'll rarely need to edit the margins
   manually. Always try to find a container to help you first; Godot comes
   with nodes to solve all the common cases for you. Need to add space
   between a lifebar and the border of the screen? Use the MarginContainer.
   Want to build a vertical menu? Use the VBoxContainer. More on these
   below.


































サイズタグを使用して、UI要素が使用可能なスペースを埋める方法を変更する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

すべての制御ノードにはサイズフラグがある(訳者：フラグ？)。
UIエレメントのスケーリング方法をコンテナに指示する。
"Fill" フラグをHorizontalプロパティまたはVerticalプロパティに追加した場合、ノードの境界ボックスは可能な限りすべてのスペースを使用するが、兄弟を尊重し、サイズを保持する。
HBoxContainerに3つのTextureRectノードがあり、両方の軸に "Fill" フラグがある場合、それらはそれぞれ使用可能なスペースの最大3分の1を占有するが、それ以上は占有しない。
コンテナがノードを引き継ぎ、自動的にサイズ変更する。

.. figure:: img/textureframe_in_box_container_fill.png

   HBoxContainerの3つのUI要素を水平方向に整列

"Expand" フラグを使用した場合、UI要素は可能な限りすべてのスペースを使用して、その兄弟に対してプッシュできる。
その境界長方形は、その親の端に対して、または別のUIノードによってブロックされるまで拡大する。

.. figure:: img/textureframe_in_box_container_expand.png

   上記と同じ例だが、中央ノードには "Expand" サイズフラグがある。

サイズタグを理解するには、インタフェースの設定方法によって効果が大きく変わる可能性があるため、ある程度の練習が必要だ。


.. 英語の原文：サイズタグを使用して、UI要素が使用可能なスペースを埋める方法を変更する
   Use size tags to change how UI elements fill the available space
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Every control node has Size Flags. They tell containers how the UI
   elements should scale. If you add the "Fill" flag to the Horizontal or
   Vertical property, the node's bounding box will take all the space it
   can, but it'll respect its siblings and retain its size. If there are 3
   TextureRect nodes in an HBoxContainer, with the "Fill" flags on both
   axes, they'll each take up to a third of the available space, but no
   more. The container will take over the node and resize it automatically.

   .. figure:: img/textureframe_in_box_container_fill.png

      3 UI elements in an HBoxContainer, they align horizontally

   The "Expand" flag lets the UI element take all the space it can, and
   push against its siblings. Its bounding rectangle will grow against the
   edges of its parent, or until it's blocked by another UI node.

   .. figure:: img/textureframe_in_box_container_expand.png

      The same example as above, but the center node has the "Expand" size
      flag

   You'll need some practice to understand the size tags, as their effect
   can change quite a bit depending on how you set up your interface.


































コンテナを使用してコントロールノードを自動的に配置
----------------------------------------------------------------------------------------------------

コンテナは、他のコンテナを含むすべての子コントロールノードを行・列などに自動配置する。
これらの特性を利用し、インタフェイスの周囲にパディングを追加するか、境界矩形の中央ノードに追加する。
すべての組み込みコンテナはエディタで更新されるため、エフェクトの確認がすぐにできる。

コンテナには、UI要素の配置方法を制御する特別なプロパティを含んでいる。
それらを変更するには、インスペクタのカスタム定数セクションを確認する。


.. 英語の原文：コンテナを使用してコントロールノードを自動的に配置
   Arrange control nodes automatically with containers
   ---------------------------------------------------

   Containers automatically arrange all children Control nodes including
   other containers in rows, columns, and more. Use them to add padding
   around your interface or center nodes in their bounding rectangles. All
   built-in containers update in the editor, so you can see the effect
   instantly.

   Containers have a few special properties to control how they arrange UI
   elements. To change them, navigate down to the Custom Constants section
   in the Inspector.




































最も便利な5つのコンテナ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ツールを構成する場合、すべてのコンテナが必要な場合がある。
しかし、ほとんどのゲームでは、一握りで十分なはず。

- MarginContainer：UIの一部の周囲にマージンを追加する。
- CenterContainer：境界ボックス内の子を中央に配置
- VboxContainer および HboxContainer：行または列にUI要素を配置する。
- GridContainer：グリッドのようなパターンでコントロールノードを配置する。

CenterContainerは、すべての子を境界矩形内に中央揃えする。
オプションをビューポートの中央に留める技法はタイトル画面に使用するときだろう。
すべてを中央に配置するため、多くの場合、単一のコンテナをその中にネストする必要がある。
代わりにテクスチャとボタンを使用することで、それらが積み重ねられる。

（訳者：どういう意味？）

.. figure:: img/five_containers_centercontainer.png

   動作中のCenterContainer。ライフゲージは、その親コンテナの中心にある。

MarginContainerは、子ノードの任意の側にマージンを追加する。
ビューポート全体を包含するMarginContainerを追加し、ウィンドウのエッジとUIの間に分離部分を追加する。
コンテナの上部・左側・右側・下部にマージンを設定できる。
チェックボックスをオンにする必要は無い。
対応する値ボックスをクリックし、任意の数値を入力する。
自動的にアクティブになる。

.. figure:: img/five_containers_margincontainer.png

   MarginContainerは、ゲームユーザインタフェイスの周囲に40pxのマージンを追加する。

2つのBoxContainersがある(VBoxContainer と HBoxContainer)。
BoxContainerノード自体はヘルパークラスになるため追加できない。
垂直及び水平のボックスコンテナを使用する。
ノードを行また列に配置する。
これらを使用し、店に商品を並べることができる。
様々な大きさの行と列を使用して、複雑なグリッドを構築できる。

（訳者：何が追加できない？）

.. figure:: img/five_containers_boxcontainer.png

   HBoxContainerは、UI要素を水平に整列する。

VBoxContainerは、子を自動的に列に配置する。
それらを次々に配置する。
分離パラメータを使用したとき、その子間にギャップが残る。
HBoxContainerは、UI要素を行に配置する。
VBoxContainerに似ているが、追加の ``add_spacer`` メソッドを使用し、スクリプトから最初の子の前または最後の子の後ろにスペーサーコントロールノードを追加する。

GridContainerを使用した場合、UI要素をグリッドのようなパターンに配置できる。
制御できるのは列の数のみになり、子の数に基づいて行数を単独で設定する。
9つの子と3つの列がある場合、9÷3=3行になる。
さらに3つの子を追加したとき、4行になる。
つまり、テクスチャとボタンを追加したときに、新しい行が作成される。
ボックスコンテナと同様に、行と列の垂直方向と水平方向の間隔をそれぞれ設定する2つのプロパティがある。

.. figure:: img/five_containers_gridcontainer.png

   2列のGridContainer。各列の大きさが自動調整される。

GodotのUIシステムは複雑であり、さらに多くの機能がある。
より高度なインタフェイスを設計する方法を学ぶには、 :ref:`GUI section <toc-learn-features-gui>` ドキュメントを参照すること。

.. todo::

   リンクの確認。


.. 英語の原文：最も便利な5つのコンテナ
   The 5 most useful containers
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   If you build tools, you might need all of the containers. But for most
   games, a handful will be enough:

   -  MarginContainer, to add margins around part of the UI
   -  CenterContainer, to center its children in its bounding box
   -  VboxContainer and HboxContainer, to arrange UI elements in rows or
      columns
   -  GridContainer, to arrange Controls nodes in a grid-like pattern

   CenterContainer centers all its children inside of its bounding
   rectangle. It's one you typically use for title screens, if you want the
   options to stay in the center of the viewport. As it centers everything,
   you'll often want a single container nested inside it. If you use
   textures and buttons instead, they'll stack up.

   .. figure:: img/five_containers_centercontainer.png

      CenterContainer in action. The life bar centers inside its parent
      container.

   The MarginContainer adds a margin on any side of the child nodes. Add a
   MarginContainer that encompasses the entire viewport to add a separation
   between the edge of the window and the UI. You can set a margin on the
   top, left, right, or bottom side of the container. No need to tick the
   checkbox: click the corresponding value box and type any number. It will
   activate automatically.

   .. figure:: img/five_containers_margincontainer.png

      The MarginContainer adds a 40px margin around the Game User Interface

   There are two BoxContainers: VBoxContainer and HBoxContainer. You cannot
   add the BoxContainer node itself, as it is a helper class, but you can
   use vertical and horizontal box containers. They arrange nodes either in
   rows or columns. Use them to line up items in a shop, or to build
   complex grids with rows and columns of different sizes, as you can nest
   them to your heart's content.

   .. figure:: img/five_containers_boxcontainer.png

      The HBoxContainer horizontally aligns UI elements

   VBoxContainer automatically arranges its children into a column. It puts
   them one after the other. If you use the separation parameter, it will
   leave a gap between its children. HBoxContainer arranges UI elements in
   a row. It's similar to the VBoxContainer, with an extra ``add_spacer``
   method to add a spacer control node before its first child or after its
   last child, from a script.

   The GridContainer lets you arrange UI elements in a grid-like pattern.
   You can only control the number of columns it has, and it will set the
   number of rows by itself, based on its children's count. If you have
   nine children and three columns, you will have 9歎3 = 3 rows. Add three
   more children and you'll have four rows. In other words, it will create
   new rows as you add more textures and buttons. Like the box containers,
   it has two properties to set the vertical and horizontal separation
   between the rows and columns respectively.

   .. figure:: img/five_containers_gridcontainer.png

      A GridContainer with 2 columns. It sizes each column automatically.

   Godot's UI system is complex, and has a lot more to offer. To learn how
   to design more advanced interfaces, head to the :ref:`GUI section <toc-learn-features-gui>` of the docs.




.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
