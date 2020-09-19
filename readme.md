Empirical logic to find summary
Split the sentences and use the first sentence and find top 3 sentences with maximum num of words among the rest
Document Summarization
	- preprocessor.py
		Class ProcessDoc
			Functions
			- special char
			- token
			- stopword removal
	- summarizer.py
		Class SummarizeDoc
			Functions
			- splitter
			- firstSentExtractor
			- findNumWords
			- findTop3Sent
			- sentenceCombiner