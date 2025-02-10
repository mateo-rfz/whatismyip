from flask import Flask , request , jsonify , render_template , send_file
import socket
import requests
import json
import server_modulus.loger as loger




def checkIpInfo(clientIp):
        info = requests.get(f"http://ip-api.com/json/{clientIp}")
        return json.loads((info.text))




app = Flask(__name__)

@app.route("/whatismyip" , methods = ["GET" , "POST"])
def whatIsMyIp():
    loger.loger(request.remote_addr , request.user_agent , request.base_url)
    return jsonify({"ip":request.remote_addr})


@app.route("/" , methods = ["GET"])
def whatismyip():
    loger.loger(request.remote_addr , request.user_agent , request.base_url)

    infq = checkIpInfo((request.remote_addr))
    return render_template("home.html" , ip = request.remote_addr ,country = infq["country"] ,
                            city = infq["city"] , isp =infq["isp"])



@app.route("/logo")
def logo() : 
     return send_file("static/logo.png")




if (__name__) == ("__main__"):
    app.run(host = socket.gethostbyname(socket.gethostname()) , port = 80)