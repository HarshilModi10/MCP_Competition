class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = collections.defaultdict(int)
        
        for domain in cpdomains:
            count, website = domain.split(" ")
            subdomains = website.split(".")
            for i in range(len(subdomains)):
                dic[".".join(subdomains[i:])] += int(count)
        
        return [str(count) + " " + key for key, count in dic.items()]