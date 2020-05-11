def max_prefix(s,words):
    """
    :param s: input string
    :param words: word dict
    :return:
    """
    trie = {}
    for word in words:
        t = trie
        for w in word:
            t = t.setdefault(w, {})
        t["#"] = 1
    # print(trie)
    trie_base=trie
    res =[]
    def helper(s,i,trie,tmp):
        if i >= len(s):
            return
        if s[i] not in trie:
            res.append(s[i])
            helper(s,i+1,trie_base,"")
        else:
            tmp+=s[i]
            trie_tmp = trie[s[i]]
            if "#" in trie_tmp and len(trie_tmp)==1:
                res.append(tmp)
                helper(s,i+1,trie_base,"")
            else:
                helper(s,i+1,trie_tmp,tmp)

    helper(s,0,trie,"")
    return res


print(max_prefix("abcdefg",["ab",'aa','defg',"a","cd",'abc']))