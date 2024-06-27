def min_subs(source, target):
    target_index = 0
    count = 0

    while target_index < len(target):
        source_index = 0
        new_target_index = target_index

        while source_index < len(source) and new_target_index < len(target):
            if source[source_index] == target[new_target_index]:
                new_target_index += 1
            source_index += 1

        if new_target_index == target_index:
            return -1

        target_index = new_target_index
        count += 1

    return count


if __name__ == "__main__":
    print(min_subs("abc", "abcbc"))
    print(min_subs("abc", "acdbc"))
    print(min_subs("xyz", "xzyxz"))
