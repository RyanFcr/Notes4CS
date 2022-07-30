"""Typing test implementation"""


from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    valid_para = []
    for s in paragraphs:
        if select(s):
            valid_para.append(s)
            
    set1 = set(valid_para)
    if k >= len(set1):
        return ''
    return valid_para[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        s = split(remove_punctuation(lower(paragraph)))
        # print("Debug:s ",s)
        for ss in topic:
            # print("Debug:ss  ",ss)
            if ss in s:
                return True
        return False

    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    success = 0
    sum = 0
    len1 = len(reference_words)
    # print("Debug: typed_words",typed_words)
    if typed_words == []:
        return 0.0
    # print("Debug: len",len1)
    for s in typed_words:
        # print("Debug: s",s)
        if sum < len1:
            # print("Debug:referemce_words[sum]",reference_words[sum])
            if reference_words[sum] == s:
                success+=1
        sum +=1
    return success / sum *100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed)/5 * 60/ elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    min = diff_function(user_word,valid_words[0],limit)
    min_s= valid_words[0]
    if user_word in valid_words:
        return user_word
    else:
        for word in valid_words:
            if diff_function(user_word,word,limit)< min:
                min = diff_function(user_word,word,limit) 
                min_s = word
        if min > limit:
            return user_word
        else:
            return min_s
    # END PROBLEM 5



def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    
    def shifty_helper(start,goal,limit,result):
        if start == '':
            result += len(goal)
            # if result > limit:
            #     return limit
            return result         
        elif goal == '':
            result += len(start)
            # if result > limit:
            #     return limit
            return result
        else :
            if start[0] == goal[0]:
                return shifty_helper(start[1:],goal[1:],limit,result)
            else:
                result += 1
                if result > limit:
                    return limit + 1
                return shifty_helper(start[1:],goal[1:],limit,result) 
    
    
    return shifty_helper(start,goal,limit,0)
    # if start == '' :
    #     if len(goal) > limit:
    #         return limit + 1
    #     return len(goal)
    # elif goal == '':
    #     if len(start) > limit:
    #         return limit + 1
    #     return len(start)
    # else:
    #     if start[0] == goal[0]:
    #         result = shifty_shifts(start[1:],goal[1:],limit)
    #         if result > limit:
    #             return limit +1
    #         return result
    #     else:
    #         result = 1 + shifty_shifts(start[1:],goal[1:],limit)
    #         if result > limit:
    #             return limit +1
    #         return result
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    

    def paw_helper(start,goal,limit,result):
        if start == '' or goal == '':
            result += len(start)+len(goal)
            return result
        else:
            if start[0] != goal[0]:
                result+=1
                if result > limit:
                    return limit + 1
                add_diff = paw_helper(start,goal[1:],limit,result) # Fill in these lines
                # print("Debug: add",add_diff," Limit:",limit)
                remove_diff = paw_helper(start[1:],goal,limit,result)
                substitute_diff = paw_helper(start[1:],goal[1:],limit,result) 
                # print("Debug: remove",remove_diff," Limit:",limit)
                # print("Debug: substitute",substitute_diff," Limit:",limit)
                return min(add_diff,remove_diff,substitute_diff)
            else:
                return paw_helper(start[1:],goal[1:],limit,result)
 
    return paw_helper(start,goal,limit,0)

    # 两种方法都可以，上方是我的做法，引入一个helper来记录result，过大时提前中断，下面是做完后参考其他人的做法，利用limit减小，是我没有想到的
    #    
    # if limit < 0: # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     return 0
    #     # END
    # elif start == '': # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     return len(goal)
    #     # END
    # elif goal == '':
    #     return len(start)
    # else:
    #     if start[0] != goal[0]:
    #         add_diff = pawssible_patches(start,goal[1:],limit -1)+1 # Fill in these lines
    #         # print("Debug: add",add_diff," Limit:",limit)
    #         remove_diff = pawssible_patches(start[1:],goal,limit - 1) + 1
    #         substitute_diff = pawssible_patches(start[1:],goal[1:],limit - 1) + 1
    #         # print("Debug: remove",remove_diff," Limit:",limit)
    #         # print("Debug: substitute",substitute_diff," Limit:",limit)
    #         return min(add_diff,remove_diff,substitute_diff)
    #     else:
    #         return pawssible_patches(start[1:],goal[1:],limit )




def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    index = 0
    success = 0
    sum = len(prompt)
    for s in typed:
        if s == prompt[index]:
            success += 1
        else:
            break
        index += 1
    progress = success / sum
    report = {
        'id':user_id,
        'progress':progress,
    }
    send(report)
    return progress
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    
    time_list = []
    
    index1 = 0
    while index1 != len(times_per_player):
        # print("Debug:")
        index2 = 0
        list_helper = []
        while index2 != len(times_per_player[index1]) - 1:
            list_helper.append(times_per_player[index1][index2+1] - times_per_player[index1][index2] ) 
            index2 += 1
            print("Debug:index2",index2)
        time_list.append(list_helper)
        index1+=1
        print("Debug: index1",index1)
    return game(words,time_list)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    result_list=[]
    print("Debug:",player_indices)
    for index in player_indices:
        result_list.append([])
        print("Debug:",index)
        index += 1
    print("Debug:",result_list)
    for word_index  in word_indices:
        player_index = 0
        min = time(game,player_index,word_index)
        min_index = player_index
        for player_index in player_indices:
            if time(game,player_index,word_index) < min:
                min = time(game,player_index,word_index)
                min_index = player_index
        result_list[min_index].append(word_at(game,word_index))

    # END PROBLEM 10
    return result_list


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)