def latest(scores):
    return scores[len(scores) - 1 ]


def personal_best(scores):
    copyScores = scores.copy()
    copyScores.sort(reverse=True)
    return copyScores[0]


def personal_top_three(scores):
    copyScores = scores.copy()
    copyScores.sort(reverse=True)
    return copyScores[0:3]
