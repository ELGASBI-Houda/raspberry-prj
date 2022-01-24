# start the tensorflow session and start streaming and image processing
sess = tf.Session()
softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    # show the frame
    cv2.imshow("face", frame)

    # transform to Gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces in our gray picture
    faces = faceDetect.detectMultiScale(gray,
                                        scaleFactor=1.3,
                                        minNeighbors=5
                                        )

    # transform into a numpy array for tf processing
    gray_np = gray.array

    for (x,y,w,h) in faces:
        #sampleNum = sampleNum+1
        #cv2.imwrite("./temp_dataset/"+str(sampleNum)+".jpg", gray[y:y+h,x:x+w])
        
        # feed the detected face (cropped image) to the tf graph
        predictions = sess.run(softmax_tensor, {'DecodeJpeg:0': gray_np[y:y+h,x:x+w]})
        prediction = predictions[0]

        # Get the highest confidence category.
        prediction = prediction.tolist()
        max_value = max(prediction)
        max_index = prediction.index(max_value)
        predicted_label = label_lines[max_index]

        print("%s (%.2f%%)" % (predicted_label, max_value * 100))

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100);

    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        cv2.destroyAllWindows()
        break