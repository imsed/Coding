class Bonuses ():
      def   getDivision (self, points):
                                                percentage=self._getDivision(points)
                                                return percentage
      def  _getDivision(self,points):
              division_sum=0
              percent_sum=0
              l=len(points)
              result=[]
              sorted_result=[]
              index=[]
              division_sum=sum(points)
              sorted_points= sorted(points, reverse=True)
              for p in points:
                  result.append(int((p*100)/division_sum))
                  percent_sum+=int((p*100)/division_sum)
              diff=100-percent_sum
              for i in range (diff):
                  for p in range(l):
                         if points[p]==sorted_points[i] and p not in index:
                                     result[p]+=1
                                     index.append(p)
                                     break
              print result




