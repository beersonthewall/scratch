import torch

# 5 rows by 3 cols
t = torch.zeros(5,3)
print(t)
print(t.dtype)

t2 = torch.ones((5,3), dtype=torch.int16)
print(t2)

torch.manual_seed(42)
r1 = torch.rand(2,2)
print(r1)

ones = torch.ones(2,2)
print(ones)

twos = torch.ones(2,2) * 2
print(twos)
print(ones + twos)

r2 = r1 -.5 * 2
print(r2.abs()) # or torch.abs(r2)
print(r2)
print(r2.max())
print(r2.mean())
print(r2.mode())
print(torch.std_mean(r2))
