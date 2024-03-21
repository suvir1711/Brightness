import cv2


# Function to detect brightness change and send alert
def detect_brightness_change(video_source):
    cap = cv2.VideoCapture(video_source)

    # Capture the first frame
    ret, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate absolute difference between consecutive frames
        diff = cv2.absdiff(prev_gray, gray)

        # Threshold the difference to detect significant changes in brightness
        threshold = 30
        _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

        # Count non-zero pixels in the thresholded image
        num_changed_pixels = cv2.countNonZero(thresh)

        # Display the video stream with detected changes
        cv2.imshow('Video Stream', frame)

        # Check for significant brightness change and send alert
        if num_changed_pixels > 500:
            print("Brightness change detected! Alert sent.")

        # Update previous frame
        prev_gray = gray

        # Check for 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Main function
if __name__ == "__main__":
    video_source = 'FaceTime HD camera'  # Use default camera (change to video file path if needed)
    detect_brightness_change(video_source)
