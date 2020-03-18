# These are the emails you will be censoring.
#The open() function is opening the text file that the emails are contained in
#and the .read() method is allowing us to save their contexts to the following
#variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#EMAIL ONE

#Write a function that can censor a specific word or phrase
#from a body of text, and then return the text.

def redact_phrase(email,word):
    phrase_instances = [word,word.upper(),word.lower(),word.title()]
    ammended_email = email
    for instance in phrase_instances:
        redaction = "*"*len(instance)
        ammended_email = ammended_email.replace(instance,redaction)
    return ammended_email


#print(email_one)
#print(redact_phrase(email_one,"learning algorithms"))

#EMAIL TWO
#Write a function that can censor not just a specific word or
#phrase from a body of text, but a whole list of words and phrases,
#and then return the text.
proprietary_terms = ["she", "personality matrix", "sense of self",
"self-preservation", "learning algorithm", "herself", "her", "Helena"]

def redact_terms(email,terms):
    ammended_email=email
    for term in terms:
        ammended_email = redact_phrase(ammended_email,term)
    return ammended_email

#print(email_two)
#print(redact_terms(email_two,proprietary_terms))


#EMAIL THREE

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming",
"alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful",
"broken", "damage", "damaging", "dismal", "distressed", "distressed",
"concerning", "horrible", "horribly", "questionable"]

test = """Hi so i am really concerned about this new knife behind my back.\n \nlike really upset, more concerned than you could believe.\n \nI am really unhappy working here. This is making me very distressed distressed distressed \n distressed distressed
distressed"""



def redact_and_relax(email,terms,negatives):
    #removes any proprietary terms
    ammended_email=email
    for term in terms:
        ammended_email = redact_phrase(ammended_email,term)
    #counts negative term occurance to relax language if necessary
    count = 0
    email_paragraphs = ammended_email.split("\n")
    email_lines = []
    for para in email_paragraphs:
        email_lines.append(para.split(" "))
    #print(email_lines)
    for words in email_lines:
        #print(words)
        for word in words:
            if word in negatives :
                count +=1
                if count > 2:
                    words[words.index(word)] = redact_phrase(word,word)
                email_lines[email_lines.index(words)] = words

    new_lines=[]
    for words in email_lines:
        new_line = " ".join(words)
        new_lines.append(new_line)
    new_para = "\n".join(new_lines)
    return new_para




print(redact_and_relax(test,proprietary_terms,negative_words))
