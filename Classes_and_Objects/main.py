class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        print("name :", name,"\n" "age :", age,"\n" "tracks :", tracks,"\n" "score :", score)
    
    def change_name(self, name):
        self.name = name
        print("New name is :", name)
    def change_age(self, age):
        self.age = age
        print("New age is :", age)
    def add_track(self, track):
        self.track = track
        print("students' track is :", track)
    def get_score(self, score):
        self.score=score
        print("stuents' score is:", score)
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print()
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(700.00)