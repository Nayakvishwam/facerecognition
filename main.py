from trainmodel import train_model, identify_faces
from capture import capture_faces


class Main:

    def main(self):
        print("Please give your id and ensure that it's number")
        user_id = int(input("Enter user ID: "))
        capture_faces(user_id)
        model = train_model()
        print("Start identify your faces")
        identify_faces(model)


obj = Main()
obj.main()