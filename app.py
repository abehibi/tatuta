from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 保存先フォルダ
UPLOAD_FOLDER = "KARAAGE"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["photo"]
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f"保存しました！ -> {filepath}"
    return "ファイルがありません"
from ultralytics import YOLO
import cv2

# モデル読み込み
model = YOLO("yolov8n.pt")

# 入力画像
results = model('wa.jpg',save=True) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
