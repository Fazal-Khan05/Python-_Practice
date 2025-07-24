# In a five-star restaurant review system (⭐️⭐️⭐️⭐️⭐️), the stars typically represent the different levels of satisfaction.

# But what does each of the stars mean?

# Start by creating a rating variable and set it equal to a decimal number.

# Make a rating system using an if/elif/else statement:

# rating greater than 4.5, print 'Extraordinary'
# rating greater than 4, print 'Excellent'
# rating greater than 3, print 'Good'
# rating greater than 2, print 'Fair'
# Everything else, print 'Poor'
rating = float(input("Enter your rating (0-5): "))
if rating > 4.5:
    print('The Rating is Extraordinary')
elif rating > 4:
    print('The Rating is Excellent')
elif rating > 3:
    print('The Rating is Good')
elif rating > 2:
    print('The Rating is Fair')
else:
    print('The Rating is Poor')
    
