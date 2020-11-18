import numpy as np
import random
import copy


class EpsilonGreedy(object):
    def __init__(self, n_arms, epsilon, draw_count_list, conv_rate_list):
        self._n_arms = copy.copy(n_arms)
        self._epsilon = copy.copy(epsilon)
        self._draw_count_list = copy.copy(draw_count_list)
        self._conv_rate_list = copy.copy(conv_rate_list)

    @property
    def n_arms(self):
        return self._n_arms

    @n_arms.setter
    def n_arms(self, value):
        self._n_arms = value

    @property
    def epsilon(self):
        return self._epsilon

    @epsilon.setter
    def epsilon(self, value):
        self._epsilon = value

    @property
    def draw_count_list(self):
        return self._draw_count_list

    @draw_count_list.setter
    def draw_count_list(self, value):
        self._draw_count_list = value

    @property
    def conv_rate_list(self):
        return self._conv_rate_list

    @conv_rate_list.setter
    def conv_rate_list(self, value):
        self._conv_rate_list = value

    def select_arm(self, verbose=True):
        bias = (self.epsilon, 1 - self.epsilon)
        choices = ("head", "tail")
        coin_face = np.random.choice(choices, p=bias)
        if coin_face == "tail":
            if verbose is True:
                print("Selection method : exploit")
            max_conv_rate = max(self.conv_rate_list)
            max_conv_rate_index = self.conv_rate_list.index(max_conv_rate)
            max_conv_rate_arm = max_conv_rate_index
            return max_conv_rate_arm
        else:
            if verbose is True:
                print("Selection method : explore")
            random_arm = random.randrange(0, len(self.conv_rate_list))
            return random_arm
