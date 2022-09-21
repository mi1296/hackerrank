hr, mins, sec = input().split(':')
sec, meridian = sec[:2], sec[2:]

if meridian == 'PM':
    if hr == '12':
        print(hr+':'+mins+':'+sec)
    else: 
        hr = str(int(hr)+12)
        print(hr+':'+mins+':'+sec)
    
else:
    if hr == '12':
        hr = '00'
    print(hr+':'+mins+':'+sec)
