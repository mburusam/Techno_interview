import re
from collections import Counter


class Solution():
    def mostFrequentIP(self, lines):
        cnt = Counter()

        ipre = re.compile(r'[0-9]{2}\.[0-9]{1}\.[0-9]{1}\.[0-9]{1}')
        for line in lines:
            m = ipre.match(line)
            if m is not None:
                # considering 1 ip in each line
                ip = m.group()
                cnt[ip] += 1

        # return the most frequent IP
        return sorted(cnt, key=lambda x: x[1])[0]


s = Solution()
lines = ["1657628632 - /index.html", "165763332 - /index.html", "1657625553 - /index.html"]
print(s.mostFrequentIP(lines))

