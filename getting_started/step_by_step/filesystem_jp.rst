.. _doc_filesystem_jp:
































ファイルシステム
================================

.. 英語の原文：ファイルシステム
   File system
   ===========

































概論
------------

ファイルシステムは、アセットの保存方法とアクセス方法を管理する。
また、適切に設計されたファイルシステムにより、複数の開発者が共同作業中に同じソースファイルとアセットを編集できる。
Godotは、すべてのアセットをファイルシステムのファイルとして保存する。


.. 英語の原文：概論
   Introduction
   ------------

   A file system manages how assets are stored and how they are accessed.
   A well-designed file system also allows multiple developers to edit the
   same source files and assets while collaborating. Godot stores
   all assets as files in its file system.



































実装
------------

ファイルシステムは、リソースをディスクに保存する。
スクリプトからシーン・PNG画像まで、すべてがエンジンのリソース扱いをする。
リソースにディスク上の他のリソースを参照するプロパティが含まれる場合、それらのリソースへのPathも含まれる。
リソースに組み込みのサブリソースがある場合、リソースはすべてのバンドルされたサブリソースとともに単一のファイルに保存される。
例えば、多くの場合、フォントリソースはフォントテクスチャと一緒にバンドルされる。

Godotファイルシステムは、メタデータファイルの使用を回避する。
既存のアセットマネージャとVCSは実装可能な物より優れているため、GodotはSVN・Git・Mercurial・Perforceなどと一緒に連携するよう最善を尽くしている。

ファイルシステムの内容例：

::

   /project.godot
   /enemy/enemy.tscn
   /enemy/enemy.gd
   /enemy/enemysprite.png
   /player/player.gd

.. todo::

   何の話をしているのか分からない。VCSとは？


.. 英語の原文：実装
   Implementation
   --------------

   The file system stores resources on disk. Anything, from a script, to a scene or a
   PNG image is a resource to the engine. If a resource contains properties
   that reference other resources on disk, the paths to those resources are also
   included. If a resource has sub-resources that are built-in, the resource is
   saved in a single file together with all the bundled sub-resources. For
   example, a font resource is often bundled together with the font textures.

   The Godot file system avoids using metadata files. Existing asset managers and VCSs are better than
   anything we can implement, so Godot tries its best to play along with SVN,
   Git, Mercurial, Perforce, etc.

   Example of file system contents:

   ::

      /project.godot
      /enemy/enemy.tscn
      /enemy/enemy.gd
      /enemy/enemysprite.png
      /player/player.gd

































project.godot
--------------------------

project.godotファイルはプロジェクト記述ファイルであり、常にプロジェクトのルートに鎮座する。
実際、その場所はルートの場所を定義する。
これは、プロジェクトを開くときにGodotが検索する最初のファイルになる。

このファイルには、win.ini形式を使用したプロジェクト構成がプレーンテキストから成り立っている。
空のproject.godotでさえ、空のプロジェクトの基本的な定義として機能する。


.. 英語の原文：project.godot
   project.godot
   -------------

   The project.godot file is the project description file, and it is always found at
   the root of the project. In fact, its location defines where the root is. This
   is the first file that Godot looks for when opening a project.

   This file contains the project configuration in plain text, using the win.ini
   format. Even an empty project.godot can function as a basic definition of a blank
   project.

































Pathの区切り文字
--------------------------------

Godotは、Path区切り文字として ``/`` のみに対応している。
これは、移植性が理由になっている。
すべてのオペレーティングシステム(OS)がこれに対応している(Windows含む)ためだ。
故に、 ``c:\project\project.godot`` などのPathを ``c:/project/project.godot`` に置き換える手間が発生する。


.. 英語の原文：Pathの区切り文字
   Path delimiter
   --------------

   Godot only supports ``/`` as a path delimiter. This is done for
   portability reasons. All operating systems support this, even Windows,
   so a path such as ``c:\project\project.godot`` needs to be typed as
   ``c:/project/project.godot``.

































リソースPath
------------------------

リソースにアクセスする場合、ホストOSファイルシステムレイアウトを使用するのは面倒で移植性がない。
この問題を解決するために、特別な ``res://`` Pathを利用することに決まった。

Path ``res://`` は常にプロジェクトルートを指す。
（project.godotが配置されているため、 ``res://project.godot`` は常に有効になっている）

このファイルシステムは、プロジェクトをエディタからローカルで実行する場合にのみ読み取り/書き込みが可能になっている。
エクスポートする場合、または異なるデバイス(スマートフォン・コンソール・DVD)から実行する場合、ファイルシステムは読み取り専用になり、書き込みは許可されない。

.. 英語の原文：リソースPath
   Resource path
   -------------

   When accessing resources, using the host OS file system layout can be
   cumbersome and non-portable. To solve this problem, the special path
   ``res://`` was created.

   The path ``res://`` will always point at the project root (where
   project.godot is located, so ``res://project.godot`` is always
   valid).

   This file system is read-write only when running the project locally from
   the editor. When exported or when running on different devices (such as
   phones or consoles, or running from DVD), the file system will become
   read-only and writing will no longer be permitted.


































ユーザPath
--------------------

ゲーム状態の保存やコンテンツパックのダウンロードなどの作業には、ディスクへの書き込みが引き続き必要になる。
この目的のために、エンジンは常に書き込み可能な、特別な ``user://`` Pathがある。



.. 英語の原文：ユーザPath
   User path
   ---------

   Writing to disk is still needed for tasks such as saving game
   state or downloading content packs. To this end, the engine ensures that there is a
   special path ``user://`` that is always writable.


































ホストファイルシステム
--------------------------------------------

上記とは別に、ホストファイルシステムPathも使用できるが、リリースされた製品ではこれらのPathがすべてのプラットフォームで動作することが保証できないため、推奨されない。
ただし、ホストファイルシステムPathを使用した場合、Godotで開発ツールを作成するときに役立つことも確かだ。



.. 英語の原文：ホストファイルシステム
   Host file system
   ----------------

   Alternatively host file system paths can also be used, but this is not recommended
   for a released product as these paths are not guaranteed to work on all platforms.
   However, using host file system paths can be useful when writing development
   tools in Godot.


































欠点
------------

この単純なファイルシステム設計にはいくつかの欠点がある。
最初の問題は、アセットを移動する(プロジェクト内で名前を変更するか、あるPathから別のPathに移動する)場合、これらのアセットへの依存存関係が破損する。
これらの参照は、新しいアセットの場所を指し直すように再定義する必要がある。

これを避けるには、ファイルシステムドックからすべての移動・削除・名前変更操作を行うこと。
アセットをGodotの外部から変更しないようにすること。
そうしなければ、依存関係を手動で修正する必要が出てくる(Godotは修正を検出し、修正しようとするが、わざわざ無駄な手間をかける理由は何だろうか)

2つ目の欠点は、WindowsおよびMacOSでは、ファイル名とPath名は大文字と小文字が区別されないこと。
区別しないホストファイルシステムで作業する開発者がアセットを "myfile.PNG" として保存し、それを "myfile.png" として参照する場合、正常に機能するが、LinuxやAndroidなどの他のプラットフォームでは機能しない。
すべてのファイルを格納するために圧縮パッケージを使用するエクスポートされたバイナリにも適用される場合がある。

Godotを使用する場合、チームはファイルの命名規則を明確に定義することを勧める。
馬鹿な利用にも耐えうる簡単な規則の1つとして、小文字のファイル名とPath名のみを許可することにつきる。


.. 英語の原文：欠点
   Drawbacks
   ---------

   There are some drawbacks to this simple file system design. The first issue is that
   moving assets around (renaming them or moving them from one path to another inside
   the project) will break existing references to these assets. These references will
   have to be re-defined to point at the new asset location.

   To avoid this, do all your move, delete and rename operations from within Godot, on the FileSystem
   dock. Never move assets from outside Godot, or dependencies will have to be
   fixed manually (Godot detects this and helps you fix them anyway, but why
   go the hard route?).

   The second is that, under Windows and macOS, file and path names are case insensitive.
   If a developer working in a case insensitive host file system saves an asset as "myfile.PNG",
   but then references it as "myfile.png", it will work fine on their platform, but not
   on other platforms, such as Linux, Android, etc. This may also apply to exported binaries,
   which use a compressed package to store all files.

   It is recommended that your team clearly define a naming convention for files when
   working with Godot. One simple fool-proof convention is to only allow lowercase
   file and path names.

.. vim:set ts=3 sw=3 tw=0 fenc=utf-8:
