import re

# Baca file nice.rsc
with open('nice.rsc', 'r') as file:
    lines = file.readlines()

# List untuk menyimpan hasil yang sudah di proses
payloads = []

# Proses setiap baris
for line in lines:
    match = re.match(r'add list=nice address="([\d./]+)"', line)
    if match:
        ip_cidr = match.group(1)
        payloads.append(f'IP-CIDR,{ip_cidr}')

# Tulis hasil ke file baru
with open('rule-indo.yaml', 'w') as file:
    file.write('\n'.join(payloads))
