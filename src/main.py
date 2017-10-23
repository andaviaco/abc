import lib
from swarm import ABC


def main():
    abc_sphere = ABC(30, 49, lib.sphere, fn_lb=[-5, -5], fn_ub=[5, 5])
    abc_ackley = ABC(30, 49, lib.ackley, fn_lb=[-20, -20], fn_ub=[20, 20])
    abc_rastrigin = ABC(30, 49, lib.rastrigin, fn_lb=[-5, -5], fn_ub=[5, 5])

    min_x, min_y = abc_sphere.optimize()
    eval_result = lib.sphere([min_x, min_y])

    print(f'Sphere MIN: x={min_x}, y={min_y}')
    print(f'Sphere({min_x}, {min_y}) = {round(eval_result, 4)}')

    min_x, min_y = abc_rastrigin.optimize()
    eval_result = lib.rastrigin([min_x, min_y])

    print(f'Rastrigin MIN: x={min_x}, y={min_y}')
    print(f'Rastrigin({min_x}, {min_y}) = {round(eval_result, 4)}')

    min_x, min_y = abc_ackley.optimize()
    eval_result = lib.ackley([min_x, min_y])

    print(f'Ackley MIN: x={min_x}, y={min_y}')
    print(f'Ackley({min_x}, {min_y}) = {round(eval_result, 4)}')

if __name__ == '__main__':
    main()
