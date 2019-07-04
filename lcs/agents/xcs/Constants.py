class Constants:

    # N
    #   The maximum size of the population
    #   (the sum of the classifier numerosities in micro-classifiers)
    #   Recommended: large enough
    n = 400

    # beta
    #   The learning rate for updating fitness, prediction, prediction error, and
    #   action set size estimate in XCS's classifiers
    #   Recommended: 0.1-0.2
    beta = 0.2

    # alpha
    #   The fall of rate in the fitness evaluation
    #   Recommended: 0.1
    alpha = 0.1

    # epsilon_0
    #   The error threshold under which the accuracy of a classifier is set to one
    #   Recommended: 1% of the maximum reward
    epsilonZero = 10

    # nu
    #   The exponent in the power function for the fitness evaluation
    #   Recommended: 5
    nu = 5

    # gamma
    #   The discount rate in multi-step problems
    #   Recommended: 0.71
    gamma = 0.71

    # theta_GA
    #   The threshold for the GA application in an action set
    #   Recommended: 25-50
    thetaGA = 25

    # chi
    #   The probability of applying crossover
    #   Recommended: 0.5-1.0
    chi = 0.8

    # mu
    #   The probability of mutating one allele and the action
    #   Recommended: 0.01-0.05
    mu = 0.04

    # theta_del
    #   The experience threshold over which the fitness of a classifier may be
    #   considered in its deletion probability
    #   Recommended: 20
    thetaDel = 20

    # delta
    #   The fraction of the mean fitness of the population below which the fitness
    #   of a classifier may be considered in its vote for deletion
    #   Recommended: 0.1
    delta = 0.1

    # theta_sub
    #   The experience of a classifier required to be a subsumer
    #   Recommended: 20
    thetaSub = 20

    # tau
    #   The tournament size for selection [Butz et al., 2003]
    #   (set "0" to use the roulette-wheel selection)
    tau = 0.0

    # P_sharp
    #   The probability of using a don't care symbol in an allele when covering
    #   Recommended: 0.33
    dontCareProbability = 0.33

    # p_I
    #   The initial prediction value when generating a new classifier
    #   Recommended: very small (essentially zero)
    initialPrediction = 0.01

    # epsilon_I
    #   The initial prediction error value when generating a new classifier
    #   Recommended: very small (essentially zero)
    initialEpsilon = 0.01

    # F_I
    #   The initial fitness value when generating a new classifier
    #   Recommended: very small (essentially zero)
    initialFitness = 0.01

    # p_explr
    #   The probability during action selection of choosing the action uniform
    #   randomly
    #   Recommended: 0.5 (depends on the type of experiment)
    exploreProbability = 1.0

    # theta_mna
    #   The minimal number of actions that must be present in a match set [M],
    #   or else covering will occur
    #   Recommended: the number of available actions
    #                (or use "0" to set automatically)
    thetaMna = 0

    # doGASubsumption
    #   Whether offspring are to be tested for possible logical subsumption by
    #   parents
    doGASubsumption = True

    # doActionSetSubsumption
    #   Whether action sets are to be tested for subsuming classifiers
    doActionSetSubsumption = True

    # doActionMutation
    #   Whether to apply the mutation to the action
    doActionMutation = True

    # useMAM
    #   Whether to use the moyenne adaptive modifee (MAM) for updating the
    #   prediction and the prediction error of classifiers
    useMAM = True
