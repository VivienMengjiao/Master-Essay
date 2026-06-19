library(ggplot2)
pd<-read.csv("S:/Studium/DH/Masterarbeit/Done/ggplot/And then there were none/And then there were none.csv")
ggplot(data=pd,aes(x=Chapter,y=Frequency))+geom_bar(stat="identity",fill="black")+labs(title="And then there were none_Justice Wargrave")
pd1<-read.csv("S:/Studium/DH/Masterarbeit/Done/ggplot/Evil under the sun/Evil under the sun.csv")
ggplot(pd1)+geom_bar(aes(x=Chapter,y=Frequency_PR,fill="PR"),stat="identity",position="dodge",alpha=0.6)+geom_bar(aes(x=Chapter,y=Frequency_CR,fill="CR"),stat="identity",position="dodge",alpha=0.6)+labs(x="Chapter",y="Frequency",title="Evil under the sun_Christine Redfern & Patrick Redfern")
library(ggplot2)
library(tidyr)
library(dplyr)

# Reshape data to long format
pd_long <- pd1 %>%
  pivot_longer(cols = c(Frequency_PR, Frequency_CR),
               names_to = "Type",
               values_to = "Frequency")

# Rename levels for better display
pd_long$Type <- recode(pd_long$Type,
                       "Frequency_PR" = "PR",
                       "Frequency_CR" = "CR")

ggplot(pd_long, aes(x = Chapter, y = Frequency, fill = Type)) +
  geom_bar(stat = "identity", position = "stack", alpha = 0.6) +
  scale_fill_manual(values = c("CR" = "black", "PR" = "grey")) +
  labs(x = "Chapter",
       y = "Frequency",
       title = "Evil under the Sun: Christine Redfern & Patrick Redfern") +
  theme_minimal()
pd2<-read.csv("S:/Studium/DH/Masterarbeit/Done/ggplot/Mystery of the blue train/Mystery of the blue train.csv")
library(tidyr)
library(dplyr)


pd_long <- pd2 %>%
  pivot_longer(cols = c(LeMarquis, Knighton, Mason),
               names_to = "Character",
               values_to = "Frequency")
library(ggplot2)

ggplot(pd_long, aes(x = Chapter, y = Frequency, fill = Character)) +
  geom_bar(stat = "identity", position = "stack", alpha = 0.8) +
  scale_fill_manual(values = c(
    "LeMarquis" = "lightgrey",
    "Knighton"   = "black",
    "Mason"      = "darkgrey"
  )) +
  labs(
    x = "Chapter",
    y = "Frequency",
    title = "Evil under the Sun: LeMarquis, Knighton & Mason"
  ) +
  theme_minimal()
pd_4<-read.csv("S:/Studium/DH/Masterarbeit/Done/ggplot/Lord Edgware dies/Lord Edgeware dies.csv")
ggplot(data=pd_4,aes(x=Chapter,y=Frequency))+geom_bar(stat="identity",fill="black")+labs(title="Lord Edgware Dies_Jane Wilkinson")
pd_5<-read.csv("S:/Studium/DH/Masterarbeit/Done/ggplot/The mirror cracked side from side/the mirror cracked side from side.csv")
ggplot(data=pd_5,aes(x=Chapter,y=Frequency))+geom_bar(stat="identity",fill="black")+labs(title="the mirror cracked side from side_Marina Gregg")
pd_6<-read.csv("S:/Studium/DH/Masterarbeit/Done/ggplot/Murdur of Roger Ackroyd/the murder of roger ackroyd.csv")
ggplot(data=pd_6,aes(x=Chapter,y=Frequency))+geom_bar(stat="identity",fill="black")+labs(title="The murder of Roger Ackroyd_James Sheppard")
