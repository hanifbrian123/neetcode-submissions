class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqTrue = {chr(i):0 for i in range(97, 123)}
        for s in s1: freqTrue[s]+=1
        
        freqWindow = {chr(i):0 for i in range(97, 123)}
        l, r, n = 0, 0, len(s2)
        while r < n:
            currS2 = s2[r]
            freqWindow[currS2] += 1
            incrementR = True
            temp = {key: freqWindow[key] for key in freqWindow if freqWindow[key] != 0}
            # print(currS2, temp)
            if freqWindow == freqTrue:
                return True
            elif not freqTrue[currS2]: # tidak ada char ini di freq true, artinya r ini sudah tidak valid lagi dan l maupun r baru bisa dipindah ke r+1, freqwindow bisa kembali di kosongkan lagi
                l = r+1
                r = l
                incrementR = False
                freqWindow = {chr(i):0 for i in range(97, 123)}
            elif freqWindow[currS2] > freqTrue[currS2]:
                while freqWindow[currS2] > freqTrue[currS2]:
                    freqWindow[s2[l]] -= 1
                    l+=1
            if incrementR:
                r+=1
        return False
