from collections import OrderedDict

def lru_miss_count_ordered(sequence, capacity):
    """
    sequence: 可迭代的序列（如字符串或列表）
    capacity: 缓存容量（int）
    返回: (miss_count, hit_count, final_cache_list)
    """
    if capacity <= 0:
        # 容量为 0，全部为 miss
        misses = len(sequence)
        return misses, 0, []

    cache = OrderedDict()
    misses = hits = 0

    for ch in sequence:
        if ch in cache:
            # hit：移动到末尾表示最近使用
            cache.move_to_end(ch)
            hits += 1
        else:
            # miss：插入
            misses += 1
            cache[ch] = True
            if len(cache) > capacity:
                cache.popitem(last=False)  # 弹出最久未使用的
    return misses, hits, list(cache.keys())

# 示范
if __name__ == "__main__":
    # seq = "ZYXXWZXYXW"
    # seq = "ABCDDCBAABCD"
    seq = "ACEGBDFHACEGBDFH"
    miss, hit, final = lru_miss_count_ordered(seq, 3)
    print("miss =", miss, "hit =", hit, "final cache =", final)

