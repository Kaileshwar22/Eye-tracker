import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
''''using mediapipe for detecting the face movements in particular'''
face = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()
while True:
    _, frame=cam.read()
    frame=cv2.flip(frame,1)
    #detecting Face
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face.process(rgb_frame)
    landmark_point=output.multi_face_landmarks
    frame_h,frame_w,_=frame.shape
    if landmark_point:
        landmarks= landmark_point[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
            if id == 1:
                screen_x=screen_w/frame_w*x
                screen_y=screen_h/frame_h*y
                pyautogui.moveTo(x,y)
        left=[landmarks[145],landmarks[159]]
        for  landmark in left:
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,255))
        if (left[0].y-left[1].y)<0.004:
            pyautogui.click()
            pyautogui.sleep(1)
            cv2.imshow('Eye Controler',frame)
    cv2.waitKey(1)
    