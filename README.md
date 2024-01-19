# sort-fssw
The Fastest Statistical Sorting in the West

# Statistics with randomized and non-deterministic algorithms in computer science

[Randomized Algorithms](https://link.springer.com/chapter/10.1007/978-3-662-04616-6_5)

Hypothesis: If we can describe the source of our data in some way, we may have knowledge on the most probably values coming from the source, their structure, sequence, or some other property of the data.

With modern computational power, we can simulate probably values coming from the source and try to come up with some knowledge about the source, instead of using analyitical solution to work the math and get to this knowledge. It is of course possible to do so, but computational angle giveas another view on the problem.

Let's look at the possibe distributions that our source can have (distribution meaning a set of all possible random variables):

- Binomial distribution: Data source providing only two output values - outcomes: 1 (yes - true); 0 (no - false)

Let's look at the applications in computer science:

- Sorting a list of numbers (array)

- Searching a list of numbers (array)

## Statistical inference

- **Estimate** parameters of our (random) data source with some **confidence**
- **Test hypotheses** of those estimated parameters

For example estimate proportion, we can estiamte the proportion of some values inside the whole population with certain confidence. What is the proportion of ones in the binomial distribution of our source, where we are confident 95%?

Another example estimate mean: is what is the mean value of data source with some confidence e.g. 95%?

Yet another example estimating the difference in parameter: what is the difference in estimate mean between two data source, with certain confidence e.g., 95%?

Confidence interval is made for parameters, not the statistics.

## Binomial (discrete) distribution

If our data source has a binomial distribution, we are observing two output values - outcomes: 1 (yes - true); 0 (no - false)

For such discrete values as 0 or 1 (or categorical values) we can calculate our proportion estimate with some confidence e.g. 95%. 
Confidence intervals are our best estimate p_hat + some margin of Error.
Estimate p_hat is our (unbiased) point estimate, and the confidence is scaled Estimated standard Errors, where the scale is a multiplier based on our desired confidence level (e.g., 95% confidence level is 0.05 significance).

### Evenly distributed binomial distribution - Equal chance probability - equaly weighted values

1 (yes - true) is just as likely as 0 (no - false).

We have two probabilities to work with. 

1. Either accept the data as-is sorted with 50% probability value being at a correct location, which allows us to search and sample our data with 50% probability (random solution). 

2. Or sort our data in absolutely correct places with 100% probability value being at a correct location, which allows us to search and sample our data with 100% probability (programming kind of solution).

#### Assumptions

- Assumption that we have a simple random sample - to get a reliable best estimate.

The representative sample of population where observatons have equal probability of beeing selected.

- Margin of Error - we need a large enough sample size

So that we can aproximate our sampling distribution with a normal curve, to get a more bell shape for a better aproximation. 
For our confidence intervals, we can say large enough is at least 10 each response outcomes.

#### Confidence and population proportion

We can ask a question 'What is the proportion of sucessful events 1 (yes - true)?' Our population is all the events, while our interest is the proportion. Desired confidence interval is 95%. Our best estimate is sucessful events divided by all events (sample size) and in this case should be around p_hat = 0.5. The Margin of Error is p_hat * 1.96 * Estimated standard Error.
Therefor, for our sample size of n, with 95% confidence the reasonable values that our population proportion of succesful events is estimated between p_hat +/- Margin of Error.
Remember that we still don't know the TRUE population proportion for all possible events in this distribution, we are just estimating the population proportion.
So it would be wrong to claim that there is a 95% chance that the TRUE population proportion is lying within our computed interval. 95% confidence is the confidence in our procedure for estimating this parameter.

We can bootstrap this estimation for multiple iterations and if we calculate how many times our calculated interval will contain the TRUE population proportion, it will be 95% of the time. We are therfore confident that we can catch that TRUE population proportion 95% of the times in our calculation method. From now on we can play around with scaling how confident we want to be in our calculations.

There is a way to be very conservative and confident by using a fixed Estimated standard Error with p_hat = 0.5, so that our 95% Margin of Error depends only on our sample size n (i.e., 1 / sqr(n)) and 95% scale of 1.96. 
From this idea, we can calcuate the sample size we need for a specific confidence and at most the Margin of Error n = (confidence scale / (2 * MoE))^2 (e.g., 3% MoE and 99% confidence 2.576 and 0.03; n >= 1844).

### Unevenly distributed binomial distribution - Equal chance probability - equaly weighted values

1 (yes - true) has certain proabbility of occuring, which is not as likely as 0 (no - false).

We have as-is givent (true) probability to work with. 

1. Either accept the data as-is with certain probability value being at a correct location, which allows us to search and sample our data with that probability (random solution). 

2. Or we can fully sort our data so values get to thier respective places with 100% probability value being at a correct location, which allows us to search and sample our data with 100% probability (programming kind of solution).

3. Not to be blind about this probability, we can sample our distribution and try to guess (estimate) this data source probability. Or we can sort our data using this estimated probability so values get to thier respective places with ~100% probability value being at a correct location, which allows us to search and sample our data with ~100% probability. 

  -  But there is a problem: becouse we are actually guessing (estimating) the givent (true) probability of the data source - how certain we are that our estimation was correct (true probability). Well, we can sample our distribution, and the greaater amount of the samples we use will increase our confidence that we have estimated the correct (true) probability.

#### Assumptions

- Assumption that we have a simple random sample - to get a reliable best estimate.

The representative sample of population where observatons have equal probability of beeing selected.

- Margin of Error - we need a large enough sample size

So that we can aproximate our sampling distribution with a normal curve, to get a more bell shape for a better aproximation. 
For our confidence intervals, we can say large enough is at least 10 each response outcomes.

#### Confidence and population proportion

We can ask a question 'What is the proportion of sucessful events 1 (yes - true)?' Our population is all the events, while our interest is the proportion. Desired confidence interval is 95%. Our best estimate is sucessful events divided by all events (sample size) and in this case should be around p_hat = binomial distribution. The Margin of Error is p_hat * 1.96 * Estimated standard Error.
Therefor, for our sample size of n, with 95% confidence the reasonable values that our population proportion of succesful events is estimated between p_hat +/- Margin of Error.
Remember that we still don't know the TRUE population proportion for all possible events in this distribution, we are just estimating the population proportion.
So it would be wrong to claim that there is a 95% chance that the TRUE population proportion is lying within our computed interval. 95% confidence is the confidence in our procedure for estimating this parameter.

We can bootstrap this estimation for multiple iterations and if we calculate how many times our calculated interval will contain the TRUE population proportion, it will be 95% of the time. We are therfore confident that we can catch that TRUE population proportion 95% of the times in our calculation method. From now on we can play around with scaling how confident we want to be in our calculations.
  
There is a way to be very conservative and confident by using a fixed Estimated standard Error with p_hat = 0.5, so that our 95% Margin of Error depends only on our sample size n (i.e., 1 / sqr(n)) and 95% scale of 1.96. 
From this idea, we can calcuate the sample size we need for a specific confidence and at most the Margin of Error n = (confidence scale / (2 * MoE))^2 (e.g., 3% MoE and 99% confidence 2.576 and 0.03; n >= 1844).

## Two proportions comparison

### Assumptions

- large enough sample sizes

- Two independent random samples 

We can compare two proportions to find the difference in two different sample proportions (p1 - p2).
We can construct our 95% confidence interval with Estimated standard error (for p1 and p2) e.g. p1 = 0.5 and p2 = 0.15, scale 1.96 and calculater EsE.
Very similar with One sample, but corrected for the difference in population proportion.

If zero 0 is contained in the calculated intervals, them we canot state that there is a difference. If zero  is not included, than the population proportions are different.

## Uniform (continuous) distribution - Equal chance probability - equalyt likely for event to occure - equaly weighted values

Using real numbers where every value has a certain change of occuring (for uniform distributions all values have the same change probability of occuring). 

## Normal (continuous) distribution - Gaussian distribution - Bell curve

True mean of the distribution is the value that has the highest probability to occur in our disctribution, with other values diminishing probability as they more away from this mean on eaither side (described by the true standard deviation from that mean). How wide are the values spread out from the mean is defined by true variance, and are direcly related to the true standard devition from the mean.

We need to guess (eestimate) there parameters of our normal distribution by sampling our distribution, to try and guess the true values. Number of samples defines how confident are we in our guess eastimation.

We can also to partialy guess (eestimate) there parameters of our normal distribution by sampling our data, to try and partialy guess the true values. Number of subsamples from our data defines how confident are we in our partial guess eastimation.

The most likely probable value in our distribution is called the central tendency, and we can define it in three ways: mode, median or mean. Spread of values in our disctribution is the variance of our distribution, and we can define it in two ways: standard deviation and intequartile range.

Tails of our distribution also have a certain shape - which we can estimate from our sample distribution using the Kurtosis method (or even partialy estimate from our subsample distribution). Negative values means that the tail is more flat than a standard noramal distribution, and positive values means that the tail is more peaky than a standard normal distribution.

Peak of of our distribution (most probable value) can be shifted to one or the other side of the central tendency of a standard normal distribution - which we can estimate from our sample distribution using the Skew method (or even partialy estimate from our subsample distribution).

### Standard deviation

Defines how distant are the data values from the mean.

### Chi squared distribution

Chi squared distribution is left squed and has only one parameter called the degrees of freedom. Degrees of freedom are related to the number of samples that we take from our normal distribution.

As we incresase our number of samples (degrees of freedom), the left squed peak value of our sample distribution starts moving towards the central tendency of a standard normal disstribution.

## Bimodal distributions - Gaussina mixture models

They have two peak values and can be modeled using two normal distributions. 

Useful when clustering the data.

## Hypothesis Testing

We can test many of our assumptions as hypotheses using statistical tests. 
One example is to test if the mean of two distribution samples is significanlty different from eachother. 
This way we can check if two sample sets came from the same distribution? 