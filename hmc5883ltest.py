from i2clibraries import i2c_hmc5883l
 
hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
 
hmc5883l.setContinuousMode()
# Home in Santa Cruz
hmc5883l.setDeclination(12, 54)
 
print(hmc5883l)
# To scaled axes
(x, y, z) = hmc5883l.getAxes()
(degrees, minutes) = hmc5883l.getHeading()
print("heading: " + str(degrees) + " " + str(minutes))
hmc5883l.