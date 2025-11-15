Marple_Modifier<-read.csv("S:/Studium/DH/Masterarbeit/Corpus/Done/Modifier/AntConc/A Murder is announced/Marple_Modifier - Kopie.csv")
Marple_Modifier$source
Marple<-Marple_Modifier$source


library(quanteda)

dfm.temp<-dfm(tokens(Marple))


dfm.sotu<-dfm_lookup(dfm.temp,dictionary=data_dictionary_LSD2015)
dfm.sotu
dfm_Marple<- as.data.frame(as.matrix(dfm.sotu))
write.csv(dfm_Marple, "S:/Studium/DH/Masterarbeit/Corpus/Done/Modifier/AntConc/A Murder is announced/Marple_Modifier - Kopie.csv", row.names = TRUE)

