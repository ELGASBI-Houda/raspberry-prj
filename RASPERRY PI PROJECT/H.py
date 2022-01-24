def emotionImage(imgPath):
    img = cv2.imread(imgPath)
    rects, faces, image = face_detector_image(img)
    i = 0
    for face in faces:
        roi = face.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        # make a prediction on the ROI, then lookup the class
        preds = classifier.predict(roi)[0]
        label = class_labels[preds.argmax()]
        label_position = (rects[i][0] + int((rects[i][1] / 2)), abs(rects[i][2] - 10))
        i = + 1
        # Overlay our detected emotion on the picture
        text_on_detected_boxes(label, label_position[0],label_position[1], image)
    cv2.imshow("Emotion Detector", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
