from Magic import *

air = Air()
fire = Fire()
water = Water()
earth = Earth()

lightning = fire + air
dust = air + earth
dirt = water + earth
storm = water + air
vapor = water + fire
lava = fire + earth
Vsem_GG = storm + lava

print(lightning)
print(dust)
print(dirt)
print(storm)
print(vapor)
print(lava)
print(Vsem_GG)
