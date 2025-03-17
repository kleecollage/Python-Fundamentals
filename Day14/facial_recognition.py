import cv2
import face_recognition as fr

# Load Images
photo_control = fr.load_image_file("FotoA.jpg")
photo_test = fr.load_image_file("FotoC.jpg")

# Transform images to RGB
photo_control = cv2.cvtColor(photo_control, cv2.COLOR_BGR2RGB)
photo_test = cv2.cvtColor(photo_test, cv2.COLOR_BGR2RGB)

# Locate face control
locate_face_a = fr.face_locations(photo_control)[0]
coded_face_a = fr.face_encodings(photo_control)[0]
locate_face_b = fr.face_locations(photo_test)[0]
coded_face_b = fr.face_encodings(photo_test)[0]

# Show rectangles
print(locate_face_a)
cv2.rectangle(photo_control, (locate_face_a[3], locate_face_a[0]), (locate_face_a[1], locate_face_a[2]), (0, 255, 0), 2)
print(locate_face_b)
cv2.rectangle(photo_test, (locate_face_b[3], locate_face_b[0]), (locate_face_b[1], locate_face_b[2]), (0, 255, 0), 2)

# Compare between 2 faces
result = fr.compare_faces([coded_face_a], coded_face_b, 0.6)
print(result)

# Distance measurement
distance = fr.face_distance([coded_face_a], coded_face_b)
print(distance)

# Show results
cv2.putText(photo_test,
            f'{result} {distance.round(3)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# Show images
cv2.imshow("Photo control", photo_control)
cv2.imshow("Photo test", photo_test)

# keep program alive
while True:
    # Close until q key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break