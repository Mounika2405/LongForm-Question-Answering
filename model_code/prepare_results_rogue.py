import re
import argparse

hyp = []
ref = []

def prepare_data(results, hypotheses, references):

	with open(results) as f:
		text = f.readlines()
		# print(text)
		# print(len(re.findall('\n', text)))

	for i in text:
		if(i.startswith('D-')):
			hyp.append(i[i.rindex('\t') + 1 : -1])


		if(i.startswith('T-')):
			ref.append(i[i.rindex('\t') +1 : -1])


	with open(hypotheses, 'w') as f:
	    for item in hyp:
	        f.write("%s\n" % item)

	with open(references, 'w') as f:
	    for item in ref:
	        f.write("%s\n" % item)



if __name__ == '__main__':


	parser = argparse.ArgumentParser()
	parser.add_argument('-results', '--results')
	parser.add_argument('-hypotheses', '--hypotheses')
	parser.add_argument('-references', '--references')
	args = parser.parse_args()


	prepare_data(args.results, args.hypotheses, args.references)


