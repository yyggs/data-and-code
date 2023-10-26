import matplotlib.pyplot as plt

# 数据
chunk_sizes = [1, 2, 4, 8, 16]
lower_bounds = [1.9107105515358676, 1.904048528625105, 1.8997199502845612, 1.9031202985298166, 1.8997434804740012]
upper_bounds = [1.9227286884641326, 1.9105614313748953, 1.9076563697154392, 1.9091656214701833, 1.9073401995259986]
mean_vals = [(l+u)/2 for l, u in zip(lower_bounds, upper_bounds)]

plt.figure(figsize=(10, 6))
plt.errorbar(chunk_sizes, mean_vals, yerr=[(u-l)/2 for l, u in zip(lower_bounds, upper_bounds)], fmt='o', capsize=5)
#plt.title("95% Confidence Interval of Time_Loop2 for Different Chunk Sizes")
plt.xlabel("Chunk Size")
plt.ylabel("Loop2 [s]")
plt.xticks(chunk_sizes)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig("confidence_intervals.png")

plt.show()
