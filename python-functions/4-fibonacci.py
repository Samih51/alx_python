def fibonacci_sequence(n):
    sequence = [0, 1] 
    if n <= 1:
        return sequence[:n ]
    else:
        while len(sequence) <= n-1:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))