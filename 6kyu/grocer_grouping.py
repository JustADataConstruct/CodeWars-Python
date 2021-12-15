"""
6kyu "Grocer grouping" kata
https://www.codewars.com/kata/593c0ebf8b90525a62000221
Ever since you started work at the grocer, you have been faithfully logging down each item and its category that passes through. One day, your boss walks in and asks, "Why are we just randomly placing the items everywhere? It's too difficult to find anything in this place!" Now's your chance to improve the system, impress your boss, and get that raise!

The input is a comma-separated list with category as the prefix in the form "fruit_banana". Your task is to group each item into the 4 categories Fruit, Meat, Other, Vegetable and output a string with a category on each line followed by a sorted comma-separated list of items.

For example, given:

"fruit_banana,vegetable_carrot,fruit_apple,canned_sardines,drink_juice,fruit_orange"
output:

"fruit:apple,banana,orange\nmeat:\nother:juice,sardines\nvegetable:carrot"
"""
import codewars_test as test


def group_groceries(inp: str) -> str:
    groceries = {'fruit': [], 'meat': [], 'other': [], 'vegetable': []}
    lines = inp.split(",")
    for l in lines:
        sp = l.split("_")
        cat = sp[0]
        prod = sp[1]
        if cat in groceries:
            groceries[cat].append(prod)
        else:
            groceries["other"].append(prod)
    res = ""
    for k in groceries.keys():
        res += "{0}:{1}\n".format(k, ",".join(sorted(groceries[k])))
    return res.rstrip()


input_ = "fruit_banana,vegetable_carrot,fruit_apple,canned_sardines,drink_juice,fruit_orange"

output = """
fruit:apple,banana,orange
meat:
other:juice,sardines
vegetable:carrot
""".strip()

test.assert_equals(group_groceries(input_), output)
