class ASeries ():
      def   longest (self, A):
                                                lenght=self._longest(A)
                                                return lenght
      def  _longest(selef,A):
              l1=2
              n=len(A)
              for i in range(n):
                  for j in range(n):
                      l2=2
                      if A[j]!=A[i]:
                          X=A[i]
                          Y=A[j]
                          print 'X=%s' % X
                          print 'Y=%s' % Y
                          diff=Y-X
                          Y=diff+Y
                          while Y in A:
                              Y=diff+Y
                              l2+=1
                      else:
                          l2=A.count(A[i])
                      if l2>l1:
                          l1=l2
              return l1
