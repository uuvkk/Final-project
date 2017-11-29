# Title: Prediction of Probability for Products Making

## Team Member(s):
Jiazheng Li

# Monte Carlo Simulation Scenario & Purpose:
Imagine that we are making a projuct, which has certain components. We make the product from the internal to the external. The most inside part of the product is a solid cone, which would be in a hollow cube. And the cube would be put in another cube. The product would have these three parts. For each part and the connection to different parts, there are some certain criteria. If any criterion is broken during the procedure, all the finished components of one product will be abondoned immidiately because the making of the products is very strict and requires high precision. The propose of this program is, knowing the cost one producer has, to output the maximum number of potential good products; and then ask the user to input the expected number of good products; finally the program would tell the user the probability of reaching the expection when making the products.

### Hypothesis before running the simulation:
To decribe the lenth of any parts we use mm. For the most inside solid cone, the best standard is 27mm (+-2) in radius and 55mm (-3,+2) in height, where the numbers in the parenthesis is the accepted ranges of errors. For the cone, the cost is 0.02 dollar per cubic mm. The best standard for the next cube is 56mm * 56mm * 56mm, but 2.5mm error of error for each edge is acceptable when its not shorter than the diameter or the height of the cone. Also the edge could not be 4mm longer than the diameter or 3.5mm longer than the height. The cost of the hollow cube is 0.04 dollow per square mm. For the out most cube, the best standard is 58mm * 58mm * 58mm, but 4mm error would be acceptable when the edges is not shorter than the previous cube's edge or 6mm longer than that. The cost of this hollow cube is 0.03 dollow per square mm.

### Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). 
For each such variable, how did you decide the range and which probability distribution to use?  
Do you think it's a good representation of reality?

There are 4 variables of the simulation, i. e. the radius and the height of the solid cone and the lenths of the edges for the two cubes. All of them are in normal distributions, which would be a good fit of actual conditions, but with different parameters. Here I set the parameter as followings:

The radius of the solid cone: (27, 0,45).
The height of the solid cone: (55, 0.92).
The edge of the first hollow cube: (56, 1).
The edge of the second hollow cube: (56, 1.4).

To calculate the max number of good products, what we use are all best standards. We should calculate the cost of one perfect product, and than divide the provided total cost by the one-product-cost. Next we start the simulation by random numbers. When one component meets the criteria we continue making the product, otherwise we abondon the whole product. We do not stopping making the products until the remaining money colud not be used to make one perfect product. You may notice that we may make more products than the estimated maxmium based on the same budget, because some qulified products may cost less than a perfect product when they are smaller but still meet the criteria. However, based on a large amount of simulation experiments to get the average number, I am positive this situation would not be shown on the final output. Let's find out.

## Instructions on how to use the program:
The program can tell the criteria of each parts of the products, and the cost of making one standard product. The user than would input the budget he has. After the program would show the max number of possible good products, the user tells the machine how many products he expect to make based on the budget. Finally the program can output the possibility of that the user's expection would be met.

## Sources Used:

