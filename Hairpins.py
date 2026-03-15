def is_complement(a, b):
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    return (a, b) in pairs

def find_hairpins(rna, min_arm=4, max_loop=10, max_arm=20):
    hairpins = []

    n = len(rna)

    for i in range(n):
        for arm_len in range(min_arm, max_arm + 1):
            if i + arm_len*2 + 1 > n + max_loop:
                break

            for loop_len in range(1, max_loop + 1):
                j = i + arm_len + loop_len
                if j + arm_len > n:
                    break

                left = rna[i:i+arm_len]
                right = rna[j:j+arm_len][::-1]  # odwrócenie do dopasowania

                if all(is_complement(left[k], right[k]) for k in range(arm_len)):
                    hairpins.append({
                        "start": i,
                        "end": j + arm_len - 1,
                        "left_arm": left,
                        "loop": rna[i+arm_len:j],
                        "right_arm": rna[j:j+arm_len]
                    })

    return hairpins


# Przykład użycia:
rna_seq = "AUGCUAGCGAAUUCGCUGAAUGCUAUUGGAACCGAUCAGAUAGACAG"
results = find_hairpins(rna_seq)

for h in results:
    print(f"Hairpin: {h['left_arm']}({h['loop']}){h['right_arm']}, "
          f"pozycje {h['start']}–{h['end']}")
