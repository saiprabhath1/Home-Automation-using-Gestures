import cv2
import mediapipe as mp
from pywizlight import wizlight, PilotBuilder
import asyncio
import logging

BULB_IP = "192.168.0.164" //replace with your bulb ip
bulb = wizlight("192.168.0.164")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    logging.error("CAMERA NOT DETECTED! EXITING...")
    exit()
    
async def control_devices(gesture):
    try:
        if gesture == "ONE FINGER":
            logging.info("Turning ON both devices")
            await bulb.turn_on()
            
        elif gesture == "FIST":
            logging.info("Turning OFF both devices")
            await bulb.turn_off()
            
        elif gesture == "THREE FINGERS":
            logging.info("Changing Wiz to BLUE")
            await bulb.turn_on(PilotBuilder(rgb=(0,0,255)))            
        elif gesture == "TWO FINGERS":
            logging.info("Changing Wiz to YELLOW")
            await bulb.turn_on(PilotBuilder(rgb=(255,255,0)))
            
    except Exception as e:
        logging.error(f"ERROR CONTROLLING DEVICE: {e}")
        
async def main():
    try:
        print("Main loop started")
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                logging.error("Not captured")
                break
    
            rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            result = hands.process(rgb_frame)
    
            gesture = None
    
            if result.multi_hand_landmarks:
                print("HAND DETECTED")
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
                    fingers = []
                    finger_tips = [4,8,12,16,20]
                    for tip in finger_tips:
                        tip_y = hand_landmarks.landmark[tip].y
                        pip_y = hand_landmarks.landmark[tip-2].y
                        is_up = (tip_y) <(pip_y)
                        fingers.append(1 if is_up else 0)
                    print(f"Finger Detected:{fingers}")
                
                    
                    if fingers == [1,1,0,0,0]:
                        gesture = "ONE FINGER"
                    elif fingers == [1,0,0,0,0]:
                        gesture = "FIST"
                    elif fingers == [1,1,1,0,0]:
                        gesture = "TWO FINGERS"
                    elif fingers == [1,1,1,1,0]:
                        gesture = "THREE FINGERS"
                
                    if gesture:
                        print(f"Detected Gesture: {gesture}")
                        await control_devices(gesture)
                    else:
                        print("NOT VALID GESTURE")
                    
            
            
            cv2.imshow("Gesture Control", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        loop.close()
