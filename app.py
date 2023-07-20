from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app,methods=['GET'])

@app.route("/fib", methods=['GET'])
def api():
    try:
        req = request.args
        n = req.get("n")
        if n is None:
             # リクエストパラメータが存在しない
             return jsonify(
            {
                "status" : 400,
                "message" : "Bad request."
            }
        )   
        n = int(n)
        if n <= 0:
            # nが0以下
            return jsonify(
            {
                "status" : 400,
                "message" : "Bad request."
            }
        )
    except:
        # nが整数でない
        return jsonify(
            {
                "status" : 400,
                "message" : "Bad request."
            }
        )
    
    return jsonify(
        {
            "result" : fibonacci(n=n)
        }
    )
    
# フィボナッチ関数
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

if __name__=='__main__':
    app.run(
        debug=True
    )
