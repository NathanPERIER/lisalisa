
genshindata = git@github.com:Dimbreath/GenshinData.git

prepare: 
	mkdir backend/src/main/resources/genshin
	git clone $(genshindata)
	
