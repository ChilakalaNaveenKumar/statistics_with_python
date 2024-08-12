from collections import Counter
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution
import logging
from scipy.stats import binom

logging.basicConfig(level=logging.DEBUG)

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials  
    """
    
    #       A binomial distribution is defined by two variables: 
    #           the probability of getting a positive outcome
    #           the number of trials
    
    #       If you know these two values, you can calculate the mean and the standard deviation
    #       
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))
    
    #       
    
    def __init__(self, prob=.5, size=20):
        
        Distribution.__init__(self)
        self.p = prob
        self.n = size
        self.mean = self.calculate_stdev()
        self.stdev = self.calculate_stdev()
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p * self.n     
        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
        
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        
        self.n = len(self.data)
        self.p = self.data.count(1) / float(self.n)
        logging.info(f'p: {self.p}, n: {self.n}')
        return self.p, self.n
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        counter = Counter(self.data)
        plt.bar(x = list(counter.keys()), y = list(counter.values()))
        plt.xlabel('Traits')
        plt.ylabel(f'Flipped count: {self.n}, count of traits')
        plt.show()        
        
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        return math.comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        pdf_values = []
        for iter in range(0, self.n):
            pdf_values.append(self.pdf(iter))
        counter = Counter(pdf_values)    
        plt.bar(x = list(counter.keys()), y = list(counter.values()))
        plt.xlabel('Probability density function')
        plt.ylabel(f'Flipped count: {self.n}, density')
        plt.show()
        
        return list(counter.keys()), list(counter.values())
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
                
        result = Binomial()
        result.n = self.n + other.n
        result. p = self.p
        
        return result
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format
    
        return f'mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}'
