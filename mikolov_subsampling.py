from collections import Counter
import random



threshold = 1e-5
word_counts = Counter(int_words)
total_count = len(int_words)
freqs = {word: count/total_count for word, count in word_counts.items()}
p_drop = {word: 1 - np.sqrt(threshold/freqs[word]) for word in word_counts}
train_words = [word for word in int_words if random.random() < (1 - p_drop[word])]




def maybe_download(filename, expected_bytes):
	local_filename = os.path.join(gettempdir(), filename)
	if not os.path.exists(local_filename):
		local_filename, _ = urllib.request.urlretrieve(url + filename,
		                                               local_filename)
	statinfo = os.stat(local_filename)
	if statinfo.st_size == expected_bytes:
		print('Found and verified', filename)
	else:
		print(statinfo.st_size)
		raise Exception('Failed to verify ' + local_filename +
	        	        '. Can you get to it with a browser?')
	return local_filename