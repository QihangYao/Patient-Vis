library('ggplot2')
library('gridExtra')
barfill <- "#4271AE"
barlines <- "#1F3552"

label= c('count_note', 'count_chart','count_lab')

p1 <- ggplot(test, aes(x =test$count_note )) +
  geom_histogram(aes(y = ..count..), binwidth = 5,
                 colour = 'darkblue', fill = 'lightblue') +
  scale_x_continuous(name = "Count of note events", breaks = seq(0,500, 100), limits=c(1,500))+
  scale_y_continuous(name = "Frequency") +
  ggtitle("Frequency histogram of note events")+
  geom_density(alpha=.2, fill="#FF6666")
p1

p2 <- ggplot(test, aes(x =test$count_chart )) +
  geom_histogram(aes(y = ..count..), binwidth = 5,
                 colour = 'purple', fill = 'white') +
  scale_x_continuous(name = "Count of chart events", breaks= seq(0,2000,200), limits=c(0,2000) )+
  scale_y_continuous(name = "Frequency") +
  ggtitle("Frequency histogram of chart events")+
  geom_density(alpha=.2, fill="#FF6666")
p2


p3 <- ggplot(test, aes(x =test$count_lab )) +
  geom_histogram(aes(y = ..count..), binwidth = 5,
                 colour = 'red', fill = 'white') +
  scale_x_continuous(name = "Count of lab events", breaks= seq(0,1000,100), limits=c(0,1000) )+
  scale_y_continuous(name = "Frequency") +
  ggtitle("Frequency histogram of lab events")+
  geom_density(alpha=.2, fill="#FF6666")


p3


grid.arrange(p1,p2,p3)
