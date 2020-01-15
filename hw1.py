# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    dot_pos = line.find('.')
    value = value + float(line[dot_pos-1:dot_pos+5])
result = value / count    
print("Average spam confidence:", result)