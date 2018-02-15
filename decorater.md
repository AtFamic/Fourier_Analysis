#デコレーターについて
- Pythonのデコレータが行っているのは、関数の上書きです。
- Pythonでは関数も第一級オブジェクのため、関数を関数の引数や返り値として使うことが出来ます。

例

    def add_two_ints(a: int, b: int):
    return a + b
     
    add_two_ints(3, 5)
    結果
    （出力無）
この関数を上書きして、計算結果を出力させるようにします。

    def print_result(func):
      def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
      return new_func
 
 
    def add_two_ints(a: int, b: int):
        return a + b
     
     
    add_two_ints = print_result(add_two_ints)
    add_two_ints(3, 5)
print_result 関数で何が起こっているか上から見ていくと

    1 引数として関数 func を取っている
    2 ローカル関数 new_func の中で func を実行しつつ、その返り値を出力している
    3 new_func の中で func の結果を返している(これがないと、上書き後の関数が値を返さなくなってしまいます)
    4 print_result の返り値として、ローカル関数 new_func を返している
    5 そして、最後から二番目の行で、add_two_ints という関数に print_result の結果を代入する
    6 add_two_ints の実行内容は new_func で定義した中身に上書きされます。

という流れです。

**Python のデコレータとは、この代入処理を”アットマーク”を用いた構文で書いているだけで、先ほどの例を次のように書き直すだけで、デコレータを使うことが出来ます**
関数を返す関数、というのがデコレータの正体です

    def print_result(func):
      def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
      return new_func
 
 
    @print_result
    def add_two_ints(a: int, b: int):
        return a + b
     
     
    # add_two_ints = print_result(add_two_ints)  <= いらないのでコメントアウト
    add_two_ints(3, 5)
    
**デコレータは複数付けることが出来るようなので、引数を出力する関数も作り、デコレータとしてくっつけてみましょう。**

    def print_args(func):
    def new_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return new_func
 
 
    def print_result(func):
        def new_func(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            return result
        return new_func
     
     
    @print_args
    @print_result
    def add_two_ints(a: int, b: int):
        return a + b
     
     
    add_two_ints(3, 5)
    print()
    add_two_ints(a=3, b=5)
    
    出力結果
    (3, 5)
    {}
    8
     
    ()
    {'a': 3, 'b': 5}
    8
    
**デコレータ自体に引数を渡して、それによって振る舞いを変えたいというときがあると思います。デコレータにも引数を渡すことは可能です。**
**例として、引数にとったメッセージを処理の前後で表示するprint_message を書いてみました。**

    def print_result(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return new_func
 
 
    def print_message(start_message: str, end_message: str):
        def _print_args(func):
            def new_function(*args, **kwargs):
                print(start_message)
                result = func(*args, **kwargs)
                print(end_message)
                return result
            return new_function
        return _print_args
     
     
    @print_message('処理開始', '処理終了')
    @print_result
    def add_two_ints(a: int, b: int):
        return a + b
     
     
    add_two_ints(3, 5)
    
    出力結果
    処理開始
    8
    処理終了
    
**上記の例を見て気付いた方がいらっしゃると思いますが、「8」と「処理終了」の出力順番は必ずしもこうなるとは限りません。どちらも “func の処理が終わったら” としか書いていないからです。**
**これは、仕様として決まっていて、デコレータは下に書かれているものから順番に実行されます。一番下のデコレータで返ってきた結果が、次のデコレータの func 引数として渡ります。**

例えば

    @print_message('処理開始', '処理終了')
    @print_result
    def add_two_ints(a: int, b: int):
        return a + b
    を
    @print_result
    @print_message('処理開始', '処理終了')
    def add_two_ints(a: int, b: int):
        return a + b
    
    出力結果
    処理開始
    処理終了
    8


    

    