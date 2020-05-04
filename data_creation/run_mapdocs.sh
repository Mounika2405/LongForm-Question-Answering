for c in {0..88}
do
	python3 select_sentences_tfidf.py -sr_n 'explainlikeimfive' -sid $c -ns 15 -nc 1
done
