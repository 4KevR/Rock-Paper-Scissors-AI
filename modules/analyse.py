import requests, sys

# Gets the contents of an image file to be sent to the
# machine learning model for classifying
def getImageFileData(locationOfImageFile):
    with open(locationOfImageFile, "rb") as f:
        data = f.read()
        if sys.version_info[0] < 3:
            # Python 2 approach to handling bytes
            return data.encode("base64")
        else:
            # Python 3 approach to handling bytes
            import base64
            return base64.b64encode(data).decode()


# This function will pass your image to the machine learning model
# and return the top result with the highest confidence
def classify(imagefile):
    key = "2f1cc280-f702-11e9-bd58-d5bb7350842c24690a8f-aa0b-496d-8358-8339029d6693"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.post(url, json={ "data" : getImageFileData(imagefile) })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


if __name__ == "__main__":

    # CHANGE THIS to the name of the image file you want to classify
    demo = classify("my-test-image.jpg")

    label = demo["class_name"]
    confidence = demo["confidence"]


    # CHANGE THIS to do something different with the result
    print ("result: '%s' with %d%% confidence" % (label, confidence))
