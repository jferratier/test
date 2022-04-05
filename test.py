#Ask a question and get a response
def ask_question():
    question = input("What is your question? ")
    return question

# Get size of the question
def get_size(question):
    size = len(question)
    return size

#Create an alpahbet list
def create_alphabet():
    alphabet = []
    for letter in range(65, 91): #65 is A, 91 is Z
        alphabet.append(chr(letter)) #chr(65) is A
    return alphabet 


#find the input by the user
def find_input(question, alphabet):
    input_list = []
    for letter in question:
        if letter in alphabet:
            input_list.append(letter)
    return input_list

# run script
def main():
    question = ask_question()
    size = get_size(question)
    alphabet = create_alphabet()
    input_list = find_input(question, alphabet)
    print(input_list)