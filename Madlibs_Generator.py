
class madlibsGenerator:
    def main(self)->None:
        with open("story.txt", 'r') as file:
            story = file.read()
        print(story)

        words = set()
        start_of_word = -1

        starting = "<"
        ending = ">"

        for i, char in enumerate(story):
            if char == starting:
                start_of_word = i
            if char == ending and start_of_word != -1:
                words.add(story[start_of_word: i+1])
        
        print("Input a word for each empty space in story: ")

        answer = {}
        for word in words:
            answer[word] = input(f"Enter a word for {word} : ")
        
        for word in words:
            story = story.replace(word, answer[word])
        
        print(story)

if __name__ == "__main__":
    story = madlibsGenerator()
    story.main()