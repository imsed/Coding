import math
class ATaleOfThreeCities():
      def   connect (self, ax, ay, bx, by, cx, cy):
                                                Message=self._connect(ax, ay, bx, by, cx, cy)
                                                return Message
      def  _connect(self,ax, ay, bx, by, cx, cy):
              d1=20000
              d2=20000
              d3=20000
              for i in range (len(ax)):
                  for j in range(len(bx)):
                      dab=(ax[i]-bx[j])**2+(ay[i]-by[j])**2
                      if dab<d1:
                          d1=dab
                  for k in range(len(cx)):
                      dac=(ax[i]-cx[k])**2+(ay[i]-cy[k])**2
                      if dac<d2:
                          d2=dac
              for i in range (len(cx)):
                  for j in range(len(bx)):
                      dbc=(cx[i]-bx[j])**2+(cy[i]-by[j])**2
                      if dbc<d3:
                          d3=dbc
              A = [math.sqrt(d1),math.sqrt(d2),math.sqrt(d3)]
              A.sort()
              d= A[0]+A[1]
              return d