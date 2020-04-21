#Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
#It should return a list in which the first value should be letter count and second value should be digit count. 
#Ignore the spaces or any other special character in the sentence.

#lex_auth_0127135838317445121147

def count_digits_letters(sentence):
    #start writing your code here
    nums = 0 
    letters = 0 
    x = sentence 
    
    for i in x:
        if i.isalpha():
            letters += 1 
        elif i.isdigit():
            nums += 1 
    return letters, nums

    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
