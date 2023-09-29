from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods = ['POST'])
def restart():
    data = request.get_json(force=True)
    if not data:
        return
    # run command,
    container_name = data['container_name']
    if container_name.isalpha():
        return 'nice try buddy'
    f"docker stop {data['container_name']}" 
    return data


if __name__ == '__main__':
    app.run()