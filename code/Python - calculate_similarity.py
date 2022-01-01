import io
import os
import csv
import sys 


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def Jaccard_Similarity(doc1, doc2): 
    
    # List the unique words in a document
    words_doc1 = set(doc1.lower().split()) 
    words_doc2 = set(doc2.lower().split())
    
    # Find the intersection of words list of doc1 & doc2
    intersection = words_doc1.intersection(words_doc2)

    # Find the union of words list of doc1 & doc2
    union = words_doc1.union(words_doc2)
        
    # Calculate Jaccard similarity score 
    # using length of intersection set divided by length of union set
    return float(len(intersection)) / len(union)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]
	
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))	

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]
	
	
#print(Jaccard_Similarity(doc_1,doc_2))
#print(cosine_sim(doc_1,doc_2))
	
	

# Use NLP to calculate different similarity between all image analysis result and the text response from dataset
# Should use a method to handle row index and the append

script_dir = os.path.dirname(__file__)

header = ['Text','JudgesBin','face','high_relate_text','low_relate_text','label','logo','high_relate_obj','low_relate_obj','guess_label','high_relate_entities','low_relate_entities']
header1_ = ['coordinating conjunction','cardinal digit','determiner','existential there','preposition','adjective','modal','noun','predeterminer','possessive ending ','personal pronoun','adverb','particle','infinite marker','interjection','verb','wh-determiner','wh- pronoun','wh- adverb','other']
header1 = ['word_count','stop_word_count','special_char_count']
header2 = ['face_j','face_c','high_relate_text_j','high_relate_text_c','low_relate_text_j','low_relate_text_c','label_j','label_c','logo_j','logo_c','high_relate_obj_j','high_relate_obj_c']
header3 = ['low_relate_obj_j','low_relate_obj_c','guess_label_j','guess_label_c','high_relate_entities_j','high_relate_entities_c','low_relate_entities_j','low_relate_entities_c']

header.extend(header1_)
header.extend(header1)
header.extend(header2)
header.extend(header3)
rows = []
with open('./creative_test_data.csv', encoding = 'cp850') as csvfile, open('./output_1.csv', 'w', encoding = 'cp850', newline='') as write_obj:
	reader = csv.reader(csvfile, delimiter=',') 
	
	csv_writer = csv.writer(write_obj)
	csv_writer.writerow(header)
	
	header = []
	header = next(reader)
	#print(header)
	
	for row in reader:
		#print (row)
		
		text_info = []
		text_response = row[0]
		
		
		alphabets,num,special,space=0,0,0,0;#variable declaration and initilization 
		for i in range(len(text_response)): 
		  if(text_response[i].isalpha()): #check Alphabets letters 
			  alphabets+=1 
		  elif(text_response[i].isdigit()):#check numeric value 
			  num+=1 
		  elif(text_response[i].isspace()):#check space 
			  space+=1 
		  else: 
			  special+=1 
		
		
		text_tokens = word_tokenize(text_response)
		tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

		#ref https://www.guru99.com/pos-tagging-chunking-nltk.html

		cc = []
		cd = []
		det = []
		ex = []
		ins = []
		adj = []
		md = []
		nouns = []
		pdt = []
		pos_count = []
		prp = []
		adv = []
		rp = []
		to = []
		uh = []
		verb = []
		wdt = []
		wp = []
		wrb = []
		other = []
		
		for (word, pos) in nltk.pos_tag(text_tokens):
			
			if(pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS'):
				nouns.append(word)
			elif(pos == 'CC'):
				cc.append(word)
			elif(pos == 'CD'):
				cd.append(word)
			elif(pos == 'DT'):
				det.append(word)
			elif(pos == 'EX'):
				ex.append(word)
			elif(pos == 'IN'):
				ins.append(word)
			elif(pos == 'JJ' or pos == 'JJR' or pos == 'JJS'):
				adj.append(word)
			elif(pos == 'MD'):
				md.append(word)
			elif(pos == 'PDT'):
				pdt.append(word)
			elif(pos == 'POS'):
				pos_count.append(word)
			elif(pos == 'PRP' or pos == 'PRP$'):
				prp.append(word)
			elif(pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
				adv.append(word)
			elif(pos == 'RP'):
				rp.append(word)
			elif(pos == 'TO'):
				to.append(word)
			elif(pos == 'UH'):
				uh.append(word)
			elif(pos == 'VB' or pos == 'VBG' or pos == 'VBD' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ'):
				verb.append(word)
			elif(pos == 'WDT'):
				wdt.append(word)
			elif(pos == 'WP'):
				wp.append(word)
			elif(pos == 'WRB'):
				wrb.append(word)
				
				
			else:
				other.append(word)
			
	
		row.extend([len(cc),len(cd),len(det),len(ex),len(ins),len(adj),len(md),len(nouns),len(pdt),len(pos),len(prp),len(adv),len(rp),len(to),len(uh),len(verb),len(wdt),len(wp),len(wrb),len(other)])
		
		stop_word_number = len(text_tokens)-len(tokens_without_sw)
		
		
		#word count
		row.append(len(text_tokens))
		#stop word count
		row.append(stop_word_number)
		#special char count
		row.append(special)
		
		
		tokens_without_sw = ' '.join(tokens_without_sw)

		face_text = row[2]
		if face_text == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,face_text),cosine_sim(tokens_without_sw,face_text)])
		
		high_relate_text = row[3]
		if high_relate_text == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,high_relate_text),cosine_sim(tokens_without_sw,high_relate_text)])
		

		low_relate_text = row[4]
		if low_relate_text == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,low_relate_text),cosine_sim(tokens_without_sw,low_relate_text)])
			

		label = row[5]
		if label == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,label),cosine_sim(tokens_without_sw,label)])
			
			
		logo = row[6]
		if logo == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,logo),cosine_sim(tokens_without_sw,logo)])
			
		high_relate_obj = row[7]
		if high_relate_obj == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,high_relate_obj),cosine_sim(tokens_without_sw,high_relate_obj)])
			
			
		low_relate_obj = row[8]
		if low_relate_obj == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,low_relate_obj),cosine_sim(tokens_without_sw,low_relate_obj)])
			
		guess_label = row[9]
		if guess_label == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,guess_label),cosine_sim(tokens_without_sw,guess_label)])
			
			
		high_relate_entities = row[10]
		if high_relate_entities == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,high_relate_entities),cosine_sim(tokens_without_sw,high_relate_entities)])
			
		low_relate_entities = row[11]
		if low_relate_entities == '':
			row.extend([0,0])
		else:
			row.extend([Jaccard_Similarity(tokens_without_sw,low_relate_entities),cosine_sim(tokens_without_sw,low_relate_entities)])
		
		
		csv_writer.writerow(row)

csvfile.close()
write_obj.close()
#sys.exit()