class AB():
      def  createString (self, N,K):
                                                Message=self._createString(N,K)
                                                return Message
      def _createString(self, N,K):

		    n = int ((N-1)/2);
		    p=0;
		    q=0;
		    i=1;
		    j=0;
		    X =[]
		    X1="";
		    if n*(N-n)<K :
			return ""
		    else :
			while j < N :
					X.append("B");
					j+=1;
			while i <= n:
				if K>=i*(N-i):
					   X[i-1]="A";
					   p=i*(N-i);
					   i+=1;

				else:
					   q=N-1-K+p-i+1; 
					   X[q]="A";
					   i=n+1;
			return ''.join(X)
	
