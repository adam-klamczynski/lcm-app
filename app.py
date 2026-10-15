from flask import Flask, request, make_response
import math


app = Flask(__name__)

@app.route("/adamklamczynski13_gmail_com")
def lcm_endpoint():
    str_x=request.args.get('x')
    str_y=request.args.get('y')

    try:
        x=int(str_x)
        y=int(str_y)
    except(TypeError, ValueError):
        return make_response("NaN", 200, {"Content-Type": "text/plain"})

    if x<0 or y<0:
        result="NaN"
    elif x==0 and y==0:
        result="0"
    else:
        lcm_result=(x*y)//math.gcd(x,y)
        result= str(lcm_result)

    return make_response(result, 200, {"Content-Type":"text/plain"})

if __name__== '__main__':
    app.run(debug=True)
