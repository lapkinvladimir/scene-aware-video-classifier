# 🎥 Scene-Aware AI Video Classifier  
*A YOLO-powered pipeline for environment-aware video understanding*

## 🚀 Overview

This project uses **YOLOv8** and **rule-based scene classification** to analyze video footage and **identify environments** like street, park, office, or kitchen — entirely through detected objects. Built as a modular pipeline, it serves as the foundation for future development in **automated editing**, **AI-powered storytelling**, and **prompt-to-video workflows**.

🧠 Originally built for research into integrating **YOLO + scene logic + diffusion models** (ComfyUI, ControlNet), this tool helps machines "understand" what they're seeing — not just objects, but the whole *context*.

---

## 🔍 Key Features

- 🧠 **Real-time object detection** using YOLOv8 (with YOLOv5 fallback)
- 🏷️ **Scene classification logic** using object co-occurrence
- 🎬 **Video frame analysis** with interval sampling and labeling
- 🛠️ **Modular structure** for plugging into ComfyUI / Automatic1111
- 📦 Lightweight and easily extendable with new scenes / rules

---

## 📂 Project Structure

videoAiPetProject/  
├── data/  
│   ├── images/                 # test frames  
│   └── videos/                 # input test video  
├── output/  
│   └── processed_test_video.mp4  
├── scripts/  
│   └── main.py                 # main detection pipeline  
│   └── yolov5s.pt              # pretrained model  
├── yolov5/                     # optional YOLOv5 fork for experiments  
├── requirements.txt  
├── VideoToVideo.ipynb          # notebook demo  
└── README.md

---

## 🧠 Sample Output

Frame 90: Scene = park, Detected: ['bench', 'dog', 'person']  
Frame 180: Scene = kitchen, Detected: ['microwave', 'refrigerator']

---

## 💡 Future Work

- Add **ComfyUI** integration for prompt-driven edits  
- Link with **ControlNet** to guide diffusion generations based on scene  
- Automate video cuts, text overlays, and transitions  
- Replace rule-based logic with fine-tuned scene classifiers

---

## 🔧 Tech Stack

- Python 3.10  
- OpenCV  
- Ultralytics YOLOv8  
- PyTorch  
- Custom inference logic

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/scene-aware-video-classifier.git
cd scene-aware-video-classifier
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python scripts/main.py
```

---

## 📽️ Demo

![demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3VidnZncXphZ3ZjMGs1ZTNzZGltM2w2b2k5YmVnOW5rZW5hd2o3MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jUwpNzg9IcyrK/giphy.gif)

_(replace with your own GIF later 😎)_

---

## 🧑‍💻 Author

**Volodymyr Lapkin**  
[GitHub](https://github.com/YOUR_USERNAME) • [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN)

---

## 🧠 Inspiration

Built out of a pure obsession with making machines **understand scenes**, not just boxes.

---

## 🏁 License

MIT — do what you want, just don’t make it NFT 🤙
