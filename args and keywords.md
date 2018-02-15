#Pythonの文法

##__*argsについて__

- 関数の位置引数を制限なく指定できる機能

例

    def print_args(*args):
    print("Positional arguments tuple:", args)
    とすると、
    
    引数なしで呼び出した
    print_args()
    Positional arguments tuple: ()
    
    引数を3つ指定して呼び出した
    print_args("a", "b", "c")
    Positional arguments tuple: ('a', 'b', 'c')

## **keywordsについて

- 引数の辞書化に当たる行為

 例

    # **によるキーワード引数の辞書化
    def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)
    に対し、
    # 引数を指定しない場合
    print_kwargs()
    # Keyword arguments: {}

    # キーワード引数を2つ指定した場合
    print_kwargs(num=1, text="aaa")
    # Keyword arguments: {'num': 1, 'text': 'aaa'}
    なお、この機能はキーワード引数（Keyword arguments）に関する機能なので、以下のように位置引数を指定した場合はエラーになります。
    # 位置引数を指定したらエラー
    print_kwargs(1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: print_kwargs() takes 0 positional arguments but 1 was given
    
##*argsと**keywordsの併用
- 注意点として、「*args -> **kwargs」の順で必ず指定する必要があります。

例

    # *argsと**kwargsとの併用
    def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    に対し、
    # 引数を指定しない場合
    print_args()
    # Positional arguments: ()
    # Keyword arguments: {}
    
    # 位置引数のみ指定した場合
    print_args(1,2,3)
    # Positional arguments: (1, 2, 3)
    # Keyword arguments: {}
    
    # キーワード引数のみ指定した場合
    print_args(name="Yohei", age=30)
    # Positional arguments: ()
    # Keyword arguments: {'name': 'Yohei', 'age': 30}
    
    # 位置引数とキーワード引数を共に指定した場合
    print_args(1, 2, 3, name="Yohei", age=30)
    # Positional arguments: (1, 2, 3)
    # Keyword arguments: {'name': 'Yohei', 'age': 30}
    
##引数を辞書で渡す
- 今までは関数の引数での話でしたが、似たように引数を辞書型で渡すことで、キーワード引数を指定することができます。

例

    # 引数が2つの関数
    def say_hello(name, age):
        print("Hi, my name is %s, %d years old" % (name, age))
    
    # 位置引数で指定できますし、
    say_hello("Yohei", 30)
    # Hi, my name is Yohei, 30 years old
    
    # キーワード引数でも指定できますし、
    say_hello(name="Yohei", age=30)
    # Hi, my name is Yohei, 30 years old
    
    # そしてなんと、辞書でも指定できます。
    user = {"name": "Yohei", "age": 30}
    say_hello(**user)
    # Hi, my name is Yohei, 30 years old