class ANDEquation():
      def   restoreY (self, A):
                                                Message=self._restoreY(A)
                                                return Message
      def  _restoreY(selef,A):
                    i=0
                    for i in range(len(A)):
						j=0
						l=0xfffff
						for j in range(len (A)):
							if j!=i:
								l&=A [j]
						if l==A[i]:
							return l
                    return -1