import numpy as np 
a=np.array([0,1,2,3])
print(a)
print(a.ndim)
print(a.shape)
print(len(a))
b=np.array([[0,1,2],[3,4,5]])
print(b)
print(b.ndim)
print(b.shape)
print(len(b))
c=np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
print(c)
print(c.ndim)
print(c.shape)
a=np.arange(1,10,2)
print(a)
a=np.linspace(0,1,6)
print(a)
a=np.ones((3,3))
print(a)
b=np.zeros((3,3))
print(b)
print(np.eye(3))
print(np.eye(3,2))
a=np.diag([1,2,3,4])
print(a)
a=np.random.randn(4);
print(a)
a=np.random.rand(4)
print(a)
