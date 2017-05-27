"""
Simple Artificial Intelligence Program
SAIP

"""
import json
net=open("association.json","r+")

existing=json.load(net)
nounsFile=open("nouns.txt","r")
nounsList=nounsFile.read().split("\n")
nouns=[x.lower() for x in nounsList]
occurence=0
keywords=[]
emotions=["good","bad","cool","gross","dirty","love","sad","dangerous","happy"]
print("\t This is ASAIP-A Simple Artificial Intelligence Program\n")
input_str=input("Please give a starting senctence for the conversation so i can learn some stuff ").split()

for word in range(len(input_str)):
	if input_str[word].lower() in nouns:
		keywords.append(input_str[word])		

association={}
emotion_association={}

for keyword in keywords:		
	description=input("tell me more about "+keyword+"(s): ")
	response=description.split()
	for emotion in emotions:
		if emotion in response:
			emotion_association[keyword]=emotion

	association[keyword]=description
open('association.json', 'w').close()
association.update(emotion_association)
association.update(existing)
net=open("association.json","a")
net.write(json.dumps(association))
