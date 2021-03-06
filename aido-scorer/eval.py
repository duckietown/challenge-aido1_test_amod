#!/usr/bin/env python

import duckietown_challenges as dc

cie = dc.ChallengeInterfaceEvaluatorConcrete()

previous = 'step1-simulation'
assert previous in cie.get_completed_steps()

# I can access artefacts from step1
fn = cie.get_completed_step_evaluation_file(previous, 'aidoScoresIntg.csv')


from read_scores import read_scores_data
stats, scores = read_scores_data(fn)

status = 'success'
msg = None

cr = dc.ChallengeResults(status=status, msg=msg, scores=scores, stats=stats)

dc.declare_challenge_results(None, cr)
