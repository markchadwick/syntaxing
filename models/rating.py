from google.appengine.ext import db

class Rating(db.Model):
	num_votes = db.IntegerProperty(default=0)
	vote_total = db.FloatProperty(default=0.0)	
	
	def add_vote(self, vote):
	    """
	    Adds a vote 
	    """
	    self.vote_total += float(vote)
	    self.num_votes += 1
	    
	def get_rating(self):
	    """
	    Returns the rating
	    """
	    if self.num_votes > 0:
	        return self.vote_total / self.num_votes
	    else:
	        return -1
	    
	def __str__(self):
	    """
	    Gets the string representation
	    """
	    return str(self.get_rating())
	    
	    
	    
	