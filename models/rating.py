from google.appengine.ext import db

class HasRating():
    def rate(self, vote):
        """
        Adds a vote 
        """
        if self.vote_total is None:
            self.vote_total = 0.0
        if self.num_votes is None:
            self.num_votes = 0
        
        self.vote_total += float(vote)
        self.num_votes += 1
        self.score = self._get_rating()

    def _get_rating(self):
        """
        Returns the rating
        """
        if self.num_votes > 0:
            return self.vote_total / self.num_votes
        else:
            return -1
    rating = property(_get_rating)

    def __str__(self):
        """
        Gets the string representation
        """
        return str(self.get_rating())