# 🌌 Evaluating Environmental Safety in Virtual Worlds
**YOLOv8-Based Hazard Detection in Unity-Based Metaverse Simulations**

[![Conference](https://img.shields.io/badge/ICNGC-2024-green?style=for-the-badge)](https://www.earticle.net/Article/A468859)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Unity](https://img.shields.io/badge/Unity-Barracuda-black?style=for-the-badge&logo=unity)](https://unity.com/)
[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-yellow?style=for-the-badge)](https://github.com/ultralytics/ultralytics)

---

## 📖 Overview

As the metaverse expands, the boundary between virtual and physical worlds blurs. However, users wearing Head-Mounted Displays (HMDs) often lose awareness of their immediate physical surroundings, leading to potential safety hazards in industrial and medical environments.

This project proposes a **Real-Time Hazard Detection System** integrating **YOLOv8** object detection within a **Unity-based Augmented Reality (AR)** environment. The system processes video feeds to identify nearby risks, ensuring user safety without breaking immersion.

---

## 📂 Dataset & Methodology

Due to hardware constraints (lack of direct HL2 video feed access during initial testing), this research utilized a webcam-based dataset to simulate HMD inputs.

* **Input Source**: Stereo Labs-ZED2 Camera & Standard Webcam.
* **Preprocessing**: Images were resized to **160, 224, 320, 480, and 640** pixels to evaluate the trade-off between inference speed and detection accuracy.
* **Environmental Conditions**:
  * ☀️ **Bright Environment**: Standard indoor lighting.
  * 🌙 **Low-light Environment**: Tested to ensure model robustness in suboptimal lighting.

---

## 🏗️ Repository Structure

This repository contains the complete Python pipeline used for the research, reconstructed from the experimental notebooks and scripts.

```bash
📂 Project Root
├── 🖼️ data_preprocessing.py   # Resizes raw images to multiple resolutions (160~640px)
├── 🚀 train_combined.py       # Trains YOLOv8n/s models (Transfer Learning, 100 Epochs)
├── 🔄 export_onnx.py          # Exports trained .pt models to ONNX (Opset 12 for Barracuda)
├── 📊 evaluate_metrics.py     # Calculates Precision, Recall, F1-Score, and mAP
└── ⏱️ benchmark_inference.py  # Measures millisecond inference latency per image size
```

## 📝 Citation
If you use this work in your research, please cite the following paper:
* Paper Link: [E-Article Link](https://www.earticle.net/Article/A468859)
```bash
@article{jin2024evaluating,
  title={Evaluating Environmental Safety in Virtual Worlds: YOLOv8-Based Hazard Detection in Unity-Based Metaverse Simulations},
  author={Jin, Se-yong and Khan, Asma and Lee, Geon-Hee and Kim, Ji-Won and Dang, L Minh and Moon, Hyeonjoon},
  journal={Proceedings of the 10th International Conference on Next Generation Computing (ICNGC 2024)},
  pages={271--274},
  year={2024},
  publisher={Korean Next Generation Computing Society}
}
```

## 🤝 Acknowledgments
* Authors: Se-yong Jin, Asma Khan, Geon-Hee Lee, Ji-Won Kim, L Minh Dang, Hyeonjoon Moon*
* Affiliation: Sejong University, Republic of Korea
* Funding: This work was supported by IITP (Institute of Information & Communications Technology Planning & Evaluation) and IPET (Korea Institute of Planning and Evaluation for Technology in Food, Agriculture, Forestry and Fisheries) grants funded by the Korea government (MSIT, MAFRA).
