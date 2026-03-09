import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

class slr_slope_simulator:


    def __init__(self, beta_0, beta_1, x, sigma, seed):
        self.beta_0 = beta_0
        self.beta_1 = beta_1
        self.sigma = sigma
        self.x = np.asarray(x)

        self.n = len(self.x)
        self.rng = np.random.default_rng(seed)
        self.slopes = []

    # Generate one dataset
    def generate_data(self):
        eps = self.rng.normal(0, self.sigma, self.n)
        y = self.beta_0 + self.beta_1 * self.x + eps
        return self.x, y

    # Fit simple linear regression and return slope
    def fit_slope(self, x, y):
        model = LinearRegression()
        model.fit(x.reshape(-1, 1), y)
        return model.coef_[0]

    # Run many simulations
    def run_simulations(self, n_sims):

        slopes = []

        for _ in range(n_sims):

            x, y = self.generate_data()
            slope_hat = self.fit_slope(x, y)

            slopes.append(slope_hat)

        self.slopes = np.array(slopes)

    # plot the sampling distribution
    def plot_sampling_distribution(self):

        if len(self.slopes) == 0:
            print("Call run_simulations() first!")
            return

        plt.hist(self.slopes, bins=20)
        plt.xlabel("Slope")
        plt.ylabel("Frequency")
        plt.show()

    def find_prob(self, value, sided):
        if len(self.slopes) == 0:
            print("Call run_simulations() first!")
            return

        if sided == "above":
            return np.mean(self.slopes > value)
        elif sided == "below":
            return np.mean(self.slopes < value)
        elif sided == "two-sided":
            return 2 * np.mean(np.abs(self.slopes) > abs(value))

        else:
            print("sided must be 'above', 'below', or 'two-sided'")


    @property
    def slope(self) -> float:
        """Return the mean of the simulated slopes"""
        if len(self.slopes) == 0:
            print("Call run_simulations() first!")
            return None

        return np.mean(self.slopes)


# Test the class and its methods
sim = slr_slope_simulator(beta_0 = 12,
                    beta_1 = 2,
                    x = np.array(list(np.linspace(start = 0, stop = 10, num = 11))*3),
                    sigma = 1,
                    seed = 10)

# call the run_simulations() without passing through argument -- should return error message
sim.run_simulations()

# run 10000 simulations
sim.run_simulations(10000)

# Plot the sampling distribution
sim.plot_sampling_distribution()

# Approximate the two-sided probability of being larger than 2.1
sim.find_prob(2.1,"two-sided")

# Print out the value of the simulated slopes
sim.slope
