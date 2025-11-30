import cv2
import os

video_path = "videos/conyouer1.mp4"
cap = cv2.VideoCapture(video_path)

# Basic info (you will put this in your report)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
duration = length / fps

print(f"Frames    : {length}")
print(f"FPS       : {fps:.2f}")
print(f"Resolution: {width}×{height}")
print(f"Duration  : {duration:.1f} seconds")

# Show first 100 frames quickly to see if camera is fixed and objects move
while cap.isOpened():
    ret, frame = cap.read()
    if not ret or cap.get(cv2.CAP_PROP_POS_FRAMES) > 100:
        break
    cv2.imshow('First frames - press q to quit', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()