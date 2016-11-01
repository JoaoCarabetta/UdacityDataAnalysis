import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import plotly.plotly as py  # tools to communicate with Plotly's server
import plotly
import scipy.stats as st
plotly.tools.set_credentials_file(username='JoaoLuizCarabetta', api_key='8pckznjw6l')


def histogram(data, bins, offset=1, plotly_url=False):
    """
    Receives raw data and transforms into a histogram.
    It can take any set of data and make a single histogram.
    :param data: List of List of numbers
    :param bin_size: Number
    :param y: List of numbers
    :param range: list [range_min, range_max]
    :param offset: number
    :return:
    """

    # init graph
    histogram=plt.figure()

    plt.hist(data, bins, alpha=0.5, normed=True)

    plt.show()

    if plotly_url:
        plot_url = py.plot_mpl(histogram, filename='docs/histogram-mpl-same')
        print plot_url

def histogram_density(data, bins):
    fig = plt.figure()

    # the histogram of the data
    plt.hist(data, bins, normed=1, alpha=0.5)

    # find minimum and maximum of xticks, so we know
    # where we should compute theoretical distribution
    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(data[0]))

    # Normal Distribution DataSet 1
    mean, standard_deviation = st.norm.fit(data[0])  # get mean and standard deviation
    pdf_g = st.norm.pdf(lnspc, mean, standard_deviation)  # now get theoretical values in our interval
    line1, = plt.plot(lnspc, pdf_g,
                      label="Normal\nMean: {}\nStd: {}".format(np.round(mean,2),
                                                                np.round(standard_deviation,2)),
                      color='blue')  # plot it

    # Normal Distribution DataSet 2
    mean, standard_deviation = st.norm.fit(data[1])  # get mean and standard deviation
    pdf_g = st.norm.pdf(lnspc, mean, standard_deviation)  # now get theoretical values in our interval
    line2, = plt.plot(lnspc, pdf_g,
                      label="Anormal\nMean: {}\nStd: {}".format(np.round(mean,2),
                                                                np.round(standard_deviation,2)),
                      color='green')  # plot it

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)

    # change x range
    plt.xlim([xmin, xmax + 3])
    plt.ylim([0, 0.16])

    # place legends
    first_legend = plt.legend(handles=[line1], loc=2)
    ax = plt.gca().add_artist(first_legend)
    plt.legend(handles=[line2], loc=1)

    # axis names and title
    fig.suptitle('Nomalized Histogram and Distribution', fontsize=20)
    plt.xlabel('Response Time', fontsize=18)
    plt.ylabel('Probability', fontsize=16)


    plt.savefig('fig/norm_hist.png', bbox='tight')
    # plot_url = py.plot_mpl(fig, filename='docs/histogram-mpl-legend')


