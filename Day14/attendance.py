import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Create Data Base
path = 'Employees'
my_images = []
names_employees = []
list_employees = os.listdir(path)

for name in list_employees:
    current_image = cv2.imread(os.path.join(path, name))
    my_images.append(current_image)
    names_employees.append(os.path.splitext(name)[0])
print("Registered employees:", names_employees)

# Encode images
def encode(images):
    encoded_list = []
    for i, img in enumerate(images):
        # Transform to RGB
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Detect faces
        f_locations = fr.face_locations(image_rgb)
        if len(f_locations) > 0:
            # Encoded faces
            encoded = fr.face_encodings(image_rgb, f_locations)
            if len(encoded) > 0:
                encoded_list.append(encoded[0])
            else:
                print(f"Warning: Failed to encoded face on image: {i}.")
        else:
            print(f"Warning: No faces detected on image: {i}.")
    return encoded_list

list_employees_encoded = encode(my_images)
# print(len(list_employees_encoded)) <- Expected: 5

# Take an image from webcam
# capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) <- FOR WINDOWS
capture = cv2.VideoCapture(0)

# Record incomes
def record_income(person):
    file = open("record.csv", "r+")
    data_list = file.readlines()
    names_record = []
    for line in data_list:
        income = line.split(',')
        names_record.append(income[0])
    if person not in names_record:
        current_time = datetime.now()
        string_time =  current_time.strftime("%H:%M:%S")
        file.writelines(f"\n{person}, {string_time}")

# Keep cam alive
while True:
    # Read webcam frame
    success, image = capture.read()
    if not success:
        print("Error al capturar imagen.")
        break
    # Detect faces in frame
    face_locations = fr.face_locations(image)
    if len(face_locations) > 0:
        # Encoded detected face
        face_encod = fr.face_encodings(image, face_locations)
        # Compare face in employees list
        if len(face_encod) > 0:
            face_encod = face_encod[0]
            # Calc face distances
            face_distances = fr.face_distance(list_employees_encoded, face_encod)
            print("Face Distances:", face_distances)
            # Custom tolerance
            umbral = 0.6
            matches = face_distances <= umbral
            print("Matches:", matches)
            # Check if there is any match
            if any(matches):
                # Get face index with lower distance
                match_index = numpy.argmin(face_distances)
                name = names_employees[match_index]
            else:
                name = "UNKNOWN"
            # Show results in image
            for (top, right, bottom, left) in face_locations:
                if name != "UNKNOWN":
                    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            # Save person found
            record_income(name)
        else:
            print(f"Warning: Failed to encoded detected face")
    else:
        print(f"Warning: No faces detected on frame.")
    # Show frame in window
    cv2.imshow("Webcam", image)
    # Exit pressing 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Free webcam and close window
capture.release()
cv2.destroyAllWindows()













