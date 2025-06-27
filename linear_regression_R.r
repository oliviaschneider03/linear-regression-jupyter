#This arg command to my understanding is similar to the one we added in python and is responsible for ensuring we have the correct number of arguments and then these arguments are listed below
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)

#This defines the linear regression as a formula which to my understanding is a way to simplify the following code
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

#This is the same code as before
library(ggplot2)
plot <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue") +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

ggsave("linear_regression_r_output.png", plot)
print(plot)



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


