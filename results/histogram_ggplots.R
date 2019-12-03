library('ggplot2')
library('gridExtra')
barfill <- "#4271AE"
barlines <- "#1F3552"


p1 <- ggplot(test, aes(x =test$count_note )) +
  geom_histogram(aes(y = ..count..), binwidth = 5,
                 colour = 'darkblue', fill = 'lightblue') +
  scale_x_continuous(name = "Count of note events", breaks = seq(0,200, 20), limits=c(0,200))+
  scale_y_continuous(name = "Frequency") +
  ggtitle("Frequency histogram of events")+
  geom_density(alpha=.2, fill="#FF6666")+
  theme(text=element_text(size=50), plot.title = element_text( vjust=2))
p1

p2 <- ggplot(test, aes(x =test$count_chart )) +
  geom_histogram(aes(y = ..count..), binwidth = 5,
                 colour = 'purple', fill = 'white') +
  scale_x_continuous(name = "Count of Chart-events", breaks= seq(0,500,50), limits=c(0,500) )+
  scale_y_continuous(name = "Frequency") +
  geom_density(alpha=.2, fill="#FF6666")+
  theme(text=element_text(size=50), plot.title = element_text( vjust=2))
  
p2


p3 <- ggplot(test, aes(x =test$count_lab )) +
  geom_histogram(aes(y = ..count..), binwidth = 5,
                 colour = 'red', fill = 'white') +
  scale_x_continuous(name = "Count of Lab-events", breaks= seq(0,200,20), limits=c(0,200) )+
  scale_y_continuous(name = "Frequency") +

  geom_density(alpha=.2, fill="#FF6666")+
  
  theme(text=element_text(size=50), plot.title = element_text( vjust=2))

p3


grid.arrange(p1,p2,p3)
