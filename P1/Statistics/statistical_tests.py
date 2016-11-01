import plots
import pandas as pd
import scipy.stats as st
import numpy as np

def descriptive_stats(set):

    mean = set.mean()
    standard_deviation = np.std(set)
    sample_size = set.size
    degrees_of_freedom = sample_size - 1

    return mean, standard_deviation, sample_size, degrees_of_freedom

def read_data(path):

    data = pd.read_csv(path)

    data = data.as_matrix()

    return data[:, 0], data[:, 1]

def t_critical(alpha, type, degrees_of_freedom):

    if type == 'two_tailed':
        return st.t.ppf(1 - alpha / 2, degrees_of_freedom)

    elif type == type == 'one_tailed_right':
        return st.t.ppf(1 - alpha, degrees_of_freedom)

    elif type == 'one_tailed_left':
        return - st.t.ppf(1 - alpha, degrees_of_freedom)

    else:
        print 'This option does not exist'

def hypothesis_test(t_crit, t_value, p_value, t_test_type):

    if t_test_type == 'one_tailed_right':

        if t_value > t_crit:
            print "Null Hypothesis rejected"

        else:
            print "Null Hypotheis Accepted"

    elif t_test_type == 'one_tailed_left':

        if t_value < t_crit:
            print "Null Hypothesis rejected"
        else:
            print "Null Hypotheis Accepted"

    elif t_test_type == 'two_tailed':

        if t_value < 0:
            if t_value < -t_crit:
                print "Null Hypothesis rejected"
            else:
                print "Null Hypotheis Accepted"
        else:
            if t_value > t_crit:
                print "Null Hypothesis rejected"
            else:
                print "Null Hypotheis Accepted"

    else:
        print 'This option does not exist'

    print "t_value = {}".format(t_value)
    print "t_critic = {}".format(t_crit)
    print "p_value is {}".format(p_value)

def dependent_test(path='dataProjeto.csv'):

    alpha = 0.05

    t_test_type = 'one_tailed_right'

    set_a, set_b = read_data(path)

    sample_size = len(set_a)
    print sample_size

    mean_a, standard_deviation_a = st.norm.fit(set_a)

    mean_b, standard_deviation_b = st.norm.fit(set_b)

    t_value, p_value = st.ttest_ind(set_b, set_a, equal_var=False)

    t_crit = t_critical(alpha, 'one_tailed_right', sample_size)

    hypothesis_test(t_crit,t_value, p_value, t_test_type)

    # plots.histogram_density([set_a, set_b], 10)


dependent_test()
