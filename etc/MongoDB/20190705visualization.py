import matplotlib.pylab as pl

ax1 = pl.subplot(111)
t = [1.,2.,3.,4.]
aa = [11.4,12.7,13.1,14.56]
pl.plot(t, aa, 'b-o', label="aa")

pl.xlabel('no')
pl.ylabel('aa')
#pl.show()

ax2 = pl.twinx()
bb = [0.9,2.2,3.54,4.0]
pl.plot(t, bb, 'r-s', label="bb")
pl.ylabel('bb')
ax2.yaxis.tick_right()
pl.show()
