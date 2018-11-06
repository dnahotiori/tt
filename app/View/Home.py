from flask import Flask, request, abort,current_app
import SDK.AlipaySDK

@api.route("/")
def homeIndex():
    SDK.AlipaySDK.AopClient().client
    value = request.args.get("sss")
    print(value)
    # abort(401)
    return "index"