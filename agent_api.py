from bottle import route, run, template, request, response
import json, os, datetime, traceback, sys

os.makedirs("exceptions", exist_ok=True)
@route('/', method=["POST"])
def api():
    try:
        data = request.json
        folder = data["hostname"]+"-"+data["username"]
        os.makedirs(folder, exist_ok=True)
        with open(folder+"/"+data["time"]+".json", "w") as f:
            json.dump(data, f)
        return "OK"
    except Exception as e:
        with open("exceptions"+"/"+datetime.datetime.now().isoformat()+".txt", "w") as f:
            f.write("".join(traceback.format_exception(*sys.exc_info())))
            f.write("\n")
            f.write("----------"*3)
            f.write("\n")
            f.write(request.body.read().decode())
            f.write("\n")
            f.write("----------"*3)
            f.write("\n")
            f.write(json.dumps(dict(request.headers)))
        response.status = 400
        return "FAIL"

run(host='0.0.0.0', port=8080)