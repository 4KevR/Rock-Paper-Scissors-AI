from flask import Flask, render_template, request, jsonify
import base64
from modules import players

app = Flask(__name__)

computerPlayer = players.ComputerPlayer()
handPlayer = players.HandPlayer()

def compare(compResult, handResult):
    if compResult == handResult:
        return "Undecided"
    elif (compResult == "r" and handResult == "s") or (compResult == "s" and handResult == "p") or (compResult == "p" and handResult == "r"):
        computerPlayer.point()
        return "Computer wins"
    elif (handResult == "r" and compResult == "s") or (handResult == "s" and compResult == "p") or (handResult == "p" and compResult == "r"):
        handPlayer.point()
        return "You win"

@app.route("/",methods=['get'])
def index():     
    return render_template("index.html")

@app.route("/image",methods=["post"])
def image():
    image = request.form["imgBase64"].split(",")[1]
    
    with open("media/img.jpg","wb") as file:
        file.write(base64.b64decode(image))
        
    handResult = handPlayer.recognize()
    computerResult = computerPlayer.random()
    
    comparison = compare(computerResult,handResult["label"])
    
    returnValue = {"computerDecision":computerResult,"playerResult":comparison,"playerPoints":handPlayer.points,"computerPoints":computerPlayer.points,"label":handResult["label"],"confidence":handResult["confidence"]}

    return jsonify(returnValue)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
