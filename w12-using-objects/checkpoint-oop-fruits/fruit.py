def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"reverse: {fruit_list}")

    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    loc = fruit_list.index("apple")
    print(f"apple location {loc}")
    fruit_list.insert(loc, "cherry")
    print(f"insert cherry: {fruit_list}")

    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    popped = fruit_list.pop()
    print(popped)
    print(f"pop: orange {fruit_list}")

    fruit_list.sort()
    print(f"sorted {fruit_list}")

    fruit_list.clear()
    print(f"clear {fruit_list}")


if __name__ == "__main__":
    main()