results = {i:0 for i in range(1,5)}

## program check
try:
    import p1
    assert p1.f("5290312400019022") == "52**********9022"
    assert p1.f("4321000055552299") == "43**********2299"
    results[1] = 1
except:
    pass    

## program check
try:
    import p2
    assert p2.f("101101") == True
    assert p2.f("100") == True
    assert p2.f("1311a10100") == False
    results[2] = 1
except:
    pass    

## program check
try:
    import p3
    assert p3.f(23) == 6
    assert p3.f(8) == 3
    assert p3.f(2) == 1
    assert p3.f(0) == 0
    results[3] = 1
except:
    pass    


## program check
try:
    import p4
    assert p4.f(3124,True) == 6
    assert p4.f(3124,False) == 4
    assert p4.f(20576,False) == 12
    assert p4.f(20576,True) == 8
    assert p4.f(13115,True) == 0
    assert p4.f(0,True) == 0
    assert p4.f(0,False) == 0
    results[4] = 1
except:
    pass    

# Final results
print('\nTOTAL PTS:', sum(results.values()), results)
print()
