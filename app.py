from flask import Flask,request,jsonify

app = Flask(__name__)

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
    prev = 0
    ans = 0
    copy = 0
    for _ in range(n):
        if ans == 0:
            ans = 1
        elif prev == 0:
            prev = 1
        else:
            copy = ans
            ans = prev + ans
            prev = copy
    return ans

if __name__=='__main__':
    app.run(
        debug=True
    )
