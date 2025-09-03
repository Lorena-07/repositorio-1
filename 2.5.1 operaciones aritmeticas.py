import numpy

a=numpy.array([[1,2],[3,4]])
print(a)
print(a.shape)
print("--")
b=numpy.array([[5,6]])
print(b)
print(b.shape)
print("----")
print(numpy.concatenate((a,b),axis=0)) # pegado por filas
print(numpy.concatenate((a,b.T),axis=1)) # pegado por columnas


a=numpy.array([[1,2],[3,4]])
print(a)
print(a.shape)
print("---")
b=numpy.array([[5,6]])
print(b)
print(b.shape)
print("----")
print(numpy.concatenate((a,b),axis=0)) #pegado por filas
print(b.T.shape)
print(numpy.concatenate((a,b.T),axis=1)) #pegado por columnas
