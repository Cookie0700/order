#!/usr/bin/env python3
# filename: main.py
# author: js-on
# date: 27.08.2021
# version: v0.0.1
from typing import Callable, Tuple
from datetime import datetime
from random import shuffle

filename = "dishes.txt"


class Dish(object):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_cost(self):
        return self.cost

    def __str__(self):
        return self.name


def greedy(dishes: list, maxCost: float, keyFnct: Callable) -> Tuple[list, float]:
    sortedDishes = sorted(dishes, key=keyFnct, reverse=True)
    result = []
    totalCal = 0
    for i in range(len(dishes)):
        if (totalCal + sortedDishes[i].get_cost() <= maxCost):
            result.append(sortedDishes[i])
            totalCal += sortedDishes[i].get_cost()
    return (result, round(totalCal, 2))


def create_menu(names: list, costs: list) -> list:
    menu = []
    for name, cost in zip(names, costs):
        menu.append(Dish(name, cost))
    return menu


def shuffle_dict(data: dict) -> dict:
    keys = list(data.keys())
    shuffle(keys)
    return {k: data[k] for k in keys}


def get_mealtime_from_hour() -> str:
    hour = datetime.now().hour
    if 6 <= hour <= 11:
        return "breakfast"
    elif 12 <= hour <= 14:
        return "lunch"
    elif 15 <= hour <= 17:
        return "nibbling break"
    elif 18 <= hour <= 22:
        return "dinner"
    else:
        return "midnight snack"


def main():
    dishes = {entry.split(",")[0].strip(): float(entry.split(
        ",")[1].strip()) for entry in open(filename, "r").readlines()}
    dishes = shuffle_dict(dishes)
    names, costs = list(dishes.keys()), list(dishes.values())
    menu = create_menu(names, costs)
    maxCost = input("How much money are you willing to spend?\nInput: $")
    try:
        maxCost = float(maxCost.replace(",", "."))
    except Exception:
        print("You need to enter a valid number!")
        exit(1)
    lunch, totalCosts = greedy(menu, maxCost, Dish.get_cost)
    print(
        f"You'll pay ${totalCosts} for your {get_mealtime_from_hour()} and this is what you'll eat:")
    for dish in lunch:
        print(f"  - {str(dish)} (${dish.get_cost()})")


if __name__ == '__main__':
    main()
