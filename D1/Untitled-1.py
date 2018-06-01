try:
    # raise SystemExit
    # b = 1
    # dict(a=1)['b']
    # [1, 2 ,3][123]
except ValueError:
    print('not a valid number!')
except (KeyError, IndexError):
    print('key or index not exist')
except Exception:
    print('others error!')  
else:
    print('everything is OK')
finally:
    print('always executed!')
