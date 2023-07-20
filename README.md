# n番目のフィボナッチ数を返すREST API

## 使用技術
フレームワーク：Flask(Python)   
サーバ：render.com
※ 無料プランを使用しており、時間が開くと起動に時間がかかるため、テストする際最初のレスポンスが遅くなります。

## 仕様
`https://fibonacci-api-hsbz.onrender.com/fib?n=5`のようにアクセスすると、5番目のフィボナッチ数を返す。
```json
{
    "result" : 5
}
```
`https://fibonacci-api-hsbz.onrender.com/fib?n=0`とアクセスすると、0番目のフィボナッチ数は定義されていないので、HTTPステータスコードは400となり、次のようなJSONが返される。
```json
{
    "status" : 400,
    "message" : "Bad request.",
    "error-message" : "n must be a natural number. Not a negative number."
}
```

エラーコードは次のように定義した。
| エラーメッセージ | エラーの説明 | 
| :---: | :---: |
| `n not found.Please enter n.` | nが存在しない |
| `n must be a natural number. Not a negative number.` | nが0以下の数字である |
| `n must be natural number.` | nが整数でない |

## フィボナッチ関数
n番目のフィボナッチ数列を求める関数は次の通りである。
```python
def fibonacci(n :int) ->int:
    fib = [0,0]
    tmp = 0
    for _ in range(n):
        if fib[1] == 0:
            fib[1] = 1
        elif fib[0] == 0:
            fib[0] = 1
        else:
            tmp = fib[1]
            fib[1] = fib[0] + fib[1]
            fib[0] = tmp
    return fib[1]
```
このプログラムは動的計画法により`O(n)`で実装されている。

## ユニットテスト
ユニットテストはPythonのunittestライブラリを使って実装した。
テストケースは以下の表のとおりである。
| nの値 | 理論値 |
| :---: | :---: |
| 1 | 1|
|2 | 1|
|3|2|
|4|3|
|5|5|
|100|354224848179261915075|
|200|280571172992510140037611932413038677189525| 

このプログラムのフィボナッチ関数のユニットテストの実行結果は次のとおりであった。
```
ynori@pika fib % python3 test.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```


