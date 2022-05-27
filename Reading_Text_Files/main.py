def read_file_content(story):
    with open("story.txt") as f:
        contents = f.read()
        print(contents)
    read_file_content()
    return "Hello World"


#def count_words():
   # text = read_file_content("./story.txt")
    # [assignment] Add your code here

   # return {"as": 10, "would": 20}
