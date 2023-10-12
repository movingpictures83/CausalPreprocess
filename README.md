# CausalPreprocess
# Language: Python
# Input: TXT
# Output: DIR
# Tested with: PluMA 1.1, Python 3.6
# Dependency: pandas==1.1.5, pycausal==1.2.1

PluMA plugin to run perform a preprocessing step for causal networks,
by filtering on the union of two sets of taxa

Input is a TXT file of tab-delimited keyword-value pairs:
inputdir: Input directory
mimosafile: Taxa to keep
top50file: Most abundant taxa

Output is a filtered data set in the user-specified folder
