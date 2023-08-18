def tribonacci(signature, n):
    for t in range(n-3):
        sum = signature[-1] + signature[-2] + signature[-3]
        signature.append(sum)
    
    return signature[:n]