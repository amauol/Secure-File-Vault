from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import hashlib

UPLOAD_DIR="/var/lib/secure-vault/uploads"
MAX_SIZE = 5*1024*1024 # 5MB

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_SIZE

@app.route("/health")
def health():
	return {"status":"ok"}

@app.route("/upload", methods=["POST"])
def upload():
	if "file" not in request.files:
		return {"error": "Nofile provided"}, 400
	f = request.files["file"]

	filename = secure_filename(f.filename)

	if filename == "":
		return {"error": "Invalid filename"}, 400

	path = os.path.join(UPLOAD_DIR, f.filename)

	f.save(path)

	sha256 = hashlib.sha256(open(path, "rb").read()).hexdigest()

	return {
		"filename" : f.filename,
		"sha256" : sha256,
		"status" : "uploaded"
	}

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)
