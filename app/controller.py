from app import app
import base64


path = '/var/www/html/'


def create_image_from_base64(baseString, name=None):
    if name==None:
        fileName = buildRandomString(30)
        fileName+=".png"
    else: fileName = name
    imgdata = base64.b64decode(baseString)
    with open(root + fileName, 'wb') as f:
        f.write(imgdata)
    return str(fileName)


@app.route('/create_image', methods=['GET', 'POST'])
def create_image():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    base64 = d['base64']
    fileName = create_image_from_base64(base64)
    return '{"status":"ok", "name":"'+fileName+'"}'





@app.route('/delete_image', methods=['GET', 'POST'])
def delete_image():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    url = d['url']
    name = url.split('/')[-1]
    os.remove(path+name)
    return '{"status":"ok"}'
   

@app.route('/update_image', methods=['GET', 'POST'])
def update_image():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    url = d['url']
    name = url.split('/')[-1]
    os.remove(path+name)
    base64 = d['base64']
    fileName = create_image_from_base64(base64, name=name)
    return '{"status":"ok"}'