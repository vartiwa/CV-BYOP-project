# BYOP Project Report

## Course Information
- Course: Computer Vision
- Assignment: Bring Your Own Project (BYOP)
- Student: Varun
- GitHub Username: vartiwa
- Email: varunt154@gmail.com
- Submission Date: March 31, 2026

## 1. Title of the Project
Real-Time Student Attention Monitor Using Face and Eye Detection

## 2. Abstract
This project presents a real-time attention monitoring system built using OpenCV and Haar Cascade classifiers. The system captures webcam input and checks for the presence of a face and eyes. If no face is visible, or if eyes are not detected within the face region, the system displays a warning message: `PAY ATTENTION!!!!!`.

The goal is to create a lightweight and practical computer vision tool that addresses a common problem in online learning and self-study environments: losing focus without immediate awareness.

## 3. Problem Description
During long study sessions, many students become distracted or drowsy. Existing productivity tools usually rely on manual tracking, which is not real-time and requires additional effort from the user. This project attempts to solve that by creating a passive, real-time visual attention checker.

### Why this problem is relevant
- Attention is critical for effective learning.
- Online learning environments increase distraction risk.
- Real-time feedback can improve study behavior.

## 4. Objectives
- Detect face and eyes from webcam frames in real time.
- Alert the user when attention appears low.
- Keep the system simple, local, and easy to run on normal hardware.

## 5. Course Concepts Applied
This project uses core computer vision topics covered in class:
- Image capture from camera streams
- Color space conversion (BGR to grayscale)
- Object detection using Haar cascades
- Region of interest (ROI) based processing
- Real-time frame rendering and interaction

## 6. Proposed Solution and Method
### 6.1 Tools and Libraries
- Python
- OpenCV
- Pretrained Haar Cascade XML models

### 6.2 Processing Flow
1. Initialize face and eye classifiers.
2. Start webcam capture.
3. Read frame and mirror it.
4. Convert to grayscale.
5. Detect face regions.
6. If no face detected, show centered warning.
7. If face detected, detect eyes inside each face ROI.
8. If no eyes found, show warning.
9. Draw bounding boxes around detected features.
10. Continue until user presses `Esc`.

## 7. Key Implementation Decisions
- Chose Haar cascades due to fast CPU inference and easy integration.
- Used real-time webcam loop for continuous monitoring.
- Kept warning logic simple and immediate for user awareness.
- Avoided cloud/API dependencies to maintain privacy and offline operation.

## 8. Results and Observations
### Positive outcomes
- Real-time processing works on standard laptops.
- Face and eye detections are visible and interpretable.
- Warning behavior is triggered in expected missing-detection scenarios.

### Observed limitations
- Detection reliability depends on lighting and camera angle.
- Eye detection can fail with head tilt or reflections.
- Frame-by-frame decisions can create unstable warning behavior.

## 9. Challenges Faced
- Managing false negatives in low-light conditions.
- Balancing detection sensitivity with practical usability.
- Maintaining smooth real-time rendering while applying multiple detections.

## 10. Ethical and Practical Considerations
- The system processes video locally and does not save user images.
- It is a supportive tool, not a strict surveillance or grading system.
- In real deployments, user consent and transparency would be required.

## 11. What I Learned
- How classical vision models can solve meaningful real-world problems.
- Trade-offs between simplicity, speed, and robustness.
- Importance of environment conditions in real-time vision systems.
- How to structure a reproducible project with documentation.

## 12. Scope for Future Work
- Add temporal smoothing to reduce false warnings.
- Integrate blink detection and drowsiness metrics.
- Use deep-learning face/eye landmarks for higher robustness.
- Add per-session analytics and reporting.
- Support multiple users or configurable detection thresholds.

## 13. Conclusion
The project successfully demonstrates a practical computer vision application to monitor user attention in real time. Although built with classical methods, it addresses a genuine student-life problem and provides a strong foundation for future improvements with advanced models.

## 14. GitHub Repository Contents
- Source code (`main.py`)
- Haar models (`haarcascade_frontalface_default.xml`, `haarcascade_eye.xml`)
- README with setup and usage instructions
- This project report document
