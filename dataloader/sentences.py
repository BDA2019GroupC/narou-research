def remove_pattern_from_text(text,patterns=[["［＃","］"],["《","》"]]):
    import re
    ret = ""
    pat_count = [0 for _ in patterns]
    history = []
    for i in range(len(text)):
        for j,p in enumerate(patterns):
            if text[i:i+len(p[0])] == p[0]:
                history.append(j)
                pat_count[j] += 1
        if sum(pat_count) == 0:
            ret += text[i]
        for j,p in enumerate(patterns):
            if text[i:i+len(p[1])] == p[1]:
                if pat_count[j] == 0: continue
                pat_count[j] -= 1
                if len(history) == 0:
                    raise Exception("COULD NOT PARSE", patterns, pat_count, history, text[i-3:i+3])
                h = history.pop()
                if h != j:
                    raise Exception("COULD NOT PARSE", patterns, pat_count, history, text[i-3:i+3])
    return ret

def split_with_delims_without_patterns(text,delims=["。"],patterns=[["「","」"]],patterns_count=[],history=[]):
    if len(patterns_count) != 0:
        pat_count = patterns_count
    else: pat_count = [0 for _ in patterns]
    if len(history) != 0:
        history = history
    else: history = []
    ret = []
    tmp = 0
    for i in range(len(text)):
        for j,p in enumerate(patterns):
            if text[i:i+len(p[0])] == p[0]:
                history.append(j)
                pat_count[j] += 1
            
            if sum(pat_count) == 0:
                for d in delims:
                    if text[i] == d:
                        ret.append(text[tmp:i+1])
                        tmp = i+1
            
            if text[i:i+len(p[1])] == p[1]:
                if pat_count[j] == 0: continue
                if len(history) == 0:
                    raise Exception("Could not parse",text,text[i-3:i+3],p[1])
                t = history.pop()
                if j != t:
                    history.append(t)
                    continue
                pat_count[j] -= 1
    if text[tmp:] != "":
        ret.append(text[tmp:])
    return ret, pat_count, history
    
def get_sentence_from_text(text,delims=["。"]):
    del_count = [-2 for _ in delims]
    ret = []
    for i,delim in enumerate(delims):
        del_count[i] = text.find(delim)
    mini = min(del_count)
    if mini == -1: ret.append(text); return ret
    if mini == -2: raise Exception("ERROR, check")
    ret+=[text[:mini+1]]
    ret+=get_sentence_from_text(text[mini+1:])
    return ret