#! encoding: UTF-8
#! /usr/bin/python 
PI=  3.1415926535897931159979634685441852
n=int(raw_input("introdusca el numero de intervalos:"))
f=1
while n>0 and f==1:
 f+=1
 suma=0
 for i in range (1,n+1):
  a=float(i-1)/n
  b=float (i)/n
  x_i=float(i-0.5)/n
  fx_i=float (4)/(1+x_i*x_i)
  suma+=fx_i
  print"el intervelo %d es: [%3.2f,%3.2f],fx_i= %4.3f" %(i,a,b,x_i)
 pi=float (suma)/n
 print pi
 print "pi es:%36.35f" %(PI)