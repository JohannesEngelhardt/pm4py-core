from pm4py.objects.random_variables.normal.random_variable import Normal
from pm4py.objects.random_variables.uniform.random_variable import Uniform


class RandomVariable(object):
    def __init__(self):
        self.random_variable = None

    def read_from_string(self, distribution_type, distribution_parameters):
        """
        Read the random variable from string

        Parameters
        -----------
        distribution_type
            Distribution type
        distribution_parameters
            Distribution parameters splitted by ;
        """
        if distribution_type == "NORMAL":
            self.random_variable = Normal()
            self.random_variable.read_from_string(distribution_parameters)
        elif distribution_type == "UNIFORM":
            self.random_variable = Uniform()
            self.random_variable.read_from_string(distribution_parameters)

    def get_distribution_type(self):
        """
        Get current distribution type

        Returns
        -----------
        distribution_type
            String representing the distribution type
        """
        if self.random_variable is not None:
            return self.random_variable.get_distribution_type()

    def get_distribution_parameters(self):
        """
        Get a string representing distribution parameters

        Returns
        -----------
        distribution_parameters
            String representing distribution parameters
        """
        if self.random_variable is not None:
            return self.random_variable.get_distribution_parameters()

    def calculate_loglikelihood(self, values):
        """
        Calculate log likelihood

        Parameters
        ------------
        values
            Empirical values to work on

        Returns
        ------------
        likelihood
            Log likelihood that the values follows the distribution
        """
        if self.random_variable is not None:
            return self.random_variable.calculate_loglikelihood(values)

    def calculate_parameters(self, values, parameters=None):
        """
        Calculate parameters of the current distribution

        Parameters
        -----------
        values
            Empirical values to work on
        parameters
            Possible parameters of the algorithm

        """

        if parameters is None:
            parameters = {}

        debug_mode = parameters["debug"] if "debug" in parameters else False

        if self.random_variable is not None:
            self.random_variable.calculate_parameters(values)
        else:
            N = Normal()
            U = Uniform()
            N.calculate_parameters(values)
            U.calculate_parameters(values)
            likelihoods = []
            likelihoods.append([N, N.calculate_loglikelihood(values)])
            likelihoods.append([U, U.calculate_loglikelihood(values)])
            likelihoods = sorted(likelihoods, key=lambda x: x[1], reverse=True)

            if debug_mode:
                print("likelihoods = ",likelihoods)

            self.random_variable = likelihoods[0][0]


    def get_value(self):
        """
        Get a random value following the distribution

        Returns
        -----------
        value
            Value obtained following the distribution
        """
        if self.random_variable is not None:
            return self.random_variable.get_value()

    def __str__(self):
        """
        Returns a representation of the current object

        Returns
        ----------
        repr
            Representation of the current object
        """
        if self.random_variable is not None:
            return str(self.random_variable)
        else:
            return "UNINITIALIZED"

    def __repr__(self):
        """
        Returns a representation of the current object

        Returns
        ----------
        repr
            Representation of the current object
        """
        if self.random_variable is not None:
            return repr(self.random_variable)
        else:
            return "UNINITIALIZED"