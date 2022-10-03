
genshindata = git@github.com:Dimbreath/GenshinData.git

prepare: 
	mkdir backend/src/main/resources/genshin
	mkdir frontend/src/assets/data
	git clone $(genshindata)
	
