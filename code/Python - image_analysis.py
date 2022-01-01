import io
import os
import csv
import sys 

from nltk.corpus import wordnet

# Imports the Google Cloud client library
from google.cloud import vision

# Special switch to alter the text result in each API return
replace = 1

##
# Get synonyms and antonyms for the input word 
# @String
# Output String, String
def get_synonyms(word, synonyms, antonyms):
	for syn in wordnet.synsets(word):
			for l in syn.lemmas():
				synonyms.append(l.name())
				if l.antonyms():
				 antonyms.append(l.antonyms()[0].name())
	return synonyms, antonyms


script_dir = os.path.dirname(__file__)

# Folder Path
path = "image"
  
# Change the directory
os.chdir(path)


# Instantiates a client
client = vision.ImageAnnotatorClient()


# Init Header for insert target CSV
header = ['image', 'face', 'high_relate_text', 'low_relate_text', 'label', 'logo', 'high_relate_obj', 'low_relate_obj','guess_label','high_relate_entities','low_relate_entities']

# Target CSV 
with open('../image_keyword.csv', 'w', encoding='UTF8') as f:

	writer = csv.writer(f)
	
	writer.writerow(header)

	# Iterate through all image file from image folder
	for file in os.listdir():
		all_keyword = [file]
		face_keyword = []
	   
		file_path = f"{path}\{file}"
		abs_file_path = os.path.join(script_dir, file_path)
	  
	  
		# Loads the image into memory
		with io.open(abs_file_path, 'rb') as image_file:
			content = image_file.read()

		# Use Vision API to analysis image and get results
		image = vision.Image(content=content)

		# Face Detection
		response = client.face_detection(image=image)
		faces = response.face_annotations
		
		# Default result and the result we want to keep
		likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')	
		keep_arr = ['POSSIBLE', 'LIKELY', 'VERY_LIKELY']
		
		# In this API request, only keep 4 face results, and only keep if the face expression is possible or above
		# also attach synonyms and antonyms
		synonyms = []
		antonyms = []
		for face in faces:
			if format(likelihood_name[face.anger_likelihood]) in keep_arr:
				face_keyword.append = 'anger'
				synonyms, antonyms = get_synonyms('anger', synonyms, antonyms)
			if format(likelihood_name[face.joy_likelihood]) in keep_arr:
				face_keyword.append = 'joy'
				synonyms, antonyms = get_synonyms('joy', synonyms, antonyms)
			if format(likelihood_name[face.surprise_likelihood]) in keep_arr:
				face_keyword.append = 'surprise'
				synonyms, antonyms = get_synonyms('surprise', synonyms, antonyms)
			if format(likelihood_name[face.sorrow_likelihood]) in keep_arr:
				face_keyword.append = 'sorrow'	
				synonyms, antonyms = get_synonyms('sorrow', synonyms, antonyms)
				
		face_keyword.extend(synonyms)	
		face_keyword.extend(antonyms)
		face_keyword = list(set(face_keyword))
		face_keyword_str = ' '.join(face_keyword)	
		
		if replace == 1:
			face_keyword_str = face_keyword_str.replace("_", " ")
		
		all_keyword.append(face_keyword_str)	
			
			
		#Text detection
		#Analysis if there any text could be identified in the image, based on the the confidence and put them into different group
		image_context = vision.ImageContext(language_hints=['en-t-i0-handwrit'])

		response = client.document_text_detection(image=image, image_context=image_context)

		high_relate_text = []
		low_relate_text = []
		high_relate_synonyms = []
		low_relate_synonyms = []
		high_relate_antonyms = []
		low_relate_antonyms = []
		
		for page in response.full_text_annotation.pages:
			for block in page.blocks:
				
				#print('\nBlock confidence: {}\n'.format(block.confidence))

				for paragraph in block.paragraphs:
					#print('Paragraph confidence: {}'.format(paragraph.confidence))

					for word in paragraph.words:
						word_text = ''.join([
							symbol.text for symbol in word.symbols
						])

						if word.confidence > 50:
							high_relate_text.append(word_text)
							high_relate_synonyms,high_relate_antonyms = get_synonyms(word_text, high_relate_synonyms, high_relate_antonyms)
						else:
							low_relate_text.append(word_text)
							low_relate_synonyms,low_relate_antonyms = get_synonyms(word_text, low_relate_synonyms, low_relate_antonyms)
							
	
		high_relate_text.extend(high_relate_synonyms)	
		low_relate_text.extend(low_relate_synonyms)	
		high_relate_text.extend(high_relate_antonyms)	
		low_relate_text.extend(low_relate_antonyms)	
		
		high_relate_text = list(set(high_relate_text))
		low_relate_text = list(set(low_relate_text))
		
		high_relate_text = ' '.join(high_relate_text)
		low_relate_text = ' '.join(low_relate_text)
		
		if replace == 1:
			high_relate_text = high_relate_text.replace("_", " ")
			low_relate_text = low_relate_text.replace("_", " ")
		
		all_keyword.append(high_relate_text)
		all_keyword.append(low_relate_text)
		
		
		#Label detect, identify if theres any label from the image
		response = client.label_detection(image=image)
		labels = response.label_annotations
		#print('Labels:')

		label_text = []
		label_synonyms = []
		label_antonyms = []
		
		for label in labels:
			label_text.append(label.description)
			label_synonyms, label_antonyms = get_synonyms(label.description, label_synonyms, label_antonyms)
			
		label_text.extend(label_synonyms)	
		label_text.extend(label_antonyms)		
		label_text = list(set(label_text))
		label_text = ' '.join(label_text)
		
		if replace == 1:
			label_text = label_text.replace("_", " ")

		all_keyword.append(label_text)
		
		
		
		#Logo detection, identify if theres any logo from the image
		response = client.logo_detection(image=image)
		logos = response.logo_annotations
		#print('Logos:')
		
		logo_text = []

		for logo in logos:
			logo_text.append(logo.description)
		logo_text = ' '.join(logo_text)

		all_keyword.append(logo_text)
		
		
		
		
		
		#Object detection, identify the object in the image
		
		high_relate_obj = []
		low_relate_obj = []
		high_relate_obj_synonyms = []
		low_relate_obj_synonyms = []
		
		high_relate_obj_antonyms = []
		low_relate_obj_antonyms = []
		
		objects = client.object_localization(image=image).localized_object_annotations

		for object_ in objects:
		
			if object_.score > 50:
				high_relate_obj.append(object_.name)
				high_relate_obj_synonyms, high_relate_obj_antonyms = get_synonyms(object_.name, high_relate_obj_synonyms, high_relate_obj_antonyms)
			else:
				low_relate_obj.append(object_.name)
				low_relate_obj_synonyms, low_relate_obj_antonyms = get_synonyms(object_.name, low_relate_obj_synonyms, low_relate_obj_antonyms)
		
		high_relate_obj.extend(high_relate_obj_synonyms)	
		low_relate_obj.extend(low_relate_obj_synonyms)	
		high_relate_obj.extend(high_relate_obj_antonyms)	
		low_relate_obj.extend(low_relate_obj_antonyms)	
		
		high_relate_obj = list(set(high_relate_obj))
		low_relate_obj = list(set(low_relate_obj))
		
		high_relate_obj = ' '.join(high_relate_obj)
		low_relate_obj = ' '.join(low_relate_obj)
		
		if replace == 1:
			high_relate_obj = high_relate_obj.replace("_", " ")
			low_relate_obj = low_relate_obj.replace("_", " ")

		all_keyword.append(high_relate_obj)
		all_keyword.append(low_relate_obj)

		
		#Web annotation detection
		response = client.web_detection(image=image)
		annotations = response.web_detection
		
		guess_label = []
		high_relate_entities = []
		low_relate_entities = []
		
		guess_label_synonyms = []
		high_relate_entities_synonyms = []
		low_relate_entities_synonyms = []
		
		guess_label_antonyms = []
		high_relate_entities_antonyms = []
		low_relate_entities_antonyms = []

		if annotations.best_guess_labels:
			for label in annotations.best_guess_labels:
				guess_label.append(label.label)
				guess_label_synonyms, guess_label_antonyms = get_synonyms(label.label, guess_label_synonyms, guess_label_antonyms)

	
		if annotations.web_entities:
			for entity in annotations.web_entities:
				if entity.score > 0.5:
					high_relate_entities.append(entity.description)
					high_relate_entities_synonyms, high_relate_entities_antonyms = get_synonyms(entity.description, high_relate_entities_synonyms, high_relate_entities_antonyms)
				else:
					low_relate_entities.append(entity.description)
					low_relate_entities_synonyms, low_relate_entities_antonyms = get_synonyms(entity.description, low_relate_entities_synonyms, low_relate_entities_antonyms)

	
		guess_label.extend(guess_label_synonyms)	
		high_relate_entities.extend(high_relate_entities_synonyms)	
		low_relate_entities.extend(low_relate_entities_synonyms)
		
		guess_label.extend(guess_label_antonyms)	
		high_relate_entities.extend(high_relate_entities_antonyms)	
		low_relate_entities.extend(low_relate_entities_antonyms)
		
		
		guess_label = list(set(guess_label))
		high_relate_entities = list(set(high_relate_entities))
		low_relate_entities = list(set(low_relate_entities))
		
		guess_label = ' '.join(guess_label)
		high_relate_entities = ' '.join(high_relate_entities)
		low_relate_entities = ' '.join(low_relate_entities)
		
		if replace == 1:
			guess_label = guess_label.replace("_", " ")
			high_relate_entities = high_relate_entities.replace("_", " ")
			low_relate_entities = low_relate_entities.replace("_", " ")
		
	
		all_keyword.append(guess_label)
		all_keyword.append(high_relate_entities)
		all_keyword.append(low_relate_entities)

		# write the data
		writer.writerow(all_keyword)
		
sys.exit()


