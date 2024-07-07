"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    6 words read

    >>> wf.random() in ["Waldo","Fido","Spot","Sparky","Felix","Montague"]
    True

    >>> wf.random() in ["Waldo","Fido","Spot","Sparky","Felix","Montague"]
    True

    >>> wf.random() in ["Waldo","Fido","Spot","Sparky","Felix","Montague"]
    True
    """
    def __init__(self,filename):
        """Initialize file reading class and open file"""
        self.filename=filename
        
      
        rdfile = open(filename)

        self.words = self.parse(rdfile)

        print(f"{len(self.words)} words read")
    def parse(self, rdfile):
        """Put rdfile into list"""

        return [w.strip() for w in rdfile]
    
    def random(self):
        """Get random word"""

        return random.choice(self.words)
class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder that omits comment lines and blank lines
    
    >>> swf = SpecialWordFinder("words2.txt")
    6 words read

    >>> swf.random() in ["Waldo","Fido","Spot","Sparky","Felix","Montague"]
    True

    >>> swf.random() in ["Waldo","Fido","Spot","Sparky","Felix","Montague"]
    True

    >>> swf.random() in ["Waldo","Fido","Spot","Sparky","Felix","Montague"]
    True
    """

    def parse(self, rdfile):
        """Filter out rdfile"""

        return [w.strip() for w in rdfile
                if w.strip() and not w.startswith("#")]