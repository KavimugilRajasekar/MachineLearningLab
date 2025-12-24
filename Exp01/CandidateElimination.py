# Candidate Elimination Algorithm for Remote Work Approval

# Attributes:
# [Role, Experience, Performance, Internet, Location]

# Training data
training_data = [
    (["Technical", "Senior", "Excellent", "Good", "Urban"], "Yes"),
    (["Technical", "Junior", "Excellent", "Good", "Urban"], "Yes"),
    (["Non-Technical", "Junior", "Average", "Poor", "Rural"], "No"),
    (["Technical", "Senior", "Average", "Good", "Rural"], "No"),
    (["Technical", "Senior", "Excellent", "Good", "Rural"], "Yes")
]

# Initialize S and G
num_attributes = len(training_data[0][0])

S = ["Ø"] * num_attributes
G = [["?"] * num_attributes]

def is_consistent(hypothesis, instance):
    for h, i in zip(hypothesis, instance):
        if h != "?" and h != i:
            return False
    return True

def more_general(h1, h2):
    return all(x == "?" or x == y for x, y in zip(h1, h2))

print("\nInitial Specific Hypothesis (S):", S)
print("Initial General Hypothesis (G):", G)

# Process each training example
for idx, (instance, label) in enumerate(training_data):
    print(f"\nProcessing Example {idx+1}: {instance} -> {label}")

    if label == "Yes":  # Positive example
        # Remove inconsistent hypotheses from G
        G = [g for g in G if is_consistent(g, instance)]

        # Generalize S
        for i in range(num_attributes):
            if S[i] == "Ø":
                S[i] = instance[i]
            elif S[i] != instance[i]:
                S[i] = "?"

    else:  # Negative example
        new_G = []
        for g in G:
            if is_consistent(g, instance):
                for i in range(num_attributes):
                    if g[i] == "?":
                        if S[i] != "?" and S[i] != "Ø":
                            new_h = g.copy()
                            new_h[i] = S[i]
                            if is_consistent(new_h, instance) is False:
                                new_G.append(new_h)
            else:
                new_G.append(g)

        G = new_G

    # Remove overly specific hypotheses in G
    G = [g for g in G if more_general(g, S)]

    print("Specific Boundary (S):", S)
    print("General Boundary (G):", G)

# Final Version Space
print("\nFinal Specific Boundary (S):", S)
print("Final General Boundary (G):", G)

# Prediction
test_instance = ["Technical", "Senior", "Excellent", "Good", "Urban"]

prediction = is_consistent(S, test_instance) and any(
    is_consistent(g, test_instance) for g in G
)

print("\nPrediction for", test_instance)
print("Remote Work Approved?" , "Yes" if prediction else "No")
