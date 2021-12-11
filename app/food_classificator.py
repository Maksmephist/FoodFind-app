import json
import requests
import base64


class FoodClassificator:
  def get_answer(self, img_path):
    header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

    with open(img_path, 'rb') as f:
        im_b64 = base64.b64encode(f.read())

    payload = {'id': '123', 'type': 'jpg', 'box': [0, 0, 100, 100], 'image': im_b64}

    resp = requests.post("http://194d-85-143-112-73.ngrok.io/predict", data=payload)

    if resp.status_code == 200:
      return resp.json()['answer']
    else:
      return error
