import imghdr

for i in range(1, 101):
    ext = imghdr.what(f'{i}.unknown')
    print(f'mv {i}.unknown {i}.{ext}')
#2e72e1ccbe59d07a67807b8ba9