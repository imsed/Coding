class Aaagmnrs():
      def   anagrams (self, A):
                                                output=self._anagrams(ax, A)
                                                return output
      def  _anagrams(self,A):
          X=[]
          O=[]
          for i in A:
              Y=''.join (sorted(i.upper().replace(" ","")))
              print Y
              if Y not in X:
                  X.append (Y)
                  O.append(i)
          return tuple (O)

