"""
Simple Artificial Intelligence Program
SAIP

"""
import wolframalpha

client = wolframalpha.Client('5L4TR5-3QRQ88JWA3')
nounsFile=open("nouns.txt","r")
nounsList=nounsFile.read().split("\n")
nouns=[x.lower() for x in nounsList]
occurence=0
keywords=[]
emotions=["good","bad","cool","gross","dirty","love","sad","dangerous","happy"]
print("\t This is ASAIP-A Simple Artificial Intelligence Program\n")
input_str=raw_input("I am your personal assistant (for eg. how's the weather) ").split()

for word in range(len(input_str)):
	if input_str[word].lower() in nouns:
		keywords.append(input_str[word])		
print(str(len(keywords))+" keywords found")
for word in keywords:
	if_word=raw_input("do you want to know about "+word+" (YES)(NO)")
	if if_word.lower() == "yes":
		res = client.query(word)
		for pod in res.pods:
			for sub in pod.subpods:
				print(sub.plaintext)
