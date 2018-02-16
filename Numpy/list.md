#リストオブジェクト

リスト型は文字列と同じくシーケンス型の一つです。複数の要素から構成され、要素が順に並んでいるものになります。

    組み込み型
      + 数値型
      |  + 整数
      |  + 長整数
      |  + 浮動小数点
      |  + 複素数
      + シーケンス型
      |  + 文字列
      |  + ユニコード文字列
      |  + リスト
      |  + タプル
      + マップ型
      |  + 辞書(ディクショナリ)
      + ファイルオブジェクト
文字列は要素として文字を持つものでしたが、リストは要素としてあらゆるオブジェクトを持つことが出来ます。その為、他の複数のオブジェクトをまとめて管理することが出来るオブジェクトであると言えます。

リスト型のオブジェクトを作成するには次のように行います。

    [オブジェクト1, オブジェクト2, ...]
括弧[]で囲んだ中にオブジェクトをカンマ(,)で区切って記述します。

具体的には次のように記述します。

    [2005, 2006, 2007, 2008]
上記ではリストの要素は全て数値オブジェクトとなっています。

また作成されたリストオブジェクトもオブジェクトの一つですので、変数に代入することが出来ます。

    list = [2005, 2006, 2007, 2008]
リストの要素は異なるオブジェクトであっても構いません。下記では数値オブジェクトと文字列オブジェクトが混在するリストオブジェクトを作成しています。

    list = [u"山田", u"太郎", 1992, 12, 31, u"男性"]
他のリストオブジェクトを要素として持つことも可能です。

    list = [10, [20, 16], [32, 34], 18]
なお、変数がオブジェクトをコピーして格納しるわけではなく、オブジェクトへの参照を持っているだけだったのと同じように、リストの各要素もオブジェクトのコピーを持っているわけではなく各オブジェクトへの参照を持っているだけです。

#要素とインデックス

文字列やリストなどのシーケンス型は、要素が順序を持って並べられています。

    list = [2005, 2006, 2007, 2008]
このリストは「2005」「2006」「2007」「2008」と言うには4つの要素を持っています。そして要素は順序を持っていますので、「2005」の要素の次の要素は「2006」ですし、「2006」の要素の次は「2007」となります。

文字列の場合と同じく要素にはインデックスが割り当てられており、先頭の要素から「0」「1」「2」...と0から順に番号が割り当てられています。この番号を使うことで要素を指定することが出来ます。(なおインデックスには負の値を指定することも可能です。負の値の場合は「-1」なら一番最後の要素、「-2」なら最後から二番目の要素となります)。

リストオブジェクトの中でインデックスを指定して要素を取得するには次の書式を使います。

    リストオブジェクト[インデックス]
引数に指定したインデックスを持つ要素を取り出します。インデックスは0から始まることに注意して下さい。

具体的には次のように記述します。

    list = [2005, 2006, 2007, 2008]
    year = list[0]
上記では、インデックス「0」の要素を取得して変数に代入しています。インデックス「0」の要素とはリストの先頭の要素ですので変数「year」には「2005」が代入されます。

#スライスを使った部分リストの取得

リストでも文字列と同じくスライスを使うことが出来ます。スライスの基本的な使い方については「スライスを使った部分文字列の取得」を参照して下さい。

リストオブジェクトに対しスライスを使って部分リストを取得するには次の書式を使います。

    リストオブジェクト[開始インデックス:終了インデックス]
具体的には次のように記述します。

    list = ["A", "B", "C", "D", "E"]
    
    slice1 = list[1:2]     # ["B"]
    slice2 = list[1:-1]    # ["B", "C", "D"]
    slice3 = list[1:]      # ["B", "C", "D", "E"]
    slice4 = list[:2]      # ["A", "B"]
    slice5 = list[:]       # ["A", "B", "C", "D", "E"]
スライスを使って取得したオブジェクトもリストオブジェクトです。例えばスライスによって取得した要素の数が1つであっても、要素数が1つのリストオブジェクトとなりますので注意して下さい。要素が参照しているオブジェクトを取得したい場合は、インデックスを指定して要素を取得する必要があります。

#スライスを使った部分文字列の取得

文字列やリストなどのシーケンス型のオブジェクトではスライスという機能を使用できます。これはオブジェクトの中の指定した範囲の要素を持つ新しいオブジェクトを作成して返してくれるものです。

スライスではどこからどこまでの要素を抽出するのかを指定する必要がります。例として「ABCDE」と言う文字列を使ってスライスの説明を行います。

     0   1   2   3   4   5
     | A | B | C | D | E |
文字列が「ABCDE」だった場合、インデックス0は最初の文字「A」の前、インデックス1は最初の文字「A」と次の文字「B」の間となります。そして抽出する文字の先頭の文字の前のインデックスから最後の文字の次のインデックスで指定します。例えば「BC」を取得する場合には、「B」の前のインデックス1から「C」の次のインデックス3を指定します。指定方法は次の通りです。

    文字列オブジェクト[開始インデックス:終了インデックス]
開始インデックスと終了インデックスをコロン(:)でつなげて指定します。具体的には次のように記述します。

    str = "ABCDE"
    slice = str[1:3]    # "BC"
インデックスの指定方法には注意して下さい。

またインデックスにはマイナスの値も指定できます。インデックスと位置の関係は次の通りです。

            -3  -2  -1
     | A | B | C | D | E |
マイナスの値を使用する場合は、最後の文字の次のインデックスを指定できませんので、最後の文字は抽出できません。具体的には次のように記述します。

    str = "ABCDE"
    slice = str[1:-1]    # "BCD"
終了インデックスを省略すると最後の文字の次のインデックスが指定されたことになります。結果的に開始インデックスから最後の文字までが抽出されます。

    文字列オブジェクト[開始インデックス:]
具体的には次のように記述します。

    str = "ABCDE"
    slice = str[1:]    # "BCDE"
開始インデックスを省略すると最初の文字の前のインデックスが指定されたことになります。結果的に先頭の文字から終了インデックスの前の文字までが抽出されます。

    文字列オブジェクト[:終了インデックス]
具体的には次のように記述します。

    str = "ABCDE"
    slice = str[:2]    # "AB"
開始インデックスと終了インデックスを省略すると先頭の文字から最後の文字までが抽出されます。

    文字列オブジェクト[:]
具体的には次のように記述します。

    str = "ABCDE"
    slice = str[:]    # "ABCDE"
このようにスライスを使うことで、対象のオブジェクトの中から一部分を抽出した新しいオブジェクトを作成することが可能となります。

#要素の変更

リストオブジェクトは一度作成された後で要素が参照するオブジェクトを変更することが出来ます。(文字列の場合は、個々の要素が参照する文字を変更できません)。

要素が参照するオブジェクトを変更するには、インデックスを指定して取得した要素に対して新しいオブジェクトを代入します。

    リスト[インデックス] = オブジェクト
この時、新しいリストオブジェクトが作成されるのではなく、元のリストオブジェクトの指定の要素が参照するオブジェクトが変更になります。

具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    list[1] = "b"
    print list      # ["A", "b", "C"]
指定したインデックスの要素が参照するオブジェクトが文字列「B」から文字列「b」に変更になります。

またスライスを使って取得したリストに対して新しいリストを代入することで、リストの一部分を別のリストに置き換えることが出来ます。

    リスト[開始インデックス:終了インデックス] = 別のリスト
具体的には次のように記述します。

    list = ["A", "B", "C", "D"]
    
    list[1:3] = ["b", "c"]
    print list      # ["A", "b", "c", "D"]
スライスによって取得した部分リストを別のリストによって置き換えています。

また今回は置き換えられるリストの要素数と置き換えるリストの要素数は同じでしたが、必ずしも同じである必要はありません。次の例を見てください。

    list = ["A", "B", "C", "D"]
    
    list[1:3] = ["B", "b", "C", "c"]
    print list      # ["A", "B", "b", "C", "c", "D"]
上記では対象のリストの2つの要素に対して、4つの新しい要素を持つリストを代入しています。結果的に2つの要素を4つの要素で置き換えることになりますのでリストは6つの要素を持つオブジェクトになります。

スライスを使う場合も、新しいリストオブジェクトが作成されるのではなく、元のリストオブジェクトが変更されていることに注意して下さい。

#リストのサイズの取得(len関数)
リストが現在持っている要素数を取得することが出来ます。組み込み関数の「len」関数を使用します。

len(リストオブジェクト)
リストに含まれる要素数を取得します。「len」関数はリストの他に文字列やタプル、辞書などの要素数を取得できます。

具体的には次のように記述します。

    list = ["A", "B", "C"]

    print len(list)
上記の場合はリストの要素数「3」を表示します。

#要素の追加と連結(appendメソッド, extendメソッド)
リストオブジェクトを作成後に新しい要素を追加することが可能です。いくつか方法がありますので順に確認していきます。

##要素を追加
まずはオブジェクトをリストの最後に追加する方法です。リスト型で用意されている「append」メソッドを使います。

    リストオブジェクト.append(オブジェクト)
リストの最後に引数に指定したオブジェクトを追加します。

具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    list.append("D")
    print list     # ["A", "B", "C", "D"]
リストの最後に新しい要素として文字列「D」が追加されます。結果的にリストは["A", "B", "C", "D"]となります。

##別のリストの要素を追加
次にリストの最後に別のリストの要素を追加する方法です。リスト型で用意されている「extend」メソッドを使います。

    リストオブジェクト.extend(リストオブジェクト)
リストの最後に引数に指定したリストが持つ要素が全て追加されます。

具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    list.extend(["D", "E"])
    print list      # ["A", "B", "C", "D", "E"]
リストの最後に別のリストに含まれている要素が追加されます。結果的にリストは["A", "B", "C", "D", "E"]となります。

なお、「extend」メソッドの代わりに「append」メソッドの引数にリストを指定した場合、リストの要素が追加されるのではなく、リストオブジェクトそのものが1つの要素として追加されますので注意して下さい。

    list = ["A", "B", "C"]
    
    list.append(["D", "E"])
    print list      # ["A", "B", "C", ["D", "E"]]
リストの連結
リストとリストを連結して新しいリストを作成するには「+」演算子を使います。

    リストオブジェクト + リストオブジェクト
「+」演算子はリストオブジェクトを変更するものではなく、リストとリストを連結して新しいリストオブジェクトを作成します。

具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    newlist = list + ["D", "E"]
    print newlist    # ["A", "B", "C", "D", "E"]
リスト["A", "B", "C"]に別のリスト["D", "E"]を連結し、新しいリストオブジェクトを作成しています。

また「*」演算子はリストオブジェクトを指定の回数繰り返した新しいリストオブジェクトを作成します。

    リストオブジェクト * 回数
具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    newlist = list * 3
    print newlist    # ["A", "B", "C", "A", "B", "C", "A", "B", "C"]
    
#要素の挿入(insertメソッド)
リストオブジェクトを作成後に新しい要素を指定の位置に挿入することが可能です。リスト型で用意されている「insert」メソッドを使います。

    リストオブジェクト.insert(インデックス, オブジェクト)
1番目の引数で指定したインデックスの要素の直前に、2番目の引数で指定したオブジェクトを新しい要素として追加します。

具体的には次のように記述します。

    list = ["A", "B", "C"]

    list.insert(1, "D")
    print list     # ["A", "D", "B", "C"]
上記ではインデックス1の要素「B」の直前に文字列「D」を新しい要素として追加します。

#要素の削除(del文, popメソッド, removeメソッド)
リストオブジェクトの中の任意の要素を削除することが可能です。要素を削除するには「del」文を使用します。

    del オブジェクト
「del」文は引数に指定したオブジェクトを削除するための文です。「del」文の引数には削除するオブジェクトを指定しますが、リストオブジェクト[インデックス]の形式で取得したリストオブジェクトの要素を指定します。

具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    del list[1]
    print list     # ["A", "C"]
上記ではインデックス1の要素をリストから削除しています。

またスライスを使って部分リストを引数に指定することも出来ます。

    list = ["A", "B", "C", "D"]
    
    del list[1:3]
    print list     # ["A", "D"]
##指定のインデックスの要素を削除する
リスト型で用意されている「pop」メソッドを使うことで、指定のインデックスの要素を削除することが出来ます。

    リストオブジェクト.pop(インデックス)
指定のインデックスの要素を削除し、その要素を返します。インデックスが省略された場合はリストの末尾の要素が削除されます。

具体的には次のように記述します。

    list = ["A", "B", "C", "D"]
    
    list.pop(1)
    print list     # ["A", "C", "D"]
    
    list.pop()
    print list     # ["A", "C"]
##指定の値を持つ要素を削除する
リスト型で用意されている「remove」メソッドを使うことで、指定の値を持つオブジェクトが代入されている要素を削除することが出来ます。

    リストオブジェクト.remove(オブジェクト)
オブジェクトそのものが同一ではなく、オブジェクトが持つ値が同じものを削除します。またリストに同じ値のオブジェクトを持つ要素が複数存在した場合には、最初の要素を削除します。

具体的には次のように記述します。

    list = ["A", "B", "C", "B", "D"]
    
    list.remove("B")
    print list     # ["A", "C", "B", "D"]
上記では文字列オブジェクトの「B」と同じ値を持つインデックス1の要素をリストから削除しています。

#スライスを使った要素の追加/挿入/削除
リストに対してスライスを指定し任意の部分リストを取得することで、要素の追加や削除を行うことが出来ます。

要素をリストの末尾に追加するには次のように行います。

    リストオブジェクト[len(リストオブジェクト):] = オブジェクト
スライスを指定して取得した部分リストに対してオブジェクトを追加することは、その部分リストをオブジェクトで置き換えることになります。
リストオブジェクト[len(リストオブジェクト):]はリストの最後の文字の次からリストの末尾までの部分リストとなります(つまり現在何も要素が存在しない部分リストとなります)。
指定したオブジェクトで置き換えることによって、結果的に末尾にオブジェクトを追加することになります。

同じように他のリストに含まれる全ての要素を追加するには次のように行います。

    リストオブジェクト[len(リストオブジェクト):] = リストオブジェクト
具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    list[len(list):] = "D"
    print list     # ["A", "B", "C", "D"]
    
    list[len(list):] = ["E", "F"]
    print list     # ["A", "B", "C", "D", "E", "F"]
任意の位置に要素を挿入するには次のように記述します。

    リストオブジェクト[インデックス:インデックス] = リストオブジェクト
例えばリストオブジェクト[1:1]に対してオブジェクトやリストオブジェクトを代入すると、インデックス1の文字の前の位置に指定したオブジェクトやリストオブジェクトに含まれる全ての要素を追加します。

具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    list[1:1] = "a"
    print list     # ["A", "a", "B", "C"]
最後に要素を削除するには次のように記述します。

    リストオブジェクト[インデックス1:インデックス2] = []
指定したスライスで取得した部分リストに対して空リストを表す[]を代入することで、部分文字列を空のリストに置き換えます。
結果的にスライスを指定して取得した部分リストが削除されることになります。

具体的には次のように記述します。

    list = ["A", "B", "C", "D"]
    
    list[1:3] = []
    print list     # ["A", "D"]
このようにスライスを使って指定した部分リストを操作することで、要素の追加や削除を行う事ができます。

#要素の確認(in演算子, indexメソッド, countメソッド)
指定の値を持つ要素がリストの中に含まれているかどうか、また含まれている場合には何回含まれているかなどの取得方法を確認します。

##指定の値を持つ要素が存在するかどうか
まず指定の値が要素に含まれているかどうかを調べるには「in」演算子を使います。書式は次の通りです。

    オブジェクト in リストオブジェクト
「in」演算子の左辺のオブジェクトを持つ値が右辺のリストオブジェクトの要素の中に存在している場合は「True」を返します。存在しない場合は「False」を返します。

同じく「not in」演算子は指定の値が含まれていない場合に「True」を返します。

    オブジェクト not in リストオブジェクト
具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    print "B" in list        # True
    print "D" in list        # False
    print "B" not in list    # False
    print "D" not in list    # True
##指定の値を持つ要素のインデックス
次に指定の値がリストの要素に含まれる場合に、要素のインデックスを取得するにはリスト型で用意されている「index」メソッドを使います。

    リストオブジェクト.index(オブジェクト)
引数で指定したオブジェクトが持つ値が要素の中に含まれている場合は、最初の要素のインデックスを返します。

具体的には次のように記述します。

    list = ["A", "B", "C"]
    
    print list.index("B")     # 1
指定した値が存在しない場合には「ValueError」が発生します。

##指定の値を持つ要素の数
次に指定の値を持つ要素がいくつ含まれるかを取得するにはリスト型で用意されている「count」メソッドを使います。

    リストオブジェクト.count(オブジェクト)
引数で指定したオブジェクトが持つ値がいくつの要素に含まれているのかを返します。

具体的には次のように記述します。

    list = ["A", "B", "C", "B"]
    
    print list.count("B")     # 2
指定した値が存在しない場合には「0」を返します。

#要素のソート(sortメソッド, reverseメソッド)
リストに含まれる要素を、要素が参照しているオブジェクトの値を使って並べ替える方法を確認します。

##要素を昇順に並び替える
値を昇順に並び替える場合はリスト型で用意されている「sort」メソッドを使います。

    リストオブジェクト.sort()
要素が参照しているオブジェクトの値を使って並び替えます。
文字列であれば文字コードの並び順、数値であれば数値が小さい順に並び替えられます。「sort」メソッドの結果、元のリストオブジェクトの要素が並び替えられます。

具体的には次のように記述します。

    strlist = ["B", "C", "A"]
    numlist = [5, 2, 3]
    
    strlist.sort()
    print strlist        # ["A", "B", "C"]
    
    numlist.sort()
    print numlist        # [2, 3, 5]
並び替えを行う場合、要素が参照しているオブジェクトの型が異なった場合でも並び替えは行えますが、型が異なる場合にどのように並べ替えられるのかは分かりませんでした。

##要素を逆に並び替える
現在要素が並んでいる順場を逆に並び替えます。リスト型で用意されている「reverse」メソッドを使います。

    リストオブジェクト.reverse()
「reverse」メソッドの結果、元のリストオブジェクトの要素が逆順に並び替えられます。

具体的には次のように記述します。

    list = ["B", "C", "A"]
    
    list.reverse()
    print list        # ["A", "C", "B"]
降順にソートされるわけではなく、あくまで現在と逆に並び替えられるだけです。降順にソートする場合はまず「sort」メソッドを実行してから「reverse」メソッドを実行して下さい。

#連続した数値の要素を持つリストの作成(range関数)
後で解説を行う「for」文などでは、順に並んだ数値を要素として持つリストが頻繁に使われます。
少ない要素数であれば、直接数値を記述してリストオブジェクトを作成することも可能ですが、数が多い場合には「range」関数を使うと便利です。

「range」関数は指定した条件に従ってリストオブジェクトを作成して返してくれます。書式は次の通りです。

    range([start,] stop[, step])
引数は全て整数で指定します。「stop」だけを指定した場合には、0から「stop - 1」まで順に1ずつ増加する要素を持つリストが作成されます。

    list = range(5)

    print list  # [0, 1, 2, 3, 4]
開始する数値を指定する場合は引数「start」を指定して下さい。

    list = range(2, 5)
    
    print list  # [2, 3, 4]
デフォルトでは次の要素は前の要素に1を加えた数値となりますが、引数「step」を指定すると指定した値だけ次の要素には追加されます。この時最後の値は「stop」より小さい最大の数値となります。

    list = range(1, 6, 2)
    
    print list  # [1, 3, 5]
各引数の値は負の整数も指定可能です。引数「step」が負の値の場合、最後の値は「stop」より大きい最小の数値となります。

    list = range(0, -5, -2)
    
    print list  # [0, -2, -4]

#シーケンス型のオブジェクトからリストを作成(list関数)
文字列やタプルなどのシーケンス型のオブジェクトからリストを作成する方法を確認します。組み込み関数の「list」を使います。

    list([sequence])
引数に指定したシーケンス型のオブジェクトが持つ要素を持ち、同じ順序で並ぶリストを作成します。

具体的には次のように記述します。

    print list("ABC")      # ["A", "B", "C"]
    print list((20, 18))   # [20, 18]
また引数にリストオブジェクトを指定した場合には、そのリストのコピーを作成して返します。

    l = ["A", "B", "C"]
    print list(l)         # ["A", "B", "C"]
タプルを作成する「tuple」関数と、リストを作成する「list」関数を使うことで、本来ソート機能が無いタプルを一度リストに変換してからソートし、改めてタプルを作成するといったことが可能になります。

    t = ("B", "C", "A")
    tmplist = list(t)
    tmplist.sort()
    t = tuple(tmplist)
    print t            # ("A", "B", "C")
「tuple」関数については「シーケンス型のオブジェクトからタプルを作成(tuple関数)」を参照して下さい。