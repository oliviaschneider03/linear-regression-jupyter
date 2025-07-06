#Used to import ggplot2 which we will need for this 
library(ggplot2)

#Read the regression file 
dataset <- read.csv("regression_data.csv")

#Creating my scatter plot
plot(dataset$YearsExperience, dataset$Salary, col="red")

#Yay made a scatter plot! Now this command is used to fit a linear model on my scatter plot
model <- lm(Salary ~ YearsExperience, data=dataset) #

#ggplot2 is a visualization package at R that makes the plot. First line adds points, second adds linear model, and the last three add titles.
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')

#This give you a bunch of statistical anaylses on the data you provided and on the linear model
summary(model)

#This is for the assignment 3 addition
# We can make a manual data frame as is done below but we can also make code to read any csv file and convert it into a data frame 
#dataset <- data.frame(x = c(1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.7, 4.0),y = c(39343.0, 46205.0, 37731.0, 43525.0, 39891.0, 56642.0, 60150.0, 54445.0, 57189.0, 63218.0))

# Loading data
filepath <- "regression_data.csv"

# Making it into a data frame
dataset <- read.csv(filepath)

# Printing data for my own sanity 
print(dataset)



# Defining which column equals which variable
x <- dataset[["YearsExperience"]]
y <- dataset[["Salary"]]

#Printing yet again.... 
print(x)
print(y)


# Fit model - These commands all define our linear model on our graph and allow for the linear model to be calculated based on our data
#MSE is used to caluclate the average squared difference between predicted values and actual values in our dataset
model <- lm(y ~ x, data = dataset)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(x, y)
pred <- predict(model)
mse <- mean((y - pred)^2)

# Plot
#geom_point adds data points 
#geom_smooth adds the regression line
#annotate adds the text and its location and size
#labs enters titles 
#theme_minimal makes the graph have a simplistic asethetic 
ggplot(dataset, aes(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  annotate("text", x = 1.5, y = max(y) - 0.5,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  labs(title = "Linear Fit",
       x = "x", y = "y") +
  theme_minimal()

ggsave("regression_plot_r.png")


