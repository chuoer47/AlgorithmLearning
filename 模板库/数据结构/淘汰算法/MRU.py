from collections import OrderedDict

def mru_miss_count(sequence, capacity):
    """
    sequence: 字母序列（如 "ABCA"）
    capacity: 缓存容量
    返回: (miss, hit, final_cache_list)
    """
    if capacity <= 0:
        return len(sequence), 0, []

    cache = OrderedDict()
    misses = hits = 0

    for ch in sequence:
        # hit：移动到末尾
        if ch in cache:
            cache.move_to_end(ch)
            hits += 1
        else:
            # miss：插入到末尾（最新）
            cache[ch] = True
            misses += 1

            # 如果超容量 → 删除 MRU（也就是最新：末尾）
            if len(cache) > capacity:
                cache.popitem(last=True)  # MRU 淘汰

    return misses, hits, list(cache.keys())


# 示例
if __name__ == "__main__":
    # seq = "ZYXXWZXYXW"
    # seq = "ABCDDCBAABCD"
    seq = "ACEGBDFHACEGBDFH"
    miss, hit, final = mru_miss_count(seq, 3)
    print("MRU miss =", miss, "hit =", hit, "final cache =", final)
