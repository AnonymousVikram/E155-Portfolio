maxFreq = 0
maxError = 0

for i in range(220, 1001):
  arr = int(4000000 / i - 1)
  fout = 4000000/(arr+1)
  error = abs(fout - i) / i * 100
  if error > maxError:
    maxError = error
    maxFreq = i

print("Max Error: ", maxError)
print("Max Freq: ", maxFreq)