# Takes a dictionary of weights and returns a number of dictionary positions which 
# are equal to the a given weight

def scales(weights_dict, target_weight):
    result = []
    for key_a in weights_dict:
        if weights_dict[key_a] == target_weight:
            result.append(key_a)
            return result
        for key_b in weights_dict:
            if key_a != key_b:
                if weights_dict[key_a] + weights_dict[key_b] == target_weight:
                    result.append(key_a)
                    result.append(key_b)
                    return result
                else:
                    for key_c in weights_dict:
                        if key_a != key_c and key_b != key_c:
                            if weights_dict[key_a] + weights_dict[key_b] + weights_dict[key_c] == target_weight:
                                result.append(key_a)
                                result.append(key_b)
                                result.append(key_c)
                                return result    
    return result


