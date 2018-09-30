invitees = ['bill gates', 'steve jobs', 'meg whitman', 'indira noori']

# hmmm we see the print function acting up here... python 2 vs python 3

print "Dear " + invitees[0].title() + ", you are cordially invited to dinner with the Queen."
print("Dear " + invitees[1].title(), ", you are cordially invited to dinner with the Queen.")
print("Dear " + invitees[2].title(), ", you are cordially invited to dinner with the Queen.")
print("Unfortunately " + invitees[3].title(), "can't make it.")

invitees.append('anderson cooper')
invitees.remove('indira noori')
print(invitees)

print "Dear " + invitees[0].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[1].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[2].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[3].title() + ", you are cordially invited to dinner with the Queen."


print "--------"
print("We found a bigger table, so we're inviting more cool folks.")

# use insert() to add one new guest to the beginning of your list
invitees.insert(0, 'munroe bergdorf')

# use insert() to add one new guest to the middle of your list
invitees.insert(3, 'hillary clinton')

# use append to add one new guest to the end of your list
invitees.append('dick cheney')


print "Dear " + invitees[0].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[1].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[2].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[3].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[4].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[5].title() + ", you are cordially invited to dinner with the Queen."
print "Dear " + invitees[6].title() + ", you are cordially invited to dinner with the Queen."


print "------\nOh no, the new table won't arrive in time! We only have space for two guests, now."

print "Dear " + invitees.pop().title() + ", \nUnfortunately we have to cancel for dinner. So sorry!"
print "Dear " + invitees.pop().title() + ", \nUnfortunately we have to cancel for dinner. So sorry!"
print "Dear " + invitees.pop().title() + ", \nUnfortunately we have to cancel for dinner. So sorry!"
print "Dear " + invitees.pop().title() + ", \nUnfortunately we have to cancel for dinner. So sorry!"
print "Dear " + invitees.pop().title() + ", \nUnfortunately we have to cancel for dinner. So sorry!"
print "-----"
print "Dear " + invitees[-1].title() + ", \nYou may have heard some people couldn't come, but you're still invited."
print "Dear " + invitees[0].title() + ", \nYou may have heard some people couldn't come, but you're still invited."

#how many people are invited to dinner?
print "There are " + str(len(invitees)) + " guests attending dinner."

# clear the guest list
#del invitees[1]
#del invitees[0]
#print(invitees)