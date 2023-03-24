linux = b""

# machine-id is stable across boots, boot_id is not.
for filename in "machine-id", "boot_id":
    try:
        with open(filename, "rb") as f:
            value = f.readline().strip()
    except OSError:
        continue

    if value:
        linux += value
        break

# Containers share the same machine id, add some cgroup
# information. This is used outside containers too but should be
# relatively stable across boots.
try:
    with open("cgroup", "rb") as f:
        linux += f.readline().strip().rpartition(b"/")[2]
except OSError:
    pass

print(linux)
