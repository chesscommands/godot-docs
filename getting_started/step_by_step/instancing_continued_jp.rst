.. _doc_instancing_continued_jp:


インスタンス化(続き)
========================================

.. 英語の原文：インスタンス化(続き)
   Instancing (continued)
   ======================





































要約
------------

インスタンス化には多くの便利な用途がある。
インスタンス化の利点は、以下の点が上げられる。

- シーンを分割し、管理しやすくする機能。
- 複数のノードインスタンスを一度に管理及び編集する機能。
- 複雑なゲームフローやUIを整理して埋め込む機能(Godotでは、UI要素もノードになる)。

.. 英語の原文：要約
   Recap
   -----

   Instancing has many handy uses. At a glance, with instancing you have:

   -  The ability to subdivide scenes and make them easier to manage.
   -  A tool to manage and edit multiple node instances at once.
   -  A way to organize and embed complex game flows or even UIs (in Godot, UI
      Elements are nodes, too).

































設計言語
----------------

上記の利点だけでなく、インスタンス化シーンに伴う最大の強みは、優れたデザイン言語として機能すること。
これにより、Godotは他のすべてのエンジンとは別格扱いされることになる。
Godotは、このコンセプトに基づいてゼロから設計された。

Godotを使用してゲームを作成する場合、MVCやエンティティ関係図などの最も一般的なデザインパターンを却下し、代わりにシーンをより自然な方法で考えることを勧める。
例えば、目に見えるゲーム要素を想像することから始める。
プログラマに限らず、それらの要素には、誰でも名前付けができる。

例えば、簡単なシューティングゲームを想像する方法は次の通り。

.. todo::

   以下の画像を日本語化したい。

.. image:: img/shooter_instancing.png

あらゆる種類のゲームで、このような図を作成できる。
視覚化できるゲームの部分を書き留めた後に、矢印を追加し、あるコンポーネントが次のコンポーネントの所有権を表すようにする。

Godotoを使ってゲームを作成するための推奨過程は、上図に列挙している各要素のシーンを作成することだ。
そして、所有関係には、インスタンス化を(コードもしくはエディタで直接)指定する。

ゲーム(またはソフトウェア全般)のプログラミングに費やす時間の多くは、アーキテクチャへのゲームコンポーネントのかみ合わせに費やされる。
シーンに基づいた設計は、そのアプローチに代わるものであり、開発をより迅速かつ簡単に行えるため、ゲーム処理の内容や手順そのものに集中できる。
ほとんどのゲームコンポーネントはシーンに直接マッピングされるため、シーンのインスタンス化に基づくデザインを使用する場合、他のアーキテクチャコードはほぼ必要なくなる。

もう1つの例は、やや複雑な多くのアセットと深い階層にある要素を持つオープンワールドタイプのゲーム例を確認する。

.. todo::

   以下の画像を日本語化したい。

.. image:: img/openworld_instancing.png

部屋の要素から説明を始める。
家具(シーン)の配置を変えて、いくつかの異なる部屋のシーンを変えて、そしてそれらを別々に作成できる。
その後、それらの部屋をつないで内装を構成する家シーンを作ることができる。

.. todo::

   以下の原著は全く理解できない。以下の解釈で合っているのだろうか。

次に、多くのインスタンス化された家々をつなぎ合わせた町のシーンを作成する。
その後、世界各地の地形を作成し、町を追加する。

後で、衛兵(及び他のNPC)のシーンを作成し、それらを町に追加することもできる。
結果として、それらはゲーム世界全体に間接的に追加される。

Godotでは、このようにゲームを簡単に複製できる。
必要なのは、より多くのシーンを作成してインスタンス化するだけだ。
さらに、エディタUIは、プログラマと非プログラマの両方にとって使いやすいように設計されている。
典型的なチーム開発プロセスには、2Dまたは3Dアーティスト・レベルデザイナー・ゲームデザイナー・およびアニメーターが含まれ、すべてエディタインタフェイスを使用する。



.. 英語の原文：設計言語
   Design language
   ---------------

   But the greatest strength that comes with instancing scenes is that it works
   as an excellent design language. This distinguishes Godot
   from all the other engines out there. Godot was designed from the ground up
   around this concept.

   When making games with Godot, the recommended approach is to dismiss most
   common design patterns, such as MVC or Entity-Relationship diagrams, and
   instead think about your scenes in a more natural way. Start by imagining the
   visible elements in your game, the ones that can be named not just by a
   programmer, but by anyone.

   For example, here's how a simple shooter game could be imagined:

   .. image:: img/shooter_instancing.png

   You can come up with a diagram like this for almost any kind
   of game. Write down the parts of the game that you can visualize, and then
   add arrows to represent ownership of one component by another.

   Once you have a diagram like this, the recommended process for making a game is
   to create a scene for each element listed in the diagram. You'll use instancing
   (either by code or directly in the editor) for the ownership relationships.

   A lot of time spent in programming games (or software in general) is on
   designing an architecture and fitting game components to that architecture.
   Designing based on scenes replaces that approach and makes development much
   faster and more straightforward, allowing you to concentrate on the game logic
   itself. Because most game components map directly to a scene, using a design based on scene instantiation means little other architectural code is needed.

   Let's take a look at one more, somewhat more complex, example of an open-world
   type game with lots of assets and nested elements:

   .. image:: img/openworld_instancing.png

   Take a look at the room element. Let's say we started there. We could make a
   couple of different room scenes, with different arrangements of furniture (also
   scenes) in them. Later, we could make a house scene, connecting rooms to make
   up its interior.

   Then, we could make a citadel scene, which is made out of many instanced
   houses. Then, we could start working on the world map terrain, adding the
   citadel onto it.

   Later, we could create scenes that represent guards (and other NPCs) and add
   them to the citadel as well. As a result, they would be indirectly added to the
   overall game world.

   With Godot, it's easy to iterate on your game like this, as all you need to do
   is create and instance more scenes. Furthermore, the editor UI is designed to be user
   friendly for programmers and non-programmers alike. A typical team development
   process can involve 2D or 3D artists, level designers, game designers,
   and animators, all working with the editor interface.





































情報過多
----------------

今回は、高い水準の情報を一度に多く説明した。
ただし、このチュートリアルの重要な部分は、一部であり、それが "実際のプロジェクトでシーンとインスタンスがどのように使用されているかを認識すること" だった。

ゲームを作成し、これらの概念を実践し始めることで、ここで説明するすべてがあなたにとって第二の人生になる。
高い水準の情報量が多かったかもしれないが、あまり心配する必要はない。
安心して次のチュートリアルに進むように。



.. 英語の原文：情報過多
   Information overload!
   ---------------------

   This has been a lot of high level information dropped on you all at once.
   However, the important part of this tutorial was to create an awareness of how
   scenes and instancing are used in real projects.

   Everything discussed here will become second nature to you once you start
   making games and putting these concepts into practice. For now, don't worry
   about it too much, and go on to the next tutorial!




.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
