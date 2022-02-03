# Assume, you have been given a tuple with details about books that won the Good Reads Choice Awards.

# Write a Python program that prints the award category, the book name, and its total votes earned as shown below.

# [Must use Tuple unpacking for printing and need to handle the quotation marks as a part of the output]

# ===================================================================

# Output:
# The Silent Patient won the 'Best Mystery & Thriller' category with 68821 votes
# The Institute won the 'Best Horror' category with 75717 votes
# The five won the 'Best History & Biography' category with 31783 votes
# The Testaments won the 'Best Fiction' category with 98291 votes

# ===================================================================

book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)

for b_info in book_info:
    (category, book, votes) = b_info
    print("The "+ book + " won the '"+ category + "' category with " + str(votes) +" votes")
    