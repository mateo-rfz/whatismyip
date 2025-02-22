from flask import Flask , request , jsonify , render_template , send_file , send_from_directory
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


@app.route("/" , methods = ["GET" , "POST"])
def whatismyip():
    loger.loger(request.remote_addr , request.user_agent , request.base_url)

    if request.method == "POST" :
        rqIp = request.form.get("ip")
        
        infq = checkIpInfo((rqIp))
        try : 
            country , city , isp , countryCode = infq["country"] , infq["city"] , infq["isp"] , infq["countryCode"]
        except Exception : 
            country , city , isp , countryCode = None , None , None , None


        return render_template("home.html" , ip = request.remote_addr ,country = country ,
                                city = city , isp = isp , countryCode = countryCode)
    
    else : 
        infq = checkIpInfo((request.remote_addr))
        try : 
            country , city , isp , countryCode = infq["country"] , infq["city"] , infq["isp"] , infq["countryCode"]
        except Exception : 
            country , city , isp , countryCode = None , None , None , None
            
        return render_template("home.html" , ip = request.remote_addr ,country = country ,
                                city = city , isp = isp , countryCode = countryCode)



@app.route("/logo")
def logo() : 
     return send_file("static/logo.png")




@app.route('/flags/<cc>')
def countryFlag(cc):
    return send_from_directory('static/flags', f"{cc.lower()}.svg")







if (__name__) == ("__main__"):
    app.run(host = socket.gethostbyname(socket.gethostname()) , port = 80 , debug=False)
