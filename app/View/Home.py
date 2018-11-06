from flask import Flask, request, abort,current_app
import AlipaySDK

@api.route("/")
def homeIndex():
    AlipaySDK.AopClient().client
    value = request.args.get("sss")
    print(value)
    # abort(401)
    return "index"