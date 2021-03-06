import math
import random


class Product:
    """
    simulate the product making procedure
    """
    cost1 = 0.02
    cost2 = 0.04
    cost3 = 0.03
    perfect_cost = 27 * 27 * 55 * math.pi / 3 * cost1 + 56 * 56 * 6 * cost2 + 58 * 58 * 6 * cost3

    @staticmethod
    def cone_cost(r, h):
        """
        calculate the cost of the first part
        :param r: the radius of the cone
        :param h: the height of the cone
        :return:  the money used by cost per cubic mm and the volume
        >>> Product.cone_cost(27, 55)
        839.7477163045518
        """
        return r * r * h * math.pi / 3 * Product.cost1

    @staticmethod
    def cube1_cost(a):
        """
        calculate the cost of the second part
        :param a: the side length of a cube
        :return: the money used by cost per square mm and the surface area
        >>> Product.cube1_cost(56)
        752.64
        """
        return a * a * 6 * Product.cost2

    @staticmethod
    def cube2_cost(a):
        """
        calculate the cost of the third part
        :param a: the side length of a cube
        :return: the money used by cost per square mm and the surface area
        >>> Product.cube2_cost(58)
        605.52
        """
        return a * a * 6 * Product.cost3

    @staticmethod
    def making() -> list:
        """
        simulate the procedure of making one product
        :return: the first element of the list is successfully making the product or not marked as 0 or 1
        the second is the cost of the procedure regardless successfully making or not
        >>> Product.making()[0] == 1 or Product.making()[0] == 0
        True
        >>> type(Product.making()[1])
        <class 'float'>
        """
        r = random.gauss(27, 0.45)
        h = random.gauss(55, 0.92)
        costA = Product.cone_cost(r, h)
        if (r > 29 or r < 25) or (h > 57 or h < 52):
            return [0, costA]
        a1 = random.gauss(56, 1)
        costB = Product.cube1_cost(a1)
        if (a1 > 58.5 or a1 < 53.5) or (a1 > (r * 2 + 2)) or (a1 > (h + 3.5)) or (a1 < r * 2 or a1 < h):
            return [0, costA + costB]
        a2 = random.gauss(58, 1.4)
        costC = Product.cube2_cost(a2)
        if (a2 > 62 or a2 < 54) or (a2 > (a1 + 6)) or a2 < a1:
            return [0, costA + costB + costC]
        else:
            return [1, costA + costB + costC]

    @staticmethod
    def success_probability():
        """
        calculate the approximate probability of successfully making a product
        :return: the calculated probability
        >>> p = Product.success_probability()
        >>> 28 > p > 25
        True
        """
        good_products = 0
        total = 0
        for i in range(100):
            for j in range(10000):
                good_products = good_products + Product.making()[0]
            total = total + good_products
            good_products = 0
        return total/10000

    @staticmethod
    def producing(budget):
        """
        knowing the budget, calculate the number of products made during the procedure
        :param budget: the amount of the budget the user has
        :return: the number of products
        >>> n = Product.producing(50000)
        >>> 6.5 < n < 8.5
        True
        """
        number = 0
        total_number = 0
        for i in range(100):
            one_budget = budget
            while one_budget > Product.perfect_cost:
                one_product = Product.making()
                number = number + one_product[0]
                one_budget = one_budget - one_product[1]
            total_number = total_number + number
            number = 0
        number = total_number / 100
        return number

if __name__ == "__main__":
    print('The cost of one perfect product is {} dollars.'.format(round(Product.perfect_cost, 2)))
    print('The probability of successfully making one product is {}%.'.format(round(Product.success_probability(), 2)))
    while True:
        try:
            budget = input('Please input your budget, we will tell you the expected number of successful products (or "q" to quit the program): ')
            if budget == 'q':
                print('Thanks for using this simulator!')
                break
            budget = float(budget)
            if budget <= 0:
                print('The input should be a positive number! Try again:')
                continue
            print('The expected number of successful products is {}.'.format(Product.producing(float(budget))))
        except ValueError:
            print('The input should be a positive number! Try again:')
            continue
