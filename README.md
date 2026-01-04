# Gesture Controlled Smart Home Automation

A real-time smart home automation system that uses **hand gestures** detected via
computer vision to control IoT devices, providing a **touch-free and intuitive**
alternative to traditional app- or voice-based systems.

---

##  Overview

Most smart home systems rely on mobile applications or voice assistants, which may not
always be convenient or accessible. This project enables users to control smart devices
using **simple hand gestures captured through a webcam**, making interaction faster,
more natural, and hands-free.

The system is designed to run efficiently on low-power hardware like **Raspberry Pi**.

---

##  Features

- Real-time hand gesture recognition using **MediaPipe**
- Touch-free control of smart devices over Wi-Fi
- Supports multiple gestures mapped to different actions
- Low-latency performance suitable for Raspberry Pi
- Modular and easy-to-extend Python codebase

---

## 🖐️ Gesture Mapping

| Hand Gesture     | Action Performed            |
|------------------|-----------------------------|
| One Finger       | Turn ON smart bulb          |
| Fist             | Turn OFF smart bulb         |
| Two Fingers      | Change bulb color to Yellow |
| Three Fingers    | Change bulb color to Blue   |

---

##  Tech Stack

- **Programming Language:** Python  
- **Computer Vision:** OpenCV, MediaPipe  
- **IoT Control:** pywizlight  
- **Hardware:** Raspberry Pi / USB Webcam  
- **OS:** Raspberry Pi OS / macOS (development)

---

##  How It Works

1. Webcam captures live video feed
2. MediaPipe detects hand landmarks in real time
3. Finger positions are analyzed to identify gestures
4. Recognized gesture is mapped to a predefined action
5. Corresponding command is sent to the smart bulb over Wi-Fi

---

##  Installation & Setup

### Prerequisites
- Python 3.8 or above
- Webcam connected
- Philips Wiz smart bulb connected to the same Wi-Fi network

## Steps

```bash
git clone https://github.com/saiprabhath1/Home-Automation-using-Gestures.git
cd Home-Automation-using-Gestures
pip install -r requirements.txt
python src/gesture_control.py
```
Make sure to update the smart bulb IP address inside the code before running.

---

## Demo

Demo screenshots are available in the demo/ folder.

---

## Performance

Smooth real-time detection
Low latency gesture recognition
Stable performance on Raspberry Pi-class hardware

---

## Future Enhancements

Face recognition for multi-user personalization
User-specific gesture-to-action mapping
Integration with Alexa / Apple HomeKit
Custom gesture training using ML models
Support for additional smart devices

---

## License

This project is open-source and available for learning and educational purposes.

---

## Author

Sai Prabhath
email: saiprabhath5@gmail.com
