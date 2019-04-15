
#Step 1 - Pre-Processing the Data:

Parse all the labels in the training data from all the files to identify (word,tag) tuples:
	Our dataset is in Spanish language. We use the labelled data of the training set to identify the (word,tag) tuples. For example, if one of the labels in the training set contains 
(Ernesto, ’NOMBRE_SUJETO_ASISTENCIA’) as one of the gold standard label for a file, we add (Ernesto,’NOMBRE_SUJETO_ASISTENCIA’) to the dictionary D. We populate the dictionary D using the approach mentioned above for all the files. 

Parse the text from the training data from all the files to identify the list L of (identifier,word) tuples:
	We then parse all the files one by one for a second time. In each file, We search for all the keywords from the dictionary D. For each keyword found from the dictionary D, we search if ‘:’ is the character that appears before the keyword.If we find ‘:’ before the keyword, we label the word before ‘:’ as an Identifier.For example, if we find ‘Nombre: Ernesto’ in the running text, we add (‘Nombre’) as an Identifier.  After the end of second pass of the text files, we get all the (Identifier,word)  tuples from all the files. From D, we have a mapping of (word,tag) and from the second pass of reading all the files, we have mappings of the form (Identifier, word). Using the transitive relation, we create a precomputed dictionary of ( Identifier, tag ). 

For example:
Precomputed dictionary D looks something like:
{ {Ernesto,’NOMBRE_SUJETO_ASISTENCIA’} , ……...}

After reading all the files second time, We get,
L = [ (‘Nombre’,’Ernesto’ ),....] 
(‘Nombre’,’Ernesto’ ) is one of the (Identifier,word) tuple from the List L.

Combine the tuples from Dictionary D and List L to generate (identifier,tag) tuples that forms the basis for our baseline model:

We use combine Dictionary D and the list L to generate the (identifier,tag) tuples. 
For example,(‘Nombre’,’Ernesto’ ) is one of the (Identifier,word) tuple. All such tuples are stored as a dictionary on the disk and these tuples form the basis of our baseline model.

#Step 2 - Creating the tags for the baseline model:
We use regex expressions to find the words of the form word1:word2 from the training/validation files. For each such tuples found, we see if the word1 is a key from the precomputed Dictionary D1. If it is a key from the Dictionary D1, we label the word2 with the tag corresponding to the word1 from Dictionary D1.  This simple baseline does not involve any machine learning. It relies on  two things 1. Finding the : separated words from the running text 2. Assigning the tag to the words using the precomputed Dictionary D1.

Training Dataset Evaluation:
		Metric:

		Training Score:
	
		Validation Score:
		
		Test Score:

