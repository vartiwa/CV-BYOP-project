# BYOP - Real-Time Student Attention Monitor (Computer Vision)

## Student Details
- Name: Varun
- GitHub Username: vartiwa
- Contact Email: varunt154@gmail.com
- Course: Computer Vision
- Submission Type: Bring Your Own Project (BYOP)

## 1. Problem Statement
In online classes, self-study, and long computer sessions, students often lose attention without realizing it. This project detects whether a face and eyes are visible in a webcam frame and gives an immediate warning when attention appears low.

This is a practical computer vision solution to an everyday problem: helping users stay focused while studying.

## 2. Why This Problem Matters
- Lack of focus reduces learning quality and productivity.
- Students may not notice distraction in real time.
- A lightweight webcam-based assistant can provide instant feedback.
- The solution can be used in home study setups with no extra hardware.

## 3. Project Objective
Build a real-time attention monitoring system using OpenCV and Haar Cascade classifiers that:
- Detects a face and eyes in live webcam video.
- Shows a red warning message when no face is detected.
- Shows a warning when a detected face has no visible eyes.
- Runs in real time on a local machine.

## 4. Approach and Methodology
### 4.1 Technologies Used
- Python
- OpenCV (`cv2`)
- Haar Cascade XML models:
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`

### 4.2 Pipeline
1. Capture frame from webcam.
2. Mirror the frame for natural interaction.
3. Convert frame to grayscale for faster detection.
4. Detect faces in the frame.
5. If no face is detected, display `PAY ATTENTION!!!!!`.
6. If face is detected, detect eyes in the face region.
7. If no eyes are detected, display warning text.
8. Draw rectangles around detected faces and eyes.
9. Exit when `Esc` key is pressed.

## 5. Key Design Decisions
- Haar cascades were chosen for simplicity and speed on CPU.
- Real-time webcam processing was prioritized over high model complexity.
- Warning logic is intentionally strict to give fast feedback.
- No cloud dependency was used so the project runs completely offline.

## 6. Project Structure
- `main.py` - Main real-time detection script.
- `haarcascade_frontalface_default.xml` - Face detection model.
- `haarcascade_eye.xml` - Eye detection model.
- `requirements.txt` - Python dependency list.

## 7. Setup Instructions
### 7.1 Prerequisites
- Python 3.8 or higher
- A working webcam

### 7.2 Installation
```bash
# 1) Clone repository
git clone <your-repository-url>

# 2) Enter project folder
cd CV

# 3) (Optional but recommended) Create virtual environment
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# 4) Install dependencies
pip install -r requirements.txt
```

### 7.3 Run
```bash
python main.py
```

### 7.4 Controls
- Press `Esc` to close the application window.

## 8. Expected Output
- A webcam window opens.
- Face and eye regions are highlighted with rectangles.
- When attention is likely low (face not found or eyes not found), warning text appears at the center of the frame.

## 9. Challenges Faced
- Real-time detection can be sensitive to lighting conditions.
- Eye detection may fail if face angle is large or if glasses cause reflections.
- Balancing warning strictness and false alerts required trial and error.

## 10. Learning Outcomes
This project strengthened understanding of:
- Classical computer vision workflows
- Real-time frame processing
- Haar-based object detection
- Region of interest (ROI) handling
- Practical limits of traditional detectors in real environments

## 11. Limitations
- Haar cascades are less robust than modern deep learning detectors.
- No temporal smoothing, so warnings can flicker.
- Single-user assumption (primary face in frame).

## 12. Future Improvements
- Add blink-rate and eye-aspect-ratio based drowsiness estimation.
- Add a confidence score and smoother warning logic.
- Store session analytics (focus percentage over time).
- Replace Haar cascades with deep learning models (DNN/MediaPipe).
- Add optional audio alerts.

## 13. Submission Checklist (BYOP)
- [x] Real-world problem identified
- [x] Solution built using course concepts
- [ ] Code uploaded to GitHub repository
- [x] README explains setup and usage
- [x] Project report prepared

## 14. License
This project is for academic submission and learning purposes.
