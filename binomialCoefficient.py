class BinomialCoefficient:

# Construct a Binomial Coefficient object
    def __init__(self, n, k):
        self.n = n
        self.k = k

#Define a method that will calculate the Binomial Coefficient
    def getBinomialCoefficient(self):
        nominator = 1
        denominator = 1
        x = self.n-(self.k)+1
        for n in range (x, (self.n)+1):
            nominator = nominator*n
        for k in range(1, (self.k)+1):
            denominator = denominator*k
        return nominator/denominator
    
# Define a method for a Bernoulli Trial

    def bernoulliTrial(self, p):
        return (self.getBinomialCoefficient())*(p**(self.k))*((1-p)**(self.n-self.k))
    
# Define a method to add color schema to our DataFrame

def gradient_color(val):
    r = 0
    g = 0
    b = 0
    return f'background-color: rgb({r},{g},{b})'