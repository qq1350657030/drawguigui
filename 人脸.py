import face_recognition

# Load the known faces
known_faces = []
for filename in os.listdir("known_faces"):
    face = face_recognition.load_image_file("known_faces/" + filename)
    known_faces.append(face_recognition.face_encodings(face)[0])

# Load the unknown face
unknown_face = face_recognition.load_image_file("unknown_face.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_face)[0]

# Compare the unknown face to the known faces
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# Print the results
for result in results:
    if result:
        print("The unknown face is a match for " + known_faces[results.index(result)].name)
    else:
        print("The unknown face is not a match for any known faces.")
