# -*- coding: utf-8 -*-
from flask import Flask, request, abort
import AlipaySDK
app = Flask(__name__)


@app.route("/")
def homeIndex():
    AlipaySDK.AopClient().client
    value = request.args.get("sss")
    print(value)
    # abort(401)
    return "index"


if __name__ == "__main__":
    app.run(debug=True, host="192.168.5.5", port=80)
