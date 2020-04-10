

import textdistance

DISTANCE_CRITERIA = 2

def fix_space_apostrophe(sentence):
    try:   
        index = sentence.index(r"'")
        #print("index", index)
    except ValueError: # No apostrophe in the sentence
        return sentence

    s1 = sentence[:index]
    if s1[-1] == ' ':
        s1 = s1[:-1]
    s2 = sentence[(index+1):]
    return s1+"'"+s2
    
#print(fix_space_apostrophe("[/EN#255357/other Boy 's] are competing in [/EN#255359/other martial arts] ."))
# Still problem:
# "[/EN#249282/people A closeup of a child] [/EN#249287/bodyparts 's face] eating [/EN#249284/clothing a blue] , [/EN#249284/other heart] shaped [/EN#249284/other lollipop] ."

def fix_space_n_apostrophe_t(sentence):
    try:   
        index = sentence.index(r"n't")
        #print("index", index)
    except ValueError: # No apostrophe in the sentence
        return sentence

    s1 = sentence[:index]
    if s1[-1] == ' ':
        s1 = s1[:-1]
    s2 = sentence[(index+3):]

    return s1+r"n't"+s2

#print(fix_space_n_apostrophe_t("[/EN#252630/people A man] with [/EN#252638/other a disability] [/EN#0/notvisual who] does n't have [/EN#252635/bodyparts legs] is walking with [/EN#252633/people another man] [/EN#0/notvisual who] is entered into [/EN#252634/other a marathon] ."))


def match_sentence(target_sentence, sentence_with_annotation):
    """
    Arguments:
        target_sentence: string. Eg: "A group of men are loading cotton onto a truck."
        sentence_with_annotation: string. Eg1: "[/EN#568/people A group of people] stand in [/EN#571/vehicles the back of a truck] filled with [/EN#569/other cotton] ." --> False
                                          Eg2: "[/EN#568/people A group of men] are loading [/EN#569/other cotton] onto [/EN#570/vehicles a truck]"  --> True
    """
    target_sentence = fix_space_apostrophe(target_sentence)
    sentence_with_annotation = fix_space_apostrophe(sentence_with_annotation)

    target_sentence = fix_space_n_apostrophe_t(target_sentence)
    sentence_with_annotation = fix_space_n_apostrophe_t(sentence_with_annotation)
    
    wordlist1 = target_sentence.lower().replace(',', ' ').replace('.', ' ').split()
    wordlist2raw = sentence_with_annotation.lower().replace(',', ' ').replace('.', ' ').replace(']', ' ').split()
    wordlist2 = [elt for elt in wordlist2raw if elt[0] != '[']

    # return wordlist1==wordlist2 # Strict check on each word

    seq1 = ""
    for word in wordlist1:
        seq1 += word
    seq2 = ""
    for word in wordlist2:
        seq2 += word
    dis = textdistance.levenshtein.distance(seq1, seq2)
    if dis <= DISTANCE_CRITERIA:
        return True
    else:
        return False

#print(match_sentence("A group of men are loading cotton onto a truck.", "[/EN#568/people A group of men] are loading [/EN#569/other cotton] onto [/EN#570/vehicles a truck]"))  #--> True
#print(match_sentence("A group of men are loading cotton onto a truck.", "[/EN#568/people A group of people] stand in [/EN#571/vehicles the back of a truck] filled with [/EN#569/other cotton] ."))  #--> False

def match_sentence_among_5(target_sentence, sentences_filepath):
    """
    Return the index of matched sentence between 0 and 4
    """
    lines = []
    with open(sentences_filepath, 'r') as f:
        i = 0
        
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line)
            if match_sentence(target_sentence, line):
                return i
            i += 1

        print("\n----Following sentence not matched automatically----")
        print("Target sentence:", target_sentence[:-1]) # [:-1] is to remove \n 
        print("potential sentences path:", sentences_filepath)
        for l in lines:
            print(l[:-1]) 
        print()
        return -1
        

#print(match_sentence_among_5("A group of men are loading cotton onto a truck.", "/home/wenjian/Internship/data/flickr30kentities/annotations/Sentences/1018148011.txt"))  # --> 3
#print(match_sentence_among_5("Three girls make faces as one takes a drink while they stand in a busy street.", "/home/wenjian/Internship/data/flickr30kentities/annotations/Sentences/1130017585.txt")) # --> 1

def sentence_matching_processing(split_filepath, target_filepath, annotated_dirpath, index_outputpath, sentence_outputpath):
    with open(sentence_outputpath, 'w') as f_s_output:
        with open(index_outputpath, 'w') as f_output:
            with open(split_filepath, 'r') as f_split:
                with open(target_filepath, 'r') as f_target:
                    
                    while(True):
                        l_split = f_split.readline()
                        l_target = f_target.readline()
                        if not l_split:
                            break
                        image_id = l_split.split('.')[0] # Eg: 1018148011.jpg --> 1018148011
                        index = match_sentence_among_5(l_target, annotated_dirpath+image_id+'.txt')
                        f_output.write(str(index)+ '\n') 
                        with open(annotated_dirpath+image_id+'.txt') as f_annotated:        
                            f_s_output.write(f_annotated.readlines()[index])         
    print("sentence matching processing terminated.")

"""
# On validation set
sentence_matching_processing("/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/image_splits/val.txt",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/raw/val.en",
                                "/home/wenjian/Internship/data/flickr30kentities/annotations/Sentences/",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/outputs/sentence_match_index_en_val.txt",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/outputs/sentence_match_sentence_en_val.txt")
"""
"""
# On training set
sentence_matching_processing("/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/image_splits/train.txt",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/raw/train.en.utf8",
                                "/home/wenjian/Internship/data/flickr30kentities/annotations/Sentences/",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/outputs/sentence_match_index_en_train.txt",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/outputs/sentence_match_sentence_en_train.txt")
"""
# On test set
sentence_matching_processing("/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/image_splits/test_2016_flickr.txt",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/raw/test_2016_flickr.en",
                                "/home/wenjian/Internship/data/flickr30kentities/annotations/Sentences/",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/outputs/sentence_match_index_en_test.txt",
                                "/home/wenjian/Internship/data/flickr30kentities/Multi30k/task1/outputs/sentence_match_sentence_en_test.txt")

