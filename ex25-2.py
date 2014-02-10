import ex25

sentence = "All good things come to those who wait"
words = ex25.break_words(sentence)
print words

print "---------------------"
sorted_words = ex25.sort_words(words)
print sorted_words

print "---------------------"
print ex25.print_first_word(words)
print ex25.print_last_word(words)

print "---------------------"
print ex25.print_first_word(sorted_words)
print ex25.print_last_word(sorted_words)

print "---------------------"
sorted_words2 = ex25.sort_sentence(sentence)
print sorted_words2


print "---------------------"
print ex25.print_first_and_last(sentence)


print "---------------------"
print ex25.print_first_and_last_sorted(sentence)
